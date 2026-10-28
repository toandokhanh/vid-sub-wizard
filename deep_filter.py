"""Invoke the native DeepFilterNet CLI without its legacy Python/Torch stack.

Output suffixes preserve existing pipeline filenames; they do not identify a model.
Configure DEEP_FILTER_MODEL explicitly when reproducing a specific experiment.
"""

import os
from pathlib import Path
import shutil
import subprocess
import tempfile


def enhance_audio(source, output_dir, suffix="_DeepFilterNet2.wav"):
    source = Path(source).resolve(strict=True)
    output_dir = Path(output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / (source.stem + suffix)
    with tempfile.TemporaryDirectory(prefix="deep-filter-") as scratch:
        scratch = Path(scratch)
        normalized = scratch / "input.wav"
        enhanced = scratch / "enhanced"
        subprocess.run(
            [
                "ffmpeg",
                "-y",
                "-i",
                str(source),
                "-ar",
                "48000",
                "-ac",
                "1",
                str(normalized),
            ],
            check=True,
            timeout=1800,
            capture_output=True,
        )
        command = [
            os.environ.get("DEEP_FILTER_BIN", "deep-filter"),
            "-D",
            "-o",
            str(enhanced),
        ]
        model = os.environ.get("DEEP_FILTER_MODEL")
        if model:
            command.extend(["-m", str(Path(model).resolve(strict=True))])
        command.append(str(normalized))
        subprocess.run(command, check=True, timeout=1800, capture_output=True)
        result = enhanced / normalized.name
        if not result.is_file():
            raise RuntimeError(
                "The native DeepFilterNet CLI did not produce its expected WAV output"
            )
        shutil.copyfile(result, target)
    return str(target)
