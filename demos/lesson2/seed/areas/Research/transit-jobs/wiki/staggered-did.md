# Staggered difference-in-differences

Staggered adoption means different tracts become treated in different years.
A single two-way fixed effects coefficient averages those timings with weights
that can be negative, so the number need not match the average effect the
author has in mind. Callaway and Sant'Anna (2021) build the comparison from
groups that share an adoption date and from tracts not yet treated.
The synthetic panel uses openings in 2016, 2018, and 2020 so that this
problem can be pointed at, not so that a coefficient can be published.
The vault does not run that estimator. code/02_did.py prints a fixed line.


## What the demo stores
The decision to name Callaway and Sant'Anna is in DECISIONS.md, dated 2026-09-20.
The clustering rule in force is district, dated 2026-09-14.
The lecture line ATT 0.031 (s.e. 0.012) is simulated and lives in CURRENT_STATE.

## What this page is for
A reader who arrives next month should not have to reconstruct the design from chat.
