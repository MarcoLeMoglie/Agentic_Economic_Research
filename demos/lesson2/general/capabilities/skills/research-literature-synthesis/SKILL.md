---
name: research-literature-synthesis
description: Turn papers, preprints, reports, and policy documents into structured, sourced research notes that separate findings from interpretations. Use when a task requires reading several sources, mapping evidence for a question, or drafting a literature/evidence note. Do not use for single-fact lookups, citation fabrication, or meta-analysis with statistical pooling.
version: 1.0
updated: 2026-11-18
---

# Research Literature Synthesis

## When to use

- The user asks for a literature review, evidence summary, or "what do we know about X".
- Several sources must be compared for one research question.
- A project needs a defensible evidence base before design or writing.

**Do not use when:** the answer is a single known fact; sources are unavailable and cannot be obtained; the user wants citations invented or padded; formal meta-analysis or risk-of-bias scoring is required (that needs a dedicated protocol).

## Inputs

- A bounded question (one sentence, with population/context/time frame if relevant).
- A source set: PDFs, notes, links, or citations. Prefer sources already registered in the project's `SOURCES.md`.
- The target project folder and, if one exists, the project's `INDEX.md`.

If the question is unbounded, narrow it first and write the narrowed version down.

## Procedure

1. **Fix the question and inclusion rules.** Write the question, what counts as relevant evidence, and what will be excluded. Keep this at the top of the note.
2. **Register provenance before reading.** For every source: ID, full title, author/publisher, date, type, locator, access date, and status. Put originals in `raw/`; register them in `SOURCES.md`. Never edit an original.
3. **Extract one claim per row.** Build a table: source ID, locator (page/section), claim, evidence type (experiment, quasi-experiment, descriptive, model, opinion), direction, and the author's stated interpretation. Quote sparingly and exactly; paraphrase the rest.
4. **Separate the layers.** For each source, distinguish:
   - **Finding** — what was observed, with magnitude and uncertainty if reported.
   - **Interpretation** — what the authors say it means.
   - **Your inference** — what you conclude across sources; label it as yours.
   - **Speculation** — plausible but untested; label it.
5. **Grade the evidence, pragmatically.** Note design, sample/context, identification strategy, and main threats. Do not invent quality scores; use plain-language judgements ("small single-site trial", "descriptive only", "credible quasi-experiment, but context-specific").
6. **Map agreement and conflict.** List where sources converge, where they disagree, and why (different populations, definitions, periods, methods). Never average away a conflict.
7. **Synthesise for the decision.** Answer the question in 3–6 sentences, then state what would change the answer. If the evidence is insufficient, say so plainly.
8. **Write to the vault in the right place.** Immediate state goes to the project's `CURRENT_STATE.md`; provenance to `SOURCES.md`; a long stable synthesis may become a `wiki/` page, but only after the core files are updated. Log the session.

## Output format

```markdown
## Evidence note — <question> — <date>

**Question:** one sentence.
**Scope:** inclusion/exclusion rules, date range, contexts.

### Bottom line
3–6 sentences. Confidence: high / medium / low, with the reason.

### Evidence table
| Source | Design / type | Finding (with locator) | Authors' interpretation | Limits |
|---|---|---|---|---|

### Where the evidence converges
- Claim — supported by S-xxx, S-yyy.

### Where it conflicts or is thin
- Conflict or gap — sources — what would settle it.

### Inference (mine, not the sources')
- ...

### What would change the answer
- ...

### Sources
- S-xxx — full reference as recorded in SOURCES.md — status: read | partial | unavailable.
```

## Quality bar

- Every factual sentence traces to a source ID and locator, or is explicitly marked as inference.
- Findings and interpretations never share a bullet without labels.
- Numbers carry units, period, and context; no number is invented or silently converted.
- Contradictions are visible, dated, and unresolved until evidence settles them.
- "Not enough evidence" appears when true, instead of a confident synthesis.
- The note can be understood by a reader who has not read the sources.

## Failure modes to avoid

- **Citation theatre:** plausible-looking references that were never opened.
- **Consensus laundering:** presenting one study as the literature.
- **Interpretation drift:** reporting the authors' enthusiasm as the finding.
- **Scope creep:** answering a broader question than the one asked.
- **False precision:** decimal estimates from descriptive evidence.
- **Wiki-first writing:** creating an elaborate page instead of updating the project's state and decisions.

## Handoff

If the synthesis is long and stable, follow [WIKI_WORKFLOW.md](../../../agent/WIKI_WORKFLOW.md) for promotion. Record verified decisions in the project's `DECISIONS.md`, not in this note. Use the project's [SOURCES template](../../../templates/project-slug-SOURCES.md) when the project does not yet have a source register.
