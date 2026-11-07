import numpy as np
def reward_fn(state):
    objs=state.get("objects",{}) or {}
    breads=[o for n,o in objs.items() if isinstance(o,dict) and ("bread" in n.lower() or "loaf" in n.lower() or "baguette" in n.lower() or "slice" in n.lower())]
    bowls=[o for n,o in objs.items() if isinstance(o,dict) and "bowl" in n.lower()]
    if not breads or not bowls: return 0.0
    bc=np.array(bowls[0].get("pos",[0,0,0]),float)
    for br in breads:
        try:
            if float(np.linalg.norm(np.array(br.get("pos",[0,0,0]),float)-bc))<0.45: return 1.0
        except Exception: pass
    return 0.0
