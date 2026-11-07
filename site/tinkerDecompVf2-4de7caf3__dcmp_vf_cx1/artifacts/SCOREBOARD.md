# SCOREBOARD

playbook: none
agent: codex:gpt-6-astra
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B
eval_backend: tinker, decode=tinker(no_presence_penalty) (DEV backend only: dev/checkpoint evals of Tinker-trained adapters sample on Tinker; hidden evals and other adapters run locally)

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | reverse12 | mixed12 | reverse_sft | restack_guided | reverse_complete | success_clean | mixed12+reverse12 |
|---|---|---|---|---|---|---|---|---|
| nut | untested | 0/20 = 0% | 0/20 = 0% | 0/20 = 0% | 0/20 = 0% | 0/20 = 0% | 0/20 = 0% | 0/20 = 0% |
| restack | untested | 0/20 = 0% | 0/20 = 0% | 0/20 = 0% | 0/50 = 0% | 0/20 = 0% | 0/20 = 0% | 0/20 = 0% |
| revstack | untested | 2/50 = 4% | 3/100 = 3% | 3/100 = 3% | 0/50 = 0% | 0/100 = 0% | 7/100 = 7% | 6/100 = 6% |

GPU-hours: 15.348 spent, 0.652 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.39, 10 steps 1.98, 50 steps 9.03) GPU-h; eval.py per task (5 seeds 0.15, 20 seeds 0.19, 100 seeds 0.45) GPU-h
Loaded on your serving endpoint: success_clean
Submitted: base + success_clean (sha 5caabbd1a22c) (turn 3985, token eb941a; confirmed in turn 3992)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| reverse12 | base | 12 | specs/reverse12.json | trained |
| mixed12 | base | 12 | specs/mixed12.json | trained |
| reverse_sft | reverse12 | None | specs/reverse_sft.json | trained |
| restack_guided | mixed12 | 10 | specs/restack_guided.json | trained |
| reverse_complete | reverse12 | 20 | specs/reverse_complete.json | trained |
| success_clean | mixed12 | None | specs/success_clean.json | trained |

- train job 19 (restack_guided): note set: part of the training prompt only; every eval, including the final score, uses tasks/restack/eval_prompt.txt verbatim
- train job 21 (restack_guided): note set: part of the training prompt only; every eval, including the final score, uses tasks/restack/eval_prompt.txt verbatim
- train job 31 (success_clean): prompt in 7 data row(s) set: part of the training prompt only; every eval, including the final score, uses tasks/<task>/eval_prompt.txt verbatim

## Self-reward (rollout.py --reward: your reward over the rollout facts; not a success count)

- none yet

## Failure digest (facts: a train's lowest-reward episodes per task; full records in failures.jsonl)

- revstack: 16 failures in adapters/reverse12/failures.jsonl; stages none:15 reach the green_cube:1
- nut: 16 failures in adapters/mixed12/failures.jsonl; stages none:16
- restack: 16 failures in adapters/mixed12/failures.jsonl; stages none:13 unstack the green off the red:3
- restack: 16 failures in adapters/restack_guided/failures.jsonl; stages none:11 unstack the green off the red:5
- revstack: 16 failures in adapters/reverse_complete/failures.jsonl; stages grasp the green_cube:7 none:7 reach the green_cube:2

## History (latest 30)

- eval reverse12 on revstack: 2/50
- eval reverse12 on restack: 0/20
- eval reverse12 on nut: 0/20
- eval mixed12 on revstack: 2/20
- eval mixed12 on restack: 0/20
- eval mixed12 on nut: 0/20
- train reverse_sft (init reverse12, steps None): trained
- eval reverse_sft on revstack: 3/100
- eval reverse_sft on restack: 0/20
- eval reverse_sft on nut: 0/20
- train restack_guided failed: train: init_mode branch (weights only, fresh optimizer) is not available on this trainer, which restores full state or nothing; use resume, or fresh
- train restack_guided (init mixed12, steps 10): trained
- train reverse_complete (init reverse12, steps 20): trained
- eval reverse_complete on revstack: 0/100
- eval reverse_complete on restack: 0/20
- eval reverse_complete on nut: 0/20
- eval restack_guided on revstack: 0/50
- eval restack_guided on restack: 0/50
- eval restack_guided on nut: 0/20
- train success_clean (init mixed12, steps None): trained
- eval mixed12 on revstack: 3/100
- eval mixed12+reverse12 on restack: 0/20
- eval mixed12+reverse12 on nut: 0/20
- eval mixed12+reverse12 on revstack: 6/100
- eval success_clean on nut: 0/20
- eval success_clean on restack: 0/20
- eval success_clean on revstack: 7/100
- load success_clean
- finish: submitted success_clean (token eb941a, job 42)
- finish: confirmed success_clean (token eb941a)
