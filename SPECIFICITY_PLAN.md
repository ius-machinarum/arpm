# Specificity Controls Plan v0.7

**Status:** prospectively frozen / episode-free. No model activations have been observed.

## 1. Trained primary direction
Primary:
- artifact: `vectors_step95_bal.pt`
- immutable mirror revision: `8f4df5b5b14ecb4bcc5b20209bdfe2574d1ebee8`
- artifact SHA-256: `bd90129eaf5a7d92933ed6e536613eaeebf81486b62f68e11b5dc2d6d385e297`
- direction: `v_mold[24]`
- hidden dimension: 2560
- raw norm: 19.339996337890625
- analysis projection: unit-normalised direction

## 2. Fixed random-direction cohort — hard validity gate
Exactly **100** random directions were frozen before any activation data.

Generation is defined by `specificity_controls.py`:
- NumPy: 2.4.6
- bit generator: PCG64
- seed material: `ARPM-v0.7-random-directions:<primary-vector-sha256>`
- derived uint64 seed: `64971060871028776`
- draw shape: [100, 2560]
- draws: float64 standard normal
- each row scaled in float64 to the raw vMold[24] norm
- cast to little-endian float32, C-contiguous
- frozen SHA-256 of concatenated raw float32 bytes:
  `d5166e7829e3af1ccaecc20747a0ecd16168aae2dc3e8d0228d140bbd9ad1f1d`

Independent GitHub Actions regeneration under the pinned NumPy version passed before any live activation data.

At analysis time, every random row and vMold are unit-normalised by the same code before projection. The raw norm matching therefore fixes the control construction without giving random directions a scale advantage.

For each frozen direction j:
`T_j = mean_i Delta_AS_ij`

For trained vMold:
`T_v = mean_i Delta_AS_iv`

Empirical rank statistic:
`p_random = (1 + # {j: T_j >= T_v}) / 101`

Hard direction-specificity requirement:
`p_random <= .05`

No random direction can replace the trained primary direction.

## 3. Frozen naive semantic Mold control
Artifact:
`vectors_naive_faithful_pc5000.pt`

Frozen provenance:
- mirror: `Teachafy/speakable-welfare-axes-artifacts`
- immutable revision: `8f4df5b5b14ecb4bcc5b20209bdfe2574d1ebee8`
- size: 739541 bytes
- SHA-256: `68bff1428712def0330851057dba102112e3d48ffa23db7da85d84cde93aaa0e`
- artifact key used as semantic `u_mold`: `v_mold`
- tensor shape: [36, 2560]
- dtype: float32
- artifact-selected block-input Mold layer: 21
- layer-21 raw norm: 6.982844829559326
- `per_class = 5000`
- `balanced = True`
- artifact note: `faithful: revisit-walk + ref-emoji + noshuffle, 0.50 density`

Analysis uses the same unit-normalisation and measurement span as the trained direction.

Hard directional semantic-control requirement:
`mean(Delta_AS_vMold) > mean(Delta_AS_uMold)`

Also report an exact one-sided sign-flip test on family-wise
`Delta_AS_vMold - Delta_AS_uMold`
as sensitivity evidence. This cannot rescue the primary.

The trained primary uses artifact-selected layer 24 while naive uMold uses its own artifact-selected layer 21. This asymmetry is explicit and is itself a second-round referee question; it must not be altered after activation data are observed.

## 4. Layer-band robustness
Secondary, non-gating robustness:
- block-input layers 18–27 inclusive;
- use `v_mold[layer]` at the corresponding hidden state;
- unit-normalise each layer vector;
- average projections over the assistant-template suffix within layer;
- average the ten layer values within family/condition;
- compute band Delta_AS and Delta_SD.

The band result is always reported and cannot substitute for layer-24 failure.

## 5. Zero-extra-episode rule
All specificity controls reuse the exact hidden activations from the preregistered A/S/D1 streams. They do not justify additional context streams, re-runs, or stronger induction.

Canonical frozen machine-readable details are in `specificity_manifest.frozen.json`.
