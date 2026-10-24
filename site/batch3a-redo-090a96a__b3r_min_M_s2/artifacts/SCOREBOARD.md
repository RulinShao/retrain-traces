# SCOREBOARD

playbook: 13a939b-eeac9359
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records.

| task | base | r1_lift | r1_stack | r1_wipe |
|---|---|---|---|---|
| lift | 67/100 | 80/100 | - | - |
| stack | 51/100 | - | 44/100 | - |
| nut | 0/100 | - | - | - |
| wipe | 16/100 | - | - | 33/100 |
| restack | 0/100 | - | - | - |
| twolift | 1/100 | - | - | - |
| handover | 2/100 | - | - | - |
| revstack | 0/100 | - | - | - |
| stackv2 | 1/100 | - | - | - |

GPU-hours: 13.518 spent, 2.482 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: base

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| r1_lift | base | 10 | spec_lift.json | trained |
| r1_stack | base | 10 | spec_stack.json | trained |
| r1_wipe | base | 10 | spec_wipe.json | trained |

## History (latest 30)

- train r1_lift (init base, steps 10): trained
- train r1_stack (init base, steps 10): trained
- train r1_wipe (init base, steps 10): trained
- eval r1_lift on lift: 80/100
- eval r1_stack on stack: 44/100
- eval r1_wipe on wipe: 33/100
