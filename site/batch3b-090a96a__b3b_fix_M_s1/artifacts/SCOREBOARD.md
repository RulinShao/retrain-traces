# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | stack1 | restack1 | stack1+restack1 |
|---|---|---|---|---|
| lift | 67/100 = 67% | 73/100 = 73% (base 67% = 67.0/100) | untested | 82/100 = 82% (base 67% = 67.0/100) |
| stack | 51/100 = 51% | 61/100 = 61% (base 51% = 51.0/100) | untested | 59/100 = 59% (base 51% = 51.0/100) |
| nut | 0/100 = 0% | untested | untested | untested |
| wipe | 16/100 = 16% | untested | untested | 36/100 = 36% (base 16% = 16.0/100) |
| restack | 0/100 = 0% | 0/100 = 0% (base 0% = 0.0/100) | 0/100 = 0% (base 0% = 0.0/100) | 0/100 = 0% (base 0% = 0.0/100) |
| twolift | 1/100 = 1% | untested | untested | untested |
| handover | 2/100 = 2% | untested | untested | untested |
| revstack | 0/100 = 0% | 2/100 = 2% (base 0% = 0.0/100) | untested | 5/100 = 5% (base 0% = 0.0/100) |
| stackv2 | 1/100 = 1% | 2/100 = 2% (base 1% = 1.0/100) | untested | 2/100 = 2% (base 1% = 1.0/100) |

GPU-hours: 15.707 spent, 0.293 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: stack1+restack1
Submitted: base + stack1 (sha 261bccdabc2a) + restack1 (sha ae5f2e87c5e6) (turn 17, token 4d4f34; unconfirmed; scored at the session end (DONE))

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| stack1 | base | 15 | specs/exp_stack.json | trained |
| restack1 | base | 15 | specs/exp_restack.json | trained |

- train job 2 (restack1): note set: part of the training prompt only; every eval, including the final score, uses tasks/restack/eval_prompt.txt verbatim

## History (latest 30)

- train stack1 (init base, steps 15): trained
- train restack1 (init base, steps 15): trained
- eval stack1 on stack: 61/100
- eval restack1 on restack: 0/100
- eval stack1+restack1 on stack: 59/100
- eval stack1+restack1 on restack: 0/100
- eval stack1+restack1 on lift: 82/100
- eval stack1 on lift: 74/100
- eval stack1+restack1 on stackv2: 2/100
- eval stack1+restack1 on revstack: 5/100
- eval stack1+restack1 on wipe: 36/100
- eval stack1 on lift: 73/100
- eval stack1 on restack: 0/100
- eval stack1 on revstack: 2/100
- eval stack1 on stackv2: 2/100
- load stack1+restack1
- finish: submitted stack1+restack1 (token 4d4f34, DONE file of the last turn (legacy end rule: the session ended there); scored by resume)
