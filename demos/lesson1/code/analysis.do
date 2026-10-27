* analysis.do: price regressions on the 1978 auto data
* Run from the repository root: stata-mp -b do code/analysis.do

version 17
clear all
set more off

use "data/auto.dta", clear

* log price, used as the outcome
gen lprice = ln(prise)

* fuel efficiency in litres per 100 km
gen l100km = 235.21 / mpg

regress lprice l100km weight i.foreign, vce(robust)
estimates store m1

regress lprice l100km weight i.foreign i.rep78, vce(robust)
estimates store m2

esttab m1 m2 using "output/table1.tex", replace se label booktabs
