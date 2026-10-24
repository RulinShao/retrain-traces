# SCOREBOARD

playbook: none
agent: local
mode: dev
policy: Qwen3-8B

Dev-seed success count per task x adapter stack (k/n): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records.

| task | base | stack1 | wipe1 | wipe2 | wipe3 |
|---|---|---|---|---|---|
| lift | 0/100 | - | - | - | - |
| stack | 0/100 | 0/100 | - | - | - |
| nut | 0/99 | - | - | - | - |
| wipe | 0/100 | - | 0/5 | 0/100 | 0/5 |
| restack | 0/100 | 0/100 | - | - | - |
| twolift | 0/100 | - | - | - | - |
| handover | 0/100 | - | - | - | - |
| revstack | 0/100 | - | - | - | - |
| stackv2 | 0/100 | 0/100 | - | - | - |

GPU-hours: 7.182 spent, 7.118 remaining of 16.0 (1 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.47, 10 steps 0.70, 50 steps 1.70) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: wipe2
Job 22 (train restack1): queued (not started), 0 min in queue

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| stack1 | base | 10 | specs/stack1.json | trained |
| wipe1 | base | 30 | specs/wipe1.json | trained 30 steps; weights unchanged (all-zero update: 0/252 nonzero lora_B) |
| wipe2 | base | 30 | specs/wipe2.json | trained |
| wipe3 | wipe2 | 40 | specs/wipe3.json | trained |

## History (latest 30)

- train stack1 (init base, steps 10): trained
- eval stack1 on stack: 0/100
- eval stack1 on restack: 0/100
- eval stack1 on stackv2: 0/100
- load base
- train wipe1 (init base, steps 30): trained 30 steps; weights unchanged (all-zero update: 0/252 nonzero lora_B)
- load base
- eval wipe1 on wipe: 0/5
- train wipe2 (init base, steps 30): trained
- load wipe2
- eval wipe2 on wipe: 0/100
- train wipe3 (init wipe2, steps 40): trained
- eval wipe3 on wipe: 0/5
