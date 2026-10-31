# SCOREBOARD

playbook: nogit-a57a4058
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | lift_a |
|---|---|---|
| lift | 67/100 = 67% | 89/100 = 89% (base 67% = 67.0/100) |

GPU-hours: 7.318 spent, 0.682 remaining of 8.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: lift_a
Submitted: base + lift_a (sha 8648a4b4cf17) (turn 21, token b9e5f5; confirmed in turn 22)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| lift_a | base | 30 | spec_lift_a.json | trained |

## History (latest 30)

- train lift_a (init base, steps 30): trained
- load lift_a
- eval lift_a on lift: 89/100
- finish: submitted lift_a (token b9e5f5, job 8)
- finish: confirmed lift_a (token b9e5f5)
