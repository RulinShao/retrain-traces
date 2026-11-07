import math
def _d(a,b): return math.sqrt(sum((x-y)**2 for x,y in zip(a,b)))
def reward_fn(state):
    o = state["objects"]
    st = [n for n in o if "strawb" in n.lower() or "berry" in n.lower()]
    if not st: return 0
    return int(_d(o[st[0]]["pos"], o[st[0]]["init_pos"]) > 0.05)
