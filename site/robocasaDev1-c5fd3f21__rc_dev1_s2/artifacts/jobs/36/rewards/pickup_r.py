import math
def _objpos(o):
    try: return [float(x) for x in o["pos"][:3]]
    except Exception: return None
def _initpos(o):
    try: return [float(x) for x in o["init_pos"][:3]]
    except Exception: return None
def reward_fn(state):
    for n, o in (state.get("objects") or {}).items():
        p = _objpos(o); q = _initpos(o)
        if p is None or q is None: continue
        d = math.sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2 + (p[2]-q[2])**2)
        if d > 0.08:
            return 1
    return 0

def reward(result):
    return reward_fn(result)
