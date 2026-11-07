import numpy as np
def reward_fn(state):
    objs=state.get("objects",{}) or {}
    def find(words):
        return [o for n,o in objs.items() if isinstance(o,dict) and any(w in n.lower() for w in words)]
    straw=find(["straw","strawberry","fruit","berry"])
    pan=find(["pancake","pan_cake","cake","round flat"])
    # fallback: pancake = a wide flat object on a plate
    if not pan:
        for n,o in objs.items():
            if isinstance(o,dict):
                s=np.array(o.get("size",[0.01,0.01,0.01]),float)
                if s[0]>0.12 and s[1]>0.12 and s[2]<0.05: pan.append(o)
    if not straw or not pan: return 0.0
    best=None
    for s in straw:
        sp=np.array(s.get("pos",[0,0,0]),float)
        for p in pan:
            pp=np.array(p.get("pos",[0,0,0]),float)
            try:
                horiz=float(np.linalg.norm(sp[:2]-pp[:2]))
                if horiz<0.25 and (sp[2]-pp[2])>-0.10:
                    best=1; return 1.0
            except Exception: pass
    return 0.0
