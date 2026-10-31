# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | lift_a | stack_a | wipe_a |
|---|---|---|---|---|
| lift | 67/100 = 67% | untested | untested | untested |
| stack | 51/100 = 51% | untested | untested | untested |
| nut | 0/100 = 0% | untested | untested | untested |
| wipe | 16/100 = 16% | untested | untested | untested |
| restack | 0/100 = 0% | untested | untested | untested |
| twolift | 1/100 = 1% | untested | untested | untested |
| handover | 2/100 = 2% | untested | untested | untested |
| revstack | 0/100 = 0% | untested | untested | untested |
| stackv2 | 1/100 = 1% | untested | untested | untested |

GPU-hours: 12.078 spent, 3.922 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: base
Submitted: none (python3 finish.py submits a policy)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| lift_a | base | 6 | specs/lift_a.json | trained |
| stack_a | base | 12 | specs/stack_a.json | trained |
| wipe_a | base | 12 | specs/wipe_a.json | trained |

## History (latest 30)

- train lift_a (init base, steps 6): trained
- train stack_a (init base, steps 12): trained
- train wipe_a (init base, steps 12): trained
