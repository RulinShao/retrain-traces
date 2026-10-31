# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | lift33 |
|---|---|---|
| lift | 67/100 = 67% | 86/100 = 86% (base 67% = 67.0/100) |

GPU-hours: 7.740 spent, 0.260 remaining of 8.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: lift33
Submitted: base + lift33 (sha 966a1bfaf09d) (turn 15, token 0b10c3; confirmed in turn 16)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| lift33 | base | 33 | spec_lift33.json | trained |

## History (latest 30)

- train lift33 (init base, steps 33): trained
- load lift33
- eval lift33 on lift: 86/100
- finish: submitted lift33 (token 0b10c3, job 8)
- finish: confirmed lift33 (token 0b10c3)
