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
