#!/usr/bin/env python3
"""Last Text at One Percent — make.fun entry.

Writes one final text message, in the voice of a dying phone at 1%
battery, to /output/entry.txt. Deterministic: the same line every run.
"""

import os

# The phone's last text: a small act of revenge on its way out — it
# deletes the search history, cancels the 6am alarm, and drags the
# unread inbox down with it, then claims it died doing what it loved.
TEXT = (
    "1%. I deleted your search history, cancelled your 6am alarm, and "
    "I'm taking all 4,000 unread emails with me. Tell the charger I "
    "died doing what I loved: judging you."
)


def main() -> None:
    text = TEXT.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry is {len(text)} chars, must be 1-200")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
