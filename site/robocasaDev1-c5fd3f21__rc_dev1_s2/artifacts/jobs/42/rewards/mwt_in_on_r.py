import math
def _is_mw(name, ftype):
    return ("microwave" in str(name).lower()) or ("microwave" in str(ftype).lower())
def reward_fn(state):
    fixes = state.get("fixtures") or {}
    objs = state.get("objects") or {}
    mw = None
    for n, f in fixes.items():
        if _is_mw(n, f.get("type")):
            mw = f; break
    if not mw:
        return 0
    on = False
    st = mw.get("state") or {}
    if isinstance(st, dict):
        for k, v in st.items():
            if isinstance(v, (int, float)) and float(v) >= 0.5 and any(w in str(k).lower() for w in ("start", "on", "press", "running")):
                on = True
    if not on:
        return 0
    for n, o in objs.items():
        if "microwave" in str(n).lower():
            continue
        c = [str(x).lower() for x in (o.get("contacts") or [])]
        if any("microwave" in x for x in c):
            return 1
    for n, o in objs.items():
        if "microwave" in str(n).lower():
            continue
        try:
            pos = [float(x) for x in o["pos"][:3]]
        except Exception:
            continue
        for r in (mw.get("regions") or []):
            try:
                pts = [r["p0"], r["px"], r["py"], r["pz"]]
                ctr = [sum(p[i] for p in pts) / 4.0 for i in range(3)]
            except Exception:
                continue
            d = math.sqrt((pos[0]-ctr[0])**2 + (pos[1]-ctr[1])**2 + (pos[2]-ctr[2])**2)
            if d < 0.3:
                return 1
    return 0

def reward(result):
    return reward_fn(result)
