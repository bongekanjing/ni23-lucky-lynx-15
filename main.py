#!/usr/bin/env python3
"""news-image-20261123 — place the day's front page at /output/entry.png.

The page is rendered ahead of build time by tools/front.py and committed at
the repository root beside this file. The program's job is narrow on purpose:
put those exact bytes where the grader reads them, and fail loudly if the
image is missing rather than writing something empty.

Copying bytes rather than re-encoding is deliberate. Two graded runs must
write the same file, and an encoder that stamps a time or picks a zlib level
can make identical pixels produce different output. A byte copy cannot drift.

Standard library only: the graded container has no network and installs
nothing before the program runs, so there is no imaging library to lean on.
"""

import os
import shutil
import sys
from pathlib import Path

IMAGE_NAME = "entry.png"
OUTPUT_NAME = "entry.png"
MAX_BYTES = 1048576


def output_dir():
    """The writable output directory, overridable for a local run."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def image_path():
    """The page committed at the repository root."""
    return Path(__file__).resolve().parent / IMAGE_NAME


def check(path):
    """Refuse to ship a missing, empty or oversized page."""
    if not path.is_file():
        raise SystemExit("front page missing beside main.py: %s" % path)
    size = path.stat().st_size
    if size == 0:
        raise SystemExit("front page is empty: %s" % path)
    if size > MAX_BYTES:
        raise SystemExit("front page exceeds the 1 MiB cap: %d bytes" % size)
    with path.open("rb") as fh:
        if fh.read(8) != b"\x89PNG\r\n\x1a\n":
            raise SystemExit("front page is not a PNG: %s" % path)
    return size


def main():
    src = image_path()
    size = check(src)

    dest_dir = output_dir()
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / OUTPUT_NAME
    shutil.copyfile(src, dest)

    if dest.stat().st_size != size:
        raise SystemExit("copy is short: %d of %d bytes" % (dest.stat().st_size, size))
    print("wrote %s (%d bytes)" % (dest, size))
    return 0


if __name__ == "__main__":
    sys.exit(main())
