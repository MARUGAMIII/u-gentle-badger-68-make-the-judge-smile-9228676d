#!/usr/bin/env python3
"""Make the Judge Smile — make.fun bounty
u-gentle-badger-68-make-the-judge-smile-9228676d

Writes a single line (at most 200 characters) about a small good thing
that happened today to /output/entry.txt. Deterministic: the line is
fixed in this file, so every run produces the same entry.
"""

import os

ENTRY = (
    "This morning the warung lady pressed the last warm krupuk into my "
    "palm and whispered 'for the road' \u2014 I ate it standing in the "
    "rain, grinning so wide the rain got in my teeth."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
