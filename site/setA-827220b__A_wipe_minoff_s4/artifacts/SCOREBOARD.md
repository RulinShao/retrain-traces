# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base |
|---|---|
| wipe | 16/100 = 16% |

GPU-hours: 0.000 spent, 8.000 remaining of 8.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: base
Submitted: base (turn 29, token 181e10; confirmed in turn 33)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|

- train job 1 (wipe1): note set: part of the training prompt only; every eval, including the final score, uses tasks/wipe/eval_prompt.txt verbatim
- train job 13 (wipe1b): note set: part of the training prompt only; every eval, including the final score, uses tasks/wipe/eval_prompt.txt verbatim

## History (latest 30)

- cancel job 1
- train wipe1 failed: train cancelled with no saved step to keep; charged 0.0 GPU-h
- cancel job 13
- finish: submitted base (token 181e10, job 27)
- train wipe1b failed: train cancelled with no saved step to keep; charged 0.0 GPU-h
- finish: confirmed base (token 181e10)
