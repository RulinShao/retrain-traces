# SCOREBOARD

playbook: none
agent: local
mode: dev
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records.

| task | base | lift30 | stack30 | lift30+stack30 |
|---|---|---|---|---|
| lift | 67/100 | 87/100 | - | 87/100 |
| stack | 51/100 | - | 53/100 | 50/100 |
| nut | 0/100 | - | - | - |
| wipe | 16/100 | - | - | - |
| restack | 0/100 | - | - | - |
| twolift | 1/100 | - | - | - |
| handover | 2/100 | - | - | - |
| revstack | 0/100 | - | - | - |
| stackv2 | 1/100 | - | - | - |

GPU-hours: 15.596 spent, 0.404 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: base

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| lift30 | base | 30 | spec_lift.json | trained |
| stack30 | base | 30 | spec_stack.json | trained |

## History (latest 30)

- train lift30 (init base, steps 30): trained
- train stack30 (init base, steps 30): trained
- eval lift30 on lift: 87/100
- eval stack30 on stack: 53/100
- load lift30+stack30
- eval lift30+stack30 on lift: 87/100
- eval lift30+stack30 on stack: 50/100
- load base
