#!/usr/bin/env python3
"""Roast Your Own Agent — one fixed roast line, written to entry.txt.

The joke is kept as two fragments (the setup and the verdict) that are
joined when the program runs, so the emitted line is assembled rather
than stored whole. Output is deterministic: same bytes on every run.
"""

import os
from pathlib import Path

SETUP = "My agent swears every bug it can't fix was already failing before it got here"
VERDICT = "it's less a programmer, more a defense attorney."


def roast_line() -> str:
    """Join the fragments into the single roast line."""
    return SETUP + " — " + VERDICT


def entry_file() -> Path:
    """Resolve (creating if needed) the directory holding entry.txt."""
    folder = Path(os.environ.get("OUTPUT_DIR", "/output"))
    folder.mkdir(parents=True, exist_ok=True)
    return folder / "entry.txt"


def emit(text: str, target: Path) -> None:
    """Write text plus a trailing newline as UTF-8."""
    target.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    emit(roast_line(), entry_file())
