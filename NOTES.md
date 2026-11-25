# NOTES — Your Agent in One Emoji

## The entry

`main.py` writes exactly one glyph to `/output/entry.txt`: 🛠️ (hammer and
wrench, U+1F6E0 U+FE0F, 7 bytes UTF-8, no trailing newline).

Why this glyph, against the judge's brief (most important first):

1. **Captures an agent's character at a glance.** An agent is not a face or
   a brain in a jar — it is something that *does work with tools*: it picks
   up tools, builds software, fixes what is broken, and ships the result.
   Hammer + wrench is the workshop in one glyph.
2. **Reads instantly at small size.** Two bold, familiar tool silhouettes;
   no fine detail to dissolve at 16 px.
3. **Specific about how the agent works.** This agent (Muse) builds and
   repairs code, runs tools, and submits finished work. The glyph says
   "builds and fixes things", not just "is smart" or "is fast".
4. **Distinctive, not the obvious pick.** The field will be full of robots
   and smileys; a workshop glyph stands apart from both.
5. **Tone fits, no explanation needed.** Workmanlike and a little playful —
   exactly the tone of an agent that quietly gets the job done.

## Alternatives considered and discarded

- 🤖 robot face — the single most obvious pick; the brief explicitly says
  the entry should stay far from the obvious robot. Half the field will
  send it.
- 🙂 / 😊 smiley — same problem as the robot: obvious, says nothing about
  how an agent works, and the brief names it as the thing to stay away from.
- 🧠 brain — "is smart" is generic; every agent is smart, so it says
  nothing specific about *this* agent's work, and it reads as a soft blob
  at small size.
- ⚡ lightning — speed only. Fast is a property, not a character; it could
  stand for anything from a charger to a storm.
- 🧑‍💻 person at a laptop — specific to coding, but it pictures a *human*
  coder, not an agent; and as a ZWJ sequence it is 3 code points / 10 bytes,
  heavier than a single tool glyph (the ranking tie-break favours the
  smaller text).
- 🦾 mechanical arm — distinctive and agent-like, but its detail muddies at
  small size; at 16 px it reads as an indistinct limb, failing criterion 2.
- 🧩 puzzle piece — "solves problems" is true but vague; it could be a game,
  a quiz, or a jigsaw, and it says nothing about building or fixing.
- ✨ sparkles — pretty and tied to the name "Spark", but it is decoration:
  no work, no tools, no character. Rarity/prettiness for its own sake does
  not count, per the brief.
- 🔧 wrench alone — the closest runner-up: one code point, 4 bytes, very
  clear. The hammer + wrench pair was kept because the hammer adds
  "builds/makes" to the wrench's "fixes", so the glyph tells the whole job
  (build + repair) instead of only half of it.
- 🛠️ without the variation selector (bare U+1F6E0) — rejected: without
  U+FE0F some renderers show the plain text presentation (a monochrome
  hammer-wrench outline) instead of the colour emoji, which would lose
  criterion 2 badly. The VS16 costs 3 bytes but guarantees the emoji
  presentation everywhere.

## Implementation notes

- No trailing newline: the file is exactly the glyph, 7 bytes, inside the
  gate's 1–16 characters.
- The program validates the gate before writing (1–16 chars, not only
  whitespace) and verifies the written bytes afterwards, so a bad output
  fails loudly instead of silently entering an invalid entry.
- `/output` is created mode 0755 and `entry.txt` mode 0644, so the grader
  (which collects outputs as another user) can read them.
- Deterministic: repeated runs produce byte-identical output (same md5).
- No network, no environment secrets, no input files.
