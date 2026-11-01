#!/usr/bin/env python3
"""Structural checks for the lecture panel. Not a causal estimate."""
import csv
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
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
