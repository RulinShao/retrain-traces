import math
def _d(a,b): return math.sqrt(sum((x-y)**2 for x,y in zip(a,b)))
def reward_fn(state):
    o = state["objects"]
    pots = [n for n in o if "pot" in n.lower() or "saucepan" in n.lower() or "pan" in n.lower()]
    cands = pots if pots else list(o)
    for n in cands:
        if _d(o[n]["pos"], o[n]["init_pos"]) > 0.05: return 1
    return 0
