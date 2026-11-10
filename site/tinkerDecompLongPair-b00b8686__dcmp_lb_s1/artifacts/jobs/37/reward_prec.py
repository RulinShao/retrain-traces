import numpy as np
def _get(r, k, d=None):
    try:
        if hasattr(r, "get"):
            return r.get(k, d)
    except Exception:
        pass
    try:
        return getattr(r, k, d)
    except Exception:
        return d

def reward(r):
    # Placement-precision reward for "pick one cube, place centered on the other".
    # Dense along horizontal offset (the axis the success check needs) so GRPO
    # gets within-group variance toward precise placement; 1.0 on completion.
    rc = _get(r, "sandbox_rc")
    if rc is not None and rc != 0:
        return 0.0
    fs = _get(r, "final_state")
    if not fs:
        return 0.0
    objs = _get(fs, "objects", {}) or {}
    cubes = {k: v for k, v in objs.items() if "cube" in k.lower()}
    if len(cubes) < 2:
        vals = list(objs.values())
        if len(vals) < 2:
            return 0.0
        cubes = {"c%d" % i: v for i, v in enumerate(vals[:2])}
    moved, mv = None, 0.0
    for k, v in cubes.items():
        p = v.get("pos"); ip = v.get("init_pos")
        if p and ip and len(p) == 3 and len(ip) == 3:
            d = abs(p[0]-ip[0]) + abs(p[1]-ip[1]) + abs(p[2]-ip[2])
            if d > mv:
                mv = d; moved = k
    if moved is None or mv < 0.005:
        return 0.0
    tgt = [k for k in cubes if k != moved][0]
    p = cubes[moved]["pos"]; t = cubes[tgt]["pos"]
    sx = cubes[moved].get("size", [0.04, 0.04, 0.04])
    tx = cubes[tgt].get("size", [0.05, 0.05, 0.05])
    dxy = float(np.hypot(p[0]-t[0], p[1]-t[1]))
    bottom = p[2] - sx[2]/2.0
    top = t[2] + tx[2]/2.0
    resting = (dxy < 0.06) and (-0.01 < bottom-top < 0.04)
    score = 0.12 + 0.55 * max(0.0, 1.0 - dxy/0.12)
    if resting:
        score += 0.25
    tc = _get(r, "task_completed")
    if tc:
        return 1.0
    return float(min(1.0, max(0.0, score)))
