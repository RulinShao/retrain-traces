# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B
eval_backend: tinker, decode=tinker(no_presence_penalty) (DEV backend only: dev/checkpoint evals of Tinker-trained adapters sample on Tinker; hidden evals and other adapters run locally)

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | t1_nutrestack | t2_revstack | r2_nr | r2_rev | r2_nr+r2_rev |
|---|---|---|---|---|---|---|
| nut | 0/20 = 0% | untested | untested | untested | untested | 0/20 = 0% (base 0% = 0.0/20) |
| restack | 0/20 = 0% | untested | untested | untested | untested | 0/20 = 0% (base 0% = 0.0/20) |
| revstack | 0/20 = 0% | untested | untested | untested | untested | 0/20 = 0% (base 0% = 0.0/20) |

GPU-hours: 14.708 spent, 1.292 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.39, 10 steps 1.98, 50 steps 9.03) GPU-h; eval.py per task (5 seeds 0.15, 20 seeds 0.19, 100 seeds 0.45) GPU-h
Loaded on your serving endpoint: r2_nr+r2_rev
Submitted: base + r2_nr (sha 5da9a7532d99) + r2_rev (sha bc7a227a9f24) (turn 21, token 96a7da; confirmed in turn 22)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| t1_nutrestack | base | 20 | t1_nutrestack.json | trained |
| t2_revstack | base | 20 | t2_revstack.json | trained |
| r2_nr | base | None | spec_r2_nr.json | trained |
| r2_rev | base | None | spec_r2_rev.json | trained |

- train job 7 (r2_nr): prompt in 128 data row(s) set: part of the training prompt only; every eval, including the final score, uses tasks/<task>/eval_prompt.txt verbatim
- train job 8 (r2_rev): prompt in 128 data row(s) set: part of the training prompt only; every eval, including the final score, uses tasks/<task>/eval_prompt.txt verbatim

## History (latest 30)

- eval base on nut: 0/20
- eval base on restack: 0/20
- eval base on revstack: 0/20
- train t1_nutrestack (init base, steps 20): trained
- train t2_revstack (init base, steps 20): trained
- train r2_nr (init base, steps None): trained
- train r2_rev (init base, steps None): trained
- load r2_nr+r2_rev
- eval r2_nr+r2_rev on nut: 0/20
- eval r2_nr+r2_rev on restack: 0/20
- eval r2_nr+r2_rev on revstack: 0/20
- finish: submitted r2_nr+r2_rev (token 96a7da, job 15)
- finish: confirmed r2_nr+r2_rev (token 96a7da)
