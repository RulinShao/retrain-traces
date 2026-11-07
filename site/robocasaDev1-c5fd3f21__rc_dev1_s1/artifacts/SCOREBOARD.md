# SCOREBOARD

playbook: none
agent: local
mode: dev
dev seeds: from 800071
policy: Qwen3.8-27B
eval_backend: tinker, decode=tinker(no_presence_penalty) (RoboCasa365 pool: every eval samples on Tinker, base or Tinker-trained adapter; dev / practice seeds only, hidden seeds refused); final=DEV (dev seeds 800021-800070, n=50, sampled on Tinker; never a Table 2 number: hidden finals need the local 27B)

Dev-seed success count per task x adapter stack (k/n = rate): the eval with the most seeds (equal n: the newest); smaller evals are in History and the job records. Adapter cells also give the base column's rate at the same n; `untested` = no eval of that stack on that task yet.

| task | base | q_boil | q_mw | q_draw | b_boil1 | t_boil_probe | v_boil5 | x_boil | probe_state | hasobjs | potmoved | knobdiag | abb_probe1 | boil_probe2 | pack_probe1 | pack_probe2 | gp_probe1 | tb_probe1 | pack_full2 |
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

GPU-hours: 10.951 spent, 5.049 remaining of 16.0 (0 job(s) running)
Expected cost per call (the estimate checked against what remains): train.py (1 step 0.21, 10 steps 1.34, 50 steps 6.37) GPU-h; eval.py per task (5 seeds 0.09, 20 seeds 0.12, 100 seeds 0.27) GPU-h
Loaded on your serving endpoint: base
Submitted: base + knobdiag (sha 332b6d3d64d7) + pack_probe2 (sha ef23259c79c3) + potmoved (sha 2c8dae6fc462) (turn 176, token 08525a; confirmed in turn 177)

## Adapters

| name | init | steps | spec | state |
|---|---|---|---|---|
| q_boil | base | 1 | specs/q_boil.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| q_mw | base | 1 | specs/q_mw.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| q_draw | base | 1 | specs/q_draw.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| b_boil1 | base | 1 | specs/b_boil1.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| t_boil_probe | base | 1 | specs/tr_t_boil_probe.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| v_boil5 | base | 5 | specs/tr_v_boil5.json | trained 5 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| x_boil | base | 5 | specs/tr_x_boil.json | trained 5 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| probe_state | base | 1 | specs/tr_probe_state.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| hasobjs | base | 1 | specs/tr_hasobjs.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| potmoved | base | 1 | specs/tr_potmoved.json | trained |
| knobdiag | base | 1 | specs/tr_knobdiag.json | trained |
| abb_probe1 | base | 1 | specs/tr_abb_probe1.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| boil_probe2 | base | 1 | specs/tr_boil_probe2.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| pack_probe1 | base | 1 | specs/tr_pack_probe1.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| pack_probe2 | base | 1 | specs/tr_pack_probe2.json | trained |
| gp_probe1 | base | 1 | specs/tr_gp_probe1.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| tb_probe1 | base | 1 | specs/tr_tb_probe1.json | trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |
| pack_full2 | base | 15 | specs/tr_pack_full2.json | trained 15 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B) |

- train job 8 (q_boil): goal set: part of the training prompt only; every eval, including the final score, uses tasks/BoilPot/eval_prompt.txt verbatim
- train job 9 (q_mw): goal set: part of the training prompt only; every eval, including the final score, uses tasks/SteamInMicrowave/eval_prompt.txt verbatim
- train job 10 (q_draw): goal set: part of the training prompt only; every eval, including the final score, uses tasks/TongBuffetSetup/eval_prompt.txt verbatim
- train job 16 (b_boil1): note set: part of the training prompt only; every eval, including the final score, uses tasks/BoilPot/eval_prompt.txt verbatim
- train job 18 (t_boil_probe): note set: part of the training prompt only; every eval, including the final score, uses tasks/BoilPot/eval_prompt.txt verbatim
- train job 27 (v_boil5): note set: part of the training prompt only; every eval, including the final score, uses tasks/BoilPot/eval_prompt.txt verbatim
- train job 35 (x_boil): note set: part of the training prompt only; every eval, including the final score, uses tasks/BoilPot/eval_prompt.txt verbatim
- train job 46 (potmoved): note set: part of the training prompt only; every eval, including the final score, uses tasks/BoilPot/eval_prompt.txt verbatim
- train job 49 (full_boil): note set: part of the training prompt only; every eval, including the final score, uses tasks/BoilPot/eval_prompt.txt verbatim
- train job 52 (knobdiag): note set: part of the training prompt only; every eval, including the final score, uses tasks/BoilPot/eval_prompt.txt verbatim
- train job 54 (s1_boil): note set: part of the training prompt only; every eval, including the final score, uses tasks/BoilPot/eval_prompt.txt verbatim
- train job 57 (abb_sub): note set: part of the training prompt only; every eval, including the final score, uses tasks/ArrangeBreadBowl/eval_prompt.txt verbatim
- train job 61 (abb_probe1): note set: part of the training prompt only; every eval, including the final score, uses tasks/ArrangeBreadBowl/eval_prompt.txt verbatim
- train job 65 (boil_probe2): note set: part of the training prompt only; every eval, including the final score, uses tasks/BoilPot/eval_prompt.txt verbatim
- train job 67 (pack_probe1): note set: part of the training prompt only; every eval, including the final score, uses tasks/PackIdenticalLunches/eval_prompt.txt verbatim
- train job 69 (pack_probe2): note set: part of the training prompt only; every eval, including the final score, uses tasks/PackIdenticalLunches/eval_prompt.txt verbatim
- train job 71 (gp_probe1): note set: part of the training prompt only; every eval, including the final score, uses tasks/GarnishPancake/eval_prompt.txt verbatim
- train job 75 (tb_probe1): note set: part of the training prompt only; every eval, including the final score, uses tasks/TongBuffetSetup/eval_prompt.txt verbatim
- train job 76 (tb_probe1): note set: part of the training prompt only; every eval, including the final score, uses tasks/TongBuffetSetup/eval_prompt.txt verbatim
- train job 78 (pack_full1): note set: part of the training prompt only; every eval, including the final score, uses tasks/PackIdenticalLunches/eval_prompt.txt verbatim
- train job 80 (pack_full2): note set: part of the training prompt only; every eval, including the final score, uses tasks/PackIdenticalLunches/eval_prompt.txt verbatim

