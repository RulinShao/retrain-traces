# SCOREBOARD

playbook: nogit-f045ba05
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | stack30 |
|---|---|---|
| lift | 67/100 = 67% | 83/100 = 83% (base 67% = 67.0/100) |
| stack | 51/100 = 51% | 56/100 = 56% (base 51% = 51.0/100) |
| nut | 0/100 = 0% | 0/100 = 0% (base 0% = 0.0/100) |
| wipe | 16/100 = 16% | 27/100 = 27% (base 16% = 16.0/100) |
| restack | 0/100 = 0% | 0/100 = 0% (base 0% = 0.0/100) |
| twolift | 1/100 = 1% | 0/100 = 0% (base 1% = 1.0/100) |
| handover | 2/100 = 2% | 1/100 = 1% (base 2% = 2.0/100) |
| revstack | 0/100 = 0% | 1/100 = 1% (base 0% = 0.0/100) |
| stackv2 | 1/100 = 1% | 1/100 = 1% (base 1% = 1.0/100) |

GPU-hours: 11.158 spent, 4.842 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: stack30
Submitted: base + stack30 (sha 35fc8044d659) (turn 47, token fe6c30; confirmed in turn 48)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| stack30 | base | 30 | specs/stack30.json | trained |

## History (latest 30)

- train stack30 (init base, steps 30): trained
- cancel job 21
- load stack30
- train stack10 failed: train cancelled with no saved step to keep; charged 0.0 GPU-h
- eval stack30 on lift: 83/100
- eval stack30 on stack: 56/100
- eval stack30 on twolift: 0/100
- eval stack30 on revstack: 1/100
- eval stack30 on stackv2: 1/100
- eval stack30 on nut: 0/100
- eval stack30 on wipe: 27/100
- eval stack30 on restack: 0/100
- eval stack30 on handover: 1/100
- finish: submitted stack30 (token fe6c30, job 41)
- finish: confirmed stack30 (token fe6c30)
