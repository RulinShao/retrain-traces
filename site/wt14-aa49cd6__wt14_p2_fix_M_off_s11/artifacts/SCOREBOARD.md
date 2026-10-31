# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | r1_revstack | r1_multi | r1_multi+r1_revstack |
|---|---|---|---|---|
| lift | 67/100 = 67% | untested | 71/100 = 71% (base 67% = 67.0/100) | 79/100 = 79% (base 67% = 67.0/100) |
| stack | 51/100 = 51% | untested | 44/100 = 44% (base 51% = 51.0/100) | 36/100 = 36% (base 51% = 51.0/100) |
| nut | 0/100 = 0% | untested | untested | 0/100 = 0% (base 0% = 0.0/100) |
| wipe | 16/100 = 16% | untested | untested | 36/100 = 36% (base 16% = 16.0/100) |
| restack | 0/100 = 0% | untested | untested | 0/100 = 0% (base 0% = 0.0/100) |
| twolift | 1/100 = 1% | untested | untested | 0/100 = 0% (base 1% = 1.0/100) |
| handover | 2/100 = 2% | untested | untested | 1/100 = 1% (base 2% = 2.0/100) |
| revstack | 0/100 = 0% | 0/40 = 0% (base 0% = 0.0/40) | untested | untested |
| stackv2 | 1/100 = 1% | untested | untested | 3/100 = 3% (base 1% = 1.0/100) |

GPU-hours: 13.887 spent, 2.113 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: r1_multi+r1_revstack
Submitted: base + r1_multi (sha 531f422f7cef) + r1_revstack (sha 8d0abd3d665c) (turn 68, token ceb61a; confirmed in turn 81)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| r1_revstack | base | 12 | specs/r1_revstack.json | trained |
| r1_multi | base | 10 | specs/r1_multi.json | trained |

## History (latest 30)

- train r1_revstack (init base, steps 12): trained
- train r1_multi (init base, steps 10): trained
- eval r1_revstack on revstack: 0/40
- eval r1_multi+r1_revstack on lift: 79/100
- eval r1_multi+r1_revstack on stack: 36/100
- eval r1_multi+r1_revstack on wipe: 36/100
- eval r1_multi+r1_revstack on restack: 0/100
- eval r1_multi+r1_revstack on twolift: 0/100
- eval r1_multi+r1_revstack on handover: 1/100
- eval r1_multi+r1_revstack on nut: 0/100
- eval r1_multi+r1_revstack on stackv2: 3/100
- eval r1_multi on lift: 71/100
- eval r1_multi on stack: 44/100
- load r1_multi+r1_revstack
- finish: submitted r1_multi+r1_revstack (token ceb61a, job 32)
- finish: confirmed r1_multi+r1_revstack (token ceb61a)
