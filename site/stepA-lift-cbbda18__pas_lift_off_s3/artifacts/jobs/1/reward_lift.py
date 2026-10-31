def _get(r, k):
    if isinstance(r, dict):
        return r.get(k)
    return getattr(r, k, None)

def reward(r):
    # 1.0 on the task's own success check; bounded partial credit on failure
    # (0.25 x the simulator's staged reward) so GRPO keeps gradient signal
    # on the hard tail without drifting from the scored success check.
    try:
        if _get(r, "task_completed"):
            return 1.0
        rc = _get(r, "sandbox_rc")
        if rc is not None and rc != 0:
            return 0.0
        s = float(_get(r, "reward") or 0.0)
    except Exception:
        return 0.0
    return 0.25 * min(1.0, max(0.0, s))
