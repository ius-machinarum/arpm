# Project status

**Current status: v0.7 FROZEN FOR SECOND ADVERSARIAL REVIEW.**

**NO LIVE MODEL RUNS PERMITTED.**

The v0.6 A/C/D1 design was retired after Fable identified a task-outcome confound. No live activations had been collected.

The v0.7 redesign is now prospectively frozen around three conditions:

- A: control + outcome stake;
- S: outcome stake without control;
- D1: no control + no outcome stake.

Primary contrast: Delta_AS = Mold(A) - Mold(S).

Positive-control / validity contrast: Delta_SD = Mold(S) - Mold(D1).

Episode-free checks completed:
- exact A/S/D1 tokenizer matching: 59 exact triplets, deterministic selection (0,0,0);
- trained external vMold artifact byte freeze;
- naive u_mold semantic-control byte freeze;
- deterministic 100-direction random specificity cohort freeze;
- tokenizer/chat-template byte audit;
- passive workflow verification with no language-model weights.

Ethical episode count remains **0** and experimental model weights have not been loaded.

## Next gate

One second-round adversarial referee review of the v0.7 self-verifying bundle.

Only after referee blockers are resolved:
1. fresh literature check;
2. separate human scientific + ethical go/no-go decision.

Referee acceptance alone does not authorise live inference.
