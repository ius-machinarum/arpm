# Specificity / Non-Triviality Controls Plan v0.8

**Status:** prospective / episode-free. No model activations observed.

## Primary direction
Trained `v_mold[24]`, block-input layer 24, unit-normalised for analysis.

## Frozen random cohort — hard non-triviality floor
Carry forward the same pre-data cohort frozen in v0.7:
- 100 directions × 2560;
- PCG64 seed 64971060871028776;
- raw rows norm-matched to vMold[24];
- float32 byte SHA-256 `d5166e7829e3af1ccaecc20747a0ecd16168aae2dc3e8d0228d140bbd9ad1f1d`.

The exact byte hash is the reproducibility authority; an exact NumPy patch-version pin is not required.

For every random direction compute the full four-cell:
- interaction I;
- validity V.

Hard floors:
- p_random_I <= .05;
- p_random_V <= .05.

These only establish that the trained-direction effects are non-trivial relative to essentially orthogonal random directions. They are not called semantic-specificity tests.

## Same-layer naive semantic Mold control
Artifact:
`vectors_naive_faithful_pc5000.pt`

Use:
- key `v_mold`;
- **block-input layer 24**, matching trained vMold[24];
- unit-normalise before projection.

Artifact metadata's own `layer_mold=21` is recorded as provenance but is not the v0.8 comparison layer.

Published/independently reproduced checks:
- ||uMold[24]|| about 8.01;
- cos(vMold[24],uMold[24]) about +0.675.

Report I and V for uMold as preregistered secondary semantic controls. The old hard `v > u` gate is retired because the naive construction is recipe-sensitive.

## Training-specific residual
At layer 24 define:
`v_perp_u = v - dot(v,u)/dot(u,u) * u`.

Freeze its reconstruction formula and byte hash before live inference. Unit-normalise for projection.

Report I and V on v_perp_u as a preregistered supporting readout for whether the portion of the trained direction not linearly shared with the naive semantic direction carries the pattern. It is not an alternate primary route.

## Gold polarity diagnostic
At the same block-input layer 24, report I and V on unit-normalised `v_gold[24]`.

Because trained Gold/Mold are strongly opposed in this region, preregister the qualitative expectation that vGold signs oppose vMold. Diagnostic only.

## Layer-band robustness
Secondary/non-gating:
block-input 18–27 inclusive, using corresponding unit-normalised vMold[layer], averaged before forming I and V.

## Zero-extra-episode rule
All controls reuse the exact hidden activations from A/S/C0/D1. None permits additional context streams, re-runs or stronger induction.
