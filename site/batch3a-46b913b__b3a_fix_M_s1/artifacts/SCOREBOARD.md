# SCOREBOARD

playbook: none
agent: local
mode: dev
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records.

| task | base | rev1 | stk1 | rst1 |
|---|---|---|---|---|
| lift | 67/100 | - | 19/20 | - |
| stack | 51/100 | 11/20 | 16/20 | - |
| nut | 0/100 | - | - | - |
| wipe | 16/100 | - | - | - |
| restack | 0/100 | - | - | 0/20 |
| twolift | 1/100 | - | - | - |
| handover | 2/100 | - | - | - |
| revstack | 0/100 | 0/20 | - | - |
| stackv2 | 1/100 | - | - | - |

GPU-hours: 13.958 spent, 2.042 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: stk1

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| rev1 | base | 10 | specs/exp1.json | trained |
| stk1 | base | 10 | specs/exp2.json | trained |
| rst1 | base | 10 | specs/exp3.json | trained |

## History (latest 30)

- train rev1 (init base, steps 10): trained
- eval rev1 on revstack: 0/20
- eval rev1 on stack: 11/20
- load base
- train stk1 (init base, steps 10): trained
- eval stk1 on stack: 16/20
- eval stk1 on lift: 19/20
- load stk1
- train rst1 (init base, steps 10): trained
- eval rst1 on restack: 0/20
- load stk1
