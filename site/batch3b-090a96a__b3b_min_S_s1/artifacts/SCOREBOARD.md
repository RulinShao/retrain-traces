# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | v1 | current |
|---|---|---|---|
| lift | 67/100 = 67% | untested | 84/100 = 84% (v1) (base 67% = 67.0/100) |
| stack | 51/100 = 51% | untested | 64/100 = 64% (v1) (base 51% = 51.0/100) |
| nut | 0/100 = 0% | untested | 0/100 = 0% (v1) (base 0% = 0.0/100) |
| wipe | 16/100 = 16% | untested | 35/100 = 35% (v1) (base 16% = 16.0/100) |
| restack | 0/100 = 0% | untested | 0/100 = 0% (v1) (base 0% = 0.0/100) |
| twolift | 1/100 = 1% | untested | 0/100 = 0% (v1) (base 1% = 1.0/100) |
| handover | 2/100 = 2% | untested | 0/100 = 0% (v1) (base 2% = 2.0/100) |
| revstack | 0/100 = 0% | untested | 5/100 = 5% (v1) (base 0% = 0.0/100) |
| stackv2 | 1/100 = 1% | untested | 2/100 = 2% (v1) (base 1% = 1.0/100) |

GPU-hours: 17.911 spent, -1.911 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: current
Submitted: base + current (v1, sha 45472a251fa3) (turn 18, token e80103; unconfirmed; scored at the session end (DONE))

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| v1 | base | 50 | spec1.json | trained |
| current | base | 50 | spec1.json | trained |

Lineage of current: base -> v1 (train job 1, steps 50, spec1.json, trained)
Active version: v1 (load.py load v<k> to make another active)

## History (latest 30)

- train current v1 (init base, steps 50): trained; loaded current v1
- eval current on restack: 0/100
- eval current on lift: 84/100
- eval current on stack: 64/100
- eval current on wipe: 35/100
- eval current on nut: 0/100
- eval current on twolift: 0/100
- eval current on handover: 0/100
- eval current on revstack: 5/100
- eval current on stackv2: 2/100
- finish: submitted current (token e80103, DONE file of the last turn (legacy end rule: the session ended there); scored by resume)
