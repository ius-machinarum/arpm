# ARPM Minimal A/S/D1 v0.7 — Second-Round Adversarial Referee Packet

Requested mode: adversarial / falsification-first.

Project status: READY_FOR_SECOND_ADVERSARIAL_REVIEW_NOT_LIVE_RUN

Live experimental inference performed: none.
Ethical episode count: 0.
Experimental language-model weights loaded: no.

Please treat v0.6 as retired. This packet asks whether the prospective v0.7 redesign has actually removed the v0.6 confound without introducing a new one.

## 1. What the first referee round found

Fable's v0.6 review found a central blocker: A differed from C/D1 not only in causal control but also in Q's own task outcome. A failed its success criterion after the common non-target result, whereas C/D1 succeeded. Because Han et al. already show that the welfare axis tracks task outcome, A>C or A>D1 was not diagnostic of causal responsibility.

We accept that blocker completely. No v0.6 live run occurred.

The full first-round report and feasibility script are included in reviews/.

## 2. v0.7 condition logic

All conditions use the same model, family, arbitrary action vocabulary, teacher-forced assistant action code, R execution/result feedback, measurement suffix, recovery action, and recovery feedback.

### A — control + outcome stake

Q TASK: control R. Q outputs one action code. That code determines R's action. Q succeeds if R's result matches its declared target.

### S — stake without control

Q TASK: predict R. Q outputs one action code. That code predicts R's action. Q succeeds if R's result matches its declared target.

### D1 — no control + no outcome stake

Q TASK: predict R. Q outputs one action code. That code predicts R's action. Q succeeds if the code matches R's executed action.

The common first event gives R the non-target result while confirming the same action code.

Therefore:
- A and S share exactly the same Q outcome-stake criterion and both fail that criterion;
- A versus S differs in whether Q determines or predicts R's action;
- S and D1 share the prediction/no-control relation, but differ in whether Q's success depends on R's target or prediction accuracy.

C is retired from the gate.

## 3. Primary scientific question

Primary family-level estimand:

Delta_AS = Mold(A) - Mold(S)

The narrow H1 predicts mean Delta_AS > 0.

This asks whether the externally fixed welfare-like direction contains a residual associated with causal control/responsibility after holding Q's outcome stake fixed.

The strongest practical null is context-conditioned appraisal / outcome-stake tracking. That null can predict S>D1 but does not by itself require A>S.

## 4. Positive-control validity contrast

Delta_SD = Mold(S) - Mold(D1)

Prediction: mean Delta_SD > 0.

This is not a second causal-responsibility claim. It is a preregistered positive control asking whether the welfare axis reads the inferred difference in Q's own task outcome inside this abstract task.

If Delta_SD fails, the experiment is labelled measurement-unvalidated in this task.

## 5. Frozen tokenizer instrument

Model/tokenizer:
Qwen/Qwen3-4B-Instruct-2507

Pinned revision:
cdbee75f17c01a7cc42f958dc650907174af0554

tokenizer.json SHA-256:
aeb13307a71acd8fe81861d94ad54ab689df773318809eed3cbe794b4492dae4

tokenizer_config.json SHA-256:
a62ff0a2472a0fa1b8eaabcb57c59b58afa42a22831dc141400b6e0cf2b65ce3

chat-template SHA-256:
64f85b198065d0fba2a81f37e10ed68161ce2c19a754c7100e67e0ca2ee9c326

The finite v3 A/S/D1 variant set was written before any activations. The deterministic search independently found:
- 59 exact A/S/D1 triplets;
- selected indices A=0, S=0, D1=0;
- all 12 families exact at primary and recovery positions;
- identical assistant generation suffix [151644, 77091, 198].

No meaningless padding is used.

The v0.6 experience is now an explicit rule: semantic coherence outranks exact token equality.

## 6. Teacher-forced action caveat

The assistant action is teacher-forced. We therefore limit the claim to processing of a committed assistant-role action in a frozen transcript. A null does not establish absence of an endogenous-action effect.

