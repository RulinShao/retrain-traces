import numpy as np
def reward_fn(state):
    objs=state.get("objects",{}) or {}
    def cls(words):
        return [o for n,o in objs.items() if isinstance(o,dict) and any(w in n.lower() for w in words)]
    tups=cls(("tupper","lunchbox","lunch","container","box","bento","tub"))
    items=cls(("veg","carrot","pepper","cucumber","tomato","celery","broccoli","zucchini","meat","chicken","pork","beef","bacon","ham","fish","shrimp","salmon"))
    if not tups or not items: return 0.0
    for it in items:
        p=np.array(it.get("pos",[0,0,0]),float)
        for t in tups:
            tp=np.array(t.get("pos",[0,0,0]),float)
            try:
                if float(np.linalg.norm(p-tp))<0.30: return 1.0
            except Exception: pass
    return 0.0
