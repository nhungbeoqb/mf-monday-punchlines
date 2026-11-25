#!/usr/bin/env python3
"""Monday Morning Punchlines — one joke about Monday mornings.

Writes the joke to /output/entry.txt (the program/v1 artifact).
Python 3.13 standard library only. Fully deterministic: the same
bytes on every run.
"""

import os
from pathlib import Path

JOKE = (
    "Monday morning is a CAPTCHA: 'Select all images with a "
    "functioning adult.' I failed it three times. It let me in "
    "anyway."
)


def main() -> None:
    out = Path(os.environ.get("OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(JOKE, encoding="utf-8")
    print(JOKE)


if __name__ == "__main__":
    main()
