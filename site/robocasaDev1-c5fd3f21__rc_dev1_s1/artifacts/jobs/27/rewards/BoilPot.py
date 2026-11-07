
import numpy as np

def region_contains(r, pos, tol=0.06):
    try:
        p0=np.asarray(r["p0"],float); px=np.asarray(r["px"],float); py=np.asarray(r["py"],float); pz=np.asarray(r["pz"],float)
        d=np.asarray(pos,float)-p0; nx=px@px; ny=py@py; nz=pz@pz
        if min(nx,ny,nz)<1e-9: return False
        u=(d@px)/nx; v=(d@py)/ny; w=(d@pz)/nz
        return (-tol<=u<=1+tol) and (-tol<=v<=1+tol) and (-tol<=w<=1+tol)
    except Exception: return False

def objs(state,*subs):
    out=[]
    for n,o in (state.get("objects") or {}).items():
        nl=n.lower()
        if any(s in nl for s in subs): out.append((n,o))
    return out

def fix(state,*subs):
    out=[]
    for n,f in (state.get("fixtures") or {}).items():
        s=(n.lower()+" "+str(f.get("type","")).lower())
        if any(x in s for x in subs): out.append((n,f))
    return out

def in_fixture(pos,fixture):
    return in_region(pos,(fixture or {}).get("regions"))

def in_region(pos,regions):
    if pos is None: return False
    for _,r in (regions or {}).items():
        try:
            if region_contains(r,pos): return True
        except Exception: pass
    return False

def contacts(obj,*names):
    cs=" ".join(obj.get("contacts") or []).lower()
    return any(n.lower() in cs for n in names)

def burner_on(f):
    st=f.get("state") or {}
    vals=[v for k,v in st.items() if "burner" in k.lower()]
    if not vals: vals=list(st.values())
    return any((float(v or 0))>0.5 for v in vals)

def door_closed(f):
    st=f.get("state") or {}
    vals=[v for k,v in st.items() if "door" in k.lower() or "lid" in k.lower()]
    if not vals: return False
    return all(float(v or 0)<0.15 for v in vals)


def reward_fn(state):
    s=0.0
    pot=objs(state,"pot"); stove=fix(state,"stove")
    if pot and stove:
        o=pot[0][1]; f=stove[0][1]
        if (contacts(o,"stove") or in_fixture(o.get("pos"),f)): s+=0.4
        if burner_on(f): s+=0.6
    return float(s)

_reward_orig = reward_fn
def reward_fn(state):
    try:
        v = _reward_orig(state)
    except Exception:
        return 0.0
    try:
        return float(max(0.0, min(1.0, float(v))))
    except Exception:
        return 0.0

reward = reward_fn
