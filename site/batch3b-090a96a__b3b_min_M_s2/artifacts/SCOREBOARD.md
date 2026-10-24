# SCOREBOARD

playbook: 13a939b-eeac9359
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records.

| task | base | s_stack | s_lift |
|---|---|---|---|
| lift | 67/100 | 14/20 | 17/20 |
| stack | 51/100 | 11/20 | 9/20 |
| nut | 0/100 | 0/20 | 0/20 |
| wipe | 16/100 | 3/20 | 2/20 |
| restack | 0/100 | 0/20 | - |
| twolift | 1/100 | 0/20 | - |
| handover | 2/100 | 0/20 | - |
| revstack | 0/100 | 1/20 | - |
| stackv2 | 1/100 | 0/20 | - |

GPU-hours: 15.752 spent, 0.248 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: s_stack+s_lift

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| s_stack | base | 20 | specs/s_stack.json | trained |
| s_lift | base | 20 | specs/s_lift.json | trained |

## History (latest 30)

- train s_stack (init base, steps 20): trained
- train s_lift (init base, steps 20): trained
- eval s_stack on lift: 14/20
- eval s_stack on stack: 11/20
- eval s_stack on nut: 0/20
- eval s_stack on wipe: 3/20
- eval s_stack on restack: 0/20
- eval s_stack on twolift: 0/20
- eval s_stack on handover: 0/20
- eval s_stack on revstack: 1/20
- eval s_stack on stackv2: 0/20
- eval s_lift on lift: 17/20
- eval s_lift on stack: 9/20
- eval s_lift on nut: 0/20
- eval s_lift on wipe: 2/20
- load s_stack+s_lift
