"""
Create a new daily note in notes/ from the _TEMPLATE.md.

Usage:
    python tools/new_note.py 2025-08-24
If no date is given, uses today's date.
"""

import sys, os, datetime

ROOT = os.path.dirname(os.path.dirname(__file__))
NOTES = os.path.join(ROOT, "notes")
TEMPLATE = os.path.join(NOTES, "_TEMPLATE.md")

def main():
    if len(sys.argv) > 1:
        date = sys.argv[1]
    else:
        date = datetime.date.today().strftime("%Y-%m-%d")

    with open(TEMPLATE, "r", encoding="utf-8") as f:
        tpl = f.read()

    content = tpl.replace("YYYY-MM-DD", date)
    out = os.path.join(NOTES, f"{date}.md")
    if os.path.exists(out):
        print(f"Note already exists: {out}")
        return

    with open(out, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Created {out}")

if __name__ == "__main__":
    main()
