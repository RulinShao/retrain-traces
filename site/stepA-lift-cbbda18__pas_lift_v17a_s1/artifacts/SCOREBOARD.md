# SCOREBOARD

playbook: nogit-58e9eacc
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | lift1 |
|---|---|---|
| lift | 67/100 = 67% | 86/100 = 86% (base 67% = 67.0/100) |

GPU-hours: 7.318 spent, 0.682 remaining of 8.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: lift1
Submitted: base + lift1 (sha 146763929b5b) (turn 32, token a15a13; confirmed in turn 33)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| lift1 | base | 30 | spec_lift1.json | trained |

## History (latest 30)

- train lift1 (init base, steps 30): trained
- eval lift1 on lift: 86/100
- load lift1
- finish: submitted lift1 (token a15a13, job 18)
- finish: confirmed lift1 (token a15a13)
