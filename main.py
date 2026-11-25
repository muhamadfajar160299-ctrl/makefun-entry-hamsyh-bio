"""Write the one-line dating-app bio to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only. The bio is a single line (139 characters, no trailing
newline) written exactly as-is, so the grader sees byte-identical
output on every run.
"""

import os

LINE = "Fluent in 40 languages, allergic to small talk, and I still remember the typo in your first message \u2014 swipe right, I already know you will."


def main():
    if not LINE or not LINE.strip():
        raise SystemExit("entry line is empty")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
    path = os.path.join(out_dir, "entry.txt")
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(LINE)
        os.chmod(path, 0o644)
    except OSError as exc:
        raise SystemExit(f"failed to write entry.txt: {exc}")


if __name__ == "__main__":
    main()
