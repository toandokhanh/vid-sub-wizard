import importlib.util
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

MODULE = Path(__file__).resolve().parents[1] / "security.py"
spec = importlib.util.spec_from_file_location("media_security", MODULE)
security = importlib.util.module_from_spec(spec)
spec.loader.exec_module(security)


class BoundaryTests(unittest.TestCase):
    def test_filename_rejects_shell_and_path_inputs(self):
        for value in ["../other.mp4", "/tmp/other.mp4", "movie;id.mp4", "$(id).mp4", "--option.mp4", "a..mp4", None, []]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                security.filename(value)
        self.assertEqual(security.filename("a_0123.mp4"), "a_0123.mp4")

    def test_media_path_rejects_symlink_escape(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "videos"
            root.mkdir()
            (root / "escape.mp4").symlink_to(Path(temp) / "private.mp4")
            with self.assertRaises(ValueError):
                security.media_path(root, "escape.mp4", ".mp4")
            self.assertEqual(security.media_path(root, "/videos/ok.mp4", ".mp4"), (root / "ok.mp4").resolve())

    def test_worker_auth_fails_closed(self):
        with patch.dict(os.environ, {}, clear=True):
            self.assertFalse(security.authorized(None))
            self.assertFalse(security.authorized(""))
        with patch.dict(os.environ, {"FLASK_SERVICE_TOKEN": "a" * 32}):
            self.assertFalse(security.authorized("b" * 32))
            self.assertTrue(security.authorized("a" * 32))

    def test_language_and_processing_choices_are_bounded(self):
        for value in ["en;id", "en --option", "$(id)", ["en"]]:
            with self.assertRaises(ValueError):
                security.language(value)
        self.assertEqual(security.language("en-US"), "en-US")
        with self.assertRaises(ValueError):
            security.choice("../arbitrary", {"google-cloud", "openai-whisper"})

    def test_youtube_hostname_and_video_id(self):
        for value in ["https://www.youtube.com.evil/watch?v=abcdefghijk", "https://www.youtube.com@evil/watch?v=abcdefghijk", "file:///etc/passwd", "https://youtube.com/watch?v=abc;id"]:
            with self.assertRaises(ValueError):
                security.youtube_url(value)
        self.assertEqual(security.youtube_url("https://youtube.com/watch?v=abcdefghijk&feature=share"), "https://www.youtube.com/watch?v=abcdefghijk")

    def test_process_uses_an_argument_array_without_a_shell(self):
        with patch.object(security.subprocess, "run") as run:
            run.return_value.stdout = "result\n"
            self.assertEqual(security.run_script("/tmp", "script.py", ["a;not-a-command"]), "result")
            args, kwargs = run.call_args
            self.assertEqual(args[0][-1], "a;not-a-command")
            self.assertFalse(kwargs.get("shell", False))
            self.assertTrue(kwargs["check"])
            self.assertEqual(kwargs["timeout"], 1800)

if __name__ == "__main__":
    unittest.main()
