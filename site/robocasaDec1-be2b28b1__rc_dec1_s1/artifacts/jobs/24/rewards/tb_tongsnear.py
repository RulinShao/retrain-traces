import math
def _d(a,b): return math.sqrt(sum((x-y)**2 for x,y in zip(a,b)))
def reward_fn(state):
    o = state["objects"]
    tongs = [n for n in o if "tong" in n.lower()]
    tray  = [n for n in o if "tray" in n.lower()]
    if not tongs or not tray: return 0
    return int(_d(o[tongs[0]]["pos"], o[tray[0]]["pos"]) < 0.5)
