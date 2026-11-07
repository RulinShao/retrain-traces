import numpy as np
def reward_fn(state):
    objs=state.get("objects",{}) or {}
    def cls(ws): return [o for n,o in objs.items() if isinstance(o,dict) and "pos" in o and any(w in n.lower() for w in ws)]
    tups=cls(["tupper","lunchbox","lunch","container","box","bento","tub","tray"])
    foods=cls(["veg","carrot","pepper","cucumber","tomato","celery","broccoli","zucchini","meat","chicken","pork","beef","bacon","ham","fish","shrimp","salmon","food"])
    if not tups or not foods: return 0
    moved=False
    for f in foods:
        try:
            if float(np.linalg.norm(np.array(f["pos"],float)-np.array(f["init_pos"],float)))>0.08: moved=True
        except Exception: pass
    if not moved: return 0
    for f in foods:
        fp=np.array(f.get("pos",[0,0,0]),float)
        ok=False
        for t in tups:
            tp=np.array(t.get("pos",[0,0,0]),float)
            try:
                if float(np.linalg.norm(fp-tp))<0.32: ok=True; break
            except Exception: pass
        if not ok: return 0
    return 1.0
