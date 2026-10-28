# Measuring and comparing randomness

**Author:** Piyush Kumar

Source: handwritten notes (photos in this folder).

## Core idea

- Randomness = deviation from predictability.
- A "stencil" is a defined predictability: an expected feature score or range, used as a fixed reference.
- Both randomness and predictability are measured against that fixed absolute reference. When features differ, a new temporary stencil is made for the comparison.
- Delta r_i = r_i − S_n, where S_n is the stencil at the n-th iteration and r_i is the i-th randomness.
- Rel(Δ, r_i, r_j) = Δ r_i − Δ r_j, where r_i ≠ r_j.
- S_{n+1} = Avg(Δ r, S_n). For k sources of randomness: S_{n+1} = Avg over k (Δ r_k, S_n), with k ∈ [0, K].
- Extension: a matrix of stencils, one per feature, instead of a single stencil for all features.

## Extension: stacking random layers

- Take n × n layers where each cell is filled (1) at random with probability p, and stack them along y.
- Chance a line of sight stays clear after N layers: (1−p)^N, which goes to 0. The stack turns opaque.
- Each layer on its own still has gaps (1 − p^N goes to 1).
- This matches the Beer–Lambert law: one graphene sheet is see-through, while a graphite block is opaque.

## Files

- `main.tex` / `main.pdf` — formal write-up
- `sim.py` — stacking simulation; writes `stacking_sim.png/.pdf`
- `notes-page-1.png`, `notes-page-2.png` — handwritten source notes
