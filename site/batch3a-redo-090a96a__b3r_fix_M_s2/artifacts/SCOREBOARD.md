# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records.

| task | base | restack1 | stack1 |
|---|---|---|---|
| lift | 67/100 | 15/20 | - |
| stack | 51/100 | 10/20 | - |
| nut | 0/100 | - | - |
| wipe | 16/100 | - | - |
| restack | 0/100 | 0/100 | - |
| twolift | 1/100 | - | - |
| handover | 2/100 | - | - |
| revstack | 0/100 | - | - |
| stackv2 | 1/100 | - | - |

GPU-hours: 13.502 spent, 1.266 remaining of 16.0 (3 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: base

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| restack1 | base | 30 | specs/restack1.json | trained |
| stack1 | base | 20 | specs/stack1.json | trained |

## History (latest 30)

- train restack1 (init base, steps 30): trained
- eval restack1 on lift: 15/20
- eval restack1 on stack: 10/20
- eval restack1 on restack: 0/100
- train stack1 (init base, steps 20): trained
