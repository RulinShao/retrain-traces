import numpy as np
def reward_fn(state):
    objs=state.get("objects",{}) or {}
    names=list(objs.keys())
    pot=None
    for n in names:
        o=objs[n]
        if isinstance(o,dict) and any(w in n.lower() for w in ("pot","kettle","saucepan","pan","water","tub","container")):
            pot=n; break
    if pot is None:
        return float(0.05 + min(len(names),30)*0.01)
    o=objs[pot]
    try: moved=float(np.linalg.norm(np.array(o.get("pos",[0,0,0]),float)-np.array(o.get("init_pos",[0,0,0]),float)))
    except Exception: moved=9.0
    gr=o.get("gripper_dist")
    val=0.30 + min(len(pot),20)*0.01
    if moved>0.04: val+=0.30
    if gr is not None and float(gr)<0.10: val+=0.10
    return float(min(val,0.99))
def reward(state): return reward_fn(state)
