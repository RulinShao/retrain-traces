def _g(r, k, d=None):
    try:
        if isinstance(r, dict):
            return r.get(k, d)
        return getattr(r, k, d)
    except Exception:
        return d

def reward(r):
    # dense, monotone over the simulator's ordered checklist; 0 at start state / crash;
    # anchored on the final (success) stage.
    rc = _g(r, "sandbox_rc", 0)
    if rc not in (0, None):
        return 0.0
    st = _g(r, "stages", None) or {}
    vals = list(st.values())
    if not vals:
        return 1.0 if _g(r, "task_completed", False) else 0.0
    n = len(vals)
    wsum = 0.0
    wmax = 0.0
    for i in range(n):
        w = float((i + 1) ** 2)
        wmax += w
        if vals[i]:
            wsum += w
    base = wsum / wmax if wmax > 0 else 0.0
    return 0.5 * (1.0 if vals[-1] else 0.0) + 0.5 * base
