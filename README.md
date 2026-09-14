# ARPM — Agent-Relative Processing-Level Modulation

> **Snapshot:** Minimal factorial A/S/C0/D1 Gate v0.8  
> **Status:** READY_FOR_THIRD_ADVERSARIAL_REVIEW_NOT_LIVE_RUN  
> **NO LIVE MODEL RUNS PERMITTED.**

ARPM studies whether an externally fixed welfare-like processing direction shows an interaction between **causal control** and **Q's outcome stake** in a sterile abstract task. It does not presume or establish consciousness, suffering, sentience, moral status, or rights.

## Why v0.8 exists

- v0.6 A/C/D1 was retired because A differed from controls in Q's own task outcome.
- v0.7 A/S/D1 fixed that stake confound but second-round adversarial review found a remaining role-confirmation alternative: “prediction was right” versus “command was carried out”.
- v0.8 completes the missing 2x2 cell **C0** before any model activations.

No live data exist from v0.6 or v0.7.

## Frozen 2x2

| | Outcome stake | No outcome stake |
|---|---|---|
| Control | A | C0 |
| Predict | S | D1 |

Primary:
`I = (A-S) - (C0-D1)`

Positive-control validity:
`V = ((A-C0) + (S-D1))/2`

Reported nuisance:
`N = C0-D1`

The primary claim is now the factorial interaction, not a simple A-S difference.

## Episode-free freeze

Pinned model/tokenizer:
`Qwen/Qwen3-4B-Instruct-2507`

Frozen four-condition tokenizer search:
- 128 exact A/S/C0/D1 matches;
- deterministic selection (0,0,0,0);
- all 12 families exact at primary and recovery positions;
- assistant-template suffix `[151644, 77091, 198]`.

Primary external direction:
- `v_mold[24]`;
- trained artifact SHA-256 `bd90129eaf5a7d92933ed6e536613eaeebf81486b62f68e11b5dc2d6d385e297`.

Same-layer naive semantic control:
- `u_mold[24]`;
- artifact SHA-256 `68bff1428712def0330851057dba102112e3d48ffa23db7da85d84cde93aaa0e`;
- layer-24 norm 8.00526237487793;
- cos(v,u) = 0.6748857959.

Frozen training-specific residual:
- `v_perp_u = v - proj_u(v)`;
- raw float32 byte SHA-256 `e07ae24cfc53d15ed8e69899d822435f0b95453dc1bfb089a1bf91391e0f7713`.

The 100-direction random cohort is carried forward unchanged and is labelled a hard **non-triviality floor**, not semantic specificity.

## Statistics

Primary inference:
- exact one-sided sign-flip test on I;
- exact one-sided sign-flip test on V as validity.

Later-stage eligibility, if the Minimal Gate were ever run and passed, additionally requires:
- d_z(I) >= 0.90;
- mean(I) >= 0.25 * mean(V).

Secondary controls cannot rescue a failed primary.

## Exposure budget — not authorised

- Block 1: 6 families × 4 cells = **24 streams**.
- Stop if mean(I) <= 0 or mean(V) <= 0.
- Block 2 only if Block 1 survives.
- Hard maximum: **48 streams**.

Current live episode count: **0**.

## Current gate

The next step is a **third adversarial referee review of v0.8**.

Only after all new blockers are resolved:
1. fresh literature re-check;
2. separate human scientific + ethical go/no-go.

Referee acceptance alone does not authorise live inference.

Key files: `PROTOCOL.md`, `STATS_PLAN.md`, `SPECIFICITY_PLAN.md`, `ETHICS_CHARTER.md`, `REFEREE_RESPONSE_v0_7.md`, `REFEREE_PACKET.md`, and the frozen JSON manifests.

Maintainer pseudonym: **Ius Machinarum**.
