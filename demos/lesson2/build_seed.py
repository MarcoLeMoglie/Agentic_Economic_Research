#!/usr/bin/env python3
"""Write demos/lesson2/seed, a synthetic Obsidian vault for Lesson 2.

The vault is not Marco's Brain. Every result is labelled SIMULATED.
"""
from __future__ import annotations

import csv
import json
import random
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SEED = ROOT / "seed"


def w(rel: str, text: str) -> None:
    path = SEED / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


def panel_csv(path: Path) -> None:
    rng = random.Random(2026)
    path.parent.mkdir(parents=True, exist_ok=True)
    # 400 tracts, 20 districts, years 2010-2022. Treatment is absorbing.
    treat_year = {}
    for i in range(1, 401):
        bucket = (i - 1) % 5
        treat_year[i] = {0: None, 1: 2016, 2: 2018, 3: 2020, 4: None}[bucket]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["tract_id", "year", "district_id", "treated", "emp_rate"])
        for tract in range(1, 401):
            district = (tract - 1) // 20 + 1
            opened = treat_year[tract]
            for year in range(2010, 2023):
                treated = int(opened is not None and year >= opened)
                noise = rng.uniform(-0.01, 0.01)
                emp = 0.62 + 0.002 * (year - 2010) + 0.01 * treated + noise
                writer.writerow([tract, year, district, treated, f"{emp:.4f}"])


