# SCOREBOARD

playbook: 7b74a5fa-a57a4058
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | lift20 |
|---|---|---|
| lift | 67/100 = 67% | 85/100 = 85% (base 67% = 67.0/100) |

GPU-hours: 5.912 spent, 2.088 remaining of 8.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: lift20
Submitted: base + lift20 (sha a94b9771930b) (turn 41, token 36e1d3; confirmed in turn 42)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| lift20 | base | 20 | spec_lift20.json | trained |

## History (latest 30)

- train lift20 (init base, steps 20): trained
- load lift20
- eval lift20 on lift: 85/100
- finish: submitted lift20 (token 36e1d3, job 23)
- finish: confirmed lift20 (token 36e1d3)
