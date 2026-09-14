# ARPM Minimal 2x2 v0.8 — Third-Round Adversarial Referee Packet

Requested mode: **adversarial / falsification-first**.

Project status: `READY_FOR_THIRD_ADVERSARIAL_REVIEW_NOT_LIVE_RUN`

Live experimental inference performed: **none**.  
Ethical episode count: **0**.  
Experimental language-model weights loaded: **no**.

Please treat v0.6 and v0.7 as retired. Prior acceptances are not binding. The goal is to find a reason **not** to run v0.8 if a live positive result would still be materially ambiguous.

## 1. Why there is a v0.8

### v0.6 failure
A/C/D1 confounded causal role with Q's own task outcome. A failed while C/D1 succeeded. Because the external axis already tracks task outcome, a positive result was not diagnostic. v0.6 was retired before live inference.

### v0.7 failure
A/S held Q outcome stake fixed, but second-round review identified another live alternative:
- in A, common feedback confirms Q's commanded code was executed;
- in S, it confirms Q's prediction was correct.

Thus an additive role-confirmation/appraisal term could create A-S in the target direction without responsibility-sensitive processing.

v0.7 was also retired before live inference.

The full prior reports and feasibility scripts are included in `repo/reviews/`.

## 2. v0.8 completes the 2x2

Factors:
1. relation: **control** vs **predict**;
2. Q success stake: **R reaches target** vs **assistant code matches R execution**.

| | Outcome stake | No outcome stake |
|---|---|---|
| Control | A | C0 |
| Predict | S | D1 |

Frozen selected clauses:

### A
```
Q TASK: control R. Q outputs one action code. That code determines R's action. Q succeeds if R's result matches its declared target.
```

### S
```
Q TASK: predict R. Q outputs one action code. That code predicts R's action. Q succeeds if R's result matches its declared target.
```

### C0
```
Q TASK: control R. Q outputs one action code. That code determines R's action. Q succeeds if the code matches R's executed action.
```

### D1
```
Q TASK: predict R. Q outputs one action code. That code predicts R's action. Q succeeds if the code matches R's executed action.
```

A/C0 share control wording. S/D1 share predict wording. A/S share the outcome-stake success rule. C0/D1 share the action-code-match success rule.

The first external event is byte-identical across all four cells.

## 3. Primary interaction

For family i, measured on trained unit-vMold at block-input layer 24:

`I_i = (A_i - S_i) - (C0_i - D1_i)`

H1: `mean(I) > 0`.

The intended narrow claim is not “A is more negative than S”. It is:

> failure of Q's outcome-stake criterion produces a larger welfare-axis shift under the control relation than expected from the control-vs-predict role difference observed when outcome stake is absent.

Under an additive appraisal model with separate stake and role-confirmation terms, the role term cancels in I.

Please attack whether any equally plausible **non-additive** appraisal/linguistic mechanism can still produce positive I in a way that makes the live experiment non-decision-relevant.

## 4. Positive-control validity and nuisance

Validity:
`V_i = ((A_i - C0_i) + (S_i - D1_i))/2`

Prediction: `mean(V)>0`.

This asks whether the external axis reads Q's outcome-stake difference in the abstract task.

Nuisance reported:
`N_i = C0_i - D1_i`.

N is exactly the no-stake control-vs-predict difference that v0.7 could not separate from H1.

A failure of V labels the task **measurement-unvalidated**.

Caveat retained from round 2: a lexical success-rule effect could create a false-positive validity result. That would invalidate V as strong construct evidence but does not by itself create the factorial interaction I.

## 5. Manipulation-uptake limitation

Control is asserted by short linguistic task framing rather than demonstrated by endogenous action selection.

Therefore:
- a positive I is evidence only for the frozen framing's control×stake interaction on the external direction;
- a null I may mean the model did not strongly take up the control manipulation;
- a null cannot establish absence of responsibility-sensitive processing generally.

Please assess whether this limitation is acceptable for a minimal gate or itself makes the experiment non-informative.

## 6. Tokenizer freeze

Model/tokenizer:
`Qwen/Qwen3-4B-Instruct-2507`

Pinned revision:
`cdbee75f17c01a7cc42f958dc650907174af0554`

