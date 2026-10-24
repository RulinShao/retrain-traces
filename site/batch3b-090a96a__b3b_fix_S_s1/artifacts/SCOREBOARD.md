# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records.

| task | base | v1 | current | v2 |
|---|---|---|---|---|
| lift | 67/100 | - | 77/100 (v1) | - |
| stack | 51/100 | - | 61/100 (v1) | - |
| nut | 0/100 | - | 0/100 (v1) | - |
| wipe | 16/100 | - | 20/100 (v1) | - |
| restack | 0/100 | - | 0/100 (v1) | - |
| twolift | 1/100 | - | 0/100 (v1) | - |
| handover | 2/100 | - | 2/100 (v1) | - |
| revstack | 0/100 | - | 2/100 (v1) | - |
| stackv2 | 1/100 | - | 1/100 (v1) | - |

GPU-hours: 14.903 spent, 1.097 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: v1

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| v1 | base | 30 | specs/stack1.json | trained |
| current | v1 | 8 | specs/revstack2.json | trained |
| v2 | v1 | 8 | specs/revstack2.json | trained |

Lineage of current: base -> v1 (train job 1, steps 30, specs/stack1.json, trained) -> v2 (train job 15, steps 8, specs/revstack2.json, trained)
Active version: v1 (load.py load v<k> to make another active)

## History (latest 30)

- train current v1 (init base, steps 30): trained; loaded current v1
- eval current on stack: 61/100
- eval current on revstack: 2/100
- eval current on restack: 0/100
- eval current on stackv2: 1/100
- eval current on lift: 77/100
- eval current on nut: 0/100
- eval current on wipe: 20/100
- eval current on twolift: 0/100
- eval current on handover: 2/100
- load current
- train current v2 (init v1, steps 8): trained; loaded current v2
- load v1
