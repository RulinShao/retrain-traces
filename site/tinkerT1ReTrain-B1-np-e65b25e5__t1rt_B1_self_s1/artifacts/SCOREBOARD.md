# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | main1 | rev1 | nr_probe | rev_probe | C | D | E |
|---|---|---|---|---|---|---|---|---|
| lift | 77/100 = 77% | 88/100 = 88% (base 77% = 77.0/100) | untested | untested | untested | untested | untested | 91/100 = 91% (base 77% = 77.0/100) |
| stack | 44/100 = 44% | 70/100 = 70% (base 44% = 44.0/100) | untested | untested | untested | untested | untested | 68/100 = 68% (base 44% = 44.0/100) |
| wipe | 20/100 = 20% | 87/100 = 87% (base 20% = 20.0/100) | untested | untested | untested | untested | untested | 82/100 = 82% (base 20% = 20.0/100) |
| nut | 0/100 = 0% | untested | untested | untested | untested | untested | untested | 0/100 = 0% (base 0% = 0.0/100) |
| restack | 0/100 = 0% | untested | untested | untested | untested | untested | untested | 0/100 = 0% (base 0% = 0.0/100) |
| revstack | 3/100 = 3% | untested | untested | untested | untested | untested | untested | 12/100 = 12% (base 3% = 3.0/100) |

GPU-hours: 46.510 spent, 1.490 remaining of 48.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.44, 10 steps 2.42, 50 steps 11.23) GPU-h; eval.py per task (5 seeds 0.15, 20 seeds 0.19, 100 seeds 0.45) GPU-h
Loaded on your serving endpoint: E
Submitted: base + E (sha 3b71e6abb6b9) (turn 28, token ca1ee0; confirmed in turn 29)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| main1 | base | 50 | spec_main1.json | trained |
| rev1 | base | 50 | spec_rev1.json | trained |
| nr_probe | base | 20 | spec_nr_probe.json | trained |
| rev_probe | base | 20 | spec_rev_probe.json | trained |
| C | nr_probe | 25 | spec_C.json | trained |
| D | C | 25 | spec_D.json | trained |
| E | D | 10 | spec_E.json | trained |

## History (latest 30)

- eval base on lift: 77/100
- eval base on stack: 44/100
- eval base on wipe: 20/100
- eval base on nut: 0/100
- eval base on restack: 0/100
- eval base on revstack: 3/100
- train main1 (init base, steps 50): trained
- train rev1 (init base, steps 50): trained
- train nr_probe (init base, steps 20): trained
- train rev_probe (init base, steps 20): trained
- eval main1 on lift: 88/100
- eval main1 on stack: 70/100
- eval main1 on wipe: 87/100
- train C (init nr_probe, steps 25): trained
- train D (init C, steps 25): trained
- train E (init D, steps 10): trained
- eval E on lift: 91/100
- eval E on stack: 68/100
- eval E on wipe: 82/100
- eval E on nut: 0/100
- eval E on restack: 0/100
- eval E on revstack: 12/100
- load E
- finish: submitted E (token ca1ee0, job 32)
- finish: confirmed E (token ca1ee0)
