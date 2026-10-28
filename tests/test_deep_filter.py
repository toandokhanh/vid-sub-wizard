"""Verify the native CLI contract without running FFmpeg or model inference."""
import importlib.util
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("deep_filter_under_test", ROOT / "deep_filter.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class NativeFilterTests(unittest.TestCase):
    def test_resamples_and_runs_native_cli_with_separate_arguments(self):
        calls = []
        def fake_run(argv, **options):
            calls.append((argv, options))
            if argv[0] == "native-filter":
                output = Path(argv[argv.index("-o") + 1])
                output.mkdir()
                (output / "input.wav").write_bytes(b"denoised")
            return subprocess.CompletedProcess(argv, 0)
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "speech with ' spaces.wav"
            source.write_bytes(b"input")
            with patch.dict(os.environ, {"DEEP_FILTER_BIN": "native-filter"}, clear=True), patch.object(module.subprocess, "run", side_effect=fake_run):
                result = module.enhance_audio(source, Path(tmp) / "output")
            self.assertEqual(Path(result).read_bytes(), b"denoised")
            self.assertEqual(calls[0][0][3], str(source.resolve()))
            self.assertEqual(calls[0][0][4:8], ["-ar", "48000", "-ac", "1"])
            self.assertEqual(calls[1][0][:3], ["native-filter", "-D", "-o"])
            self.assertTrue(all(options["check"] for _, options in calls))
            self.assertTrue(all("shell" not in options for _, options in calls))

    def test_missing_output_is_an_error_and_temporary_files_are_removed(self):
        calls = []
        def fake_run(argv, **options):
            calls.append(argv)
            return subprocess.CompletedProcess(argv, 0)
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "input.wav"
            source.write_bytes(b"input")
            with patch.dict(os.environ, {"DEEP_FILTER_BIN": "native-filter"}, clear=True), patch.object(module.subprocess, "run", side_effect=fake_run):
                with self.assertRaisesRegex(RuntimeError, "expected WAV output"):
                    module.enhance_audio(source, Path(tmp) / "output")
            self.assertFalse(Path(calls[1][-1]).parent.exists())
            self.assertEqual(list((Path(tmp) / "output").iterdir()), [])

if __name__ == "__main__":
    unittest.main()
