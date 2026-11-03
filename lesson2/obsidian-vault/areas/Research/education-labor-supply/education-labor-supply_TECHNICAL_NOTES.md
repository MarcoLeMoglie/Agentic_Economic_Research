# Technical notes

```stata
use data/clean/women_1940_58, clear
rdrobust lfp cohort, c(1949) cluster(cohort_prov)
```

Bandwidth chosen by `rdbwselect`: 4.6 cohorts.
