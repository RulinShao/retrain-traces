import math

def _get(r, k, default=None):
    if isinstance(r, dict):
        return r.get(k, default)
    return getattr(r, k, default)

def _fs(r):
    fs = _get(r, "final_state")
    return fs if fs else None

def reward(r):
    if _get(r, "task_completed"):
        return 1.0
    fs = _fs(r)
    if not fs:
        return 0.0
    ob = fs.get("objects") or {}
    g = (fs.get("grippers") or {}).get("arm0") or {}
    gpos = g.get("pos")
    if not gpos:
        return 0.0
    if "red_cube" in ob and "green_cube" in ob:
        target, base = ob["red_cube"], ob["green_cube"]
    elif "square_nut" in ob and "square_peg" in ob:
        target, base = ob["square_nut"], ob["square_peg"]
    else:
        return 0.0
    tp, bp = target.get("pos"), base.get("pos")
    if not tp or not bp:
        return 0.0
    # gripper reached the target object
    dist = math.sqrt(sum((a - b) ** 2 for a, b in zip(gpos, tp)))
    reach = max(0.0, 1 - dist / 0.08)
    # target lifted (proxy for a successful grasp)
    ip = target.get("init_pos") or tp
    mz = target.get("max_z")
    lift = (mz - ip[2]) if mz is not None else 0.0
    liftc = max(0.0, min(1.0, lift / 0.20))
    # target moved near the base (alignment / placement)
    horiz = math.sqrt((tp[0] - bp[0]) ** 2 + (tp[1] - bp[1]) ** 2)
    placec = max(0.0, 1 - horiz / 0.06)
    return 0.20 * reach + 0.35 * liftc + 0.45 * placec
