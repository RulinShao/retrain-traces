import numpy as np

def _f(x, d=0.0):
    try:
        return float(x)
    except Exception:
        return d

def reward_fn(state):
    if state.get("task_completed"):
        return 1.0
    fix = state.get("fixtures") or {}
    bl = None
    for fn, f in fix.items():
        if "blender" in fn.lower():
            bl = (fn, f)
            break
    if bl is None:
        return 0.0
    fn, f = bl
    stt = f.get("state") or {}
    if not isinstance(stt, dict):
        stt = {}
    ist = f.get("init_state") or {}
    on = 0.0
    lid_seated = 0.0
    for k, v in stt.items():
        kl = str(k).lower()
        if isinstance(v, (int, float)):
            vv = _f(v)
            iv = _f(ist.get(k), vv) if isinstance(ist, dict) else vv
            if "on" == kl or "button" in kl or "switch" in kl or "start" in kl:
                if vv >= 0.5:
                    on = 1.0
            if "lid" in kl:
                if abs(vv - 0.0) < 0.2:
                    lid_seated = 1.0
                elif abs(vv) > abs(iv) * 0 + 0.2:
                    lid_seated = max(lid_seated, min(1.0, 1.0 - vv / 0.5))
        elif isinstance(v, dict):
            for k2, v2 in v.items():
                kl2 = str(k2).lower()
                if isinstance(v2, (int, float)):
                    vv2 = _f(v2)
                    if ("lid" in kl2 or "lid" in kl) and vv2 <= 0.2:
                        lid_seated = 1.0
    r = 0.25 * on + 0.4 * lid_seated
    for c in ((f.get("contacts")) or []):
        if "fruit" in str(c).lower() or "apple" in str(c).lower() or "banana" in str(c).lower() or "kiwi" in str(c).lower():
            r = max(r, 0.5)
    return float(min(1.0, r))
