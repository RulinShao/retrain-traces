import math
def _region_center(regions):
    pts=[]
    for r in (regions or []):
        for k in ("p0","px","py","pz"):
            v=r.get(k)
            if v and len(v)>=3: pts.append(v[:3])
    if not pts: return None
    n=len(pts)
    return [sum(p[i] for p in pts)/n for i in range(3)]
def reward_fn(state):
    st = state["fixtures"].get("stove") or {}
    c = _region_center(st.get("regions"))
    if c is None: return 0
    o = state["objects"]
    pots = [n for n in o if ("pot" in n.lower() or "saucepan" in n.lower())]
    if not pots: return 0
    p = o[pots[0]]["pos"]
    d = math.sqrt(sum((p[i]-c[i])**2 for i in range(3)))
    return int(d < 0.5)
