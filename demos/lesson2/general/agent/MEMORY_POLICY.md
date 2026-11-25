# MEMORY_POLICY — What Counts as Memory

This policy decides what is authoritative, what may be written where, and how disagreement is handled. It applies to humans and agents equally.

## 1. Authority order

When sources disagree, resolve in this order:

1. **Verified Markdown in this vault** — a dated, sourced statement that a human or agent has checked.
2. **Git history** — what the file used to say, and when it changed. Useful for reconstruction, never for overriding the current file.
3. **Raw sources in a project's `raw/`** — primary evidence. They outrank summaries *about* them, but must be interpreted, not quoted as conclusions.
4. **Ephemeral agent context** — the current conversation, model recall, cached summaries.
5. **Optional external tools** — note apps, memory services, issue trackers, chat search.

Lower layers may *inform* an edit; only layer 1 is authoritative once written. An agent's confident recollection is not evidence. A stale external tool is not evidence. If layers 1 and 3 conflict, the raw source wins for facts about the source, and the Markdown note must be corrected with a dated log entry.

**External tools are optional mirrors.** No database, MCP server, vector store, or cloud memory is required for this Brain to function. If one is used, it must be rebuildable from these files, and no knowledge may exist *only* there. When an external summary and a vault file disagree, the vault file wins until someone re-verifies the source.

## 2. What to write, and where

| Kind of knowledge | Destination | Rule |
|---|---|---|
| Binding choice with rationale | `DECISIONS.md` (project) or `GLOBAL_DECISIONS.md` | Only when confirmed; dated; alternatives noted |
| Current situation | `CURRENT_STATE.md` | Replace, do not accumulate; date the snapshot |
| Planned work | `NEXT_ACTIONS.md` | Concrete, with a done-when test |
| Durable briefing for newcomers | `AGENT_MEMORY.md` | Short; traps and vocabulary over narrative |
| Commands, errors, fixes | `TECHNICAL_NOTES.md` | Reproducible; symptom → cause → fix |
| Provenance | `SOURCES.md` + `raw/` | Never edit the original; register it |
| Chronology | `LOG.md` | Dated, factual, one entry per session |
| Session digest | `SESSION_SUMMARIES.md` | 5–10 lines, standalone |
| Reusable prompts | `PROMPTS.md` | Parameterised, with intended use |
| Stable, long reference | `wiki/` page | Only after the core files are current; indexed from `INDEX.md` |
| Cross-project procedure | New skill under `general/capabilities/skills/` | Only when reused by 2+ projects |
| Passwords, keys, tokens | **Nowhere in the vault** | Record the location and owner only |

**One fact, one home.** Link to it rather than copying it. Copies drift; links get validated.

## 3. Memory types and labels

Every durable claim should be recognisable as one of:

- **Fact** — verified, sourced, dated.
- **Decision** — chosen and binding; carries an ID.
- **Preference** — how the user wants work done; may change without ceremony.
- **Hypothesis** — plausible, untested; must be labelled as such.
- **Open question** — unknown; carries what would settle it.
- **Correction** — supersedes an earlier claim; keeps the earlier claim visible with a date.

Use explicit language: *confirmed*, *assumed*, *unverified*, *superseded*. Never let a hypothesis harden into a fact by repetition.

Optional confidence marker for material claims:

```markdown
> **Confidence:** high | medium | low — basis: <source or check>
```

## 4. Write rules

- **Atomic:** one claim per sentence or bullet; no multi-topic paragraphs.
- **Dated:** `YYYY-MM-DD` on every state snapshot, decision, and log entry.
- **Sourced:** name the file, dataset, person, or command that supports the claim.
- **Reversible:** prefer appending or superseding over deleting. Git is the undo, but readers need the trail in the text.
- **Scoped:** project knowledge stays in the project. If it must be global, promote it deliberately and record why.
- **Idempotent:** re-running a close should not duplicate entries; update the same dated entry instead.
- **Honest:** "unknown" is a valid and useful value. Padding is not.

## 5. Privacy and safety

Never store:

- passwords, API keys, access tokens, recovery codes, private keys;
- credentials in URLs, connection strings, or command history;
- unnecessary personal data about the user or third parties;
- full conversation transcripts, raw chain-of-thought, or hidden prompts;
- confidential source material that the user has not cleared for this vault.

If a secret is accidentally committed: rotate it first, then remove it from history (`git filter-repo` or equivalent), then note the incident in `LOG.md` **without the value**. Deleting the line in a new commit is not sufficient.

The vault is plain text. Assume anything written here can be read by anyone with filesystem or sync access.

## 6. Conflicts and contradictions

When two statements disagree:

1. Do not delete either.
2. Add a dated `> [!warning] Unresolved contradiction` block naming both claims and their files.
3. Prefer the more recent **verified** statement as provisional truth; say that you did.
4. If the conflict changes a decision or an action, ask the user before proceeding.
5. Record the resolution as a correction with the evidence that settled it.

A silent resolution is a memory bug.

## 7. Staleness and review

- `CURRENT_STATE.md`: review every session; it describes *now*.
- `NEXT_ACTIONS.md`: review every session; anything older than 90 days without progress is either blocked (say on what) or dropped.
- `AGENT_MEMORY.md`: re-verify when a core file changes materially.
- `wiki/` pages: review quarterly; write that the page is stale and add a review date, rather than deleting.
- `DECISIONS.md`: never stale, only superseded. Old decisions remain valid history.
- Archived projects: move nothing; mark the project archived in its index and in the registry, and stop loading them by default.

## 8. Corrections and deletion

- Wrong fact: append a correction with date and evidence; link the superseded claim.
- Wrong decision: add a new decision that supersedes it; never rewrite the old rationale.
- Obsolete page: mark it deprecated in the page, keep it, remove inbound links except the historical one.
- Genuinely harmful content (secrets, private data): remove it and rewrite history if committed; log the removal without reproducing the content.

## 9. What "remembering" means here

An agent has remembered something only when it is written to the correct file, with a date and provenance, and validation passes. Anything else is a claim about the current context window. If a future agent cannot recover it from Markdown, it was never memory.
