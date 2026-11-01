#!/usr/bin/env python3
"""Create a project from general/templates/PROJECT_TEMPLATE. Demo vault only."""
import argparse
import datetime as dt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "general" / "templates" / "PROJECT_TEMPLATE"


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--name", required=True)
    p.add_argument("--title", required=True)
    p.add_argument("--category", default="Research", choices=["Research", "Grant", "Teaching", "Tesi", "Other"])
    args = p.parse_args()
    slug = args.name.strip().lower().replace(" ", "-")
    dest = ROOT / "areas" / args.category / slug
    if dest.exists():
        raise SystemExit(f"already exists: {dest}")
    today = dt.date.today().isoformat()
    dest.mkdir(parents=True)
    (dest / "raw" / "notes").mkdir(parents=True)
    (dest / "skills").mkdir()
    for src in TEMPLATE.glob("*.md"):
        text = src.read_text(encoding="utf-8")
        text = text.replace("{{SLUG}}", slug).replace("{{TITLE}}", args.title).replace("{{DATE}}", today)
        (dest / src.name.replace("{{SLUG}}", slug)).write_text(text, encoding="utf-8")
    memory = ROOT / "general" / "MEMORY.md"
    row = f"| {slug} | areas/{args.category}/{slug}/{slug}_INDEX.md | CURRENT_STATE | AGENT_MEMORY | DECISIONS |\n"
    text = memory.read_text(encoding="utf-8")
    if slug not in text:
        memory.write_text(text.rstrip() + "\n" + row, encoding="utf-8")
    index = ROOT / "general" / "INDEX.md"
    idx = index.read_text(encoding="utf-8")
    line = f"| {slug} | {args.category} | [areas/{args.category}/{slug}/{slug}_INDEX.md](../areas/{args.category}/{slug}/{slug}_INDEX.md) |\n"
    if slug not in idx:
        index.write_text(idx.rstrip() + "\n" + line, encoding="utf-8")
    print(f"created {dest}")


if __name__ == "__main__":
    main()
