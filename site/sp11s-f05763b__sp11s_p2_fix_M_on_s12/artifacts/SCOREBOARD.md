# SCOREBOARD

playbook: e9fea0d6-a57a4058
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | rev1 | wipe1 |
|---|---|---|---|
| lift | 67/100 = 67% | untested | 63/100 = 63% (base 67% = 67.0/100) |
| stack | 51/100 = 51% | untested | 57/100 = 57% (base 51% = 51.0/100) |
| nut | 0/100 = 0% | untested | 0/20 = 0% (base 0% = 0.0/20) |
| wipe | 16/100 = 16% | untested | 90/100 = 90% (base 16% = 16.0/100) |
| restack | 0/100 = 0% | untested | 0/20 = 0% (base 0% = 0.0/20) |
| twolift | 1/100 = 1% | untested | 0/20 = 0% (base 1% = 0.2/20) |
| handover | 2/100 = 2% | untested | 0/20 = 0% (base 2% = 0.4/20) |
| revstack | 0/100 = 0% | untested | 0/20 = 0% (base 0% = 0.0/20) |
| stackv2 | 1/100 = 1% | untested | 0/20 = 0% (base 1% = 0.2/20) |

GPU-hours: 12.592 spent, 3.408 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: wipe1
Submitted: base + wipe1 (sha a59308fada08) (turn 23, token 38347e; confirmed in turn 24)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| rev1 | base | 1 | specs/rev1.json | trained 1 steps; weights unchanged (all-zero update: 0/304 nonzero lora_B) |
| wipe1 | base | 25 | specs/wipe1.json | trained |

## History (latest 30)

- train rev1 (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/304 nonzero lora_B)
- train wipe1 (init base, steps 25): trained
- load wipe1
- eval wipe1 on wipe: 90/100
- eval wipe1 on lift: 63/100
- eval wipe1 on stack: 57/100
- eval wipe1 on nut: 0/20
- eval wipe1 on restack: 0/20
- eval wipe1 on twolift: 0/20
- eval wipe1 on revstack: 0/20
- eval wipe1 on handover: 0/20
- eval wipe1 on stackv2: 0/20
- finish: submitted wipe1 (token 38347e, job 19)
- finish: confirmed wipe1 (token 38347e)
