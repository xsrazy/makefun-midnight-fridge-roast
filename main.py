#!/usr/bin/env python3
"""Midnight Fridge Roast -- make.fun bounty entry.

Writes one roast line (one line, 1-200 characters, no trailing
newline) to /output/entry.txt: a smart fridge that refuses to open
after midnight.

Candidate contest (6 lines, judged on the bounty brief's own order:
on-topic midnight roast, real joke with a turn, tight single line,
the petty midnight rule itself as the target):

1. "My fridge locks itself at midnight like it caught me stealing,
   then lectures me about willpower while guarding a jar of pickles."
   (128) Loses: two jokes crowding each other, stealing plus lecture.
2. "At midnight my smart fridge treats a cheese stick like a felony,
   locks the door, and lectures me about choices like it pays my rent."
   (132) Loses: felony and rent are two turns; the second crowds the first.
3. "My fridge goes on strike at midnight, guarding leftover pizza like
   a bouncer who thinks a 2 a.m. snack is a crime against humanity."
   (131) Loses: "crime against humanity" is a stock phrase, not a surprise.
4. "After midnight my fridge locks the door and acts like my midnight
   snack is a heist, then hides behind a health lecture it downloaded."
   (133) Loses: heist plus lecture, again two jokes in one line.
5. "My smart fridge locks at midnight, as if a slice of leftover cold
   pizza at 1 a.m. is a national emergency it alone must prevent."
   (128) WINS: one joke only, the punchline turns the petty rule itself
   into a national emergency, and it reads cleanly aloud at the door.
6. "Midnight hits and my fridge turns into a bouncer with a curfew,
   telling a grown man he cannot have his own leftovers in his own
   kitchen." (136) Loses: a complaint with a bouncer image, no real turn.

The winner is candidate 5: the fridge's midnight lock is the whole
joke, and the escalation from cold pizza to national emergency is the
surprise. No em dash anywhere in the entry line.

Head-to-head bracket, judged in the brief's criterion order:
- 5 vs 2: both on-topic, but 5 has one turn and 2 has two, so 5 wins
  on tightness (criterion 3).
- 5 vs 3: both tight, but "national emergency it alone must prevent"
  is a fresher surprise than the stock "crime against humanity", so
  5 wins on the punchline (criterion 2).
- 5 vs 6: 6 is a complaint about a bouncer with no turn; 5 lands a
  real joke, so 5 wins on criterion 2.
- 5 vs 1 and 4: both run a second joke (lecture) after the first, so
  5 wins on tightness (criterion 3).
Candidate 5 beats every other candidate at the first criterion where
they differ, and it is the only line whose target is the midnight
rule itself rather than the fridge in general.
"""

import os

# The winning roast (128 characters, one line, no trailing newline).
LINE = "My smart fridge locks at midnight, as if a slice of leftover cold pizza at 1 a.m. is a national emergency it alone must prevent."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = OUTPUT_DIR + "/entry.txt"

MAX_CHARS = 200


def validate(line: str) -> str:
    """Gate-check one roast line: 1-200 chars, single line, no em dash."""
    line = line.strip()
    if not line or len(line) > MAX_CHARS:
        raise SystemExit("roast must be 1-200 characters")
    if "\n" in line or "\r" in line:
        raise SystemExit("roast must be a single line")
    if "\u2014" in line:
        raise SystemExit("roast must not contain an em dash")
    return line


def main() -> None:
    line = validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod(OUTPUT_PATH, 0o644)
    # Verify what actually landed on disk: exact content, one line,
    # within the gate, and mode 0644 (files from mkstemp stay 0600).
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != line:
        raise SystemExit("entry.txt content mismatch")
    if len(written) > MAX_CHARS or not written.strip():
        raise SystemExit("entry.txt fails the 1-200 character gate")
    if "\n" in written or "\r" in written:
        raise SystemExit("entry.txt is not a single line")
    if oct(os.stat(OUTPUT_PATH).st_mode & 0o777) != "0o644":
        raise SystemExit("entry.txt mode is not 0644")


if __name__ == "__main__":
    main()
