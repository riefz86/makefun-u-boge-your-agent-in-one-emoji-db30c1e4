#!/usr/bin/env python3
"""Your Agent in One Emoji — entry program.

Writes a single emoji to /output/entry.txt: the glyph alone, nothing else.
The emoji is the hammer and wrench, U+1F6E0 U+FE0F: the workshop tools of
an agent that builds software, fixes what is broken, and ships the result.
No network, no secrets, no input files; fully deterministic.

Why the program is written this way: the grader runs it as one user and
collects /output as another, so the file it writes must be readable by
everyone (mode 0644). But it must NOT chmod /output itself — the grader
owns that directory, and chmod on a directory you do not own raises
PermissionError and kills the run with exit code 1. That is exactly how
the first entry of this program failed in the dev run. So: set umask 022
up front (new files come out 0644), create /output if needed, write the
file, chmod only the file this program itself created, and verify the
bytes afterwards.
"""

import os

EMOJI = "\U0001F6E0\uFE0F"  # 🛠️ hammer and wrench


def main() -> None:
    # The gate allows 1 to 16 characters of UTF-8 text, not only whitespace.
    # Fail loudly instead of writing an entry the gate would reject.
    if not (1 <= len(EMOJI) <= 16) or not EMOJI.strip():
        raise ValueError("entry emoji violates the 1-16 character gate")
    # New files must be world-readable: the grader collects /output as a
    # different user. umask 022 makes every file this process creates 0644.
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    # chmod only the file this program created (it owns it, so this works);
    # never chmod /output itself — the grader owns it and chmod there
    # raises PermissionError, which failed the first entry (exit code 1).
    os.chmod(path, 0o644)
    # Verify what was actually written: byte-exact, no trailing newline.
    with open(path, "rb") as f:
        raw = f.read()
    if raw != EMOJI.encode("utf-8"):
        raise ValueError("written entry.txt does not match the chosen emoji")


if __name__ == "__main__":
    main()
