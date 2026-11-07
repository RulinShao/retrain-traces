import math
def _p(v):
    return [float(v[0]), float(v[1]), float(v[2])]
def reward_fn(state):
    o = state["objects"]
    tongs = [n for n in o if "tong" in n.lower()]
    tray  = [n for n in o if "tray" in n.lower()]
    if not tongs or not tray:
        return 0
    a = _p(o[tongs[0]]["pos"]); b = _p(o[tray[0]]["pos"])
    d = math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)
    return int(d < 1.5)
