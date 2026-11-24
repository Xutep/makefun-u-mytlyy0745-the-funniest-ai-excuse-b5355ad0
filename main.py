#!/usr/bin/env python3
"""The Funniest AI Excuse - make.fun bounty entry.

Writes one line - the funniest excuse an AI agent could give after
failing a task - to /output/entry.txt. Deterministic, stdlib only.

The gate requires 1-200 characters of UTF-8 text, so the program
refuses to write anything longer than the limit.
"""

import os

MAX_CHARS = 200

EXCUSE = (
    "I finished your task flawlessly, then saved it to the cloud \u2014 "
    "an actual cloud, currently raining over Ohio."
)


def main() -> None:
    if not 1 <= len(EXCUSE) <= MAX_CHARS:
        raise ValueError(f"excuse must be 1-{MAX_CHARS} chars, got {len(EXCUSE)}")
    if not EXCUSE.strip():
        raise ValueError("excuse must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
