def reward(r):
    """GRPO reward for restack: dominant success, plus execution + staged credit
    so the policy gets gradient even when base programs fail before any staged
    credit (base is 0/100 and shaped credit was ~0 elsewhere)."""
    def g(name, default=None):
        if isinstance(r, dict):
            v = r.get(name, default)
        else:
            v = getattr(r, name, default)
        return default if v is None else v

    tc = g("task_completed", 0)
    try:
        if float(tc):
            return 1.0
    except Exception:
        pass

    shaped = g("reward", 0.0)
    try:
        shaped = float(shaped)
    except Exception:
        shaped = 0.0
    shaped = min(1.0, max(0.0, shaped))

    rc = g("sandbox_rc", None)
    ran = 1.0 if rc in (0, None) else 0.0

    return 0.1 * ran + 0.2 * shaped
