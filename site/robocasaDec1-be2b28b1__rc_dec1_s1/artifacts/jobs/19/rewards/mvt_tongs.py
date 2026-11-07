import math
def _d(a,b): return math.sqrt(sum((x-y)**2 for x,y in zip(a,b)))
def reward_fn(state):
    o = state["objects"]
    # the tong: an object whose name contains tong, else the most-moved object that started in a drawer
    tongs = [n for n in o if "tong" in n.lower()]
    moved_any = False
    if tongs:
        for n in tongs:
            if _d(o[n]["pos"], o[n]["init_pos"]) > 0.05: return 1
        return 0
    # fallback: any object that moved > 0.12 (picked out of a drawer)
    best = 0.0
    for n in o:
        d = _d(o[n]["pos"], o[n]["init_pos"])
        if d > best: best = d
    return int(best > 0.12)
