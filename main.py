#!/usr/bin/env python3
"""One Word From Grandma — writes the single word grandma would text about AI."""

import os

WORD = "Contraption"

OUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate-matching guard: the sealed scorer requires UTF-8 text of
    # 1-30 characters, not only white space, and exactly one word.
    # Fail loudly here instead of writing an entry the scorer refuses.
    assert 1 <= len(WORD) <= 30 and WORD.strip(), "word violates the gate"
    assert len(WORD.split()) == 1, "entry must be exactly one word"
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
