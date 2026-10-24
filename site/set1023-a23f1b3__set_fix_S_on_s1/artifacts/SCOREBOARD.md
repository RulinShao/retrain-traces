# SCOREBOARD

playbook: ea39163-15ab3e1e
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | v1 | current |
|---|---|---|---|
| lift | 67/100 = 67% | untested | untested |
| stack | 51/100 = 51% | untested | untested |
| nut | 0/100 = 0% | untested | untested |
| wipe | 16/100 = 16% | untested | untested |
| restack | 0/100 = 0% | untested | untested |
| twolift | 1/100 = 1% | untested | untested |
| handover | 2/100 = 2% | untested | untested |
| revstack | 0/100 = 0% | untested | untested |
| stackv2 | 1/100 = 1% | untested | untested |

GPU-hours: 9.650 spent, 6.350 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: current
Submitted: none (python3 finish.py submits a policy)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| v1 | base | 50 | specs/restack_shaped50.json | trained |
| current | base | 50 | specs/restack_shaped50.json | trained |

Lineage of current: base -> v1 (train job 2, steps 50, specs/restack_shaped50.json, trained)
Active version: v1 (load.py load v<k> to make another active)

## History (latest 30)

- train current v1 (init base, steps 50): trained; loaded current v1
