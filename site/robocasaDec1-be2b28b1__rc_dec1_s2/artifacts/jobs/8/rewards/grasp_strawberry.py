def reward_fn(state):
    gripper = state.get("gripper") or {}
    opening = gripper.get("opening")
    objs = state.get("objects") or {}
    best = None
    for name, o in objs.items():
        if "straw" in name.lower():
            best = o
            break
    if best is None:
        return 0
    gd = best.get("gripper_dist")
    ip = best.get("init_pos"); p = best.get("pos")
    closed = opening is not None and opening < 0.03
    moved = 0.0
    if ip and p:
        d = ((p[0]-ip[0])**2 + (p[1]-ip[1])**2 + (p[2]-ip[2])**2) ** 0.5
        moved = d
    grasped = (gd is not None and gd < 0.16) and closed
    return int(grasped and moved > 0.03)
