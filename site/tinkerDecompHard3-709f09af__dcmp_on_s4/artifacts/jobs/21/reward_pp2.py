import math

def _get(r, k, default=None):
    if isinstance(r, dict):
        return r.get(k, default)
    return getattr(r, k, default)

def _dist(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))

def reward(r):
    if _get(r, "task_completed"):
        return 1.0
    fs = _get(r, "final_state")
    if not fs:
        return 0.0
    ob = fs.get("objects") or {}
    g = (fs.get("grippers") or {}).get("arm0") or {}
    gpos = g.get("pos")
    if not gpos:
        return 0.0
    if "red_cube" in ob and "green_cube" in ob:
        tgt, base = ob["red_cube"], ob["green_cube"]
        gp, bp = tgt.get("pos"), base.get("pos")
        if not gp or not bp:
            return 0.0
        reach = max(0.0, 1 - _dist(gpos, gp) / 0.10)          # gripper got to the cube (targets the miss)
        ip = tgt.get("init_pos") or gp
        mz = tgt.get("max_z")
        lift = max(0.0, min(1.0, ((mz - ip[2]) if mz is not None else 0.0) / 0.15))  # grasped & lifted
        bsize = base.get("size") or [0.04] * 3
        base_top = bp[2] + bsize[2] / 2
        stacked_z = 1.0 if gp[2] > base_top + 0.005 else 0.0  # red ABOVE green's top (not the initial side-by-side)
        prox = max(0.0, 1 - math.hypot(gp[0] - bp[0], gp[1] - bp[1]) / 0.05)
        stack = prox * stacked_z
        return 0.45 * reach + 0.25 * lift + 0.30 * stack
    if "square_nut" in ob and "square_peg" in ob:
        nut, peg = ob["square_nut"], ob["square_peg"]
        np_, pp = nut.get("pos"), peg.get("pos")
        if not np_ or not pp:
            return 0.0
        reach = max(0.0, 1 - _dist(gpos, (nut.get("handle_pos") or np_)) / 0.10)
        ip = nut.get("init_pos") or np_
        mz = nut.get("max_z")
        lift = max(0.0, min(1.0, ((mz - ip[2]) if mz is not None else 0.0) / 0.15))
        insert = max(0.0, 1 - math.hypot(np_[0] - pp[0], np_[1] - pp[1]) / 0.04)  # nut moved to the peg
        return 0.45 * reach + 0.25 * lift + 0.30 * insert
    return 0.0
