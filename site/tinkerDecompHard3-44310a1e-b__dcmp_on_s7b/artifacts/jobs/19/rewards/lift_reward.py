import math

def _trace(r):
    return (r.get("trace") or {}).get("points") or []

def _final_objects(r):
    return (r.get("final_state") or {}).get("objects") or {}

def _init_z(r, name):
    o = _final_objects(r).get(name) or {}
    ip = o.get("init_pos")
    if ip: return float(ip[2])
    # fallback: first trace point
    for p in _trace(r):
        pos = ((p.get("objects") or {}).get(name) or {}).get("pos")
        if pos: return float(pos[2])
    return None

def _maxz(r, name):
    zmax = None
    for p in _trace(r):
        pos = ((p.get("objects") or {}).get(name) or {}).get("pos")
        if pos:
            z = float(pos[2])
            if zmax is None or z > zmax: zmax = z
    o = _final_objects(r).get(name) or {}
    if o.get("pos"):
        z = float(o["pos"][2])
        if zmax is None or z > zmax: zmax = z
    return zmax

def _closed_min_d(r, name):
    # min distance gripper-center to object-center while gripper is closed (opening<0.03)
    best = None
    for p in _trace(r):
        o = ((p.get("objects") or {}).get(name) or {}).get("pos")
        g = (p.get("grippers", {}).get("arm0") or {})
        gp = g.get("pos"); op = g.get("opening")
        if o and gp and op is not None and op < 0.03:
            d = math.dist(gp, o)
            if best is None or d < best: best = d
    return best

def _aligned(r, above, base):
    fa = _final_objects(r)
    if not fa:
        # use last trace point
        pts = _trace(r)
        if not pts: return False
        fa = ((pts[-1].get("objects") or {}))
    a = (fa.get(above) or {}).get("pos"); b = (fa.get(base) or {}).get("pos")
    if not a or not b: return False
    return (a[2]-b[2]) > 0.02 and math.hypot(a[0]-b[0], a[1]-b[1]) < 0.06

def _shaped(r):
    try: return float(r.get("reward") or 0.0)
    except Exception: return 0.0

def _clip(x): return max(0.0, min(1.0, x))

def reward(r):
    if r.get("task_completed"):
        return 1.0
    task = r.get("task", "")
    if task in ("restack", "revstack"):
        target = "red_cube" if task == "restack" else "green_cube"
        base = "green_cube" if task == "restack" else "red_cube"
        d = _closed_min_d(r, target)
        grasp = _clip(1.0 - d / 0.08) if d is not None else 0.0
        iz = _init_z(r, target); mz = _maxz(r, target)
        lift = _clip((mz - iz) / 0.04) if (mz is not None and iz is not None) else 0.0
        align = 1.0 if _aligned(r, target, base) else 0.0
        return min(1.0, 0.5 * grasp + 0.3 * lift + 0.2 * align)
    if task == "nut":
        stages = r.get("stages") or {}
        if stages.get("insert the nut"): return 0.95
        if stages.get("align the nut over the peg"): return 0.75
        if stages.get("grasp the nut"): return 0.5
        if stages.get("reach the handle"): return 0.25
        return max(0.0, 0.15 * _shaped(r))
    return max(0.0, _shaped(r))