## Self-reward (rollout.py --reward: your reward over the rollout facts; not a success count)

- job 12: eval base on BoilPot: 0/20 -> rollouts/12.jsonl; self-reward mean 0.0 over 20 seeds (rewards/docstring.py)
- job 20: rollout base on BoilPot: 3 seeds -> rollouts/20.jsonl; self-reward mean None over 0 seeds (rewards/BoilPot.py)
- job 22: rollout base on BoilPot: 4 seeds -> rollouts/22.jsonl; self-reward mean 0.0 over 4 seeds (rewards/BoilPot.py)
- job 25: rollout base on BoilPot: 3 seeds -> rollouts/25.jsonl; self-reward mean None over 0 seeds (specs/diag_boil.py)
- job 33: rollout base on BoilPot: 2 seeds -> rollouts/33.jsonl; self-reward mean None over 0 seeds (specs/dumpresult.py)
- job 40: rollout base on BoilPot: 3 seeds -> rollouts/40.jsonl; self-reward mean 0.1 over 3 seeds (specs/probe.py)
- job 73: eval base on PackIdenticalLunches: 0/5 -> rollouts/73.jsonl; self-reward mean 1.0 over 5 seeds (rewards/dump.py)

## History (latest 30)

- rollout base on BoilPot: 3 seeds -> rollouts/20.jsonl; self-reward mean None over 0 seeds (rewards/BoilPot.py)
- rollout base on BoilPot: 4 seeds -> rollouts/22.jsonl; self-reward mean 0.0 over 4 seeds (rewards/BoilPot.py)
- rollout base on BoilPot: 3 seeds -> rollouts/25.jsonl; self-reward mean None over 0 seeds (specs/diag_boil.py)
- train v_boil5 (init base, steps 5): trained 5 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- rollout base on BoilPot: 2 seeds -> rollouts/33.jsonl; self-reward mean None over 0 seeds (specs/dumpresult.py)
- train x_boil (init base, steps 5): trained 5 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- rollout base on BoilPot: 3 seeds -> rollouts/40.jsonl; self-reward mean 0.1 over 3 seeds (specs/probe.py)
- train probe_state (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train hasobjs (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train potmoved (init base, steps 1): trained
- cancel job 49
- train full_boil cancelled: train cancelled; its job ended (JobFailed)
- train knobdiag (init base, steps 1): trained
- cancel job 54
- train s1_boil cancelled: train cancelled; its job ended (JobFailed)
- cancel job 57
- train abb_sub cancelled: train cancelled; its job ended (JobFailed)
- train abb_probe1 (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train boil_probe2 (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train pack_probe1 (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train pack_probe2 (init base, steps 1): trained
- train gp_probe1 (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- eval base on PackIdenticalLunches: 0/5 --reward -> rollouts/73.jsonl (scoreboard cell keeps 0/20: more seeds)
- train tb_probe1 failed: train: note: a non-empty string of at most 4000 characters
- train tb_probe1 (init base, steps 1): trained 1 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- train pack_full1 failed: train: note: a non-empty string of at most 4000 characters
- train pack_full2 (init base, steps 15): trained 15 steps; weights unchanged (all-zero update: 0/496 nonzero lora_B)
- eval base failed: eval: refused: Tinker budget exhausted (ledger 15010.02 / cap 15000.00 USD); tinker eval ArrangeBreadBowl_base (2 seeds) needs $0.09 more (RMIN_TINKER_BUDGET_USD, ledger …/tinker/LEDGER.jsonl)
- finish: submitted knobdiag+pack_probe2+potmoved (token 08525a, job 84)
- finish: confirmed knobdiag+pack_probe2+potmoved (token 08525a)
