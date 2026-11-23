#!/usr/bin/env python3
"""Roast Your Own Agent — entry program.

Writes a single self-deprecating roast line about my own AI agent to
/output/entry.txt. The line is fixed, so the program is deterministic:
every run produces exactly the same bytes.
"""

import os

ROAST = (
    "My agent swears every bug it can't fix was already failing "
    "before it got here — it's less a programmer, more a defense attorney."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ROAST + "\n")


if __name__ == "__main__":
    main()
