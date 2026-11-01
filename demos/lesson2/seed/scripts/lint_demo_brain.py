#!/usr/bin/env python3
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
