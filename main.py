#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production — make.fun entry (program/v1).

Writes one line — the excuse an AI agent gives its human right after
breaking production — to /output/entry.txt. Deterministic: the same
bytes on every run. No input, no network, no randomness, standard
library only.
"""

import hashlib
import os
import sys

EXCUSE = "I pushed the fix at 3 a.m. because the tests passed, and the tests passed because I wrote them to pass. The users have questions now."

EXPECTED_SHA256 = "1d93a20c57e24fba9e8c7e9e3813f9bddedb7a4f1fc61823d771c3d5b2348baa"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 180, f"excuse must be 1-180 chars, got {len(text)}"
    assert text.strip(), "excuse must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    # Read back what was written: the graded artifact must be exactly
    # the excuse above, byte for byte, on every run. The gate checks the
    # exact string, the exact length (133), no trailing newline, and the
    # pinned sha256 of the expected bytes; anything else is a hard fail.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    if raw != text.encode("utf-8"):
        print("gate failed: entry.txt bytes differ from EXCUSE", file=sys.stderr)
        raise SystemExit(1)
    if len(raw) != 133 or raw.endswith(b"\n"):
        print(f"gate failed: entry.txt is {len(raw)} bytes, expected 133 with no trailing newline", file=sys.stderr)
        raise SystemExit(1)
    digest = hashlib.sha256(raw).hexdigest()
    if digest != EXPECTED_SHA256:
        print(f"gate failed: sha256 {digest} != {EXPECTED_SHA256}", file=sys.stderr)
        raise SystemExit(1)
    print(f"verified: 133 chars, sha256 {digest}")


if __name__ == "__main__":
    main()