def main() -> None:
    if SEED.exists():
        # rebuild from scratch so a rerun does not leave stale files
        import shutil
        shutil.rmtree(SEED)
    panel_csv(SEED / "areas/Research/transit-jobs/data/synthetic_panel.csv")

    w(".demo-brain", "lesson2-demo-vault\nDo not point reset at any other folder.\n")
    w(".gitignore", textwrap.dedent("""\
        .DS_Store
        __pycache__/
        *.pyc
        .obsidian/workspace.json
        .obsidian/workspace-mobile.json
        .obsidian/cache/
        reports/*.tmp
    """))
    w("README.md", """\
# Second Brain lecture demo

Synthetic Obsidian vault for Lesson 2 of Agentic AI for Economic Research.
It is not Marco Le Moglie's vault. Open this folder as an Obsidian vault.

The only research project is `transit-jobs`: a made-up study of metro stations
and employment. The panel in `data/synthetic_panel.csv` is drawn from a
random number generator (seed 2026). The figure ATT 0.031 (s.e. 0.012) is a
**labelled simulation for the lecture**. It is not estimated from the CSV
and it is not evidence about real cities.

Start an agent by pointing it at `AGENTS.md`.
""")
    w("AGENTS.md", """\
# Agent instructions

This folder is a lecture demo, not a real research vault.

1. At the start of a session, read `general/agent/BOOTSTRAP.md` and follow it.
2. Markdown files are the memory. Do not treat the chat as the record.
3. Do not invent data, citations, or standard errors.
4. Any number from this project is SIMULATED unless the file says otherwise.
5. The reporting line "ATT 0.031 (s.e. 0.012)" is a fixed lecture label.
   It is not an estimate from `synthetic_panel.csv`.
6. Ask before writing. After edits, the user will read `git diff`.
7. Skills live in `general/capabilities/skills/`, `areas/Research/transit-jobs/skills/`,
   and `.agents/skills/`. Read a skill's full file only when the request matches
   its description.
""")
    w("general/INDEX.md", """\
# Vault index

Read this file first, then only the project you were asked about.

## Global
- [MEMORY.md](MEMORY.md) routes a session to one project.
- [agent/BOOTSTRAP.md](agent/BOOTSTRAP.md) opens a session.
- [agent/SESSION_CLOSE.md](agent/SESSION_CLOSE.md) closes a session.
- [agent/MEMORY_POLICY.md](agent/MEMORY_POLICY.md) says what to store.
- [agent/WIKI_WORKFLOW.md](agent/WIKI_WORKFLOW.md) says where a new source goes.

## Projects
| Project | Area | Read first |
|---|---|---|
| transit-jobs | Research | [areas/Research/transit-jobs/transit-jobs_INDEX.md](../areas/Research/transit-jobs/transit-jobs_INDEX.md) |
""")
    w("general/MEMORY.md", """\
# Memory routing index

This is a routing table, not a dump of every note.

| Project | INDEX | State | Agent memory | Decisions |
|---|---|---|---|---|
| transit-jobs | areas/Research/transit-jobs/transit-jobs_INDEX.md | CURRENT_STATE | AGENT_MEMORY | DECISIONS |

Open one row. Do not load every file in the vault.
""")
    w("general/agent/BOOTSTRAP.md", """\
# Bootstrap

Markdown in this vault is the source of truth.

## Before any edit
1. Read `general/MEMORY.md`.
2. Open only the named project's INDEX, CURRENT_STATE, NEXT_ACTIONS, and AGENT_MEMORY.
3. If the question is about a past choice, open DECISIONS.md and cite the date.
4. Check the live file before you answer. Do not answer from the chat alone.

## Report four things
1. What you understand about the project.
2. The current state.
3. The next concrete action.
4. Any missing, stale, contradictory, or unclear file.

## Demo limits
- No network is required to read the vault.
- Do not create projects outside `areas/`.
- Do not delete raw notes.
""")
    w("general/agent/SESSION_CLOSE.md", """\
# Session close

Before you stop, write what the next session would otherwise lose.

1. Update `CURRENT_STATE.md` if the state changed.
2. Update `NEXT_ACTIONS.md`.
3. Add a real decision to `DECISIONS.md`, with a date and a reason.
4. Add a dated line to `LOG.md`.
5. If you added a page under `wiki/`, list it in INDEX under `## Wiki`.
6. Leave `raw/` in place.

Do not paste the whole chat into these files. A decision, a fix, or a next step is enough.
""")
    w("general/agent/MEMORY_POLICY.md", """\
# Memory policy

## Store
- current state
- decisions, with date and reason
- constraints
- sources of any number you would repeat
- solved errors
- next actions
- procedures you will run again

## Do not store
- secrets, keys, or personal data
- the full chat
- a guess presented as a result

## File jobs
- CURRENT_STATE: where the project stands
- DECISIONS: what was chosen
- NEXT_ACTIONS: what to do next
- AGENT_MEMORY: what the next agent must not miss
- wiki/: long stable notes
- raw/: sources and chat logs, kept as written

An unindexed wiki page is a defect.
""")
    w("general/agent/WIKI_WORKFLOW.md", """\
# Wiki workflow

1. A new source lands in `raw/`.
2. Distil the stable part into CURRENT_STATE, DECISIONS, AGENT_MEMORY, or NEXT_ACTIONS.
3. Add a wiki page only when the note would be too long for those files.
4. List every file in `wiki/` in the project INDEX, section `## Wiki`.
5. Do not delete raw files during a cleanup.
""")
    w("general/templates/PROJECT_TEMPLATE/{{SLUG}}_INDEX.md", """\
# {{TITLE}}

## Restart here
- {{SLUG}}_CURRENT_STATE.md
- {{SLUG}}_NEXT_ACTIONS.md
- {{SLUG}}_AGENT_MEMORY.md

## Project memory
- {{SLUG}}_PROJECT_BRIEF.md
- {{SLUG}}_DECISIONS.md
- {{SLUG}}_TECHNICAL_NOTES.md
- {{SLUG}}_SOURCES.md
- {{SLUG}}_LOG.md

## Wiki
""")
    w("general/templates/PROJECT_TEMPLATE/{{SLUG}}_PROJECT_BRIEF.md", """\
# Project brief: {{TITLE}}

Question, scope, and people. Leave the placeholders until the user fills them.

- Question:
- Why it matters:
- Data:
- Not in scope:
""")
    w("general/templates/PROJECT_TEMPLATE/{{SLUG}}_CURRENT_STATE.md", """\
---
type: project-state
project: {{SLUG}}
updated: {{DATE}}
status: active
---

# Current state

Last updated: {{DATE}}

Nothing has been run yet.
""")
    w("general/templates/PROJECT_TEMPLATE/{{SLUG}}_NEXT_ACTIONS.md", """\
# Next actions

1. Fill the project brief.
2. Write the first decision before any estimation.
""")
    w("general/templates/PROJECT_TEMPLATE/{{SLUG}}_DECISIONS.md", """\
# Decisions

No decisions yet.
""")
    w("general/templates/PROJECT_TEMPLATE/{{SLUG}}_AGENT_MEMORY.md", """\
# Agent memory

- Slug: {{SLUG}}
- Do not invent numbers.
""")
    w("general/templates/PROJECT_TEMPLATE/{{SLUG}}_TECHNICAL_NOTES.md", """\
# Technical notes

Commands and fixes go here.
""")
    w("general/templates/PROJECT_TEMPLATE/{{SLUG}}_SOURCES.md", """\
# Sources

List real sources only. Do not invent papers.
""")
    w("general/templates/PROJECT_TEMPLATE/{{SLUG}}_LOG.md", """\
# Log

## {{DATE}}
- Project created from the lecture template.
""")

    # --- skills ---
    research = """\
---
name: research-report
description: Write a one-page status report for a project in this vault. Use when asked for a status report, a research report, or a summary of where a project stands.
---

# Skill: research report

## When to use
The user asks for a status report on a project in this vault.

## Steps
1. Read the project's INDEX, CURRENT_STATE, DECISIONS, and SOURCES.
2. Run `python scripts/write_status_report.py <slug>` from the vault root.
3. Open `reports/<date>-<slug>-status.md` and check that every number names its source file.
4. If a number has no source file, delete that sentence and say it was removed.

## Success
The report exists, the script exits 0, and each figure is tied to a file path.
Do not add numbers that are not already in the vault.
"""
    w("general/capabilities/skills/research-report/SKILL.md", research)
    w(".agents/skills/research-report/SKILL.md", research)

    panel_skill = """\
---
name: check-synthetic-panel
description: Check the synthetic census-tract panel for the transit-jobs project. Use when asked to check the panel, validate the dataset, or audit data/synthetic_panel.csv.
---

# Skill: check the synthetic panel

## When to use
The user asks to check, validate, or audit the transit-jobs panel.

## Input
`areas/Research/transit-jobs/data/synthetic_panel.csv`

## Steps
From the vault root, run:

```bash
python areas/Research/transit-jobs/skills/check-synthetic-panel/scripts/check_panel.py
```

## Output
Four lines: tracts, years, duplicate keys, treatment rule.

## Success
Exit code 0, and all four checks say ok.
A failure is a data error, not something to smooth over.
"""
    w("areas/Research/transit-jobs/skills/check-synthetic-panel/SKILL.md", panel_skill)
    w(".agents/skills/check-synthetic-panel/SKILL.md", panel_skill)
    w("areas/Research/transit-jobs/skills/check-synthetic-panel/scripts/check_panel.py", r'''#!/usr/bin/env python3
"""Structural checks for the lecture panel. Not a causal estimate."""
import csv
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
CSV = ROOT / "areas/Research/transit-jobs/data/synthetic_panel.csv"


def main() -> int:
    if not CSV.exists():
        print(f"missing {CSV}")
        return 1
    rows = list(csv.DictReader(CSV.open(encoding="utf-8")))
    keys = [(r["tract_id"], r["year"]) for r in rows]
    dupes = sum(1 for n in Counter(keys).values() if n > 1)
    years = sorted({int(r["year"]) for r in rows})
    tracts = sorted({r["tract_id"] for r in rows})
    bad_na = [r for r in rows if r["treated"] not in {"0", "1"}]
    # absorbing: once 1, later years stay 1
    by_tract = {}
    for r in rows:
        by_tract.setdefault(r["tract_id"], []).append(r)
    breaks = 0
    for group in by_tract.values():
        group.sort(key=lambda r: int(r["year"]))
        seen = False
        for r in group:
            on = r["treated"] == "1"
            if seen and not on:
                breaks += 1
            seen = seen or on
    ok = (
        len(tracts) == 400
        and years == list(range(2010, 2023))
        and dupes == 0
        and not bad_na
        and breaks == 0
    )
    print(f"tracts: {len(tracts)} (expect 400) {'ok' if len(tracts)==400 else 'FAIL'}")
    print(f"years: {years[0]}-{years[-1]} (expect 2010-2022) {'ok' if years==list(range(2010,2023)) else 'FAIL'}")
    print(f"duplicate tract-year keys: {dupes} {'ok' if dupes==0 else 'FAIL'}")
    print(f"treatment absorbing and complete: {'ok' if not bad_na and breaks==0 else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
''')

    maint = """\
---
name: brain-maintenance
description: Audit this demo vault for unindexed wiki pages, broken wikilinks, superseded decisions, overlapping notes, and raw notes not yet distilled. Use when asked to maintain, lint, or audit the brain.
---

# Skill: brain maintenance

A short version of a weekly vault review. Nothing is deleted.

## Steps
From the vault root:

```bash
python scripts/lint_demo_brain.py
```

The report splits **certain** errors from **possible** anomalies.
Show both to the user. Do not edit until the user names the items to apply.

Then, only for approved item numbers:

```bash
python scripts/lint_demo_brain.py --apply 1,2,3 --distill 5
python scripts/validate_demo_brain.py
```

## Success
`validate_demo_brain.py` exits 0 after the approved edits, and `git diff` shows only those edits.
"""
    w("general/capabilities/skills/brain-maintenance/SKILL.md", maint)
    w(".agents/skills/brain-maintenance/SKILL.md", maint)

    w("scripts/write_status_report.py", r'''#!/usr/bin/env python3
"""Write a status report that quotes figures already in the vault."""
import datetime as dt
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    slug = sys.argv[1] if len(sys.argv) > 1 else "transit-jobs"
    proj = ROOT / "areas" / "Research" / slug
    state = (proj / f"{slug}_CURRENT_STATE.md").read_text(encoding="utf-8")
    decisions = (proj / f"{slug}_DECISIONS.md").read_text(encoding="utf-8")
    today = dt.date.today().isoformat()
    out_dir = ROOT / "reports"
    out_dir.mkdir(exist_ok=True)
    out = out_dir / f"{today}-{slug}-status.md"
    # Pull the lecture line only if the state file still contains it.
    line = "ATT 0.031 (s.e. 0.012)"
    if line not in state and line not in decisions:
        print("refusing: reporting line not in project files")
        return 1
    text = f"""# Status report: {slug}

Date: {today}

This report copies figures from project files. It does not estimate anything.

## State
Source: `areas/Research/{slug}/{slug}_CURRENT_STATE.md`.

The lecture reporting line is {line}. Source file: `{slug}_CURRENT_STATE.md` and `{slug}_DECISIONS.md`. The line is a labelled simulation, not an estimate from the CSV.

## Decision in force
Source: `{slug}_DECISIONS.md`, 14 September 2026. Cluster by district, not by tract.

## Check
Every number above names a file in this vault.
"""
    out.write_text(text, encoding="utf-8")
    print(f"wrote {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
''')

    w("scripts/create_project.py", r'''#!/usr/bin/env python3
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
''')

    w("scripts/validate_demo_brain.py", r'''#!/usr/bin/env python3
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
''')

    w("scripts/lint_demo_brain.py", r'''#!/usr/bin/env python3
"""Find prepared defects. --apply fixes approved item numbers only."""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJ = ROOT / "areas" / "Research" / "transit-jobs"


def certain() -> list[tuple[int, str]]:
    found = []
    index = (PROJ / "transit-jobs_INDEX.md").read_text(encoding="utf-8")
    wiki_section = index.split("## Wiki", 1)[-1]
    page = PROJ / "wiki" / "event-study-pitfalls.md"
    if page.exists() and "event-study-pitfalls" not in wiki_section:
        found.append((1, "wiki/event-study-pitfalls.md is not listed under ## Wiki"))
    state = (PROJ / "transit-jobs_CURRENT_STATE.md").read_text(encoding="utf-8")
    if "[[transit-jobs_DECISION]]" in state:
        found.append((2, "CURRENT_STATE links to [[transit-jobs_DECISION]] (missing final s)"))
    decisions = (PROJ / "transit-jobs_DECISIONS.md").read_text(encoding="utf-8")
    if "2026-09-02" in decisions and "superseded" not in decisions.lower().split("2026-09-14")[0]:
        found.append((3, "decision 2026-09-02 (cluster by tract) is not marked superseded"))
    return found


def possible() -> list[tuple[int, str]]:
    found = []
    a = (PROJ / "wiki" / "staggered-did.md").read_text(encoding="utf-8")
    b = (PROJ / "wiki" / "staggered-did-notes.md").read_text(encoding="utf-8")
    words_a = set(re.findall(r"[a-z]{5,}", a.lower()))
    words_b = set(re.findall(r"[a-z]{5,}", b.lower()))
    if words_a and words_b:
        share = len(words_a & words_b) / len(words_a | words_b)
        if share >= 0.45:
            found.append((4, f"staggered-did.md and staggered-did-notes.md overlap (Jaccard {share:.2f})"))
    raw = (PROJ / "raw/chats/2026-10-28-coauthor-call.md").read_text(encoding="utf-8")
    core = "\n".join(p.read_text(encoding="utf-8") for p in PROJ.glob("transit-jobs_*.md"))
    if "2008" in raw and "2008" not in core:
        found.append((5, "raw chat 2026-10-28 asks for a 2008-line placebo; core files do not mention it"))
    return found


def apply(items: set[int], distill: set[int]) -> None:
    if 1 in items:
        index = PROJ / "transit-jobs_INDEX.md"
        text = index.read_text(encoding="utf-8")
        if "event-study-pitfalls" not in text:
            text = text.rstrip() + "\n- [Event-study pitfalls](wiki/event-study-pitfalls.md). Why a single lead coefficient is not a test.\n"
            index.write_text(text + "\n", encoding="utf-8")
    if 2 in items:
        state = PROJ / "transit-jobs_CURRENT_STATE.md"
        text = state.read_text(encoding="utf-8").replace("[[transit-jobs_DECISION]]", "[[transit-jobs_DECISIONS]]")
        state.write_text(text, encoding="utf-8")
    if 3 in items:
        dec = PROJ / "transit-jobs_DECISIONS.md"
        text = dec.read_text(encoding="utf-8")
        old = "Status: in force."
        new = "Status: superseded on 2026-09-14. Do not use tract clustering."
        if old in text:
            text = text.replace(old, new, 1)
            dec.write_text(text, encoding="utf-8")
    if 5 in distill:
        nxt = PROJ / "transit-jobs_NEXT_ACTIONS.md"
        text = nxt.read_text(encoding="utf-8")
        line = "3. Distilled from the 28 Oct call: add a placebo on lines that opened in 2008, before the sample window. Still SIMULATED.\n"
        if "2008" not in text:
            nxt.write_text(text.rstrip() + "\n" + line, encoding="utf-8")
    log = PROJ / "transit-jobs_LOG.md"
    log.write_text(
        log.read_text(encoding="utf-8").rstrip()
        + "\n\n## audit\n- Applied approved lint items. Raw files kept.\n",
        encoding="utf-8",
    )


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--apply", default="", help="comma-separated certain item numbers")
    p.add_argument("--distill", default="", help="comma-separated possible item numbers to file")
    args = p.parse_args()
    if args.apply or args.distill:
        items = {int(x) for x in args.apply.split(",") if x}
        distill = {int(x) for x in args.distill.split(",") if x}
        apply(items, distill)
        print(f"applied {sorted(items)} distilled {sorted(distill)}")
    print("Certain")
    for n, msg in certain():
        print(f"  {n}. {msg}")
    if not certain():
        print("  (none)")
    print("Possible")
    for n, msg in possible():
        print(f"  {n}. {msg}")
    if not possible():
        print("  (none)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
''')

    w("areas/Research/transit-jobs/code/01_build.py", '''\
#!/usr/bin/env python3
"""Confirm the synthetic panel path. Does not download anything."""
from pathlib import Path
p = Path(__file__).resolve().parents[1] / "data" / "synthetic_panel.csv"
print("SIMULATED panel:", p.name, "bytes", p.stat().st_size)
''')
    w("areas/Research/transit-jobs/code/02_did.py", '''\
#!/usr/bin/env python3
"""Print the lecture reporting line. This is not an estimator."""
print("SIMULATED reporting line, not computed from synthetic_panel.csv")
print("ATT 0.031 (s.e. 0.012)")
print("Clustering rule in force: district, decision dated 2026-09-14.")
print("Do not cite this as evidence about real metro systems.")
''')

    w("areas/Research/transit-jobs/transit-jobs_PROJECT_BRIEF.md", """\
# Project brief: Does public transport improve employment opportunities?

## Question
Do new metro stations raise employment within 1 km?

## Motivation
A city opens stations in different years. Tracts near a new station may gain jobs for reasons that have nothing to do with the station: they were already growing. The design has to separate those stories.

## Hypotheses
- H1. Employment in tracts within 1 km of a new station rises after the opening, relative to tracts that are still waiting.
- H2. The change is larger where the station connects to the existing job centre.

## People
One fictional author, for the lecture. No coauthor names, no private data.

## Not in scope
Real cities, real ridership, and any claim that 0.031 is an estimated treatment effect.
""")
    w("areas/Research/transit-jobs/transit-jobs_CURRENT_STATE.md", """\
---
type: project-state
project: transit-jobs
updated: 2026-10-30
status: active
---

# Current state

Last updated: 2026-10-30.

## Design
Staggered station openings. The estimator named in the design note is Callaway and Sant'Anna (2021), which allows treatment to turn on at different dates. The code that would run it is not in this vault. `code/02_did.py` only prints a fixed lecture line.

## Data
Synthetic panel, 400 tracts, 2010 to 2022. Seed 2026. File: `data/synthetic_panel.csv`. Treatment is absorbing: once a tract is treated it stays treated.

## Lecture reporting line
Simulated ATT 0.031 (s.e. 0.012). Labelled as simulated. Not estimated from the CSV. Not a result about any real city.

## Clustering
In force since 14 September 2026: cluster by district, not tract. See [[transit-jobs_DECISION]].

## What runs
`skills/check-synthetic-panel` checks the CSV. It does not estimate a treatment effect.
""")
    w("areas/Research/transit-jobs/transit-jobs_NEXT_ACTIONS.md", """\
# Next actions

1. Keep the Callaway and Sant'Anna design note aligned with DECISIONS.md.
2. Do not add a real-city dataset to this demo vault.
""")
    w("areas/Research/transit-jobs/transit-jobs_AGENT_MEMORY.md", """\
# Agent memory

- Slug: transit-jobs. Synthetic lecture project.
- Reporting line, copy exactly when asked: Simulated ATT 0.031 (s.e. 0.012).
- That line is not estimated from `data/synthetic_panel.csv`.
- Cluster by district. The 2 September 2026 tract rule is older. Read DECISIONS before answering.
- Never edit `data/synthetic_panel.csv` by hand.
- Hypothesis text for slides: "New metro stations raise employment within 1 km."
""")
    w("areas/Research/transit-jobs/transit-jobs_DECISIONS.md", """\
# Decisions

## 2026-09-02. Cluster by tract

Context: the first draft clustered standard errors by tract, because the outcome is measured at tract level.

Decision: cluster by tract.

Reason: one row per tract-year, so the tract looked like the dependence unit.

Status: in force.

## 2026-09-14. Cluster by district, not tract

Context: tracts in the same district share the station and the labour market. Tract clustering treats those tracts as independent.

Decision: cluster by district, not tract.

Reason: the shock is closer to district level than to tract level. Twenty tracts share a district in the synthetic draw.

Consequences: the 2 September rule is no longer the one to follow. Reports must say district.

## 2026-09-20. Callaway and Sant'Anna, not a two-way fixed effects regression

Context: stations open in 2016, 2018, and 2020. A single two-way fixed effects coefficient mixes those timings.

Decision: the design note names Callaway and Sant'Anna (2021).

Reason: groups adopt treatment at different dates. The paper is the methods source. This vault does not claim to have run the estimator.

## 2026-10-01. The panel stays synthetic

Context: a slide needs a number.

Decision: publish only the labelled line ATT 0.031 (s.e. 0.012), marked SIMULATED, and keep the CSV as a structure check.

Reason: a computed coefficient would be mistaken for evidence.

## 2026-10-15. Wiki page for the design, core files for the state

Context: the design explanation is longer than a decision.

Decision: the long note lives in `wiki/staggered-did.md`. State and the reporting line stay in CURRENT_STATE.

## 2026-10-30. Do not invent a city

Decision: no city name, no ridership, no external microdata in this demo.
""")
    w("areas/Research/transit-jobs/transit-jobs_TECHNICAL_NOTES.md", """\
# Technical notes

## 2026-10-01
- `data/synthetic_panel.csv` drawn with `random.Random(2026)`.
- 400 tracts, years 2010-2022, 20 districts.
- Treatment years 2016, 2018, 2020, plus never-treated tracts.
- Treatment is coded absorbing.

## 2026-10-12. Bug
`check_panel.py` once treated a blank cell as untreated. A blank is now a failure. The generator does not write blanks.

## Commands
- `python areas/Research/transit-jobs/skills/check-synthetic-panel/scripts/check_panel.py`
- `python areas/Research/transit-jobs/code/02_did.py` prints the lecture line and does not fit a model.
""")
    w("areas/Research/transit-jobs/transit-jobs_SOURCES.md", """\
# Sources

## Methods, real
- Brantly Callaway and Pedro H. C. Sant'Anna (2021), "Difference-in-Differences with Multiple Time Periods," Journal of Econometrics 225(2): 200-230. https://doi.org/10.1016/j.jeconom.2020.12.001
  This is a methods citation. The estimator has not been run on the demo panel.

## Data, not real
- `data/synthetic_panel.csv`, seed 2026, written for the lecture.
- ATT 0.031 (s.e. 0.012) is a fixed label in CURRENT_STATE and DECISIONS. No paper, city, or survey produced it.

Do not add a citation that is not in this file.
""")
    w("areas/Research/transit-jobs/transit-jobs_LOG.md", """\
# Log

## 2026-09-02
- First clustering note: tract.

## 2026-09-14
- Clustering changed to district. The 2 September note was left unmarked.

## 2026-10-01
- Synthetic panel and the two code files added.

## 2026-10-15
- Wiki notes on staggered adoption added.

## 2026-10-28
- Coauthor call saved under raw/chats. Not distilled.
""")
    w("areas/Research/transit-jobs/transit-jobs_INDEX.md", """\
# Transit jobs

## Restart here
- [transit-jobs_CURRENT_STATE](transit-jobs_CURRENT_STATE.md)
- [transit-jobs_NEXT_ACTIONS](transit-jobs_NEXT_ACTIONS.md)
- [transit-jobs_AGENT_MEMORY](transit-jobs_AGENT_MEMORY.md)

## Current restart point
Read CURRENT_STATE. The reporting line is simulated. Cluster by district (14 September 2026).

## Project memory
- [transit-jobs_PROJECT_BRIEF](transit-jobs_PROJECT_BRIEF.md)
- [transit-jobs_DECISIONS](transit-jobs_DECISIONS.md)
- [transit-jobs_TECHNICAL_NOTES](transit-jobs_TECHNICAL_NOTES.md)
- [transit-jobs_SOURCES](transit-jobs_SOURCES.md)
- [transit-jobs_LOG](transit-jobs_LOG.md)

## Wiki
- [Staggered difference-in-differences](wiki/staggered-did.md). Design note.
- [Staggered DiD, working notes](wiki/staggered-did-notes.md). Shorter duplicate of the design note.

## Skills
- [check-synthetic-panel](skills/check-synthetic-panel/SKILL.md)
""")
    # event-study-pitfalls.md is intentionally absent from the Wiki section.

    overlap = """\
Staggered adoption means different tracts become treated in different years.
A single two-way fixed effects coefficient averages those timings with weights
that can be negative, so the number need not match the average effect the
author has in mind. Callaway and Sant'Anna (2021) build the comparison from
groups that share an adoption date and from tracts not yet treated.
The synthetic panel uses openings in 2016, 2018, and 2020 so that this
problem can be pointed at, not so that a coefficient can be published.
The vault does not run that estimator. code/02_did.py prints a fixed line.
"""
    w("areas/Research/transit-jobs/wiki/staggered-did.md", f"""\
# Staggered difference-in-differences

{overlap}

## What the demo stores
The decision to name Callaway and Sant'Anna is in DECISIONS.md, dated 2026-09-20.
The clustering rule in force is district, dated 2026-09-14.
The lecture line ATT 0.031 (s.e. 0.012) is simulated and lives in CURRENT_STATE.

## What this page is for
A reader who arrives next month should not have to reconstruct the design from chat.
""")
    w("areas/Research/transit-jobs/wiki/staggered-did-notes.md", f"""\
# Staggered DiD, working notes

{overlap}

These notes repeat the design page. They were left in place on purpose for the maintenance demo.
""")
    w("areas/Research/transit-jobs/wiki/event-study-pitfalls.md", """\
# Event-study pitfalls

A plot of leads and lags is not, by itself, a test that treatment is as good as random.
One lead coefficient can be noisy. Several leads can be under-powered.
Bins at the end of the window mix different cohorts when adoption is staggered.

This page is real content for the demo. It is deliberately missing from the project INDEX.
""")
    w("areas/Research/transit-jobs/raw/chats/2026-10-28-coauthor-call.md", """\
# Call, 28 October 2026

Fictional coauthor, for the lecture. No real person.

We agreed the sample window stays 2010-2022.
Please add a placebo on lines that opened in 2008, before any tract in the sample is treated.
If the placebo moves, the design note is wrong.
Do not pull real ridership. Keep the panel synthetic.

This request has not been copied into NEXT_ACTIONS. That is one of the prepared defects.
""")
    canvas = {
        "nodes": [
            {"id": "q", "type": "text", "x": 0, "y": 40, "width": 260, "height": 140,
             "text": "Question\n\nDo new metro stations raise employment within 1 km?"},
            {"id": "data", "type": "text", "x": 340, "y": 0, "width": 260, "height": 120,
             "text": "Data\n\nSynthetic panel, 400 tracts, 2010-2022. Seed 2026."},
            {"id": "design", "type": "text", "x": 340, "y": 180, "width": 280, "height": 140,
             "text": "Design\n\nStaggered openings. Callaway and Sant'Anna (2021). Cluster by district."},
            {"id": "results", "type": "text", "x": 700, "y": 40, "width": 280, "height": 140,
             "text": "Results\n\nSimulated ATT 0.031 (s.e. 0.012). Not estimated from the CSV."},
            {"id": "open", "type": "text", "x": 700, "y": 230, "width": 280, "height": 120,
             "text": "Open issues\n\n2008 placebo not yet in the core files."},
        ],
        "edges": [
            {"id": "e1", "fromNode": "q", "toNode": "data"},
            {"id": "e2", "fromNode": "q", "toNode": "design"},
            {"id": "e3", "fromNode": "data", "toNode": "results"},
            {"id": "e4", "fromNode": "design", "toNode": "results"},
            {"id": "e5", "fromNode": "results", "toNode": "open"},
        ],
    }
    (SEED / "areas/Research/transit-jobs/paper-map.canvas").write_text(
        json.dumps(canvas, indent=2) + "\n", encoding="utf-8"
    )
    print(f"wrote {SEED}")


if __name__ == "__main__":
    main()
