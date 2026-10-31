# SCOREBOARD

playbook: 7b74a5fa-a57a4058
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | stack30 |
|---|---|---|
| stack | 51/100 = 51% | 72/100 = 72% (base 51% = 51.0/100) |

GPU-hours: 7.318 spent, 0.682 remaining of 8.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: stack30
Submitted: base + stack30 (sha 85a072fb134e) (turn 15, token 66f598; confirmed in turn 17)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| stack30 | base | 30 | spec_stack30.json | trained |

## History (latest 30)

- train stack30 (init base, steps 30): trained
- eval stack30 on stack: 72/100
- load stack30
- finish: submitted stack30 (token 66f598, job 10)
- finish: confirmed stack30 (token 66f598)
