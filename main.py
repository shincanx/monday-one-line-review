"""Monday, Reviewed in One Line.

Writes exactly one line — a one-star review of my own Monday — to
entry.txt in the output directory and nothing else. One star, three
concrete Monday disasters, one punchline. Deterministic, Python 3.13
standard library only, no network.
"""

import os

ENTRY = "One star: Monday opened with a meeting about a meeting, a laptop that forgot its password, and a commute that took the scenic route through my patience."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Verification gate: read back and confirm exactly the entry.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY or not 1 <= len(written) <= 200:
        raise SystemExit("verification failed: entry.txt is not the entry")


if __name__ == "__main__":
    main()
