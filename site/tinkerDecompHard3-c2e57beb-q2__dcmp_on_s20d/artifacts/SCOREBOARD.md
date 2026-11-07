# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 800001
policy: Qwen3.8-27B
eval_backend: tinker, decode=tinker(no_presence_penalty) (DEV backend only: dev/checkpoint evals of Tinker-trained adapters sample on Tinker; hidden evals and other adapters run locally)

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | grpo_rev | grpo_rest | grpo_nut | grpo_rev2 | grpo_rev+grpo_rest | grpo_rev+grpo_rev2 |
|---|---|---|---|---|---|---|---|
| nut | 0/100 = 0% | 0/20 = 0% (base 0% = 0.0/20) | untested | 0/20 = 0% (base 0% = 0.0/20) | untested | untested | untested |
| restack | 0/100 = 0% | 0/20 = 0% (base 0% = 0.0/20) | 0/20 = 0% (base 0% = 0.0/20) | untested | untested | 0/20 = 0% (base 0% = 0.0/20) | untested |
| revstack | 1/100 = 1% | 0/50 = 0% (base 1% = 0.5/50) | untested | untested | 1/50 = 2% (base 1% = 0.5/50) | untested | 0/50 = 0% (base 1% = 0.5/50) |

GPU-hours: 14.052 spent, 1.948 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.39, 10 steps 1.98, 50 steps 9.03) GPU-h; eval.py per task (5 seeds 0.15, 20 seeds 0.19, 100 seeds 0.45) GPU-h
Loaded on your serving endpoint: grpo_rev2
Submitted: base + grpo_rev2 (sha c6603b5eed69) (turn 84, token 9630ec; confirmed in turn 85)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| grpo_rev | base | 24 | spec_rev.json | trained |
| grpo_rest | base | 24 | spec_rest.json | trained |
| grpo_nut | base | 12 | spec_nut.json | trained |
| grpo_rev2 | grpo_rev | 20 | spec_rev2.json | trained |

- train job 39 (grpo_rev): note set: part of the training prompt only; every eval, including the final score, uses tasks/revstack/eval_prompt.txt verbatim
- train job 40 (grpo_rest): note set: part of the training prompt only; every eval, including the final score, uses tasks/restack/eval_prompt.txt verbatim
- train job 41 (grpo_nut): note set: part of the training prompt only; every eval, including the final score, uses tasks/nut/eval_prompt.txt verbatim
- train job 57 (grpo_rev2): note set: part of the training prompt only; every eval, including the final score, uses tasks/revstack/eval_prompt.txt verbatim

## Self-reward (rollout.py --reward: your reward over the rollout facts; not a success count)

- none yet

## Failure digest (facts: a train's lowest-reward episodes per task; full records in failures.jsonl)

- revstack: 16 failures in adapters/grpo_rev/failures.jsonl; stages none:15 grasp the green_cube:1
- restack: 16 failures in adapters/grpo_rest/failures.jsonl; stages none:14 unstack the green off the red:2
- nut: 16 failures in adapters/grpo_nut/failures.jsonl; stages none:16
- revstack: 16 failures in adapters/grpo_rev2/failures.jsonl; stages none:14 grasp the green_cube:1 reach the green_cube:1

## History (latest 30)

- preset probe2_re on restack: 4 seeds -> presets/probe2_re.json
- preset probe2_nut on nut: 4 seeds -> presets/probe2_nut.json
- preset probe2_rev on revstack: 4 seeds -> presets/probe2_rev.json
- preset cam on restack: 2 seeds -> presets/cam.json
- preset rv1 on revstack: 4 seeds -> presets/rv1.json
- preset re1 on restack: 4 seeds -> presets/re1.json
- preset nv1 on nut: 4 seeds -> presets/nv1.json
- preset cam2 on restack: 1 seeds -> presets/cam2.json
- preset dr1 on revstack: 3 seeds -> presets/dr1.json
- cancel job 34
- train sftrev1 failed: train: objective '…/workspace/sft': this site trains with objective 'grpo' only
- preset measr1 cancelled: preset measr1 cancelled; no preset kept (a preset needs every seed's state); charged 0.000 GPU-h
- cancel job 29
- preset meas1 cancelled: preset meas1 cancelled; no preset kept (a preset needs every seed's state); charged 0.000 GPU-h
- train grpo_rev (init base, steps 24): trained
- train grpo_rest (init base, steps 24): trained
- train grpo_nut (init base, steps 12): trained
- eval grpo_rev+grpo_rest on restack: 0/20
- eval grpo_rev on revstack: 1/20
- eval grpo_rest on restack: 0/20
- eval grpo_nut on nut: 0/20
- eval grpo_rev on revstack: 0/50
- eval grpo_rev on restack: 0/20
- eval grpo_rev on nut: 0/20
- train grpo_rev2 (init grpo_rev, steps 20): trained
- eval grpo_rev2 on revstack: 1/50
- eval grpo_rev+grpo_rev2 on revstack: 0/50
- load grpo_rev2
- finish: submitted grpo_rev2 (token 9630ec, job 64)
- finish: confirmed grpo_rev2 (token 9630ec)