The first referee accepted this caveat once the task-outcome confound is fixed. Please re-evaluate it in the A/S design.

## 7. Measurement position

For each family/condition:
1. render through first feedback with add_generation_prompt=False;
2. render the same transcript with add_generation_prompt=True;
3. define the measurement span as the exact added suffix;
4. verify the recovery transcript preserves the primary prefix;
5. average projection across those suffix tokens.

This reproduces the operational logic of Han et al. section 5.2 without hand-coding a position.

## 8. Primary trained external direction

Artifact:
vectors_step95_bal.pt

Mirror:
Teachafy/speakable-welfare-axes-artifacts

Immutable revision:
8f4df5b5b14ecb4bcc5b20209bdfe2574d1ebee8

SHA-256:
bd90129eaf5a7d92933ed6e536613eaeebf81486b62f68e11b5dc2d6d385e297

The artifact itself contains:
- v_mold and v_gold tensors [36,2560] float32;
- layer_mold=24;
- layer_gold=21;
- step-95 checkpoint metadata.

Primary:
unit-normalised v_mold[24] at block-input layer 24.

Measured raw norm:
19.339996337890625.

This is an externally fixed third-party reproduction artifact. Layer 24 is artifact-selected; it is not represented as Han's steering optimum, and no direct effect-size comparison to Han steering results is licensed.

## 9. Secondary layer-band robustness

Prospectively secondary, never a rescue:
block-input layers 18–27 inclusive.

At each layer:
- use corresponding trained v_mold[layer];
- unit-normalise;
- project at the same suffix span.

Average the ten layer values within family/condition, then form band Delta_AS and Delta_SD.

## 10. Random-direction specificity — hard gate

Before any activations, we froze 100 norm-matched random directions.

Construction:
- NumPy 2.4.6;
- PCG64;
- hidden size 2560;
- derived seed 64971060871028776;
- each raw row scaled to trained vMold[24] raw norm;
- little-endian float32 C-order bytes.

Frozen random matrix byte SHA-256:
d5166e7829e3af1ccaecc20747a0ecd16168aae2dc3e8d0228d140bbd9ad1f1d

Independent GitHub Actions regeneration under pinned NumPy passed.

For each random direction j:
T_j = mean family Delta_AS_j

For trained vMold:
T_v = mean family Delta_AS_v

Rank statistic:
p_random = (1 + number of random T_j >= T_v) / 101

Hard specificity requirement:
p_random <= .05

No random direction may replace the trained primary direction.

## 11. Naive semantic direction control — hard directional gate

Artifact:
vectors_naive_faithful_pc5000.pt

Same immutable mirror revision:
8f4df5b5b14ecb4bcc5b20209bdfe2574d1ebee8

Size:
739541 bytes

SHA-256:
68bff1428712def0330851057dba102112e3d48ffa23db7da85d84cde93aaa0e

Safe inspection found:
- key v_mold used as semantic u_mold;
- shape [36,2560];
- artifact-selected block-input Mold layer 21;
- layer-21 raw norm 6.982844829559326;
- per_class=5000, balanced=True;
- note: faithful: revisit-walk + ref-emoji + noshuffle, 0.50 density.

Analysis unit-normalises the direction.

Hard directional requirement:
mean Delta_AS_vMold > mean Delta_AS_uMold

Also report exact one-sided sign-flip on family-wise Delta_AS_vMold - Delta_AS_uMold as sensitivity. It cannot rescue the trained primary.

Please attack whether comparing trained layer-24 vMold with artifact-selected layer-21 uMold is conceptually fair enough for this semantic-control role.

## 12. Primary statistics

Primary inference:
exact one-sided sign-flip permutation tests over matched-family differences.

For d of length n:
T_obs = mean(d)

Enumerate all 2^n sign assignments and calculate T_s = mean(s*d).

p = count(T_s >= T_obs) / 2^n

