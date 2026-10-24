# SCOREBOARD

playbook: none
agent: local
mode: dev
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records.

| task | base | revstack_pilot |
|---|---|---|
| lift | 67/100 | 68/100 |
| stack | 51/100 | 49/100 |
| nut | 0/100 | - |
| wipe | 16/100 | - |
| restack | 0/100 | - |
| twolift | 1/100 | - |
| handover | 2/100 | - |
| revstack | 0/100 | 2/100 |
| stackv2 | 1/100 | - |

GPU-hours: 5.747 spent, 4.821 remaining of 16.0 (1 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: revstack_pilot

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| revstack_pilot | base | 12 | specs/revstack_pilot.json | trained |

## History (latest 30)

- train revstack_pilot (init base, steps 12): trained
- eval revstack_pilot on revstack: 2/100
- eval revstack_pilot on stack: 49/100
- eval revstack_pilot on lift: 68/100
- load revstack_pilot
