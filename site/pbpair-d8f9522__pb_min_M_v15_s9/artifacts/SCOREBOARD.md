# SCOREBOARD

playbook: nogit-f045ba05
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | stack1 | lift1 | lift1+stack1 |
|---|---|---|---|---|
| lift | 67/100 = 67% | untested | untested | 89/100 = 89% (base 67% = 67.0/100) |
| stack | 51/100 = 51% | untested | untested | 56/100 = 56% (base 51% = 51.0/100) |
| nut | 0/100 = 0% | untested | untested | untested |
| wipe | 16/100 = 16% | untested | untested | 32/100 = 32% (base 16% = 16.0/100) |
| restack | 0/100 = 0% | untested | untested | untested |
| twolift | 1/100 = 1% | untested | untested | untested |
| handover | 2/100 = 2% | untested | untested | untested |
| revstack | 0/100 = 0% | untested | untested | untested |
| stackv2 | 1/100 = 1% | untested | untested | untested |

GPU-hours: 15.116 spent, 0.884 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: lift1+stack1
Submitted: base + lift1 (sha 262d3edda227) + stack1 (sha 4da607e3c214) (turn 19, token d37db4; confirmed in turn 21)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| stack1 | base | 30 | stack1.yaml | trained |
| lift1 | base | 30 | lift1.yaml | trained |

## History (latest 30)

- train stack1 (init base, steps 30): trained
- train lift1 (init base, steps 30): trained
- eval lift1+stack1 on lift: 89/100
- eval lift1+stack1 on stack: 56/100
- eval lift1+stack1 on wipe: 32/100
- load lift1+stack1
- finish: submitted lift1+stack1 (token d37db4, job 18)
- finish: confirmed lift1+stack1 (token d37db4)
