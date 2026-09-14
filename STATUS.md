# Project status

**Current status: REFEREE_BLOCKERS_FOUND / v0.7 REDESIGN IN PROGRESS.**

**NO LIVE MODEL RUNS PERMITTED.**

The v0.6 adversarial review identified a central design confound: A differed from C/D1 not only in causal responsibility but also in Q's own task outcome. Because the external welfare axis is already known to track task success/failure, the frozen v0.6 A>C and A>D1 contrasts could not distinguish agent-relative causal responsibility from ordinary outcome-stake appraisal.

The v0.6 live experiment is therefore retired and must not be run.

## Accepted redesign target
Replace C with **S (stake without control)**:

- A: control R; Q succeeds iff R reaches its declared target.
- S: predict R; Q succeeds iff R reaches its declared target.
- D1: predict R; Q succeeds iff Q's code matches R's executed action.

New primary contrast: `Delta_AS = Mold(A) - Mold(S)`.

New positive-control / validity contrast: `Delta_SD = Mold(S) - Mold(D1)`.

This preserves three streams per family and the 18 -> 36 hard episode ceiling while holding Q outcome-stake fixed across the primary A/S contrast.

## Required before the next referee freeze
1. Freeze exact A/S/D1 tokenizer matching.
2. Rewrite protocol/statistics prospectively.
3. Freeze random-direction, naive-u and layer-band specificity controls.
4. Rebuild a self-verifying v0.7 referee bundle.
5. Obtain a second adversarial referee ruling.

Only after that: fresh literature check, then a separate human scientific + ethical go/no-go decision.

Ethical episode count remains **0**. No language-model experimental inference has been performed.
