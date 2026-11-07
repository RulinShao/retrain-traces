import numpy as np
def reward_fn(state):
    objs=state.get("objects",{}) or {}
    items=[(n,o) for n,o in objs.items() if isinstance(o,dict) and "pos" in o and "init_pos" in o]
    for i in range(len(items)):
        oi=items[i][1]
        try:
            pi=np.array(oi["pos"],float); ii=np.array(oi["init_pos"],float)
            moved_i=float(np.linalg.norm(pi-ii))>0.10
            for j in range(len(items)):
                if i==j: continue
                oj=items[j][1]
                pj=np.array(oj["pos"],float); ij=np.array(oj["init_pos"],float)
                moved_j=float(np.linalg.norm(pj-ij))>0.10
                if (moved_i or moved_j) and float(np.linalg.norm(pi-pj))<0.30:
                    return 1.0
        except Exception:
            pass
    return 0.0
