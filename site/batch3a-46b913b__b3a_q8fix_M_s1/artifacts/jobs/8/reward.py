def _get(r, k, default=None):
    if isinstance(r, dict):
        return r.get(k, default)
    return getattr(r, k, default)

def reward(r):
    # 1.0 task completed
    # 0.0 program did not execute (crash / sandbox error)
    # 0.05 execution floor + 0.1 * shaped otherwise (executed but failed)
    tc = _get(r, "task_completed", False)
    if tc:
        return 1.0
    rc = _get(r, "sandbox_rc", 0)
    try:
        rc_i = int(rc)
    except Exception:
        rc_i = 0
    if rc_i != 0:
        return 0.0
    shaped = _get(r, "reward", 0.0)
    try:
        shaped = float(shaped)
    except Exception:
        shaped = 0.0
    return 0.05 + 0.1 * max(0.0, min(shaped, 1.0))
