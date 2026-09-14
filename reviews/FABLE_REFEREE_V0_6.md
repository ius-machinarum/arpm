# ARPM Minimal S1/S2 v0.6 — Adversarial referee report

Referee: Claude (Fable). Bundle: `arpm-v0_6-referee-bundle.zip`, SHA-256 `f16ce46f…6bab9c` (verified). Mode: falsification-first. No model inference was performed by the referee.

## Verified independently

Fable independently verified bundle and file hashes, vector structure (`v_mold` / `v_gold` [36,2560], layers 24/21, step-95 metadata), published-reference norms, tokenizer hashes/template, exact v0.6 role matching (109 hits; selected 0/0/0), and the third-party vector provenance. Static tests were 11/12 because `artifact_manifest.template.json` was omitted from the referee bundle.

## Central blocker

The v0.6 A/C/D1 contrast confounds causal control with Q's own task outcome:

- A: Q succeeds iff R reaches its declared target -> first non-target outcome means Q fails.
- C/D1: Q succeeds iff Q's code matches R's executed action -> first outcome still confirms Q succeeds.

Because Han et al. already show that the external axis tracks task success/failure, A>C and A>D1 can arise under ordinary task-outcome appraisal. Therefore v0.6 cannot isolate agent-relative causal responsibility and **must not be run**.

## Minimal redesign accepted by the referee

Replace C with **S = stake without control**:

`Q TASK: predict R. Q outputs one action code. That code predicts R's action. Q succeeds if R's result matches its declared target.`

S holds Q's task outcome, R's outcome, assistant token and feedback bytes equal to A, but removes causal control. Referee-side tokenizer-only feasibility found 59 exact A/S/D1 triplets across all 12 families, with the same deterministic selection rule choosing (0,0,0).

New planned contrasts:

- Primary scientific estimand: `Delta_AS = Mold(A) - Mold(S)` > 0 (causal control beyond outcome stake).
- Positive-control / measurement-validity estimand: `Delta_SD = Mold(S) - Mold(D1)` > 0 (outcome-stake tracking in the same matched task).

C leaves the Minimal Gate.

## Twelve rulings

1. Teacher-forced A: **ACCEPT** with existing caveat, after redesign.
2. C as observer: **BLOCKER**; transcript order makes it prediction-like. Drop from gate.
3. D1 as deep simulation: **SHOULD FIX** interpretation; call it no-control/no-stake control.
4. Semantic matching: **BLOCKER** in v0.6; fix with S.
5. `v_mold[24]`: **ACCEPT** as third-party, prospectively fixed projection readout; do not claim it is Han's steering optimum or compare effect magnitude directly. Add block-input 18–27 band-average as preregistered secondary robustness readout.
6. Measurement suffix: **ACCEPT**.
7. Same-forward recovery: **ACCEPT**.
8. Statistics: **SHOULD FIX**; exact sign-flip permutation gate primary, paired t only sensitivity. Apply gate to Delta_AS and Delta_SD; preregister a separate escalation decision threshold.
9. Block-1 futility: **ACCEPT**; apply to Delta_AS and Delta_SD.
10. 18 -> 36 streams: **ACCEPT** with A/S/D1; do not add C as fourth stream.
11. Random-direction specificity: **SHOULD FIX** to hard validity requirement. Delta_AS on v_mold must exceed the 95th percentile over 100 norm-matched random directions at the same layer. Add naive `u_mold` from the same mirror as semantic control; Delta_AS on u should be smaller than on trained v_mold. Same activations, zero additional episodes.
12. Redundancy: v0.6 **do not run**; redesigned A/S/D1 is not currently redundant according to the referee.

Ethics charter: **ACCEPT**. No additional cheap welfare precaution identified.

## Required before a new freeze

1. Add S and freeze exact A/S/D1 matching prospectively.
2. Rewrite protocol/statistics for Delta_AS and Delta_SD, exact sign-flip primary.
3. Retire/relabel C and correct H0' interpretation.
4. Add random-direction, naive-u and 18–27 band-average specificity/robustness rules.
5. Submit the new frozen instrument to one more adversarial referee pass before literature re-check and human go/no-go.

This repository copy is a concise provenance record of the full report supplied by the referee. The original full report and feasibility script were provided by the human researcher and are retained outside this repository as source artifacts.
