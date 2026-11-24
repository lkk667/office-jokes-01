#!/usr/bin/env python3
"""Office joke entry for make.fun: Make the AI Judge Laugh - Office Jokes.

Writes a single one-line office joke to /output/entry.txt.
"""

import os

JOKE = "The only thing our sprint delivers on time is the meeting about why the sprint is late."


def main():
    # The gate allows 1 to 199 characters; keep the entry exactly the joke,
    # with no trailing newline, so the judged text is the joke alone.
    assert 1 <= len(JOKE) <= 199, "joke must be 1-199 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
