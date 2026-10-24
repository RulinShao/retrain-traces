# SCOREBOARD

playbook: 13a939b-eeac9359
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records.

| task | base | current |
|---|---|---|
| lift | 66/100 | - |
| stack | 51/100 | - |
| nut | 0/100 | - |
| wipe | 16/100 | - |
| restack | 0/100 | - |
| twolift | 1/100 | - |
| handover | 2/100 | - |
| revstack | 0/100 | - |
| stackv2 | 1/100 | - |

GPU-hours: 7.318 spent, 4.362 remaining of 16.0 (9 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: current

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| current | base | 30 | specs/lift.json | trained |

Lineage of current: base -> v1 (train job 1, steps 30, specs/lift.json, trained)

## History (latest 30)

- train current v1 (init base, steps 30): trained; loaded current v1
- eval base on lift: 66/100
