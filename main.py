#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one line -- an alien tourist's review of Earth after a
two-day visit -- to /output/entry.txt.
"""

import os

LINE = (
    "Two days on Earth: five-star sunsets, lovely locals, but the "
    "dominant species communicates by staring at glowing rectangles "
    "in silence. 4/5, would orbit again."
)


def main() -> None:
    # The gate allows 1 to 200 characters; refuse to write an entry
    # that would be invalid instead of shipping it silently.
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"entry line is {len(LINE)} characters, must be 1-200")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
