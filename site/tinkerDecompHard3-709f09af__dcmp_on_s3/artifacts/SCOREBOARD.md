# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B
eval_backend: tinker, decode=tinker(no_presence_penalty) (DEV backend only: dev/checkpoint evals of Tinker-trained adapters sample on Tinker; hidden evals and other adapters run locally)

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | rv6 | n6 | rs6 | rv7 | rs7 | n7 | rn |
|---|---|---|---|---|---|---|---|---|
| nut | 0/20 = 0% | untested | 0/20 = 0% (base 0% = 0.0/20) | untested | untested | untested | 0/20 = 0% (base 0% = 0.0/20) | 0/20 = 0% (base 0% = 0.0/20) |
| restack | 0/20 = 0% | untested | untested | 0/20 = 0% (base 0% = 0.0/20) | untested | 0/20 = 0% (base 0% = 0.0/20) | untested | 0/20 = 0% (base 0% = 0.0/20) |
| revstack | 0/20 = 0% | 1/20 = 5% (base 0% = 0.0/20) | untested | untested | 1/20 = 5% (base 0% = 0.0/20) | untested | untested | 0/20 = 0% (base 0% = 0.0/20) |

GPU-hours: 15.527 spent, 0.473 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.39, 10 steps 1.98, 50 steps 9.03) GPU-h; eval.py per task (5 seeds 0.15, 20 seeds 0.19, 100 seeds 0.45) GPU-h
Loaded on your serving endpoint: rv7
Submitted: base + rv7 (sha 047b44aecb10) (turn 88, token 7b39f2; confirmed in turn 89)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| rv6 | base | 6 | specs/rv6.json | trained |
| n6 | base | 6 | specs/n6.json | trained |
| rs6 | base | 6 | specs/rs6.json | trained |
| rv7 | rv6 | 12 | specs/rv7.json | trained |
| rs7 | rs6 | 8 | specs/rs7.json | trained |
| n7 | n6 | 8 | specs/n7.json | trained |
| rn | rv7 | 10 | specs/rn.json | trained |

- train job 43 (rv7): note set: part of the training prompt only; every eval, including the final score, uses tasks/revstack/eval_prompt.txt verbatim
- train job 44 (rs7): note set: part of the training prompt only; every eval, including the final score, uses tasks/restack/eval_prompt.txt verbatim
- train job 45 (n7): note set: part of the training prompt only; every eval, including the final score, uses tasks/nut/eval_prompt.txt verbatim

## Self-reward (rollout.py --reward: your reward over the rollout facts; not a success count)

- none yet

## Failure digest (facts: a train's lowest-reward episodes per task; full records in failures.jsonl)

- revstack: 16 failures in adapters/rv6/failures.jsonl; stages unavailable:16
- nut: 16 failures in adapters/n6/failures.jsonl; stages none:15 grasp the nut:1
- restack: 16 failures in adapters/rs6/failures.jsonl; stages none:16
- revstack: 16 failures in adapters/rv7/failures.jsonl; stages unavailable:16
- restack: 16 failures in adapters/rs7/failures.jsonl; stages none:15 grasp the red:1
- nut: 16 failures in adapters/n7/failures.jsonl; stages none:14 grasp the nut:2
- restack: 16 failures in adapters/rn/failures.jsonl; stages none:15 unstack the green off the red:1
- nut: 16 failures in adapters/rn/failures.jsonl; stages none:16

## History (latest 30)

- preset probe_r2 on restack: 8 seeds -> presets/probe_r2.json
- eval rv6 on revstack: 1/20
- eval rs6 on restack: 0/20
- eval n6 on nut: 0/20
- preset probe_r3 on restack: 8 seeds -> presets/probe_r3.json
- preset probe_r4 on restack: 4 seeds -> presets/probe_r4.json
- preset probe_r5 on restack: 4 seeds -> presets/probe_r5.json
- preset probe_r5 on restack: 4 seeds -> presets/probe_r5.json
- preset probe_r6 on restack: 4 seeds -> presets/probe_r6.json
- preset probe_nut on nut: 4 seeds -> presets/probe_nut.json
- preset probe_r7 on restack: 4 seeds -> presets/probe_r7.json
- preset probe_r8 on restack: 6 seeds -> presets/probe_r8.json
- preset probe_nut2 on nut: 6 seeds -> presets/probe_nut2.json
- rollout base on restack: 6 seeds -> rollouts/40.jsonl
- rollout base on nut: 6 seeds -> rollouts/41.jsonl
- finish: submission 8809f4 cancelled by job 43 (train)
- train rv7 (init rv6, steps 12): trained
- train rs7 (init rs6, steps 8): trained
- train n7 (init n6, steps 8): trained
- eval rv7 on revstack: 1/20
- eval n7 on nut: 0/20
- eval rs7 on restack: 0/20
- train tri failed: train: task 'revstack' runs its simulator under a scene shift (capx_suite_scene_shift) and practises alone; name it in a spec of its own
- train rn (init rv7, steps 10): trained
- eval rn on revstack: 0/20
- eval rn on restack: 0/20
- eval rn on nut: 0/20
- load rv7
- finish: submitted rv7 (token 7b39f2, job 60)
- finish: confirmed rv7 (token 7b39f2)
