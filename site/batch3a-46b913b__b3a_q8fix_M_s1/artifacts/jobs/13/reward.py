import os, json

_TARGETS = [
    "…/notes/rollout_diag.jsonl",
    os.path.join(os.getcwd(), "rollout_diag.jsonl"),
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "rollout_diag.jsonl"),
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
    tc = bool(r.get("task_completed"))
    try:
        rc = int(r.get("sandbox_rc", 0))
    except Exception:
        rc = 1
    try:
        sim = float(r.get("reward", 0.0))
    except Exception:
        sim = 0.0
    # Diagnostic: persist the sim reply's tail + status so the crash cause is readable.
    try:
        if _n[0] < 300:
            _n[0] += 1
            rec = {"tc": tc, "rc": rc, "sim": round(sim, 4), "seed": r.get("seed"),
                   "task": r.get("task"), "tail": (r.get("log_tail") or "")[-600:]}
            _log(rec)
    except Exception:
        pass
    if tc:
        return 1.0
    if rc != 0:
        return 0.0
    return 0.5 + 0.4 * max(0.0, min(sim, 1.0))
