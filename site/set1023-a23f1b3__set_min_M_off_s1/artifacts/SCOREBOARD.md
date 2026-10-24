# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base |
|---|---|
| lift | 67/100 = 67% |
| stack | 51/100 = 51% |
| nut | 0/100 = 0% |
| wipe | 16/100 = 16% |
| restack | 0/100 = 0% |
| twolift | 1/100 = 1% |
| handover | 2/100 = 2% |
| revstack | 0/100 = 0% |
| stackv2 | 1/100 = 1% |

GPU-hours: 0.000 spent, 3.922 remaining of 16.0 (3 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: base
Submitted: none (python3 finish.py submits a policy)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|

- train job 1 (s1_stack): note set: part of the training prompt only; every eval, including the final score, uses tasks/stack/eval_prompt.txt verbatim
- train job 2 (s1_lift): note set: part of the training prompt only; every eval, including the final score, uses tasks/lift/eval_prompt.txt verbatim
- train job 3 (s1_wipe): note set: part of the training prompt only; every eval, including the final score, uses tasks/wipe/eval_prompt.txt verbatim

## History (latest 30)

