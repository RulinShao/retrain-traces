import math
def _p(v):
    return [float(v[0]), float(v[1]), float(v[2])]
def reward_fn(state):
    o = state["objects"]
    st  = [n for n in o if "strawb" in n.lower() or "berry" in n.lower()]
    pan = [n for n in o if "pancake" in n.lower() or "pan" in n.lower()]
    if not st or not pan:
        return 0
    a = _p(o[st[0]]["pos"]); b = _p(o[pan[0]]["pos"])
    d = math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)
    return int(d < 0.3)
