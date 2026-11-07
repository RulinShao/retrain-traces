import numpy as np
def reward_fn(state):
    objs=state.get("objects",{}) or {}
    pot=None
    for n,o in objs.items():
        if isinstance(o,dict) and any(w in n.lower() for w in ("pot","kettle","saucepan","pan","water","tub","container")):
            pot=n; break
    if pot is None: return 0.0
    o=objs[pot]
    pos=np.array(o.get("pos",[0,0,0]),float)
    on=any("stove" in str(c).lower() for c in (o.get("contacts") or []))
    if not on:
        for fn,f in (state.get("fixtures",{}) or {}).items():
            if isinstance(f,dict) and ("stove" in fn.lower() or "range" in fn.lower() or "burner" in fn.lower()):
                for rn,r in (f.get("regions",{}) or {}).items():
                    p0=(r or {}).get("p0")
                    try:
                        if p0 is not None and float(np.linalg.norm(pos-np.array(p0,float)))<0.5: on=True
                    except Exception: pass
    return 1.0 if on else 0.0
