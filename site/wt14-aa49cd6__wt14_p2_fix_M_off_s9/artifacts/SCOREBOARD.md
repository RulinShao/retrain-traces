# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | core3 | rev | nutrst |
|---|---|---|---|---|
| lift | 67/100 = 67% | 2/5 = 40% (base 67% = 3.4/5) | untested | untested |
| stack | 51/100 = 51% | 4/5 = 80% (base 51% = 2.5/5) | untested | untested |
| nut | 0/100 = 0% | 0/5 = 0% (base 0% = 0.0/5) | untested | untested |
| wipe | 16/100 = 16% | 2/5 = 40% (base 16% = 0.8/5) | untested | untested |
| restack | 0/100 = 0% | 0/5 = 0% (base 0% = 0.0/5) | untested | untested |
| twolift | 1/100 = 1% | 0/5 = 0% (base 1% = 0.1/5) | untested | untested |
| handover | 2/100 = 2% | 0/5 = 0% (base 2% = 0.1/5) | untested | untested |
| revstack | 0/100 = 0% | 0/5 = 0% (base 0% = 0.0/5) | untested | untested |
| stackv2 | 1/100 = 1% | untested | untested | untested |

GPU-hours: 15.770 spent, 0.230 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 2.76, 10 steps 4.03, 50 steps 9.65) GPU-h; eval.py per task (5 seeds 0.36, 20 seeds 0.38, 100 seeds 0.48) GPU-h
Loaded on your serving endpoint: core3
Submitted: base + core3 (sha f3941afcb6e1) (turn 32, token f67405; confirmed in turn 33)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| core3 | base | 6 | specs/core3.json | trained |
| rev | base | 6 | specs/rev.json | trained |
| nutrst | base | 6 | specs/nutrst.json | trained |

- train job 3 (rev): note set: part of the training prompt only; every eval, including the final score, uses tasks/revstack/eval_prompt.txt verbatim

## History (latest 30)

- train core3 (init base, steps 6): trained
- train rev (init base, steps 6): trained
- load core3
- train nutrst (init base, steps 6): trained
- eval core3 on lift: 2/5
- eval core3 on stack: 4/5
- eval core3 on wipe: 2/5
- eval core3 on nut: 0/5
- eval core3 on restack: 0/5
- eval core3 on twolift: 0/5
- eval core3 on handover: 0/5
- eval core3 on revstack: 0/5
- finish: submitted core3 (token f67405, job 23)
- finish: confirmed core3 (token f67405)
