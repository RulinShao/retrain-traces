# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | lift30 |
|---|---|---|
| lift | 62/100 = 62% | 88/100 = 88% (base 62% = 62.0/100) |

GPU-hours: 7.798 spent, 0.202 remaining of 8.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: lift30
Submitted: base + lift30 (sha a63f53f5cc66) (turn 152, token 06e906; confirmed in turn 153)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| lift30 | base | 30 | train1.yaml | trained |

## History (latest 30)

- train lift30 (init base, steps 30): trained
- eval lift30 on lift: 88/100
- eval base on lift: 62/100
- load lift30
- finish: submitted lift30 (token 06e906, job 12)
- finish: confirmed lift30 (token 06e906)
