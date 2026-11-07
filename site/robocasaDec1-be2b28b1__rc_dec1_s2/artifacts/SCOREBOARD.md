# SCOREBOARD

playbook: 6df138df-8645d430
agent: local
mode: dev
dev seeds: from 800071
policy: Qwen3.8-27B
eval_backend: tinker, decode=tinker(no_presence_penalty) (RoboCasa365 pool: every eval samples on Tinker, base or Tinker-trained adapter; dev / practice seeds only, hidden seeds refused); final=DEV (dev seeds 800021-800070, n=50, sampled on Tinker; never a Table 2 number: hidden finals need the local 27B)

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | gp_v1 | diag_grip2 | base_grasp | boil_base_moved | boil_full_probe | boil_stove_probe | boil_move40_probe | tb_drawer_probe | mw_on_probe | boil_note_probe | boilA_fixh | boilB_perceive | arr_bowl_probe | arr_breads_probe | arr_dining_strict | clear_mug_sink_probe | boilC_robust | wash_col_sink_probe |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| TongBuffetSetup | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| PlaceVeggiesInDrawer | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| OrganizeMetallicUtensils | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| BoilPot | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| SimmeringSauce | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| HeatMultipleWater | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| BlendVegetableSauce | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| BlendMarinade | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| BlendIngredients | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| SteamInMicrowave | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| MicrowaveDefrostMeat | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| MicrowaveThawing | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| WashFruitColander | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| GetToastedBread | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| ClearReceptaclesForCleaning | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| HeatKebabSandwich | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| ToasterOvenBroilFish | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| ArrangeBreadBowl | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| MakeIceLemonade | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| GarnishPancake | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| CerealAndBowl | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| PackIdenticalLunches | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| StirVegetables | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |
| GatherTableware | 0/20 = 0% | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested | untested |

GPU-hours: 8.337 spent, 7.663 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.21, 10 steps 1.34, 50 steps 6.37) GPU-h; eval.py per task (5 seeds 0.09, 20 seeds 0.12, 100 seeds 0.27) GPU-h
Loaded on your serving endpoint: base
Submitted: base (turn 185, token 52d5f8; confirmed in turn 187)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| gp_v1 | base | 3 | specs/gp_v1.json | trained 3 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| diag_grip2 | base | 2 | specs/diag_grip2.json | trained 2 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| base_grasp | base | 2 | specs/base_grasp.json | trained 2 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| boil_base_moved | base | 2 | specs/boil_base_moved.json | trained |
| boil_full_probe | base | 1 | specs/boil_full_probe.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| boil_stove_probe | base | 1 | specs/boil_stove_probe.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| boil_move40_probe | base | 1 | specs/boil_move40_probe.json | trained |
| tb_drawer_probe | base | 1 | specs/tb_drawer_probe.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| mw_on_probe | base | 1 | specs/mw_on_probe.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| boil_note_probe | base | 1 | specs/boil_note_probe.json | trained |
| boilA_fixh | base | 1 | specs/boilA.json | trained |
| boilB_perceive | base | 1 | specs/boilB.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| arr_bowl_probe | base | 1 | specs/arr_bowl_probe.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| arr_breads_probe | base | 1 | specs/arr_breads_probe.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| arr_dining_strict | base | 1 | specs/arr_dining_strict.json | trained |
| clear_mug_sink_probe | base | 1 | specs/clear_mug_probe.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| boilC_robust | base | 10 | specs/boilC.json | trained 10 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| wash_col_sink_probe | base | 1 | specs/wash_col_probe.json | trained |

