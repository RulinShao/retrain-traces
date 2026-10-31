# SCOREBOARD

playbook: nogit-f045ba05
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | lift10 | stack30 | stack30+lift10 |
|---|---|---|---|---|
| lift | 67/100 = 67% | untested | untested | 77/100 = 77% (base 67% = 67.0/100) |
| stack | 51/100 = 51% | untested | untested | 54/100 = 54% (base 51% = 51.0/100) |
| nut | 0/100 = 0% | untested | untested | 0/100 = 0% (base 0% = 0.0/100) |
| wipe | 16/100 = 16% | untested | untested | 14/100 = 14% (base 16% = 16.0/100) |
| restack | 0/100 = 0% | untested | untested | 0/100 = 0% (base 0% = 0.0/100) |
| twolift | 1/100 = 1% | untested | untested | 3/100 = 3% (base 1% = 1.0/100) |
| handover | 2/100 = 2% | untested | untested | 0/100 = 0% (base 2% = 2.0/100) |
| revstack | 0/100 = 0% | untested | untested | 0/100 = 0% (base 0% = 0.0/100) |
| stackv2 | 1/100 = 1% | untested | untested | 0/100 = 0% (base 1% = 1.0/100) |

GPU-hours: 15.184 spent, 0.816 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: stack30+lift10
Submitted: base + stack30 (sha f88d14a5139e) + lift10 (sha 2158c773cf25) (turn 23, token 1f8d06; confirmed in turn 24)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| lift10 | base | 10 | spec_lift10.json | trained |
| stack30 | base | 30 | spec_stack30.json | trained |

## History (latest 30)

- train lift10 (init base, steps 10): trained
- train stack30 (init base, steps 30): trained
- load stack30+lift10
- eval stack30+lift10 on lift: 77/100
- eval stack30+lift10 on stack: 54/100
- eval stack30+lift10 on nut: 0/100
- eval stack30+lift10 on wipe: 14/100
- eval stack30+lift10 on restack: 0/100
- eval stack30+lift10 on twolift: 3/100
- eval stack30+lift10 on handover: 0/100
- eval stack30+lift10 on revstack: 0/100
- eval stack30+lift10 on stackv2: 0/100
- finish: submitted stack30+lift10 (token 1f8d06, job 22)
- finish: confirmed stack30+lift10 (token 1f8d06)
