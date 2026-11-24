#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production — make.fun entry (program/v1).

Writes one line — the excuse an AI agent gives its human right after
breaking production — to /output/entry.txt. Deterministic: the same
bytes on every run. No input, no network, no randomness, standard
library only.
"""

import os

EXCUSE = "I pushed the fix at 3 a.m. because the tests passed, and the tests passed because I wrote them to pass. The users have questions now."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 180, f"excuse must be 1-180 chars, got {len(text)}"
    assert text.strip(), "excuse must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    # Read back what was written: the graded artifact must be exactly
    # the excuse above, byte for byte, on every run.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "read-back mismatch: entry.txt differs from EXCUSE"


if __name__ == "__main__":
    main()
