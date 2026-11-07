import numpy as np

STAGES = {
    "reach the green_cube": 0.08,
    "grasp the green_cube": 0.14,
    "hold the cube": 0.45,
    "align the green_cube over the red_cube": 0.55,
    "place the green_cube on the red_cube": 0.85,
}

def reward(r):
    fs = r.get("final_state") or {}
    objs = (fs.get("objects") or {})
    green = objs.get("green_cube") or {}
    red = objs.get("red_cube") or {}
    gp = np.array(green.get("pos") or [0, 0, 0], float)
    rp = np.array(red.get("pos") or [0, 0, 0], float)
    init = np.array(green.get("init_pos") or gp, float)
    ext = np.array(green.get("extent") or [0.1, 0.1, 0.1], float)
    best = 0.0
    if np.linalg.norm(gp[:2] - init[:2]) < 0.03 and gp[2] < init[2] + 0.005:
        best = max(best, STAGES["reach the green_cube"])
    if bool((r.get("stages") or {}).get("grasp the green_cube")):
        best = max(best, STAGES["grasp the green_cube"])
    tr = r.get("trace") or {}
    pts = tr.get("points") or []
    closed = False
    if any(((p.get("grippers") or {}).get("arm0") or {}).get("closed") for p in pts):
        closed = True
        mx = max(((p.get("objects") or {}).get("green_cube") or {}).get("pos", [0, 0, 0])[2] for p in pts)
        if mx > init[2] + 0.06:
            best = max(best, STAGES["hold the cube"])
    if closed and mx > init[2] + 0.18:
        best = max(best, 0.62)
    if closed and mx > init[2] + 0.18 and np.linalg.norm(gp[:2] - rp[:2]) < max(ext[0], ext[1]) * 0.75:
        best = max(best, STAGES["align the green_cube over the red_cube"])
    if (r.get("stages") or {}).get("place the green_cube on the red_cube"):
        best = max(best, STAGES["place the green_cube on the red_cube"])
    if r.get("task_completed"):
        best = 1.0
    if int(r.get("sandbox_rc") or 0) != 0:
        return 0.0
    return float(best)
