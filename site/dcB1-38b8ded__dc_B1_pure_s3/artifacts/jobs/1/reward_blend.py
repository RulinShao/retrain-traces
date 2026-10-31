def _get(r, k, d=0.0):
    try:
        v = r[k]
    except Exception:
        try:
            v = getattr(r, k)
        except Exception:
            v = d
    return d if v is None else v

def _f(x, d=0.0):
    try:
        return float(x)
    except Exception:
        return d

def reward(r):
    # Success-first reward: full success -> 1.0 (clean binary signal for GRPO).
    # Failure -> up to 0.3 * (staged simulator reward clamped to [0,1]) as shaping,
    # so 0%-success tasks still get a small gradient when any stage progress happens.
    tc = _f(_get(r, 'task_completed', 0.0))
    staged = _f(_get(r, 'reward', 0.0))
    staged = max(0.0, min(1.0, staged))
    if tc >= 0.5:
        return 1.0
    return 0.3 * staged
