# SCOREBOARD

playbook: 13a939b-eeac9359
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records.

| task | base | lift_v1 | stack_v1 | wipe_v1 | lift_v1+wipe_v1 |
|---|---|---|---|---|---|
| lift | 67/100 | - | - | - | 84/100 |
| stack | 51/100 | - | 57/100 | - | 61/100 |
| nut | 0/100 | - | - | - | - |
| wipe | 16/100 | - | - | - | 48/100 |
| restack | 0/100 | - | - | - | - |
| twolift | 1/100 | - | - | - | - |
| handover | 2/100 | - | - | - | - |
| revstack | 0/100 | - | - | - | - |
| stackv2 | 1/100 | - | - | - | - |

GPU-hours: 13.998 spent, 2.002 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: lift_v1+wipe_v1

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| lift_v1 | base | 10 | specs/lift_v1.json | trained |
| stack_v1 | base | 10 | specs/stack_v1.json | trained |
| wipe_v1 | base | 10 | specs/wipe_v1.json | trained |

## History (latest 30)

- train lift_v1 (init base, steps 10): trained
- train stack_v1 (init base, steps 10): trained
- train wipe_v1 (init base, steps 10): trained
- eval lift_v1+stack_v1+wipe_v1 failed: eval: stack rank 96 > 64 (the serving's --max-lora-rank): at most 2 adapters of rank 32
- eval lift_v1+stack_v1+wipe_v1 failed: eval: stack rank 96 > 64 (the serving's --max-lora-rank): at most 2 adapters of rank 32
- eval lift_v1+stack_v1+wipe_v1 failed: eval: stack rank 96 > 64 (the serving's --max-lora-rank): at most 2 adapters of rank 32
- eval lift_v1+wipe_v1 on lift: 84/100
- eval lift_v1+wipe_v1 on stack: 61/100
- eval lift_v1+wipe_v1 on wipe: 48/100
- eval stack_v1 on stack: 57/100
- load lift_v1+wipe_v1
