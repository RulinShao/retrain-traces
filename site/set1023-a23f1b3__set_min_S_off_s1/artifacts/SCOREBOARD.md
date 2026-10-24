# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | v1 | current |
|---|---|---|---|
| lift | 67/100 = 67% | untested | 77/100 = 77% (v1) (base 67% = 67.0/100) |
| stack | 51/100 = 51% | untested | 67/100 = 67% (v1) (base 51% = 51.0/100) |
| nut | 0/100 = 0% | untested | untested |
| wipe | 16/100 = 16% | untested | untested |
| restack | 0/100 = 0% | untested | untested |
| twolift | 1/100 = 1% | untested | untested |
| handover | 2/100 = 2% | untested | untested |
| revstack | 0/100 = 0% | untested | 1/100 = 1% (v1) (base 0% = 0.0/100) |
| stackv2 | 1/100 = 1% | untested | 0/100 = 0% (v1) (base 1% = 1.0/100) |

GPU-hours: 6.649 spent, 6.951 remaining of 16.0 (5 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: current
Submitted: none (python3 finish.py submits a policy)
Job 8 (eval current): queued (not started), 0 min in queue
Job 9 (eval current): queued (not started), 0 min in queue
Job 10 (eval current): queued (not started), 0 min in queue

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| v1 | base | 15 | specs/stack1.yaml | trained |
| current | base | 15 | specs/stack1.yaml | trained |

Lineage of current: base -> v1 (train job 1, steps 15, specs/stack1.yaml, trained)
Active version: v1 (load.py load v<k> to make another active)

## History (latest 30)

- train current v1 (init base, steps 15): trained; loaded current v1
- eval current on stack: 67/100
- eval current on lift: 77/100
- eval current on revstack: 1/100
- eval current on stackv2: 0/100
