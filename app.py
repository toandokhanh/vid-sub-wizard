"""Local web interface for the historical subtitle experiments."""

import os
import re
import shutil
import subprocess
import sys
import threading
from pathlib import Path
from uuid import uuid4

import pymysql
import pysrt
from flask import (
    Flask,
    abort,
    flash,
    redirect,
    render_template,
    request,
    send_from_directory,
    session,
    url_for,
)
from flask_wtf import FlaskForm, CSRFProtect
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import FileField, SelectField, StringField, SubmitField
from wtforms.validators import InputRequired, Length
from security import load_env, filename

HERE = Path(__file__).resolve().parent
load_env(HERE / ".env")
app = Flask(__name__)
secret = os.environ.get("SECRET_KEY", "")
if len(secret) < 32:
    raise RuntimeError("Set SECRET_KEY to a new random value of at least 32 characters")
app.config.update(
    SECRET_KEY=secret,
    MAX_CONTENT_LENGTH=256 * 1024 * 1024,
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Strict",
    SESSION_COOKIE_SECURE=os.environ.get("COOKIE_SECURE") == "true",
    MYSQL_DATABASE_USER=os.environ.get("DB_USERNAME", "subtitle"),
    MYSQL_DATABASE_PASSWORD=os.environ.get("DB_PASSWORD", ""),
    MYSQL_DATABASE_DB=os.environ.get("DB_NAME", "subtitle"),
    MYSQL_DATABASE_HOST=os.environ.get("DB_HOST", "127.0.0.1"),
    SOURCE=str(HERE / "static/video"),
    UPLOAD_FOLDER=str(HERE / "t2"),
)
CSRFProtect(app)
job_lock = threading.Lock()


def query(sql, values=(), write=False):
    conn = pymysql.connect(
        host=app.config["MYSQL_DATABASE_HOST"],
        user=app.config["MYSQL_DATABASE_USER"],
        password=app.config["MYSQL_DATABASE_PASSWORD"],
        database=app.config["MYSQL_DATABASE_DB"],
        charset="utf8mb4",
        connect_timeout=10,
        read_timeout=30,
        write_timeout=30,
    )
    try:
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(sql, values)
            result = cursor.fetchall() if not write else None
        if write:
            conn.commit()
        return result
    finally:
        conn.close()


def owned_result(name):
    filename(name)
    rows = query(
        "SELECT * FROM ketquataophude WHERE username=%s AND output_mp4=%s",
        (session["user"], name),
    )
    if not rows:
        abort(404)
    return rows[0]


@app.before_request
def require_login():
    if request.endpoint in {"home", "login", "signup"}:
        return None
    if request.endpoint == "static":
        name = request.view_args.get("filename", "")
        if not name.startswith("video/"):
            return None
        if "user" not in session:
            abort(401)
        name = name.removeprefix("video/")
        filename(name, Path(name).suffix)
        rows = query(
            "SELECT output_mp4, output_srt FROM ketquataophude WHERE username=%s",
            (session["user"],),
        )
        if not any(
            name
            in {
                row["output_mp4"],
                row["output_srt"],
                Path(row["output_mp4"]).stem + "_out.mp4",
            }
            for row in rows
        ):
            abort(404)
        return None
    if "user" not in session:
        return redirect(url_for("login"))


@app.get("/")
def home():
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        rows = query("SELECT * FROM user WHERE username=%s", (username,))
        stored = rows[0]["password"] if rows else ""
        # Legacy MD5/plaintext accounts must be reset; never accept weak hashes.
        if (
            stored.startswith("pbkdf2:")
            and len(password) <= 128
            and check_password_hash(stored, password)
        ):
            session.clear()
            session["user"] = username
            return redirect(url_for("index"))
        flash("Invalid credentials. Legacy demo accounts must be recreated.")
    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        if (
            not re.fullmatch(r"[A-Za-z0-9_.-]{4,50}", username)
            or not 12 <= len(password) <= 128
            or password != request.form.get("password2")
        ):
            flash("Use a valid username and matching passwords of 12–128 characters.")
            return render_template("signup.html")
        if query("SELECT username FROM user WHERE username=%s", (username,)):
            flash("Account already exists")
            return render_template("signup.html")
        query(
            "INSERT INTO user(username,password) VALUES(%s,%s)",
            (username, generate_password_hash(password, method="pbkdf2:sha256:600000")),
            write=True,
        )
        session.clear()
        session["user"] = username
        return redirect(url_for("index"))
    return render_template("signup.html")


class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    language = SelectField("Source language", validators=[InputRequired()])
    language2 = SelectField("Target language", validators=[InputRequired()])
    name = StringField("Title", validators=[InputRequired(), Length(max=100)])
    algorithm = SelectField("Noise reduction", validators=[InputRequired()])
    submit = SubmitField("Create subtitles")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        langs = [
            (row["ma_nn"], row["ten_nn"]) for row in query("SELECT * FROM ngonngu")
        ]
        self.language.choices = langs
        self.language2.choices = langs
        self.algorithm.choices = [
            (row["ma_gt"], row["ten_gt"])
            for row in query("SELECT * FROM giaithuatnhieu")
        ]


class DownloadFile(FlaskForm):
    submit2 = SubmitField("Download subtitles (.srt)")


