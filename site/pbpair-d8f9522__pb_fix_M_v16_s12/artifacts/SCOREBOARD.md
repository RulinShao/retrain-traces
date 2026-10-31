# SCOREBOARD

playbook: 7b74a5fa-a57a4058
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | w1 | s1 | s1+w1 |
|---|---|---|---|---|
| lift | 67/100 = 67% | 50/100 = 50% (base 67% = 67.0/100) | untested | 53/100 = 53% (base 67% = 67.0/100) |
| stack | 51/100 = 51% | 51/100 = 51% (base 51% = 51.0/100) | 53/100 = 53% (base 51% = 51.0/100) | 61/100 = 61% (base 51% = 51.0/100) |
| nut | 0/100 = 0% | untested | untested | untested |
| wipe | 16/100 = 16% | 77/100 = 77% (base 16% = 16.0/100) | untested | 39/50 = 78% (base 16% = 8.0/50) |
| restack | 0/100 = 0% | untested | untested | untested |
| twolift | 1/100 = 1% | untested | untested | untested |
| handover | 2/100 = 2% | untested | untested | untested |
| revstack | 0/100 = 0% | untested | untested | untested |
| stackv2 | 1/100 = 1% | untested | untested | untested |

GPU-hours: 15.676 spent, 0.324 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: s1+w1
Submitted: base + s1 (sha 0fd3656d8e01) + w1 (sha e92f6d6e0a16) (turn 87, token 33bb08; confirmed in turn 88)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| w1 | base | 25 | specs/w1.json | trained |
| s1 | base | 15 | specs/s1.json | trained |

## History (latest 30)

- train w1 (init base, steps 25): trained
- load w1
- eval w1 on wipe: 77/100
- eval w1 on stack: 8/20
- eval w1 on lift: 9/20
- eval w1 on lift: 50/100
- eval w1 on stack: 51/100
- train s1 (init base, steps 15): trained
- eval s1 on stack: 53/100
- eval s1+w1 on stack: 61/100
- eval s1+w1 on lift: 53/100
- eval s1+w1 failed: eval reached its Slurm time limit before the cell runner wrote results (it writes them only when all 100 seeds finish); no seed counted (job 42549548); charged 0.350 GPU-h
- eval w1 on lift: 23/50 (scoreboard cell keeps 50/100: more seeds)
- eval s1+w1 on wipe: 39/50
- load s1+w1
- finish: submitted s1+w1 (token 33bb08, job 72)
- finish: confirmed s1+w1 (token 33bb08)