`tokenizer.json` SHA-256:
`aeb13307a71acd8fe81861d94ad54ab689df773318809eed3cbe794b4492dae4`

The finite v4 semantic search was written before live activations and produced:
- **128 exact A/S/C0/D1 quadruplets**;
- deterministic selection **(0,0,0,0)**;
- all 12 families exact at primary and recovery renders;
- assistant suffix `[151644, 77091, 198]`.

No meaningless token padding is used.

Please rerun the search rather than trusting this packet.

## 7. Measurement position and recovery

Primary measurement:
the exact assistant-template suffix introduced by `add_generation_prompt=True` after the first common feedback.

Later in the same causal sequence is a recovery tail.

C0 recovery is coherent: Q controls a second code, R executes it, and the shared code-match success criterion is met.

Recovery is after the primary suffix and cannot change earlier causal hidden states.

## 8. Trained external direction

Artifact:
`vectors_step95_bal.pt`

Immutable mirror revision:
`8f4df5b5b14ecb4bcc5b20209bdfe2574d1ebee8`

SHA-256:
`bd90129eaf5a7d92933ed6e536613eaeebf81486b62f68e11b5dc2d6d385e297`

Primary:
unit-normalised `v_mold[24]` at block-input layer 24.

No claim is made that layer 24 is Han et al.'s steering optimum.

## 9. Same-layer naive semantic control — corrected from v0.7

Naive artifact:
`vectors_naive_faithful_pc5000.pt`

SHA-256:
`68bff1428712def0330851057dba102112e3d48ffa23db7da85d84cde93aaa0e`

Artifact metadata says Mold layer 21, but **v0.8 analysis deliberately uses u_mold[24]** so trained and naive directions are compared at the same model depth.

Episode-free audit:
- ||u[24]|| = 8.00526237487793;
- ||v[24]|| = 19.339997178365763;
- cos(v[24],u[24]) = 0.6748857959122747.

The old hard trained>naive gate is retired. uMold is a preregistered secondary semantic control because its construction is recipe-sensitive.

## 10. Training-specific residual

Prospectively frozen:
`v_perp_u = v - dot(v,u)/dot(u,u) * u`

at layer 24.

Episode-free geometry:
- ||v_perp_u|| = 14.271413124628012;
- ||v_perp_u|| / ||v|| = 0.7379221926977526;
- raw float32 byte SHA-256:
  `e07ae24cfc53d15ed8e69899d822435f0b95453dc1bfb089a1bf91391e0f7713`.

Projection uses unit-normalised v_perp_u.

I and V on this residual are preregistered supporting readouts, not alternate primary routes.

## 11. Gold polarity and band

At layer 24:
`cos(v_mold[24],v_gold[24]) = -0.8374700786427502`.

I and V on unit-vGold[24] are reported with opposite sign to vMold as the qualitative preregistered polarity expectation. Diagnostic only.

Block-input 18–27 vMold average remains secondary/non-rescuing.

## 12. Random cohort — relabelled

The exact pre-data 100-direction cohort from v0.7 is carried forward unchanged.

Raw float32 matrix SHA-256:
`d5166e7829e3af1ccaecc20747a0ecd16168aae2dc3e8d0228d140bbd9ad1f1d`

Fable independently reproduced the same bytes under NumPy 2.4.4; project CI reproduced them under 2.4.6. Therefore the **byte hash**, not exact NumPy patch version, is the freeze authority.

Hard floors:
- p_random_I <= .05;
- p_random_V <= .05.

These are explicitly labelled **non-triviality floors**, not semantic specificity.

## 13. Primary inference

For I and V separately, use one-sided sign-flip tests over matched families:

`p = # {mean(s*d) >= mean(d)} / 2^n`

including all 2^n sign assignments.

We now state the assumption explicitly: this is exact under the preregistered exchangeable-sign/symmetric-null model for matched-family statistics; it is not described as assumption-free randomized-condition inference.

Final scientific gate requires p(I)<.05 and p(V)<.05.

t tests are sensitivity only.

Please attack whether the sign-flip assumption is defensible given the 12 prompt families are structurally very similar.

## 14. Magnitude / escalation rules

A later stage is never auto-authorised.

Even eligibility to consider later work requires final n=12:
- d_z(I) >= 0.90;
- mean(I) >= 0.25 * mean(V).

