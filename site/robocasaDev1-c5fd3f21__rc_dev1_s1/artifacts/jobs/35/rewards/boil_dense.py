import numpy as np
def _pick(state, words):
    objs = state.get("objects", {}) or {}
    cands = [n for n in objs if isinstance(objs[n], dict) and any(w in n.lower() for w in words)]
    if not cands: return None
    def moved(n):
        o=objs[n]; p=o.get("pos"); ip=o.get("init_pos")
        try: return float(np.linalg.norm(np.array(p,dtype=float)-np.array(ip,dtype=float)))
        except Exception: return -1.0
    cands.sort(key=lambda n: moved(n), reverse=True)
    return cands[0]
def _d(a,b):
    try: return float(np.linalg.norm(np.array(a,dtype=float)-np.array(b,dtype=float)))
    except Exception: return 9.0
def reward_fn(state):
    try:
        pot=_pick(state,["pot","kettle","saucepan","pan","pot with water","water pot"])
        if pot is None:
            return 0.0
        o=state["objects"][pot]
        s=0.0
        moved = _d(o.get("pos",[0,0,0]), o.get("init_pos",[0,0,0])) > 0.04
        gd = o.get("gripper_dist")
        gp = state.get("gripper",{}).get("opening")
        grasped = (gd is not None and float(gd) < 0.10) and (gp is not None and float(gp) < 0.12)
        onstove = any(("stove" in str(c).lower()) for c in (o.get("contacts") or []))
        stove=None
        for fn,f in (state.get("fixtures",{}) or {}).items():
            if isinstance(f,dict) and "stove" in fn.lower(): stove=f; break
        if not onstove and stove is not None:
            for rn,r in (stove.get("regions",{}) or {}).items():
                p0=(r or {}).get("p0")
                if p0 and _d(o.get("pos",[0,0,0]), p0) < 0.4: onstove=True
        burner=False
        if stove is not None:
            st=stove.get("state",{}) or {}
            burner = any(isinstance(v,(int,float)) and float(v)>0.5 for v in st.values())
        s = 0.30*(1.0 if (moved or grasped) else 0.0) + 0.50*(1.0 if onstove else 0.0) + 0.20*(1.0 if burner else 0.0)
        return float(min(1.0, max(0.0, s)))
    except Exception:
        return 0.0
def reward(state):
    return reward_fn(state)
