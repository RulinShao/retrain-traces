# SCOREBOARD

playbook: 13a939b-eeac9359
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records.

| task | base | v1 | current | v2 | v3 |
|---|---|---|---|---|---|
| lift | 67/100 | - | 13/20 (v3) | - | - |
| stack | 51/100 | - | 10/20 (v3) | - | - |
| nut | 0/100 | - | - | - | - |
| wipe | 16/100 | - | 16/20 (v3) | - | - |
| restack | 0/100 | - | - | - | - |
| twolift | 1/100 | - | - | - | - |
| handover | 2/100 | - | - | - | - |
| revstack | 0/100 | - | 0/20 (v3) | - | - |
| stackv2 | 1/100 | - | 0/20 (v3) | - | - |

GPU-hours: 15.838 spent, 0.162 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: v3

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| v1 | base | 10 | spec_lift.json | trained |
| current | v2 | 10 | spec_wipe.json | trained |
| v2 | v1 | 10 | spec_stack.json | trained |
| v3 | v2 | 10 | spec_wipe.json | trained |

Lineage of current: base -> v1 (train job 1, steps 10, spec_lift.json, trained) -> v2 (train job 9, steps 10, spec_stack.json, trained) -> v3 (train job 11, steps 10, spec_wipe.json, trained)
Active version: v3 (load.py load v<k> to make another active)

## History (latest 30)

- train current v1 (init base, steps 10): trained; loaded current v1
- eval current on lift: 16/20
- eval current on stack: 13/20
- eval current on wipe: 6/20
- eval current on stackv2: 0/20
- eval current on revstack: 1/20
- train current v2 (init v1, steps 10): trained; loaded current v2
- train current v3 (init v2, steps 10): trained; loaded current v3
- eval current on lift: 13/20
- eval current on stack: 10/20
- eval current on wipe: 16/20
- eval current on stackv2: 0/20
- eval current on revstack: 0/20
- load v3
