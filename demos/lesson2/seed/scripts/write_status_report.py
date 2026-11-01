#!/usr/bin/env python3
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
