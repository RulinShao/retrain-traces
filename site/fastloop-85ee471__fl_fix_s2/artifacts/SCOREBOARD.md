# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 900001
policy: Qwen3-8B+init:79fbddb55dd8

Dev-seed success count per task x adapter stack (k/n): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records.

| task | base | restack1 | nut1 | stack1 | wipe1 | revstack1 |
|---|---|---|---|---|---|---|
| lift | 89/100 | - | - | - | - | - |
| stack | 57/100 | - | - | 56/100 | - | - |
| nut | 0/100 | - | 0/100 | - | - | - |
| wipe | 22/100 | - | - | - | 11/100 | - |
| restack | 0/100 | 0/100 | - | - | - | - |
| twolift | 0/100 | - | - | - | - | - |
| handover | 0/100 | - | - | - | - | - |
| revstack | 2/100 | - | - | - | - | 0/100 |
| stackv2 | 1/100 | - | - | - | - | - |

GPU-hours: 10.900 spent, 2.150 remaining of 16.0 (1 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.47, 10 steps 0.70, 50 steps 1.70) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: base

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| restack1 | base | 50 | specs/restack1.json | trained |
| nut1 | base | 50 | specs/nut1.json | trained |
| stack1 | base | 50 | specs/stack1.json | trained |
| wipe1 | base | 50 | specs/wipe1.json | trained |
| revstack1 | base | 50 | specs/revstack1.json | trained |

## History (latest 30)

- train restack1 (init base, steps 50): trained
- train nut1 (init base, steps 50): trained
- train stack1 (init base, steps 50): trained
- train wipe1 (init base, steps 50): trained
- train revstack1 (init base, steps 50): trained
- eval restack1 on restack: 0/100
- eval nut1 on nut: 0/100
- eval stack1 on stack: 56/100
- eval wipe1 on wipe: 11/100
- eval revstack1 on revstack: 0/100
- load base
