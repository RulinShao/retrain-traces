import math

def _obj_pos(r, name):
    fs = r.get("final_state") or {}
    o = (fs.get("objects") or {}).get(name) or {}
    return o.get("init_pos"), o.get("pos")

def _maxz_trace(r, name):
    pts = (r.get("trace") or {}).get("points") or []
    zmax = None
    for p in pts:
        o = ((p.get("objects") or {}).get(name) or {})
        pos = o.get("pos")
        if pos is not None:
            try:
                z = float(pos[2])
                if zmax is None or z > zmax:
                    zmax = z
            except Exception:
                pass
    return zmax

def _lift(r, name):
    init_pos, pos = _obj_pos(r, name)
    zmax = _maxz_trace(r, name)
    if zmax is None and pos is not None:
        zmax = float(pos[2])
    if zmax is None:
        return 0.0
    iz = float(init_pos[2]) if init_pos is not None else 0.82
    return max(0.0, zmax - iz)

def _contacted(r, name):
    fs = r.get("final_state") or {}
    for c in (fs.get("contacts") or []):
        if isinstance(c, (list, tuple)) and len(c) == 2:
            if "arm" in str(c[0]) and c[1] == name:
                return True
            if "arm" in str(c[1]) and c[0] == name:
                return True
    return False

def reward(r):
    if r.get("task_completed"):
        return 1.0
    task = r.get("task", "")
    target = "green_cube" if task == "revstack" else "red_cube"
    shaped = 0.0
    try:
        shaped = float(r.get("reward") or 0.0)
    except Exception:
        shaped = 0.0
    if task == "restack":
        # suppress the easy "bump the green off the red" component so the
        # signal rewards actually grasping/lifting the red cube
        stages = r.get("stages") or {}
        if stages.get("unstack the green off the red"):
            shaped *= 0.3
        lift = _lift(r, target)
        contacted = 1.0 if _contacted(r, target) else 0.0
        return min(1.0, 0.3 * shaped + 0.35 * contacted + 1.2 * lift)
    if task == "revstack":
        lift = _lift(r, target)
        contacted = 1.0 if _contacted(r, target) else 0.0
        return min(1.0, 0.3 * shaped + 0.35 * contacted + 1.2 * lift)
    if task == "nut":
        stages = r.get("stages") or {}
        if stages.get("insert the nut"):
            return 0.95
        if stages.get("align the nut over the peg"):
            return 0.75
        if stages.get("grasp the nut"):
            return 0.5
        if stages.get("reach the handle"):
            return 0.25
        return max(0.0, 0.15 * shaped)
    return max(0.0, shaped)
