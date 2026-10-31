# SCOREBOARD

playbook: 212e0bab-a57a4058
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | stack1 | wipe1 | wipe1+stack1 |
|---|---|---|---|---|
| lift | 67/100 = 67% | untested | untested | 76/100 = 76% (base 67% = 67.0/100) |
| stack | 51/100 = 51% | 62/100 = 62% (base 51% = 51.0/100) | untested | 54/100 = 54% (base 51% = 51.0/100) |
| nut | 0/100 = 0% | untested | untested | 0/20 = 0% (base 0% = 0.0/20) |
| wipe | 16/100 = 16% | untested | 76/100 = 76% (base 16% = 16.0/100) | 84/100 = 84% (base 16% = 16.0/100) |
| restack | 0/100 = 0% | untested | untested | 0/20 = 0% (base 0% = 0.0/20) |
| twolift | 1/100 = 1% | untested | untested | 0/20 = 0% (base 1% = 0.2/20) |
| handover | 2/100 = 2% | untested | untested | 0/20 = 0% (base 2% = 0.4/20) |
| revstack | 0/100 = 0% | untested | untested | 1/20 = 5% (base 0% = 0.0/20) |
| stackv2 | 1/100 = 1% | untested | untested | 0/20 = 0% (base 1% = 0.2/20) |

GPU-hours: 15.801 spent, 0.199 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: wipe1+stack1
Submitted: base + wipe1 (sha e8e9a79c3209) + stack1 (sha 9df57f3efbca) (turn 34, token 46548e; confirmed in turn 35)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| stack1 | base | 12 | specs/stack.json | trained |
| wipe1 | base | 30 | specs/wipe.json | trained |

## History (latest 30)

- train stack1 (init base, steps 12): trained
- train wipe1 (init base, steps 30): trained
- eval wipe1+stack1 on wipe: 84/100
- eval wipe1+stack1 on stack: 54/100
- eval wipe1+stack1 on nut: 0/20
- eval wipe1+stack1 on restack: 0/20
- eval wipe1+stack1 on revstack: 1/20
- eval wipe1+stack1 on twolift: 0/20
- eval wipe1+stack1 on lift: 76/100
- eval wipe1+stack1 on stackv2: 0/20
- eval wipe1+stack1 on handover: 0/20
- eval wipe1 on wipe: 76/100
- eval stack1 on stack: 62/100
- load wipe1+stack1
- finish: submitted wipe1+stack1 (token 46548e, job 32)
- finish: confirmed wipe1+stack1 (token 46548e)
