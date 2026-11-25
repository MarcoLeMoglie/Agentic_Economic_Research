# Global Decisions

Decisions that bind the whole Brain. Project decisions live in each project's `DECISIONS.md`. Append only: supersede an entry with a new dated entry and mark the old one `superseded by D-xxx`; never rewrite history to look cleaner.

| ID | Date | Decision | Status |
|---|---|---|---|
| D-001 | 2026-11-18 | Markdown is the canonical memory format | active |
| D-002 | 2026-11-18 | `MEMORY.md` is a router, not a store | active |
| D-003 | 2026-11-18 | Core files are updated before wiki pages are created | active |
| D-004 | 2026-11-18 | Strict project isolation with on-demand cross-links | active |
| D-005 | 2026-11-18 | No secrets, credentials, or transcripts in the vault | active |
| D-006 | 2026-11-18 | Skills are stored once and discovered by metadata | active |
| D-007 | 2026-11-18 | Synthetic example data must be visibly labelled | active |
| D-008 | 2026-11-18 | Relative Markdown links, not wikilinks | active |

---

## D-001 — Markdown is canonical

**Date:** 2026-11-18
**Decision:** All durable knowledge is stored as plain Markdown inside this vault.
**Rationale:** Portable across Obsidian, editors, Git, and any AI runtime; readable without tooling; diffable; survives product churn.
**Consequences:** No database, embedding store, or sync service is required or authoritative. Any external memory tool is an optional mirror. Formatting must stay simple enough to read as text.

## D-002 — `MEMORY.md` is a router

**Date:** 2026-11-18
**Decision:** `general/MEMORY.md` contains a project registry and short-lived global facts only. It must stay compact enough to read at every session start.
**Rationale:** A growing memory dump becomes expensive to load, hard to trust, and impossible to audit. Routing keeps bootstrap cheap.
**Consequences:** New knowledge goes to the owning project or protocol. If `MEMORY.md` exceeds roughly 120 lines, move detail out rather than compressing it into ambiguity.

## D-003 — Core files before wiki pages

**Date:** 2026-11-18
**Decision:** Update `CURRENT_STATE.md`, `NEXT_ACTIONS.md`, `DECISIONS.md`, and `AGENT_MEMORY.md` first. Create or extend a `wiki/` page only when content is long, stable, and modular (see [WIKI_WORKFLOW.md](agent/WIKI_WORKFLOW.md)).
**Rationale:** Premature wiki pages fork the truth and go stale; the core files are what the next agent actually reads.
**Consequences:** A wiki page must be indexed from the project's `INDEX.md` and must not contradict core files. Validation checks indexing.

## D-004 — Strict project isolation

**Date:** 2026-11-18
**Decision:** A session loads one project's core files by default. Cross-project reads happen only on explicit request or through a named link.
**Rationale:** Context budget, privacy between domains, and fewer cross-contamination errors.
**Consequences:** Global files must never accumulate project detail. Shared knowledge is promoted deliberately, with provenance.

## D-005 — No secrets or transcripts

**Date:** 2026-11-18
**Decision:** Passwords, API keys, tokens, private credentials, unnecessary personal data, and full conversation transcripts are never written to the vault.
**Rationale:** The vault is plain text, often synced and versioned; secrets are effectively published once committed.
**Consequences:** Record *where* a secret lives, never its value. If a secret is committed, rotate it and rewrite history; deleting the line is not enough. See [MEMORY_POLICY.md](agent/MEMORY_POLICY.md).

## D-006 — Skills stored once, discovered by metadata

**Date:** 2026-11-18
**Decision:** Each skill has one canonical `SKILL.md` under `general/capabilities/skills/<name>/`. Runtimes that scan `.agents/skills/` get a relative symlink. Agents read metadata first and load bodies only on match.
**Rationale:** Avoids per-model drift and avoids loading every instruction into every context.
**Consequences:** Editing the canonical file updates every adapter. If symlinks are unsupported on a platform, copy the folder and record the copy as deprecated in favour of the canonical path.

## D-007 — Synthetic content must be labelled

**Date:** 2026-11-18
**Decision:** Illustrative projects and data are marked synthetic in the project `INDEX.md`, `PROJECT_BRIEF.md`, and every `raw/` document.
**Rationale:** A demo must never be mistaken for evidence.
**Consequences:** No fabricated estimates or citations, even inside examples. Hypotheses use "would", "expected", "to be tested".

## D-008 — Relative Markdown links

**Date:** 2026-11-18
**Decision:** Use standard relative Markdown links; do not use `[[wikilinks]]` or absolute filesystem paths.
**Rationale:** Renders in Obsidian, GitHub, VS Code, and plain viewers; validation can resolve targets; the vault stays movable.
**Consequences:** Renaming a file requires updating inbound links; validation catches breakage immediately.