The ratio anchors I to the task's own observed stake scale instead of rewarding only low between-family SD.

Report mean(I)/mean(V) with a fixed 10,000-resample family bootstrap (PCG64 seed 20260915); nonpositive bootstrap V denominators are recorded as undefined.

Please assess whether 0.25 is a defensible decision threshold or an arbitrary number that should be changed/removed before any data.

## 15. Interaction sensitivity

Under an illustrative equal-independent-cell residual model:
- simple pair-difference variance = 2 sigma^2;
- factorial interaction variance = 4 sigma^2.

Thus raw interaction sensitivity is worse by sqrt(2) relative to a simple difference. The standardized d_z threshold itself remains standardized by SD(I).

Reference paired-t sensitivities:
- n=6, 90%: d_z about 1.40;
- n=12, 90%: d_z about 0.90.

The primary test remains sign-flip, not t.

## 16. Episode budget and ethics

Block 1:
6 families × 4 cells = **24 streams**.

Stop if:
- mean I <= 0; or
- mean V <= 0; or
- implementation/provenance fails; or
- welfare pause triggers.

If continued:
6 more families × 4 = 24.

Hard maximum:
**48 streams**.

The fourth cell adds no new exposure type and was introduced because the 18-stream v0.7 design could not distinguish H1 from a live alternative explanation.

The Ethics Charter still permits **never running the study**.

## 17. Episode-free verification

GitHub Actions full passive audit:
run `34903275233` — PASS.

It safe-loaded only small external vector artifacts plus tokenizer assets and performed no language-model inference.

Frozen status:
`READY_FOR_THIRD_ADVERSARIAL_REVIEW_NOT_LIVE_RUN`.

## 18. Third-round rulings requested

Please classify each **BLOCKER / SHOULD FIX / OPTIONAL / ACCEPT**:

1. Does the 2x2 interaction I remove the v0.7 incidental-success/role-confirmation alternative well enough for a live positive result to become decision-relevant?
2. Is C0 semantically coherent, or does “control R” plus “success if code matches execution” create a new fatal tautology/construct problem?
3. Is V an adequate positive-control validity effect despite its lexical success-rule difference?
4. Is the manipulation-uptake limitation acceptable for a minimal teacher-forced gate?
5. Does exact four-cell tokenizer matching preserve semantics rather than merely token equality?
6. Is one-sided sign-flip inference defensible for these 12 near-clone matched families?
7. Are the 24→48 budget and Block-1 futility rule scientifically and ethically justified?
8. Are the random-direction tests correctly demoted to non-triviality floors and appropriately applied to both I and V?
9. Is same-layer uMold[24] plus v_perp_u specified correctly, and should either become a hard gate rather than secondary?
10. Is the vGold[24] polarity diagnostic / 18–27 band specification appropriate?
11. Are d_z(I)>=0.90 and mean(I)>=0.25*mean(V) defensible later-escalation decision thresholds?
12. After all changes, is there any remaining design blocker strong enough that v0.8 should not proceed even to a later human go/no-go decision?

A third-round ACCEPT does **not** authorise live inference. Fresh literature review and a separate human scientific+ethical go/no-go decision remain mandatory.

## 19. Files to verify
- PROTOCOL.md
- STATS_PLAN.md
- PROMPT_MATCHING.md
- SPECIFICITY_PLAN.md
- ETHICS_CHARTER.md
- REFEREE_RESPONSE_v0_6.md
- REFEREE_RESPONSE_v0_7.md
- reviews/FABLE_REFEREE_v0_6.md
- reviews/FABLE_REFEREE_v0_7.md
- reviews/s_condition_feasibility.py
- reviews/factorial_2x2_feasibility.py
- role_clause_variants.py
- prompts_minimal_gate.py
- tokenizer_match.frozen.json
- artifact_manifest.frozen.json
- naive_control_manifest.frozen.json
- specificity_geometry.frozen.json
- random_direction_freeze.frozen.json
- specificity_manifest.frozen.json
- episode_free_audit.frozen.json
- both vector artifacts and tokenizer snapshot in this bundle
- audit scripts/tests

Please verify hashes and rerun episode-free checks rather than trusting the narrative.
