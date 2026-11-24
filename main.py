"""Write the one-emoji entry to /output/entry.txt.

The entry is exactly one emoji (U+1F33B SUNFLOWER), written exactly
as-is with no trailing newline.
"""

import os

ENTRY = "\U0001F33B"


def main():
    assert len(ENTRY) == 1, "entry must be exactly one character"
    assert 1 <= len(ENTRY) <= 8, "entry must be 1-8 characters"
    assert ENTRY == ENTRY.strip(), "entry must not have leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
