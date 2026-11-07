def _get(r, key, default=None):
    try:
        if hasattr(r, "get"):
            return r.get(key, default)
    except Exception:
        pass
    try:
        return getattr(r, key, default)
    except Exception:
        return default

def reward(r):
    # Stage-fraction reward for staged manipulation tasks.
    # 0.0 on any crash; 0.0 on a no-op (no stage reached);
    # n/k for reaching n of the k ordered checklist stages; 1.0 on task completion.
    rc = _get(r, "sandbox_rc")
    if rc is not None and rc != 0:
        return 0.0
    stages = _get(r, "stages")
    if not stages:
        return 0.0
    k = len(stages)
    if k == 0:
        return 0.0
    n = sum(1 for v in stages.values() if v)
    val = n / k
    tc = _get(r, "task_completed")
    if tc:
        val = max(val, 1.0)
    return float(val)
