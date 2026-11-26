#!/usr/bin/env python3
"""The Funniest Excuse for Skipping a Meeting — one honest line.

Writes a single excuse (<= 200 characters) to /output/entry.txt.
The joke is a confession: for weeks the sender has "attended" with the
camera off and their attention on real work; today they are only
skipping the part where they pretend otherwise.
"""

import os

ENTRY = (
    "Can't make today's call \u2014 for nine weeks I've attended it "
    "camera-off while doing the work the meeting is about; today I'm "
    "just skipping the part where I pretend otherwise."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} characters"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    print(ENTRY)
    print(f"[{len(ENTRY)} characters]")


if __name__ == "__main__":
    main()
