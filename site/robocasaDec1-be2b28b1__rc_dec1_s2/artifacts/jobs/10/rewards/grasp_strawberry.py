def reward_fn(state):
    gripper = state.get("gripper") or {}
    opening = gripper.get("opening")
    gpos = gripper.get("pos")
    closed = opening is not None and opening < 0.03
    objs = state.get("objects") or []
    def items():
        if isinstance(objs, dict):
            return list(objs.items())
        return [( (o.get("name","") if isinstance(o,dict) else str(o)), o ) for o in objs]
    best = None
    for name, o in items():
        if isinstance(o, dict) and "straw" in str(name).lower():
            best = o
    if best is None:
        return 0
    ip = best.get("init_pos"); p = best.get("pos")
    moved = 0.0
    if ip and p:
        moved = ((p[0]-ip[0])**2 + (p[1]-ip[1])**2 + (p[2]-ip[2])**2) ** 0.5
    gd = best.get("gripper_dist")
    if gd is None and gpos and p:
        gd = ((p[0]-gpos[0])**2 + (p[1]-gpos[1])**2 + (p[2]-gpos[2])**2) ** 0.5
    grasped = (gd is not None and gd < 0.16) and closed
    return int(grasped and moved > 0.03)
