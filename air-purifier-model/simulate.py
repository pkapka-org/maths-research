"""Illustrative simulation of Ray Parker's air purifier model.
ALL PARAMETERS ARE ILLUSTRATIVE, NOT MEASURED."""
import json, math, numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
np.random.seed(0)  # fixed seed (model itself is deterministic)
S0, Sol0, alpha0 = 1.0, 100.0, 5.0      # alpha0: "measured" first-step removal (illustrative)
Vol0, x, k = 10.0, 1.0, 0.02            # volume per step, solvent per volume, clog rate
gamma = alpha0/(S0*Vol0*x)              # chosen so formula agrees with alpha0 at t=0
c = lambda s: math.exp(-k*max(s,0))     # clog factor, c(-1)=c(0)=1
Vol = lambda t: Vol0*c(t-1)
T = 60; tmax = Sol0/alpha0 + 1
def run(refined):
    S=[S0]; a=[alpha0]
    for t in range(1,T+1):
        den = Sol0-sum(a[:t-1]) if refined else Sol0-(t-1)*alpha0
        if den<=0: break
        S.append(max(S[-1]*(1-a[t-1]/den),0.0)); a.append(S[-1]*Vol(t)*x*gamma)
    return np.array(S)
Sr, Sf = run(False), run(True)
t = np.arange(T+1); Se = S0*np.exp(-(alpha0/Sol0)*t)   # CADR*dt/V = alpha0/Sol0
fig,ax=plt.subplots(figsize=(6.4,4))
ax.plot(range(len(Sr)),Sr,'o-',ms=3,label="Ray's model (constant-$\\alpha_0$ denominator)")
ax.plot(range(len(Sf)),Sf,'s-',ms=2,label="Refinement (exact remaining solute)")
ax.plot(t,Se,'k--',label="CADR decay $e^{-\\mathrm{CADR}\\,t/V}$ (no clogging)")
ax.axvline(tmax,color='r',ls=':',label=f"validity limit $t={tmax:.0f}$")
ax.set_xlabel("step $t$"); ax.set_ylabel("$S_t/S_0$"); ax.set_title("Illustrative parameters (not measured)")
ax.legend(fontsize=8); fig.tight_layout()
for e in ("png","pdf"): fig.savefig(f"simulation.{e}")
res=dict(params=dict(S0=S0,Sol0=Sol0,alpha0=alpha0,Vol0=Vol0,x=x,k=k,gamma=gamma),
  validity_limit=tmax, ray_steps=len(Sr)-1, S_ray_10=Sr[10], S_ref_10=Sf[10], S_exp_10=Se[10],
  S_ray_last=Sr[-1], S_ref_20=Sf[20], S_exp_20=Se[20], S_ref_60=Sf[60], S_exp_60=Se[60])
json.dump(res,open("results.json","w"),indent=1); print(res)
