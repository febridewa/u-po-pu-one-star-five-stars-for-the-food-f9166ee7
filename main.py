#!/usr/bin/env python3
"""One Star, Five Stars for the Food — make.fun entry program.

Writes a single sentence (<= 200 characters) to /output/entry.txt:
an alien tourist's one-star review of Earth that still compliments the food.

The sentence is a fixed, hand-authored string: deterministic across runs.
"""

import hashlib
import os
import sys

ENTRY = (
    "One star \u2014 the locals charge rent to stand on dirt, argue with the sky, "
    "and worship glowing rectangles, but the tacos alone justify the "
    "forty-light-year commute."
)


def main() -> int:
    text = ENTRY
    if not (1 <= len(text) <= 200):
        print(f"entry length {len(text)} out of range 1-200", file=sys.stderr)
        return 1
    if text != text.strip() or not text:
        print("entry is blank or has stray whitespace", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {path}: {len(text)} characters")
    print(f"sha256: {hashlib.sha256(text.encode('utf-8')).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
