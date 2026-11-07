import math
def _dist(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))
def reward_fn(state):
    o = state["objects"]
    for name in o:
        p = o[name]
        if _dist(p["pos"], p["init_pos"]) > 0.04:
            return 1
    return 0
