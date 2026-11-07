# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B
eval_backend: tinker, decode=tinker(no_presence_penalty) (DEV backend only: dev/checkpoint evals of Tinker-trained adapters sample on Tinker; hidden evals and other adapters run locally)

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | a_nr10 | b_rs10 | a_nr20 | b_rs20 | b_rs30 | a_nr20+b_rs30 |
|---|---|---|---|---|---|---|---|
| nut | 0/100 = 0% | 0/100 = 0% (base 0% = 0.0/100) | untested | untested | untested | untested | 0/100 = 0% (base 0% = 0.0/100) |
| restack | 0/100 = 0% | 0/100 = 0% (base 0% = 0.0/100) | untested | untested | untested | untested | 0/100 = 0% (base 0% = 0.0/100) |
| revstack | 3/100 = 3% | untested | 2/100 = 2% (base 3% = 3.0/100) | untested | untested | untested | 5/100 = 5% (base 3% = 3.0/100) |

GPU-hours: 15.965 spent, 0.035 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.39, 10 steps 1.98, 50 steps 9.03) GPU-h; eval.py per task (5 seeds 0.15, 20 seeds 0.19, 100 seeds 0.45) GPU-h
Loaded on your serving endpoint: base
Submitted: base + a_nr20 (sha d44389fba451) + b_rs30 (sha 3be378fb6ee1) (turn 21, token b8ca8f; confirmed in turn 22)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| a_nr10 | base | 10 | spec_a.json | trained |
| b_rs10 | base | 10 | spec_b.json | trained |
| a_nr20 | a_nr10 | 10 | spec_a2.json | trained |
| b_rs20 | b_rs10 | 10 | spec_b2.json | trained |
| b_rs30 | b_rs20 | 5 | spec_b3.json | trained |

## History (latest 30)

- eval base on nut: 0/100
- eval base on restack: 0/100
- eval base on revstack: 3/100
- train a_nr10 (init base, steps 10): trained
- train b_rs10 (init base, steps 10): trained
- eval a_nr10 on nut: 0/100
- eval a_nr10 on restack: 0/100
- eval b_rs10 on revstack: 2/100
- train a_nr20 (init a_nr10, steps 10): trained
- train b_rs20 (init b_rs10, steps 10): trained
- train b_rs30 (init b_rs20, steps 5): trained
- eval a_nr20+b_rs30 on nut: 0/100
- eval a_nr20+b_rs30 on restack: 0/100
- eval a_nr20+b_rs30 on revstack: 5/100
- finish: submitted a_nr20+b_rs30 (token b8ca8f, job 22)
- finish: confirmed a_nr20+b_rs30 (token b8ca8f)
