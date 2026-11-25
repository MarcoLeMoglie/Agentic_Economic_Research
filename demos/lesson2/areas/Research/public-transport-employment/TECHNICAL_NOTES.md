---
title: Public Transport and Employment — Technical Notes
type: technical
status: active
project: public-transport-employment
updated: 2026-11-21
---

# Technical Notes

Synthetic project: the "data" described here is hypothetical. The technical conventions are real and reusable.

## Environment

- macOS (Apple Silicon), `bash` 3.2, Git 2.x, Obsidian-compatible Markdown.
- No database, Python package, R package, or cloud service is required for the memory layer.
- Vault root: `demos/lesson2/` of the course repository.
- Validation: [.infra/scripts/validate.sh](../../../.infra/scripts/validate.sh).

## Commands

```bash
# Validate structure, links, registration, and wiki indexing
bash .infra/scripts/validate.sh

# Read recent project history (last entry only)
tail -40 areas/Research/public-transport-employment/LOG.md

# Search project knowledge without loading whole files
grep -rn --include='*.md' -i 'treatment definition' areas/Research/public-transport-employment

# List project files in reading order
find areas/Research/public-transport-employment -maxdepth 1 -name '*.md' | sort
```

## Data conventions (hypothetical panel)

| Item | Convention |
|---|---|
| Unit ID | `district_id`, three-letter code (`RIV-01` … `RIV-24`) |
| Time ID | `quarter`, `YYYY-Qn` (e.g. `2019-Q3`) |
| Employment | `formal_emp`, integer count; `working_age_pop`, integer |
| Outcome | `formal_emp_rate = formal_emp / working_age_pop` |
| Treatment | `first_open_quarter`, `YYYY-Qn`; empty if never treated |
| Exposure | `stations_open`, cumulative count at quarter end |
| Missing values | empty field, never `0`, never `NA` mixed with text |
| Encoding | UTF-8, comma-separated, header row, ISO dates |

Aggregation rules: counts sum within district–quarter; rates are recomputed from counts, never averaged. Never forward-fill population across years without a flag.

## Errors and fixes

### Relative links resolve in Obsidian but not in the validator

**Symptom:** the validator reports a missing target for a link that opens fine in Obsidian.
**Cause:** the target was an Obsidian `[[wikilink]]` or an absolute path, which the vault policy forbids; the validator only resolves relative Markdown links.
**Fix:** rewrite as `[text](relative/path.md)`, relative to the file that contains the link.
**Verify:** rerun `bash .infra/scripts/validate.sh` and confirm zero link errors.

### Link with an anchor reported as missing

**Symptom:** `file.md#section` fails even though `file.md` exists.
**Cause:** the checker resolves the whole string as a path.
**Fix:** ensure the checker strips the fragment before testing. Current validator does this; if it regresses, fix the script rather than removing the anchor.
**Verify:** add a temporary `[x](CURRENT_STATE.md#confirmed)` link and rerun.

### Git refuses to commit on a fresh machine

**Symptom:** `Author identity unknown`.
**Cause:** no local or global `user.name` / `user.email`.
**Fix:** set them locally (`git config user.name "..."`, `git config user.email "..."`); do not commit with a placeholder identity.
**Verify:** `git config --get user.email` returns a value, then `git commit`.

## Validation notes

- `bash .infra/scripts/validate.sh` → PASS on 2026-11-18 (41 checks) and 2026-11-21 (46 checks, after a second project was registered), 0 errors, 0 warnings.
- Negative probe: adding an unindexed page under `wiki/` produced `wiki page not linked from project INDEX` and exit code 1; deleting the probe restored PASS. The check works, not just the happy path.
- Link and frontmatter checks ignore fenced/inline code and `general/templates/`. Templates contain `{{placeholder}}` links by design and are excluded.
- Registration is bidirectional: a project missing from `MEMORY.md` fails, and a `MEMORY.md` entry pointing at a non-project fails.

## Constraints

- No remote repository; Git is local history only.
- No secrets or personal data. Record locations, not values.
- The sample is 24 districts; anything that requires many clusters (e.g. wild bootstrap variants) must be justified explicitly.
- Do not install a semantic-search stack. Index-first reading and `grep` are sufficient at this size.

## Panel-construction checklist (for the future dry run)

- [ ] 24 districts × 40 quarters = 960 rows; confirm no duplicate `district_id` × `quarter`.
- [ ] Every treated district has a `first_open_quarter` inside 2014Q1–2023Q4.
- [ ] At least four pre-periods for every cohort in the main estimate.
- [ ] Outcome recomputed from counts and compared with the supplied rate.
- [ ] Missingness table by district and year, with reasons.
- [ ] No real place names or identifiers in the synthetic extract.
