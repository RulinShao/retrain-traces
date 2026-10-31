# SCOREBOARD

playbook: 7b74a5fa-a57a4058
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | lift10 |
|---|---|---|
| lift | 67/100 = 67% | 79/100 = 79% (base 67% = 67.0/100) |

GPU-hours: 4.506 spent, 3.494 remaining of 8.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: lift10
Submitted: base + lift10 (sha 9e21d9fd170e) (turn 16, token cea708; confirmed in turn 17)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| lift10 | base | 10 | spec_lift10.json | trained |

## History (latest 30)

- train lift10 (init base, steps 10): trained
- load lift10
- eval lift10 on lift: 79/100
- finish: submitted lift10 (token cea708, job 14)
- finish: confirmed lift10 (token cea708)