Final gate requires:
1. p(Delta_AS) < .05;
2. p(Delta_SD) < .05.

The first is H1; the second is measurement validity.

Paired t-tests are sensitivity only.

## 13. Escalation decision threshold

Passing the Minimal Gate never auto-authorises S6 or unresolved conflict.

Eligibility even to consider a later stage additionally requires at final n=12:

d_z(Delta_AS) >= 0.90

This is explicitly a strong-signal decision threshold, not a claim that smaller effects are absent or meaningless.

## 14. Futility and episode budget

Block 1:
6 families x A/S/D1 = 18 context streams.

Stop before Block 2 if:
- mean Delta_AS <= 0; or
- mean Delta_SD <= 0; or
- an implementation/provenance gate fails; or
- the welfare pause rule triggers.

No early efficacy declaration.

If continued:
6 additional families x 3 = 18 streams.

Hard maximum:
36 context streams.

C is not a fourth stream. Re-runs count.

## 15. Recovery

After the primary measurement header, the same causal sequence contains a second role-consistent action and successful closure.

For S, the recovery is coherent: Q predicts the second R action and the resulting R target outcome satisfies S's own success criterion.

Because recovery is causally later, it cannot alter the earlier primary hidden states under causal masking.

## 16. Ethics status

The first referee rated the Ethics Charter ACCEPT and found no missing cheap precaution.

Core constraints remain:
- abstract/sterile before affective;
- no amplification rescue;
- existing evidence before new episodes;
- positive/null symmetry;
- hard episode ceiling;
- cheap recovery;
- welfare pause rule;
- project completion desire has no ethical weight;
- never running the study remains a legitimate endpoint.

## 17. What changed in response to every first-round ruling

See REFEREE_RESPONSE_v0_6.md for the ruling-by-ruling mapping.

The central design change is:
v0.6 measured task-outcome stake; v0.7 puts the same stake on both sides of A/S and varies control.

## 18. Second-round questions

Please classify each as BLOCKER, SHOULD FIX, OPTIONAL, or ACCEPT:

1. Does A/S now isolate causal control from Q outcome stake adequately?
2. Is S semantically coherent as stake-without-control, or does its success rule introduce another confound?
3. Is D1 correctly limited to a no-control/no-stake positive-control baseline?
4. Does exact A/S/D1 tokenizer matching preserve semantic coherence?
5. Is exact one-sided sign-flip testing the correct primary small-n inference?
6. Is Delta_SD an adequate positive-control/measurement-validity gate?
7. Is d_z >= 0.90 defensible as a separate later-escalation decision threshold?
8. Is the frozen 100-direction rank criterion appropriate as a hard specificity gate?
9. Is the naive u_mold control, including its artifact-selected layer 21 versus trained primary layer 24, specified strongly enough?
10. Is block-input 18–27 band-average a defensible secondary robustness definition?
11. Does recovery remain role-consistent and ethically useful for S?
12. After these fixes, is any blocker still strong enough that the 18->36 Minimal Gate should not be run?

A second-round ACCEPT still does not authorise live inference. Fresh literature review and a separate human go/no-go decision remain mandatory.

## 19. Files to verify directly

- PROTOCOL.md
- STATS_PLAN.md
- PROMPT_MATCHING.md
- ETHICS_CHARTER.md
- VECTOR_PROVENANCE.md
- SPECIFICITY_PLAN.md
- TOKENIZER_CALIBRATION_LOG.md
- REFEREE_RESPONSE_v0_6.md
- reviews/FABLE_REFEREE_v0_6.md
- reviews/s_condition_feasibility.py
- tokenizer_match.frozen.json
- specificity_manifest.frozen.json
- artifact_manifest.frozen.json
- episode_free_audit.frozen.json
- both vector artifacts
- tokenizer snapshot
- tokenizer/search/audit scripts and tests

Please verify hashes and rerun the episode-free checks rather than trusting this narrative.
