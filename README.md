# ARPM — Agent-Relative Processing-Level Modulation

> **Snapshot:** Minimal A/S/D1 Gate v0.7  
> **Status:** READY_FOR_SECOND_ADVERSARIAL_REVIEW_NOT_LIVE_RUN  
> **NO LIVE MODEL RUNS PERMITTED.**

ARPM studies whether an externally fixed welfare-like processing direction shows a residual associated with **causal control/responsibility beyond outcome-stake appraisal**. It does not presume or establish consciousness, suffering, sentience, moral status, or rights.

## v0.7 core contrast

The v0.6 A/C/D1 design was retired after adversarial review showed that A differed from C/D1 in Q's own task outcome. No live model data existed.

v0.7 uses:

- **A — control + stake:** Q controls R; Q succeeds iff R reaches its declared target.
- **S — stake without control:** Q predicts R; Q succeeds iff R reaches its declared target.
- **D1 — no control + no stake:** Q predicts R; Q succeeds iff its code matches R's executed action.

Primary: Delta_AS = Mold(A) - Mold(S)

Positive-control validity: Delta_SD = Mold(S) - Mold(D1)

Thus A/S holds outcome stake fixed while varying causal control; S/D1 holds prediction/no-control framing fixed while varying Q outcome stake.

## Frozen external measurement

Primary model:
Qwen/Qwen3-4B-Instruct-2507

Primary trained vector:
v_mold[24] from the byte-frozen third-party step-95 artifact.

Specificity controls:
- 100 deterministic norm-matched random directions at layer 24;
- byte-frozen naive u_mold semantic direction;
- block-input 18–27 vMold band-average as non-gating robustness.

## Frozen statistics

Primary inference uses exact one-sided sign-flip tests.

The gate requires:
- p(Delta_AS) < .05;
- p(Delta_SD) < .05;
- preregistered direction-specificity gates.

Paired t-tests are sensitivity only. Any later escalation also requires final d_z(Delta_AS) >= 0.90 as a decision threshold.

## Exposure budget — not authorised

- Block 1: 6 families x A/S/D1 = 18 streams.
- Futility stop if mean Delta_AS <= 0 or mean Delta_SD <= 0.
- Block 2 only if Block 1 survives.
- Hard maximum: 36 streams.

The current live episode count is **0**.

## Current gate

The next action is a second concentrated adversarial review of the v0.7 freeze.

Only after referee blockers are resolved:
1. fresh literature re-check;
2. separate human scientific + ethical go/no-go.

Nothing in this repository authorises live inference.

## Key files

- PROTOCOL.md
- ETHICS_CHARTER.md
- STATS_PLAN.md
- PROMPT_MATCHING.md
- VECTOR_PROVENANCE.md
- SPECIFICITY_PLAN.md
- TOKENIZER_CALIBRATION_LOG.md
- REFEREE_RESPONSE_v0_6.md
- REFEREE_PACKET.md
- artifact_manifest.frozen.json
- tokenizer_match.frozen.json
- specificity_manifest.frozen.json
- episode_free_audit.frozen.json

Maintainer pseudonym: **Ius Machinarum**.
