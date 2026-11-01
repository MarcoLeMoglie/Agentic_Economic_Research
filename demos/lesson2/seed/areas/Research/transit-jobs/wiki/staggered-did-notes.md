# Staggered DiD, working notes

Staggered adoption means different tracts become treated in different years.
A single two-way fixed effects coefficient averages those timings with weights
that can be negative, so the number need not match the average effect the
author has in mind. Callaway and Sant'Anna (2021) build the comparison from
groups that share an adoption date and from tracts not yet treated.
The synthetic panel uses openings in 2016, 2018, and 2020 so that this
problem can be pointed at, not so that a coefficient can be published.
The vault does not run that estimator. code/02_did.py prints a fixed line.


These notes repeat the design page. They were left in place on purpose for the maintenance demo.
