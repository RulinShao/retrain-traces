import numpy as np
def _stove_pts(state):
    pts=[]
    for fn,f in (state.get("fixtures",{}) or {}).items():
        if not isinstance(f,dict): continue
        if any(w in fn.lower() for w in ("stove","range","burner","cooktop")):
            for rn,r in (f.get("regions",{}) or {}).items():
                p0=(r or {}).get("p0")
                if p0 is not None:
                    try: pts.append(np.array(p0,float))
                    except Exception: pass
    return pts
def reward_fn(state):
    objs=state.get("objects",{}) or {}
    pot=None
    for n,o in objs.items():
        if isinstance(o,dict) and any(w in n.lower() for w in ("pot","kettle","saucepan","pan","water","tub","container")):
            pot=n; break
    if pot is None: return 0.0
    o=objs[pot]
    pos=np.array(o.get("pos",[0,0,0]),float)
    ipos=np.array(o.get("init_pos",[0,0,0]),float)
    if float(np.linalg.norm(pos-ipos))<0.08: return 0.0  # must have been moved
    sp=_stove_pts(state)
    if not sp:
        on=any("stove" in str(c).lower() for c in (o.get("contacts") or []))
        return 1.0 if on else 0.0
    for p in sp:
        if float(np.linalg.norm(pos-p))<0.55: return 1.0
    return 0.0
