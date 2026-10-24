import os, json

_TARGETS = [
    "…/notes/rollout_tc.jsonl",
    os.path.join(os.getcwd(), "rollout_tc.jsonl"),
]
_n = [0]

def _log(rec):
    for t in _TARGETS:
        try:
            d = os.path.dirname(t)
            if d:
                os.makedirs(d, exist_ok=True)
            with open(t, "a") as f:
                f.write(json.dumps(rec) + "\n")
        except Exception:
            pass

def reward(r):
    # completion-dominant: passing the task's own success check stands far above
    # merely running with a high staged reward, so GRPO concentrates on completions.
    tc = bool(r.get("task_completed"))
    try:
        rc = int(r.get("sandbox_rc", 0))
    except Exception:
        rc = 1
    try:
        sim = float(r.get("reward", 0.0))
    except Exception:
        sim = 0.0
    try:
        if _n[0] < 2000:
            _n[0] += 1
            _log({"tc": tc, "rc": rc, "sim": round(sim, 4), "seed": r.get("seed"),
                  "task": r.get("task")})
    except Exception:
        pass
    if tc:
        return 1.0
    if rc != 0:
        return 0.0
    return 0.02 + 0.08 * max(0.0, min(sim, 1.0))   # ran-but-failed: small, << 1.0
