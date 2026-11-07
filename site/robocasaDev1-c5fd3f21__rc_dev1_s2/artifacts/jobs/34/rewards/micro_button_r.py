def _any_on(f, words):
    st = f.get("state") or {}
    if not isinstance(st, dict): return False
    for k, v in st.items():
        kl = str(k).lower()
        if isinstance(v, (int, float)) and float(v) >= 0.5 and any(w in kl for w in words):
            return True
    return False
def reward_fn(state):
    for n, f in (state.get("fixtures") or {}).items():
        nl = n.lower(); t = str(f.get("type") or "").lower()
        if ("microwave" in nl or "microwave" in t):
            if _any_on(f, ("start", "button", "on", "press", "running", "on_")):
                return 1
    return 0
