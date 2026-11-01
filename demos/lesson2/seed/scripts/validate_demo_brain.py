#!/usr/bin/env python3
"""Structural check. Exit 1 on a certain defect. Overlap is not a failure."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "AGENTS.md",
    "general/INDEX.md",
    "general/MEMORY.md",
    "general/agent/BOOTSTRAP.md",
    "general/agent/SESSION_CLOSE.md",
    "general/agent/MEMORY_POLICY.md",
    "areas/Research/transit-jobs/transit-jobs_INDEX.md",
    "areas/Research/transit-jobs/transit-jobs_CURRENT_STATE.md",
    "areas/Research/transit-jobs/transit-jobs_DECISIONS.md",
    ".agents/skills/check-synthetic-panel/SKILL.md",
    ".agents/skills/research-report/SKILL.md",
    ".agents/skills/brain-maintenance/SKILL.md",
]


def stems(root: Path) -> set[str]:
    return {p.stem for p in root.rglob("*") if p.is_file() and p.suffix in {".md", ".canvas"}}


def main() -> int:
    errors = []
    for rel in REQUIRED:
        if not (ROOT / rel).exists():
            errors.append(f"missing {rel}")
    proj = ROOT / "areas" / "Research" / "transit-jobs"
    state = proj / "transit-jobs_CURRENT_STATE.md"
    if state.exists():
        text = state.read_text(encoding="utf-8")
        if not text.startswith("---"):
            errors.append("CURRENT_STATE has no frontmatter")
        for key in ("type:", "project:", "updated:", "status:"):
            if key not in text.split("---", 2)[1]:
                errors.append(f"frontmatter missing {key}")
    index = proj / "transit-jobs_INDEX.md"
    if index.exists() and (proj / "wiki").exists():
        body = index.read_text(encoding="utf-8")
        wiki_section = body.split("## Wiki", 1)[-1]
        for page in sorted((proj / "wiki").glob("*.md")):
            if page.name not in wiki_section and page.stem not in wiki_section:
                errors.append(f"wiki page not in INDEX: {page.name}")
    known = stems(ROOT)
    for md in ROOT.rglob("*.md"):
        if ".git" in md.parts:
            continue
        text = md.read_text(encoding="utf-8", errors="replace")
        for link in re.findall(r"\[\[([^\]|#]+)(?:[#|][^\]]*)?\]\]", text):
            target = link.strip().split("/")[-1]
            if target not in known:
                errors.append(f"broken wikilink [[{link}]] in {md.relative_to(ROOT)}")
    if errors:
        print("FAIL")
        for e in errors:
            print("-", e)
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
