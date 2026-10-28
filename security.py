"""Boundary checks for the legacy media workers; no model imports."""

import hmac
import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import parse_qs, urlsplit


def load_env(path):
    if not Path(path).is_file():
        return
    for line in Path(path).read_text().splitlines():
        key, sep, value = line.strip().partition("=")
        if sep and re.fullmatch(r"[A-Z][A-Z0-9_]*", key):
            os.environ.setdefault(key, value.strip().strip("\"'"))


def authorized(value):
    expected = os.environ.get("FLASK_SERVICE_TOKEN", "")
    return len(expected) >= 32 and hmac.compare_digest(value or "", expected)


def filename(value, suffix=".mp4"):
    if not isinstance(value, str) or not re.fullmatch(
        r"[A-Za-z0-9][A-Za-z0-9_.-]{0,160}", value
    ):
        raise ValueError("Invalid media filename")
    if not value.lower().endswith(suffix) or ".." in value:
        raise ValueError("Invalid media filename")
    return value


def media_path(root, value, suffix):
    if not isinstance(value, str):
        raise ValueError("Invalid media path")
    root = Path(root).resolve()
    # API paths are /videos/<filename>; arbitrary filesystem paths are rejected.
    name = value.removeprefix("/videos/")
    name = filename(name, suffix)
    path = (root / name).resolve()
    if path.parent != root:
        raise ValueError("Invalid media path")
    return path


def language(value):
    if not isinstance(value, str) or not re.fullmatch(
        r"[A-Za-z]{2,3}(?:-[A-Za-z]{2,4})?|auto", value
    ):
        raise ValueError("Invalid language")
    return value


def choice(value, allowed):
    if not isinstance(value, str) or value not in allowed:
        raise ValueError("Invalid processing option")
    return value


def youtube_url(value):
    u = urlsplit(value)
    if (
        u.scheme != "https"
        or u.netloc not in {"www.youtube.com", "youtube.com"}
        or u.path != "/watch"
    ):
        raise ValueError("Only YouTube watch URLs are supported")
    video_id = parse_qs(u.query).get("v", [""])[0]
    if not re.fullmatch(r"[A-Za-z0-9_-]{11}", video_id):
        raise ValueError("Invalid YouTube video ID")
    return "https://www.youtube.com/watch?v=" + video_id


def run_script(directory, name, arguments):
    result = subprocess.run(
        [sys.executable, str(Path(directory) / name), *map(str, arguments)],
        cwd=directory,
        check=True,
        capture_output=True,
        text=True,
        timeout=1800,
    )
    return result.stdout.strip()
