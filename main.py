#!/usr/bin/env python3
"""Write one line about a small good thing that happened today to /output/entry.txt.

A neighbour, a mango, and a tree everyone had written off: one concrete
detail (the note on the doorstep) and the turn in the last words.
The line is 111 characters, inside the 1-200 gate.
"""
import os

LINE = "My neighbour left a mango on my doorstep with a note: 'From the tree you said was dying.' It fruited overnight."


def main():
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.strip() == LINE, "no leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
