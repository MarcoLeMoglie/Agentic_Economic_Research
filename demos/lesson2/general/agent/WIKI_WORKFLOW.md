---
title: LLM Wiki Workflow
type: protocol
status: active
updated: 2026-11-18
---

# WIKI_WORKFLOW — Ingest, Query, Lint, Promote

A deliberately small wiki loop, in the spirit of Karpathy's "LLM wiki": sources come in, claims get distilled, links get checked, and only genuinely reusable knowledge is promoted. The wiki is **not** the default destination for new knowledge.

## The core rule

> **Update the project's core memory files first. Create or extend a wiki page only when the content is sufficiently long, stable, or modular.**

"Sufficiently" means at least two of:

- longer than roughly 80 lines of self-contained explanation;
- stable across at least two sessions, or backed by a completed analysis;
- reused by a second project, question, or document;
- modular enough to be cited as a unit (a method, a definition, a protocol).

If it fails those tests, it belongs in `CURRENT_STATE.md`, `DECISIONS.md`, `TECHNICAL_NOTES.md`, or `SOURCES.md`. A premature wiki page forks the truth.

## Layout

```text
areas/<Area>/<slug>/
├── INDEX.md          # must link every wiki page
├── ...               # 11 core files
├── raw/              # original sources, never edited
└── wiki/             # long, stable, modular notes
    └── kebab-case.md
```

Global, cross-project wiki content is not created by default. If a page is genuinely cross-project, promote it to `general/` as documentation or to a skill, and record the move in [GLOBAL_DECISIONS.md](../GLOBAL_DECISIONS.md).

## 1. Ingest

Acquire and register before interpreting.

1. **Place the original** in `raw/` with a dated, descriptive name: `2026-11-18-source-short-title.md` (or `.pdf`, `.txt`, `.csv` kept as-is).
2. **Never edit the original.** If it needs cleaning, create a derived file and name the transformation.
3. **Register it in `SOURCES.md`:** ID, title, author/publisher, date, type, location, access date, reliability note, status (`acquired`, `partial`, `unavailable`).
4. **Label the synthetic/real status.** Demo material gets `SYNTHETIC` in the first line.
5. **Extract claims, not vibes.** For each material claim: statement, locator (page/section/line), direction of evidence, and the author's own interpretation versus yours.
6. **Distinguish** finding / interpretation / speculation / your inference. Use separate labels.
7. **Write the distillation into the owning core file** (usually `CURRENT_STATE.md` for state, `SOURCES.md` for provenance, `TECHNICAL_NOTES.md` for method detail). Add a `LOG.md` entry.
8. **Only then** decide whether a wiki page is warranted.

**Never invent** a source, quotation, number, author, or date. If a document is unavailable, record `status: unavailable` and the reason. An empty register entry is honest; a plausible-looking fake citation is corruption.

## 2. Query

Retrieve with indexes before search, and search before reading wholesale.

1. Start at the project's `INDEX.md`; follow only relevant links.
2. If the index does not point to an answer, use `general/MEMORY.md` to confirm scope, then search the project folder:

```bash
grep -rn --include='*.md' -i 'search term' areas/Research/public-transport-employment
```

3. Read the smallest matching section, not the whole file. For `LOG.md`, read the tail only.
4. Prefer primary sources in `raw/` over summaries when the claim is contested.
5. Answer with provenance: file path and, where relevant, the source ID.
6. If the answer is not in the vault, say **"not recorded"** and record the gap as an open question or a next action. Do not fill it from model memory and present it as vault knowledge.

Query patterns that work: "what did we decide about X and why", "what is blocked", "what do we know about Y, with sources", "what changed since DATE".

## 3. Lint

Run after structural edits, at session close, and at least monthly. The validator automates the mechanical checks; the rest needs judgement.

**Automatic** (`bash .infra/scripts/validate.sh`):

- required directories and global files exist;
- every project has all 11 core files;
- registered projects resolve to a real `INDEX.md` (and every real project is registered);
- relative links resolve to existing files/directories;
- every existing wiki page is linked from its project's `INDEX.md`.

**Manual checklist:**

- [ ] Duplicate pages covering the same concept → merge, leave a link, mark the loser `deprecated`.
- [ ] Contradictions → `> [!warning] Unresolved contradiction` block with both claims, dates, and files; then resolve or ask.
- [ ] Stale claims → check the date and source; mark `status: stale` with a review date; do not silently rewrite.
- [ ] Orphan notes → link from `INDEX.md` or delete if truly redundant (keep provenance in Git).
- [ ] Over-long core files → split stable sections into a wiki page, then link it.
- [ ] Wiki pages that duplicate core files → core files win; reduce the wiki page to the stable part.
- [ ] Undated decisions → add dates or move to open questions.
- [ ] Unsourced numbers → find the source or mark them as illustrative.
- [ ] Secrets scan → no keys, tokens, passwords, or private data.

**Contradiction format:**

```markdown
> [!warning] Unresolved contradiction (2026-11-18)
> `CURRENT_STATE.md` says the rollout began in 2019; `raw/2026-11-10-program-note.md` says 2020.
> Neither is verified. Resolution requires the implementing agency's timetable. Tracked as A-03.
```

## 4. Promotion

Promotion is a deliberate move up the stability ladder:

```text
conversation insight
  -> core project file        (default; immediate)
  -> project wiki page        (long, stable, modular)
  -> global documentation     (cross-project, stable)
  -> skill                    (reusable procedure, executable)
```

**Promote to a wiki page when:** the content is stable and long, and the core files would become bloated by keeping it inline. Create the page with frontmatter, link it from `INDEX.md`, and replace the inline detail with a one-line link.

**Promote to global documentation when:** two unrelated projects rely on it. Move it, leave a redirect line in the old location, and log the move.

**Promote to a skill when:** the knowledge is a *procedure* that another agent must execute, not just read. A skill needs: name, description (when to use / when not), inputs, numbered steps, output format, quality bar, failure modes. Store it once under `general/capabilities/skills/<name>/SKILL.md`; expose it via `.agents/skills/`.

**Never promote** unverified claims, one-off project results, or anything containing private data. Promotion does not upgrade truth status.

## Page template

```markdown
---
title: Page Title
type: wiki
status: active
project: project-slug
updated: 2026-11-18
sources: [S-001]
---

# Page Title

**Scope:** what this page covers and what it does not.

## Summary
Three to six sentences a reader can rely on.

## Detail
The stable explanation. Sections, tables, formulas as needed.

## Limits and open questions
What is uncertain, contested, or version-dependent.

## Related
- [Project index](../INDEX.md)
- [Related note](related-note.md)
```

Every page ends with a link back to the project index. Every page states its limits. A page with no limits is usually a page that has not been checked.