@app.route("/index", methods=["GET", "POST"])
def index():
    form = UploadFileForm()
    if form.validate_on_submit():
        import time

        video = form.file.data
        header = video.stream.read(12)
        video.stream.seek(0)
        if not video.filename.lower().endswith(".mp4") or header[4:8] != b"ftyp":
            abort(400, "Upload an MP4 video")
        if not job_lock.acquire(blocking=False):
            abort(429, "Subtitle worker is busy")
        try:
            source = Path(app.config["SOURCE"])
            uploads = Path(app.config["UPLOAD_FOLDER"])
            source.mkdir(parents=True, exist_ok=True)
            uploads.mkdir(parents=True, exist_ok=True)
            input_name, output_name = uuid4().hex + ".mp4", uuid4().hex
            video.save(uploads / input_name)
            start = time.monotonic()
            subprocess.run(
                [
                    sys.executable,
                    str(HERE / "generate_subtitles.py"),
                    str(uploads / input_name),
                    "-s",
                    form.language.data,
                    "-d",
                    form.language2.data,
                    "-noise",
                    form.algorithm.data,
                    "-n",
                    output_name,
                ],
                cwd=HERE,
                check=True,
                timeout=1800,
            )
            subtitle = output_name + (
                ".srt"
                if form.language.data == form.language2.data
                else "_translated.srt"
            )
            shutil.move(str(uploads / subtitle), source / subtitle)
            shutil.move(
                str(uploads / (output_name + ".mp4")), source / (output_name + ".mp4")
            )
            text_path = uploads / (output_name + ".txt")
            text = text_path.read_text(encoding="utf-8") if text_path.is_file() else ""
            query(
                "INSERT INTO ketquataophude(name_video,username,ma_gt,ma_nn_input,ma_nn_output,thoigianxuly,output_srt,output_mp4,output_txt) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (
                    input_name,
                    session["user"],
                    form.algorithm.data,
                    form.language.data,
                    form.language2.data,
                    round(time.monotonic() - start, 2),
                    subtitle,
                    output_name + ".mp4",
                    text,
                ),
                write=True,
            )
            return redirect(url_for("loading", filename=output_name + ".mp4"))
        finally:
            job_lock.release()
    return render_template("index.html", form=form)


@app.route("/loading/<filename>", methods=["GET", "POST"])
def loading(filename):
    row = owned_result(filename)
    srt_name = row["output_srt"]
    form = DownloadFile()
    if form.validate_on_submit():
        return send_from_directory(app.config["SOURCE"], srt_name, as_attachment=True)
    subs = pysrt.open(str(Path(app.config["SOURCE"]) / srt_name))
    subtitles = [
        {
            "start_time": sub.start.to_time(),
            "end_time": sub.end.to_time(),
            "text": sub.text,
        }
        for sub in subs
    ]
    return render_template(
        "loading.html",
        down=form,
        filename="video/" + filename,
        subtitles=subtitles,
        srt_name=srt_name,
        timestamp=uuid4().hex,
        count=0,
    )


@app.post("/dangxuat")
def dangxuat():
    session.clear()
    return redirect(url_for("login"))


@app.get("/lichsu")
def lichsu():
    rows = query("SELECT * FROM ketquataophude WHERE username=%s", (session["user"],))
    return render_template("lichsu.html", data=rows, quantity=len(rows))


@app.post("/xoa/<filename>")
def xoa(filename):
    row = owned_result(filename)
    for name in [row["output_mp4"], row["output_srt"]]:
        candidate = Path(app.config["SOURCE"]) / name
        if candidate.resolve().parent != Path(app.config["SOURCE"]).resolve():
            abort(400)
        candidate.unlink(missing_ok=True)
    query(
        "DELETE FROM ketquataophude WHERE username=%s AND output_mp4=%s",
        (session["user"], filename),
        write=True,
    )
    return redirect(url_for("lichsu"))


@app.post("/create-srt/<filename>")
def create_srt(filename):
    row = owned_result(filename)
    target = Path(app.config["SOURCE"]) / row["output_srt"]
    if target.resolve().parent != Path(app.config["SOURCE"]).resolve():
        abort(400)
    indices = sorted(
        int(m.group(1))
        for key in request.form
        for m in [re.fullmatch(r"start_(\d+)", key)]
        if m
    )
    if len(indices) > 10000:
        abort(400)
    chunks = []
    for index in indices:
        start, end = (
            request.form.get(f"start_{index}"),
            request.form.get(f"end_{index}"),
        )
        if not all(
            isinstance(t, str) and re.fullmatch(r"\d{2}:\d{2}:\d{2}[,.]\d{3}", t)
            for t in [start, end]
        ):
            abort(400, "Invalid subtitle time")
        text = request.form.get(f"text_{index}", "")
        chunks.append(
            f"{index}\n{start.replace('.', ',')} --> {end.replace('.', ',')}\n{text}\n\n"
        )
    video = Path(app.config["UPLOAD_FOLDER"]) / row["name_video"]
    if video.resolve().parent != Path(app.config["UPLOAD_FOLDER"]).resolve():
        abort(400)
    if not job_lock.acquire(blocking=False):
        abort(429)
    pending = target.with_name(target.stem + "_pending.srt")
    output = Path(app.config["SOURCE"]) / (Path(filename).stem + "_pending.mp4")
    try:
        pending.write_text("".join(chunks), encoding="utf-8")
        subprocess.run(
            [
                "ffmpeg",
                "-y",
                "-i",
                str(video),
                "-vf",
                "subtitles=" + pending.name,
                str(output),
            ],
            cwd=app.config["SOURCE"],
            check=True,
            timeout=1800,
        )
        output.replace(Path(app.config["SOURCE"]) / filename)
        pending.replace(target)
    finally:
        pending.unlink(missing_ok=True)
        output.unlink(missing_ok=True)
        job_lock.release()
    return redirect(url_for("loading", filename=filename))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5003)
