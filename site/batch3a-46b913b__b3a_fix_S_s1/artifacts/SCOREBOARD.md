# SCOREBOARD

playbook: none
agent: local
mode: dev
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records.

| task | base | current |
|---|---|---|
| lift | 67/100 | 78/100 (v1) |
| stack | 51/100 | 50/100 (v1) |
| nut | 0/100 | 0/100 (v1) |
| wipe | 16/100 | 15/100 (v1) |
| restack | 0/100 | 0/100 (v1) |
| twolift | 1/100 | 0/100 (v1) |
| handover | 2/100 | 1/100 (v1) |
| revstack | 0/100 | 1/100 (v1) |
| stackv2 | 1/100 | 2/100 (v1) |

GPU-hours: 12.372 spent, 2.188 remaining of 16.0 (3 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: current

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| current | current v1 | 10 | specs/wipe1.json | trained |

Lineage of current: base -> v1 (train job 1, steps 10, specs/stack1.json, trained) -> v2 (train job 14, steps 10, specs/wipe1.json, trained)

## History (latest 30)

- train current v1 (init base, steps 10): trained; loaded current v1
- eval current on lift: 78/100
- eval current on stack: 50/100
- eval current on nut: 0/100
- eval current on wipe: 15/100
- eval current on restack: 0/100
- eval current on twolift: 0/100
- eval current on handover: 1/100
- eval current on revstack: 1/100
- eval current on stackv2: 2/100
- load current
- train current v2 (init current v1, steps 10): trained; loaded current v2
