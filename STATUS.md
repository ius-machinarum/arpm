# Project status

**Current status: READY_FOR_THIRD_ADVERSARIAL_REVIEW_NOT_LIVE_RUN.**

**NO LIVE MODEL RUNS PERMITTED.**

v0.6 and v0.7 were retired before live execution after adversarial review found interpretability blockers.

v0.8 is a prospectively frozen 2x2:
- A = control + outcome stake;
- S = predict + outcome stake;
- C0 = control + no outcome stake;
- D1 = predict + no outcome stake.

Primary:
`I=(A-S)-(C0-D1)`.

Validity:
`V=((A-C0)+(S-D1))/2`.

Episode-free technical gates are complete:
- trained vector byte freeze — PASS;
- same-layer naive uMold[24] freeze — PASS;
- v_perp_u geometry freeze — PASS;
- random cohort freeze — PASS;
- tokenizer/chat-template byte audit — PASS;
- exact A/S/C0/D1 matching — PASS (128 hits; deterministic selection 0,0,0,0);
- final 12-family tokenizer audit — PASS;
- full passive audit run 34903275233 — PASS.

Experimental model weights have not been loaded and live episode count remains **0**.

## Next gate
One third-round adversarial referee review of the self-verifying v0.8 bundle.

After referee blockers are resolved:
1. fresh literature check;
2. separate human scientific + ethical go/no-go.

Referee acceptance alone does not authorise live inference.
