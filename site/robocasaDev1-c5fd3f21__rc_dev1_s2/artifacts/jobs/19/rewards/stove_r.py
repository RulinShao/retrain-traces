import numpy as np

def _f(x, d=0.0):
    try:
        return float(x)
    except Exception:
        return d

def reward_fn(state):
    if state.get("task_completed"):
        return 1.0
    objs = state.get("objects") or {}
    fix = state.get("fixtures") or {}
    pot = None
    for n, o in objs.items():
        if "pot" in n.lower() and "soup" not in n.lower():
            pot = (n, o)
            break
    if pot is None:
        return 0.0
    pp = np.asarray(pot[1].get("pos") or [0, 0, 0], dtype=float)
    on_fix = None
    for fn, f in fix.items():
        st = f.get("state") or {}
        if isinstance(st, dict) and any("pot" in str(k).lower() for k in st):
            on_fix = fn
            break
    if on_fix is None:
        for fn in fix:
            if "stove" in fn.lower() or "range" in fn.lower():
                on_fix = fn
                break
    st = fix.get(on_fix) or {} if on_fix else {}
    stt = st.get("state") or {}
    if not isinstance(stt, dict):
        stt = {}
    ist = st.get("init_state") or {}
    on = 0.0
    changed = False
    vals = {}
    for k, v in stt.items():
        kl = str(k).lower()
        if isinstance(v, (int, float)) and 0.0 <= _f(v) <= 1.0 and ("burner" in kl or "on" in kl or "flame" in kl or "lit" in kl or "stove" in kl):
            initv = _f(ist.get(k), 0.0) if isinstance(ist, dict) else 0.0
            if _f(v) >= 0.5:
                on = max(on, 1.0)
            if abs(_f(v) - initv) > 1e-4:
                changed = True
            vals[str(k)] = _f(v)
    def h(q):
        q = np.asarray(q, dtype=float)
        return float(np.hypot(pp[0] - q[0], pp[1] - q[1]))
    r = 0.0
    cfl = [str(c).lower() for c in (pot[1].get("contacts") or [])]
    near_stove = False
    if on_fix:
        fp = np.asarray(st.get("pos") or [99, 99, 99], dtype=float)
        near_stove = h(fp) < 0.6
        if near_stove:
            r = max(r, 0.3)
        for c in cfl:
            if on_fix in c or "stove" in c or "range" in c:
                r = max(r, 0.45)
                near_stove = True
    best_b = 0.0
    if near_stove:
        for fn, f in fix.items():
            regs = f.get("regions") or {}
            if isinstance(regs, dict):
                for rk, rv in regs.items():
                    if "burner" in str(rk).lower():
                        try:
                            b = np.array([_f(rv["px"][0]), _f(rv["py"][0]), _f(rv["pz"][0])])
                            best_b = max(best_b, 1.0 - min(1.0, h(b) / 0.18))
                        except Exception:
                            pass
    r = max(r, 0.5 + 0.25 * best_b if near_stove else 0.0)
    r = max(r, 0.6 * on)
    if on and near_stove:
        r = max(r, 0.85)
    return float(min(1.0, r))
