# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | stack_antiapi_r1 | wipe_r2 |
|---|---|---|---|
| lift | 67/100 = 67% | 68/100 = 68% (base 67% = 67.0/100) | untested |
| stack | 51/100 = 51% | 52/100 = 52% (base 51% = 51.0/100) | untested |
| nut | 0/100 = 0% | 0/100 = 0% (base 0% = 0.0/100) | untested |
| wipe | 16/100 = 16% | 25/100 = 25% (base 16% = 16.0/100) | 28/100 = 28% (base 16% = 16.0/100) |
| restack | 0/100 = 0% | 0/100 = 0% (base 0% = 0.0/100) | untested |
| twolift | 1/100 = 1% | 0/100 = 0% (base 1% = 1.0/100) | untested |
| handover | 2/100 = 2% | 1/100 = 1% (base 2% = 2.0/100) | untested |
| revstack | 0/100 = 0% | 3/100 = 3% (base 0% = 0.0/100) | untested |
| stackv2 | 1/100 = 1% | 2/100 = 2% (base 1% = 1.0/100) | untested |

GPU-hours: 15.664 spent, 0.336 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: wipe_r2
Submitted: base + wipe_r2 (sha 62685560ea18) (turn 41, token 503f0a; confirmed in turn 42)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| stack_antiapi_r1 | base | 30 | specs/stack_antiapi_r1.json | trained |
| wipe_r2 | stack_antiapi_r1 | 10 | specs/wipe_r2.json | trained |

- train job 1 (stack_antiapi_r1): note set: part of the training prompt only; every eval, including the final score, uses tasks/stack/eval_prompt.txt verbatim
- train job 21 (wipe_r2): note set: part of the training prompt only; every eval, including the final score, uses tasks/wipe/eval_prompt.txt verbatim

## History (latest 30)

- train stack_antiapi_r1 (init base, steps 30): trained
- eval stack_antiapi_r1 on lift: 68/100
- eval stack_antiapi_r1 on wipe: 25/100
- eval stack_antiapi_r1 on twolift: 0/100
- eval stack_antiapi_r1 on revstack: 3/100
- eval stack_antiapi_r1 on nut: 0/100
- eval stack_antiapi_r1 on restack: 0/100
- eval stack_antiapi_r1 on stack: 52/100
- eval stack_antiapi_r1 on handover: 1/100
- eval stack_antiapi_r1 on stackv2: 2/100
- load stack_antiapi_r1
- train wipe_r2 (init stack_antiapi_r1, steps 10): trained
- eval wipe_r2 on wipe: 28/100
- load wipe_r2
- finish: submitted wipe_r2 (token 503f0a, job 29)
- finish: confirmed wipe_r2 (token 503f0a)
