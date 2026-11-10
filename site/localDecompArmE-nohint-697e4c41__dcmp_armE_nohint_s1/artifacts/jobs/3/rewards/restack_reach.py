# Ordered stage-reach reward for restack (real start).
# Stages (simulator checklist order): unstack -> grasp -> lift -> align -> place.
# Frontier (stage 1, unstack) carries 0.5; the final stage keeps its 0.5;
# small bonuses for the never-reached middle stages; continuous progress
# term inside the frontier so GRPO groups vary; crash / no-op pays 0.
STAGES = [
    "unstack the green off the red",
    "grasp the red",
    "lift the red",
    "align the red over the green",
    "place the red on the green",
]
MID = {2: 0.52, 3: 0.54, 4: 0.56}

def g(r, k, d=None):
    try:
        if isinstance(r, dict):
            return r.get(k, d)
        return getattr(r, k, d)
    except Exception:
        return d

def reward(r):
    if g(r, "task_completed"):
        return 1.0
    rc = g(r, "sandbox_rc", 0)
    if rc not in (0, None):
        return 0.0
    fs = g(r, "final_state")
    st = g(r, "stages") or {}
    if not fs:
        return 0.0
    objs = fs.get("objects") if isinstance(fs, dict) else None
    if not objs:
        return 0.0
    red = objs.get("red_cube")
    green = objs.get("green_cube")
    if not red or not green:
        return 0.0
    rp = red.get("pos"); gp = green.get("pos")
    if not rp or not gp:
        return 0.0
    dx = gp[0] - rp[0]; dy = gp[1] - rp[1]; dz = gp[2] - rp[2]
    h = (dx * dx + dy * dy) ** 0.5
    # ordered prefix of reached stages
    k = 0
    for s in STAGES:
        if st.get(s):
            k += 1
        else:
            break
    if k >= 5:
        return 1.0
    if k >= 2:
        return MID[k]
    if k == 1:
        return 0.5
    # k == 0: continuous progress inside the frontier (stage 1 = unstack)
    on_top = (dz > 0.015) and (h < 0.045)
    if on_top:
        return 0.0  # start state / no-op scores lowest
    p = 0.55 * min(1.0, h / 0.06) + 0.45 * min(1.0, max(0.0, (0.045 - dz)) / 0.045)
    return 0.15 * p
