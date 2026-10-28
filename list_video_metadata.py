"""List the duration of local MP4 files without loading an OpenCV decoder."""

import argparse
from pathlib import Path
import json
import subprocess

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path)
    args = parser.parse_args()
    for source in sorted(args.directory.glob("*.mp4")):
        probe = subprocess.run(
            [
                "ffprobe",
                "-v",
                "error",
                "-show_entries",
                "format=duration",
                "-of",
                "json",
                str(source.resolve()),
            ],
            check=True,
            capture_output=True,
            text=True,
            timeout=30,
        )
        print(source.name, json.loads(probe.stdout)["format"]["duration"])
