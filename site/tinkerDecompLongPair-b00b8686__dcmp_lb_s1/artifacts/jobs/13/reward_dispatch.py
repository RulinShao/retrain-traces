import math

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

def _clip(x, lo, hi):
    return max(lo, min(hi, x))

def _dist(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))

def _stages_frac(r):
    stages = _get(r, "stages")
    if not stages:
        return 0.0
    n = sum(1 for v in stages.values() if v)
    k = len(stages)
    val = n / k if k else 0.0
    if _get(r, "task_completed"):
        val = max(val, 1.0)
    return val

def _nut_reward(r):
    fs = _get(r, "final_state")
    tr = _get(r, "trace")
    if not fs or not tr:
        return _stages_frac(r)
    objs = fs.get("objects") or {}
    nut = objs.get("square_nut")
    peg = objs.get("square_peg")
    if not nut or not peg:
        return _stages_frac(r)
    init = nut.get("init_pos"); final = nut.get("pos"); handle = nut.get("handle_pos")
    pegp = peg.get("pos")
    if not init or not final or not handle or not pegp:
        return _stages_frac(r)
    pts = tr.get("points") or []
    min_appr = None
    max_lift = 0.0
    best_xy = 1e9
    for p in pts:
        g = (p.get("grippers") or {}).get("arm0") or {}
        gp = g.get("pos")
        if gp:
            d = _dist(gp, handle)
            d2 = _dist(gp, init)  # near body counts too (handle may be hidden)
            d = min(d, d2)
            if min_appr is None or d < min_appr:
                min_appr = d
        on = (p.get("objects") or {}).get("square_nut") or {}
        op = on.get("pos")
        if op:
            lift = op[2] - init[2]
            if lift > max_lift:
                max_lift = lift
            dxy = math.hypot(op[0] - pegp[0], op[1] - pegp[1])
            if dxy < best_xy:
                best_xy = dxy
    # fold in final state
    dxyf = math.hypot(final[0] - pegp[0], final[1] - pegp[1])
    if dxyf < best_xy:
        best_xy = dxyf
    liftf = final[2] - init[2]
    if liftf > max_lift:
        max_lift = liftf
    approach = _clip(1 - (min_appr - 0.04) / (0.12 - 0.04), 0, 1) if min_appr is not None else 0.0
    held_lift = max_lift > 0.03
    lift_f = _clip((max_lift - 0.02) / 0.06, 0, 1)
    align = _clip(1 - (best_xy - 0.03) / (0.12 - 0.03), 0, 1)
    znear = _clip(1 - abs(final[2] - pegp[2]) / 0.06, 0, 1)
    insert = align * znear
    score = 0.20 * approach
    if held_lift:
        score += 0.15 + 0.15 * lift_f + 0.25 * align + 0.25 * insert
    if _get(r, "task_completed"):
        score = max(score, 1.0)
    return _clip(score, 0, 1)

def reward(r):
    rc = _get(r, "sandbox_rc")
    if rc is not None and rc != 0:
        return 0.0
    t = _get(r, "task")
    if t == "nut":
        try:
            return _nut_reward(r)
        except Exception:
            return _stages_frac(r)
    return _stages_frac(r)
