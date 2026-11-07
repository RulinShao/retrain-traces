def _g(o, k):
    try:
        if isinstance(o, dict): return o[k]
        return getattr(o, k)
    except Exception:
        return None

def reward(r):
    tc = _g(r, 'task_completed')
    tc = 1.0 if tc else 0.0
    st = _g(r, 'stages') or {}
    n = 0
    try:
        for v in st.values():
            if v: n += 1
    except Exception:
        pass
    return tc + 0.05 * n
