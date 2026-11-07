import numpy as np
def reward_fn(state):
    objs=state.get("objects",{}) or {}
    def pick(words):
        out=[]
        for n,o in objs.items():
            if isinstance(o,dict) and any(w in n.lower() for w in words): out.append(o)
        return out
    breads=pick(("bread","bread0","bread1","loaf","baguette","slice"))
    bowls=pick(("bowl","bread bowl","bowl0"))
    if not breads or not bowls: return 0.0
    b0=bowls[0]; bc=np.array(b0.get("pos",[0,0,0]),float)
    r=float(np.max(b0.get("size",[0.15,0.15,0.15])))
    n_in=0
    for br in breads:
        p=np.array(br.get("pos",[0,0,0]),float)
        if float(np.linalg.norm(p-bc))<max(0.30,1.2*r): n_in+=1
    if n_in==0: return 0.0
    b_on_counter=any("dining" in str(c).lower() or "counter" in str(c).lower() for c in (b0.get("contacts") or []))
    if n_in>=len(breads) and b_on_counter: return 1.0
    return 0.0
