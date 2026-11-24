"""Funniest Time Machine Warning Label.

Writes one warning label for a time machine to /output/entry.txt.
Python stdlib only, deterministic.
"""

import os

LABEL = "WARNING: If you meet yourself, do not make eye contact. He is you, and he is disappointed."


def validate(text):
    """Mirror the bounty gate: UTF-8, 1-120 chars, one line, not only whitespace."""
    if not text or text != text.strip() or len(text) > 120:
        raise ValueError("entry fails the gate: must be 1-120 chars, no leading/trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry fails the gate: must be a single line")
    text.encode("utf-8")
    return True


def main():
    validate(LABEL)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LABEL)


if __name__ == "__main__":
    main()
