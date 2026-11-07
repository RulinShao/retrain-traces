import numpy as np
def _bn(st):
    if not st: return False
    for k,v in st.items():
        kl=k.lower()
        if any(t in kl for t in ("burner","knob","dial","on","press","button","toggle","lever","switch","stove")):
            if isinstance(v,(int,float)) and float(v)>0.5: return True
    return False
def reward_fn(state):
    objs=state.get("objects",{}) or {}
    pot=None
    for n,o in objs.items():
        if isinstance(o,dict) and any(w in n.lower() for w in ("pot","kettle","saucepan","pan","water","tub","container")):
            pot=n; break
    if pot is None: return 0.0
    o=objs[pot]
    onstove=any("stove" in str(c).lower() for c in (o.get("contacts") or []))
    if not onstove:
        for fn,f in (state.get("fixtures",{}) or {}).items():
            if "stove" in fn.lower():
                for rn,r in (f.get("regions",{}) or {}).items():
                    p0=(r or {}).get("p0")
                    try:
                        if p0 and float(np.linalg.norm(np.array(o["pos"],float)-np.array(p0,float)))<0.45: onstove=True
                    except Exception: pass
    burner=False
    for fn,f in (state.get("fixtures",{}) or {}).items():
        if "stove" in fn.lower() or "burner" in fn.lower() or "range" in fn.lower():
            if _bn(f.get("state",{}) or {}): burner=True
    if burner: return 1.0
    if onstove: return 0.5
    return 0.0
