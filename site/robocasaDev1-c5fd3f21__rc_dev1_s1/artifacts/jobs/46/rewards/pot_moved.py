import numpy as np
def reward_fn(state):
    objs=state.get("objects",{}) or {}
    pot=None
    for n,o in objs.items():
        if isinstance(o,dict) and any(w in n.lower() for w in ("pot","kettle","saucepan","pan","water","tub","container")):
            pot=n; break
    if pot is None: return 0.0
    o=objs[pot]
    try:
        d=float(np.linalg.norm(np.array(o.get("pos",[0,0,0]),float)-np.array(o.get("init_pos",[0,0,0]),float)))
    except Exception:
        return 0.0
    return 1.0 if d>0.05 else 0.0