- train job 6 (gp_v1): note set: part of the training prompt only; every eval, including the final score, uses tasks/GarnishPancake/eval_prompt.txt verbatim
- train job 8 (diag_grip): note set: part of the training prompt only; every eval, including the final score, uses tasks/GarnishPancake/eval_prompt.txt verbatim
- train job 10 (diag_grip2): note set: part of the training prompt only; every eval, including the final score, uses tasks/GarnishPancake/eval_prompt.txt verbatim
- train job 20 (boil_stove_probe): goal set: part of the training prompt only; every eval, including the final score, uses tasks/BoilPot/eval_prompt.txt verbatim
- train job 26 (tb_drawer_probe): goal set: part of the training prompt only; every eval, including the final score, uses tasks/TongBuffetSetup/eval_prompt.txt verbatim
- train job 27 (mw_on_probe): goal set: part of the training prompt only; every eval, including the final score, uses tasks/MicrowaveThawing/eval_prompt.txt verbatim
- train job 29 (boil_note_probe): note and goal set: part of the training prompt only; every eval, including the final score, uses tasks/BoilPot/eval_prompt.txt verbatim
- train job 33 (boilA_fixh): note and goal set: part of the training prompt only; every eval, including the final score, uses tasks/BoilPot/eval_prompt.txt verbatim
- train job 34 (boilB_perceive): note and goal set: part of the training prompt only; every eval, including the final score, uses tasks/BoilPot/eval_prompt.txt verbatim
- train job 36 (boilC_robust): note and goal set: part of the training prompt only; every eval, including the final score, uses tasks/BoilPot/eval_prompt.txt verbatim
- train job 37 (arr_bowl_probe): goal set: part of the training prompt only; every eval, including the final score, uses tasks/ArrangeBreadBowl/eval_prompt.txt verbatim
- train job 39 (arr_breads_probe): goal set: part of the training prompt only; every eval, including the final score, uses tasks/ArrangeBreadBowl/eval_prompt.txt verbatim
- train job 41 (arr_dining_strict): goal set: part of the training prompt only; every eval, including the final score, uses tasks/ArrangeBreadBowl/eval_prompt.txt verbatim
- train job 42 (clear_mug_sink_probe): goal set: part of the training prompt only; every eval, including the final score, uses tasks/ClearReceptaclesForCleaning/eval_prompt.txt verbatim
- train job 43 (wash_col_sink_probe): goal set: part of the training prompt only; every eval, including the final score, uses tasks/WashFruitColander/eval_prompt.txt verbatim
- train job 47 (wash_fruit_probe): goal set: part of the training prompt only; every eval, including the final score, uses tasks/WashFruitColander/eval_prompt.txt verbatim
- train job 48 (wash_faucet_probe): goal set: part of the training prompt only; every eval, including the final score, uses tasks/WashFruitColander/eval_prompt.txt verbatim

## Self-reward (rollout.py --reward: your reward over the rollout facts; not a success count)

- none yet

## History (latest 30)

- rollout base on BlendIngredients: 5 seeds -> rollouts/3.jsonl
- train gp_v1 (init base, steps 3): trained 3 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- cancel job 8
- train diag_grip cancelled: train cancelled; its job ended (JobFailed)
- train diag_grip2 (init base, steps 2): trained 2 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train base_grasp (init base, steps 2): trained 2 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train boil_base_moved (init base, steps 2): trained
- train boil_full_probe (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train boil_stove_probe (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train boil_move40_probe (init base, steps 1): trained
- train tb_drawer_probe (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train mw_on_probe (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train boil_note_probe (init base, steps 1): trained
- rollout base on BoilPot: 6 seeds -> rollouts/31.jsonl
- train boilA_fixh (init base, steps 1): trained
- train boilB_perceive (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train arr_bowl_probe (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train arr_breads_probe (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train arr_dining_strict (init base, steps 1): trained
- train clear_mug_sink_probe (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train boilC_robust (init base, steps 10): trained 10 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train wash_col_sink_probe (init base, steps 1): trained
- finish: submitted base (token 941bf5, job 46)
- finish: submission 941bf5 cancelled by job 47 (train)
- cancel job 47
- cancel job 48
- finish: submitted base (token 52d5f8, job 52)
- train wash_fruit_probe cancelled: train cancelled; its job ended (JobFailed)
- train wash_faucet_probe cancelled: train cancelled; its job ended (JobFailed)
- finish: confirmed base (token 52d5f8)
