def _g(r, k, d=0.0):
    if isinstance(r, dict):
        return r.get(k, d)
    return getattr(r, k, d)

def reward(r):
    try:
        tc = float(_g(r, "task_completed", 0))
    except Exception:
        tc = 0.0
    if tc >= 1.0:
        return 1.0
    try:
        s = float(_g(r, "reward", 0))
    except Exception:
        s = 0.0
    return min(s, 1.0) * 0.25
