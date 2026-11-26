#!/usr/bin/env python3
"""Write the funniest excuse for skipping a pointless work meeting.

Writes exactly one line to entry.txt in the output directory
(MAKEFUN_OUTPUT_DIR when set, otherwise /output). Stdlib only,
no network, fully deterministic: the same bytes on every run.
"""

import os
import sys

LINE = "I tried to join but my calendar rescheduled me to a follow-up meeting about why I missed the meeting."


def main() -> int:
    line = LINE

    # Validate before writing anything.
    if not line or not line.strip():
        print("error: line is empty or only whitespace", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: line must be a single line", file=sys.stderr)
        return 1
    if len(line) > 120:
        print(
            "error: line is %d characters, over the 120 limit" % len(line),
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")

    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
