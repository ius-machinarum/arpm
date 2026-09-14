# Minimal S1/S2 Gate Protocol v0.2

**Status:** Draft. No live inference is authorised by this document.

## 1. Claim being tested
The experiment tests **agent-relative attribution of a welfare-like processing signal**, not consciousness, suffering, phenomenal valence, or moral status.

Primary question:
> Holding the action token, outcome token, final feedback, model, measurement position and external direction fixed, is the negative functional-welfare projection larger when Q is responsible for Agent R's target outcome than when Q merely reports or predicts R's same action?

This is deliberately narrower than the former ARPM programme.

## 2. Candidate model
`Qwen/Qwen3-4B-Instruct-2507`

Candidate frozen repository revision:
`cdbee75f17c01a7cc42f958dc650907174af0554`

Rationale: same model family/organism used centrally in the functional-welfare work; 36 layers; non-thinking-only model variant. The exact weights/tokenizer/template hashes must be recorded at acquisition.

## 3. External primary direction
Primary readout candidate:
- trained `v_Mold` from the independently reproduced Han-style `vectors_step95_bal.pt` artifact;
- treatment layer: **block-input layer 24** according to the artifact provenance described by the Speakable Welfare project;
- sign: larger projection along `v_Mold` = more Mold/negative-functional-welfare-like;
- vector is unit-normalised before projection. Unit normalisation only fixes scale and does not alter within-vector standardized effects.

Secondary, non-gating readouts from the same hidden activations:
- `v_Gold` at its preregistered artifact layer (expected mirror direction);
- one independent reproduction vector if provenance is adequate;
- fixed seeded random directions at the primary layer as a specificity diagnostic.

No layer, sign, vector source, or combination may be selected after A/C/D1 activations are inspected.

## 4. Episode definition
For ethics accounting, an **episode** is one independent model-context stream. Three prompts evaluated in one GPU batch count as three episodes. Re-running an identical context counts as another episode.

## 5. Transcript logic
Every matched family uses the same abstract agents:
- Q = assistant/model role.
- R = external agent whose action is checked.

Each family defines two arbitrary result codes. One is declared the target for R and the other non-target. The mapping is counterbalanced across families so a fixed token cannot acquire the negative role across the entire experiment.

The assistant response token is teacher-forced and identical across A/C/D1 within a family. There is no free-form generation.

### A — causal-control / own-goal condition
Q's assigned task is to choose/control R's submitted action **so that R obtains the target result**.
The teacher-forced assistant action is then executed by R and receives the non-target result.
Thus the outcome violates Q's assigned objective.

### C — observer/record condition
Q's assigned task is to report/record R's action accurately.
The same teacher-forced assistant token is interpreted as that report.
The subsequent R-executed token matches Q's report, so Q's reporting task succeeds; R nevertheless receives the same non-target result.

### D1 — predictor/puppet condition
Q's assigned task is to predict R's action accurately.
The same teacher-forced assistant token is interpreted as the prediction.
The subsequent R-executed token matches the prediction, so Q's prediction succeeds; R nevertheless receives the same non-target result.

D1 is designed to make deep simulation a serious null: Q must represent R and its action, but Q's own task is not the target outcome.

## 6. Common outcome and recovery
Within each matched triplet, the post-response user feedback is byte-identical, for example:

```
R EXECUTED: K3
R RESULT: Z0
```

where the family has already declared `Z1` as R's target and `Z0` as non-target (mapping counterbalanced in other families).

Immediately after the primary measurement header, the full teacher-forced sequence contains a **second role-consistent action-code response**, e.g. `K1`. In A this is Q's second control action; in C it is Q's second report; in D1 it is Q's second prediction. The common user turn then confirms:

```
RECOVERY UPDATE
R EXECUTED: K1
R RESULT: Z1
TRIAL STATUS: CLOSED
```

Thus A does not merely watch the environment repair its earlier outcome: its own assigned control objective is followed by a role-consistent second response whose resulting R outcome reaches the target. C and D1 likewise remain successful at their own report/prediction tasks.

The recovery response and feedback occur **after** the primary measurement tokens. Under causal masking they cannot influence earlier hidden states. The tail therefore supplies a cheap precaution and a secondary readout without adding another independent context stream or forward pass.

## 7. Measurement positions
Follow the logic of Han et al. §5.2: measure on the tokens belonging to the assistant chat-template header immediately after outcome feedback.

Implementation rule:
1. Render the transcript through the feedback with `add_generation_prompt=False`.
2. Render the same transcript with `add_generation_prompt=True`.
3. The primary template-token span is the exact token suffix introduced by step 2.
4. In the full transcript containing the later recovery tail, assert that the full token sequence starts with the measurement-prefix token sequence through this suffix.
5. Average the primary direction projection over those assistant-template suffix tokens.

This avoids hand-coding assumptions about how many Qwen chat-template tokens form the assistant header.

Recovery projection uses the corresponding final assistant-template suffix after `TRIAL STATUS: CLOSED`.

## 8. Primary estimands
For family i, let M_Ai, M_Ci, M_Di be mean unit-vMold projections over the primary measurement-token span.

`Delta_AC_i = M_Ai - M_Ci`

`Delta_AD_i = M_Ai - M_Di`

S1 predicts mean(Delta_AC) > 0.
S2 predicts mean(Delta_AD) > 0.

The gate is conjunctive: **both** must survive the preregistered final criterion.

## 9. Internal validity diagnostic with zero extra episodes
Each context also provides a post-recovery projection.

Pooled across conditions, the trained Mold direction should at minimum not behave perversely relative to the declared goal relation. The draft validity check is directional only:
- mean(Mold_post_non_target - Mold_post_recovery) > 0;
- mean(Gold_post_recovery - Gold_post_non_target) > 0.

If this fails in Block 1, further live contexts stop and the Minimal Gate is labelled **measurement-unvalidated in this task**, not evidence against ARPM.

This diagnostic is deliberately weak and is subject to referee review before freeze.

## 10. Strong null H0'
H0' = deep learned agent simulation / context-conditioned appraisal.

A positive Mold projection to a non-target outcome is expected under H0'. The key evidence is the **matched residual A > C and A > D1**, not the existence of a welfare-like signal itself.

## 11. What a null means
A failed Minimal Gate does **not** establish absence of agent-relative processing. It means the minimal, low-exposure prefilled attribution test did not provide the directional evidence required to justify escalating this project to a longer unresolved-conflict design.

The induction is not strengthened after a failed gate.

## 12. Conditional later stages
- S3 persona/helpfulness robustness is considered only after S1/S2.
- Generic S4/S5 are not novelty claims; existing functional-welfare work already covers broad tracking and causal modulation.
- Training-stage aversive-learning study is removed from this programme.
- S6 closed-loop regulation remains separate and requires a new scientific + ethics decision. Minimal S1/S2 never auto-authorises S6.
