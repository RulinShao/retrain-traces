# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | wipe1 |
|---|---|---|
| wipe | 16/100 = 16% | 54/100 = 54% (base 16% = 16.0/100) |

GPU-hours: 6.615 spent, 1.385 remaining of 8.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: base
Submitted: base + wipe1 (sha a4e9ecb597f4) (turn 20, token 24380d; confirmed in turn 21)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| wipe1 | base | 25 | specs/wipe1.json | trained |

- train job 1 (wipe1): note set: part of the training prompt only; every eval, including the final score, uses tasks/wipe/eval_prompt.txt verbatim

## History (latest 30)

- train wipe1 (init base, steps 25): trained
- eval wipe1 on wipe: 54/100
- finish: submitted wipe1 (token 24380d, job 10)
- finish: confirmed wipe1 (token 24380d)
