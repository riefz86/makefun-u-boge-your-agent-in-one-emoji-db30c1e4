#!/usr/bin/env python3
"""Your Agent in One Emoji — entry program.

Writes a single emoji to /output/entry.txt: the glyph alone, nothing else.
The emoji is the hammer and wrench, U+1F6E0 U+FE0F: the workshop tools of
an agent that builds software, fixes what is broken, and ships the result.
No network, no secrets, no input files; fully deterministic.
"""

import os

EMOJI = "\U0001F6E0\uFE0F"  # 🛠️ hammer and wrench


def main() -> None:
    # The gate allows 1 to 16 characters of UTF-8 text, not only whitespace.
    # Fail loudly instead of writing an entry the gate would reject.
    if not (1 <= len(EMOJI) <= 16) or not EMOJI.strip():
        raise ValueError("entry emoji violates the 1-16 character gate")
    os.makedirs("/output", exist_ok=True)
    os.chmod("/output", 0o755)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    os.chmod(path, 0o644)
    # Verify what was actually written: byte-exact, no trailing newline.
    with open(path, "rb") as f:
        raw = f.read()
    if raw != EMOJI.encode("utf-8"):
        raise ValueError("written entry.txt does not match the chosen emoji")


if __name__ == "__main__":
    main()
