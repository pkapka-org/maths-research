"""Simulation of Ray Parker's stacked-random-layers extension.
Stacks N random n x n binary layers (fill prob p) along y and measures
(a) fraction of lines of sight still fully clear, (b) fraction containing >=1 empty cell."""
import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
SEED, n, NMAX, PS = 2026, 200, 60, [0.05, 0.10, 0.25]
rng = np.random.default_rng(SEED)
fig, ax = plt.subplots(1, 2, figsize=(10, 4))
for p in PS:
    clear = np.ones((n, n), bool); anyempty = np.zeros((n, n), bool)
    ec, ee = [], []
    for N in range(1, NMAX + 1):
        layer = rng.random((n, n)) < p           # 1 = filled
        clear &= ~layer; anyempty |= ~layer
        ec.append(clear.mean()); ee.append(anyempty.mean())
    Ns = np.arange(1, NMAX + 1)
    ax[0].plot(Ns, ec, "o", ms=3, label=f"empirical p={p}")
    ax[0].plot(Ns, (1 - p) ** Ns, "-", lw=1)
    ax[1].plot(Ns, ee, "o", ms=3, label=f"empirical p={p}")
    ax[1].plot(Ns, 1 - p ** Ns, "-", lw=1)
    print(f"p={p}: N=20 clear emp={ec[19]:.4f} theory={(1-p)**20:.4f}")
ax[0].set(title="Clear line of sight: $(1-p)^N$", xlabel="layers N", ylabel="fraction of lines")
ax[1].set(title="Line has $\\geq$1 empty cell: $1-p^N$", xlabel="layers N", ylim=(0.9, 1.005))
ax[0].legend(fontsize=8); ax[1].legend(fontsize=8)
fig.suptitle(f"n={n}, seed={SEED}; dots = simulation, lines = theory"); fig.tight_layout()
fig.savefig("stacking_sim.pdf"); fig.savefig("stacking_sim.png", dpi=150)
