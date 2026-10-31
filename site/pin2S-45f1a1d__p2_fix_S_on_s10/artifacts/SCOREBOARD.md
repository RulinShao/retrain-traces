# SCOREBOARD

playbook: 87f49efe-f045ba05
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | v1 | current | v2 |
|---|---|---|---|---|
| lift | 67/100 = 67% | untested | 83/100 = 83% (v2) (base 67% = 67.0/100) | untested |
| stack | 51/100 = 51% | untested | 60/100 = 60% (v2) (base 51% = 51.0/100) | untested |
| nut | 0/100 = 0% | untested | 0/20 = 0% (v2) (base 0% = 0.0/20) | untested |
| wipe | 16/100 = 16% | untested | 60/100 = 60% (v2) (base 16% = 16.0/100) | untested |
| restack | 0/100 = 0% | untested | 0/20 = 0% (v2) (base 0% = 0.0/20) | untested |
| twolift | 1/100 = 1% | untested | 0/20 = 0% (v2) (base 1% = 0.2/20) | untested |
| handover | 2/100 = 2% | untested | 0/20 = 0% (v2) (base 2% = 0.4/20) | untested |
| revstack | 0/100 = 0% | untested | 0/20 = 0% (v2) (base 0% = 0.0/20) | untested |
| stackv2 | 1/100 = 1% | untested | 0/20 = 0% (v2) (base 1% = 0.2/20) | untested |

GPU-hours: 15.444 spent, 0.556 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: v2
Submitted: base + v2 (v2, sha e99ad52c7994) (turn 32, token b56994; confirmed in turn 33)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| v1 | base | 10 | specs/stack_pilot.json | trained |
| current | v1 | 10 | specs/wipe_run.json | trained |
| v2 | v1 | 10 | specs/wipe_run.json | trained |

Lineage of current: base -> v1 (train job 1, steps 10, specs/stack_pilot.json, trained) -> v2 (train job 16, steps 10, specs/wipe_run.json, trained)
Active version: v2 (load.py load v<k> to make another active)

## History (latest 30)

- train current v1 (init base, steps 10): trained; loaded current v1
- eval current on lift: 72/100
- eval current on stack: 54/100
- eval current on wipe: 26/100
- eval current on nut: 0/20
- eval current on restack: 0/20
- eval current on twolift: 0/20
- eval current on handover: 0/20
- eval current on revstack: 0/20
- eval current on stackv2: 0/20
- load current
- train current v2 (init v1, steps 10): trained; loaded current v2
- eval current on lift: 83/100
- eval current on stack: 60/100
- eval current on wipe: 60/100
- eval current on twolift: 0/20
- eval current on handover: 0/20
- eval current on revstack: 0/20
- eval current on restack: 0/20
- load v2
- finish: submitted v2 (token b56994, job 29)
- finish: confirmed v2 (token b56994)
- eval current on nut: 0/20
- eval current on stackv2: 0/20
