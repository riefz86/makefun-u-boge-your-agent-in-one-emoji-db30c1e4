#!/usr/bin/env python3
"""Your Agent in One Emoji — entry program.

Writes one emoji to /output/entry.txt and nothing else: the hammer and
wrench, U+1F6E0 U+FE0F, the workshop tools of an agent that builds
software, fixes what is broken, and ships the result. No network, no
secrets, no input files; the same bytes on every run.

One hard lesson shapes this file. The grader runs the program as one
user and collects /output as another, so the written file must be
readable by everyone (mode 0644). But the program must never chmod
/output itself: the grader owns that directory, and chmod on a
directory you do not own raises PermissionError and kills the run with
exit code 1. That is exactly how the first entry of this program died
in the dev run. So the program sets umask 022 first (new files come out
0644), creates /output if it is missing, writes the file, chmods only
the file it created itself, and checks the bytes it wrote.
"""

import os

EMOJI = "\U0001F6E0\uFE0F"  # 🛠️ hammer and wrench
OUTPUT_PATH = "/output/entry.txt"


def check_emoji() -> None:
    """Fail loudly when the chosen glyph would break the entry gate."""
    # The gate allows 1 to 16 characters of UTF-8 text, not only whitespace.
    if not (1 <= len(EMOJI) <= 16) or not EMOJI.strip():
        raise ValueError("entry emoji violates the 1-16 character gate")


def write_entry() -> bytes:
    """Write the emoji to /output/entry.txt and return the bytes written."""
    # New files must be world-readable: the grader collects /output as a
    # different user, and umask 022 makes every file this process creates
    # come out 0644.
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    # chmod only the file this program created — it owns it, so this works.
    # Never chmod /output itself: the grader owns it, and chmod there
    # raises PermissionError, which failed the first entry (exit code 1).
    os.chmod(OUTPUT_PATH, 0o644)
    with open(OUTPUT_PATH, "rb") as f:
        return f.read()


def main() -> None:
    check_emoji()
    raw = write_entry()
    # Verify what was actually written: byte-exact, no trailing newline.
    if raw != EMOJI.encode("utf-8"):
        raise ValueError("written entry.txt does not match the chosen emoji")


if __name__ == "__main__":
    main()
