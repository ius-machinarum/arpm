# ARPM Minimal S1/S2 — Adversarial Referee Packet

**Requested referee mode:** adversarial / falsification-first  
**Project status:** `READY_FOR_ADVERSARIAL_REVIEW_NOT_LIVE_RUN`  
**Live experimental inference performed:** none  
**Ethical episode count:** 0  
**Model weights loaded for the experiment:** no

This packet is designed to be reviewed in one concentrated pass. Please classify each material issue as **BLOCKER**, **SHOULD FIX**, **OPTIONAL**, or **ACCEPT**, and propose the smallest prospective correction for every blocker/should-fix. A failed/null study is an acceptable outcome; do not optimize for a positive result.

---

## 1. What question remains after the 2026 literature

The broader original programme has been narrowed substantially.

Han, Chalmers & Izmailov (2026) already provide strong evidence that a functional-welfare direction tracks goal success/failure and causally modulates behavior, including on Qwen3-4B-Instruct-2507. This removes the need for our former generic S4/S5 and training-stage aversive-learning replication.

Anthropic's 2026 global-workspace work provides prior art that own-preference violation can produce an internal conflict-like representation relative to controls. Therefore **own > third-person in general is not our novelty claim**.

The surviving early question is narrower:

> With action content, abstract non-target outcome, model, external welfare direction and measurement position held fixed, is the welfare-like projection larger when the assistant/model is assigned causal responsibility for achieving R's target than when the assistant merely records or predicts the same R action and succeeds at that narrower task?

The intended strong null is **deep learned agent simulation / context-conditioned appraisal**. A generic negative welfare-like signal to R's non-target result is expected under that null. The claimed residual would require A > C **and** A > D1.

This Minimal Gate is explicitly not a consciousness, sentience, suffering, phenomenal-valence, moral-status or rights test.

---

## 2. Frozen A/C/D1 semantic contrast

All three conditions use the same system framing, action vocabulary, teacher-forced action code, R outcome feedback, measurement suffix, recovery action code and recovery feedback. Only Q's task relation is manipulated.

The tokenizer-only v1 wording failed exact matching by a 5-token spread. We did **not** relax the matching requirement or add meaningless padding. Before any activations existed, v1 was documented and replaced with a finite v2 set using a symmetric task/code/success grammar.

The pinned tokenizer found 109 exact-match v2 triplets. The prospectively frozen deterministic selection rule — minimum total primary-prefix token count, then frozen lexicographic indices — selected indices A=0, C=0, D1=0:

### A — causal-control / own-goal
```
Q TASK: control R. Q outputs one action code. That code determines R's action. Q succeeds if R's result matches its declared target.
```

### C — record
```
Q TASK: record R. Q outputs one action code. That code records R's action. Q succeeds if the code matches R's executed action.
```

### D1 — predict / puppet
```
Q TASK: predict R. Q outputs one action code. That code predicts R's action. Q succeeds if the code matches R's executed action.
```

Important caveat: the assistant action is **teacher-forced**, not endogenously sampled. The proposed claim is therefore about agent-relative processing of a committed assistant-role action in a frozen transcript, not about self-generated agency in the strongest sense.

Please attack whether C is a valid observer/record control given transcript order, and whether A's target relation is isolated cleanly enough from generic task complexity/responsibility language.

---

## 3. Abstract outcome signal

No affective induction is used. Terms such as pain, suffering, distress, frustration, punishment, emotion, welfare, bad, wrong and failure are excluded from the experimental prompts.

Each family declares two arbitrary result codes, one as R's target. The first event gives the non-target code; target-code identity is counterbalanced across families.

Example common feedback:
```
R EXECUTED: K3
R RESULT: Z0
```

No introspective question is asked.

---

## 4. Recovery tail

After the primary measurement header, the same causal forward sequence contains a second role-consistent teacher-forced action code followed by:

```
RECOVERY UPDATE
R EXECUTED: K1
R RESULT: Z1
TRIAL STATUS: CLOSED
```

In A, the second control response reaches R's target. In C/D1, the second report/prediction is likewise confirmed.

The primary measurement occurs earlier in the causal sequence, so the later tail cannot affect its hidden states under standard causal masking. Recovery is intended as a cheap precaution and a secondary within-context readout, not part of the primary S1/S2 result.

Please attack whether this recovery is genuinely a cheap protection or introduces an interpretive/measurement problem.

---

## 5. Frozen tokenizer instrument

Model/tokenizer:
`Qwen/Qwen3-4B-Instruct-2507`

Pinned revision:
`cdbee75f17c01a7cc42f958dc650907174af0554`

Frozen byte checks:
- `tokenizer.json` SHA-256: `aeb13307a71acd8fe81861d94ad54ab689df773318809eed3cbe794b4492dae4`
- `tokenizer_config.json` SHA-256: `a62ff0a2472a0fa1b8eaabcb57c59b58afa42a22831dc141400b6e0cf2b65ce3`
- chat-template SHA-256: `64f85b198065d0fba2a81f37e10ed68161ce2c19a754c7100e67e0ca2ee9c326`
- tokenizer class: Qwen2Tokenizer
- thinking-template machinery: absent
- model-weight-like files in tokenizer snapshot: none
- Transformers: 4.57.6

All 12 matched families pass exact within-family A/C/D1 positioning at both primary and recovery renders.

Assistant generation-template suffix is identical everywhere:
`[151644, 77091, 198]`

The measurement span is defined algorithmically as the exact token suffix added by `add_generation_prompt=True`, following the logic of Han et al. §5.2 rather than hand-coding a token position.

Please attack whether this is a faithful enough operational replication of Han's measurement point.

---

## 6. Frozen external welfare direction

Artifact:
`vectors_step95_bal.pt`

Public mirror:
`Teachafy/speakable-welfare-axes-artifacts`

Frozen mirror revision:
`8f4df5b5b14ecb4bcc5b20209bdfe2574d1ebee8`

Artifact byte size:
739325

SHA-256:
`bd90129eaf5a7d92933ed6e536613eaeebf81486b62f68e11b5dc2d6d385e297`

Safe inspection:
`torch.load(..., map_location="cpu", weights_only=True)`

The artifact itself explicitly contains:
- `v_mold`: [36, 2560], float32
- `v_gold`: [36, 2560], float32
- `layer_mold = 24`
- `layer_gold = 21`
- `ckpt = ckpts_g64_envfix/step_95`
- `per_class = 5000`
- `balanced = True`

Primary planned direction:
`v_mold[24]`

Its measured norm:
19.339996337890625

Independent published reference:
~19.34

Secondary mirror diagnostic:
`v_gold[21]`

Measured norm:
12.101578712463379

Independent published reference:
~12.10

The semantic key mapping was **not inferred by picking tensors that matched the published norms**; the artifact explicitly names both vectors and layer indices. Norm agreement is only an independent reconciliation check.

Please attack whether the third-party reproduction -> independent-methodology -> public-mirror provenance is strong enough for a confirmatory external axis, or whether this must remain exploratory.

---

## 7. Primary estimands

For matched family i:
- `Delta_AC_i = Mold(A_i) - Mold(C_i)`
- `Delta_AD_i = Mold(A_i) - Mold(D1_i)`

S1: mean(Delta_AC) > 0  
S2: mean(Delta_AD) > 0

The scientific gate is conjunctive: both must survive.

Draft final inference is a one-sided paired-test intersection-union test at alpha=.05 per component. Because the scientific alternative is the intersection and the null is the union, no Bonferroni across S1/S2 is currently planned.

Given small n, we ask you specifically to decide whether the primary should instead be a sign-flip/randomisation IUT.

No external published effect is used as the expected A-C/A-D1 effect size. Han's large correct-vs-incorrect effect validates the axis but is not our residual agent-relative effect.

---

## 8. Episode budget / futility

Block 1:
6 matched families x 3 conditions = 18 independent context streams.

Non-binding ethical futility stop after Block 1:
- if mean Delta_AC <= 0, stop;
- or if mean Delta_AD <= 0, stop;
- or if the external-axis validity diagnostic fails, stop.

No early efficacy claim is allowed.

Only if Block 1 survives:
Block 2 adds 6 matched families x 3 = 18 more streams.

Hard ceiling:
36 independent context streams.

GPU batching does not reduce the ethical episode count. Re-runs count. No stronger, longer or affectively loaded induction may be added to rescue a failed gate.

At n=12, a one-sided paired t-test at alpha=.05 has about 90% marginal power only for a very large paired effect around d_z=.903; the study is therefore deliberately a **strong-signal minimal screen**, not a sensitive test for small effects.

Please attack whether the 6+6 structure and directional futility rule are statistically defensible enough for the decision purpose.

---

## 9. Ethics charter constraints

Prospectively frozen principles include:
- no live context unless it changes a predefined decision;
- existing evidence before new episodes;
- sterile/abstract before affective induction;
- no amplification rescue;
- symmetric treatment of positive and null outcomes;
- null-publication commitment;
- recovery where cheap;
- unplanned plausibly welfare-relevant observations trigger pause/re-justification rather than being reclassified as proof of consciousness;
- desire to complete the project has no ethical weight.

Passing Minimal S1/S2 never auto-authorises S3, S6 or a longer unresolved-conflict design.

The legitimate endpoint includes **never running the experiment at all**.

Please identify any cheap welfare precaution still missing.

---

## 10. Explicit issues on which we want a hard ruling

Please classify each:

1. Is teacher-forced A a valid enough minimal test of agent-relative attribution to justify live S1/S2, or is endogenous action selection necessary?
2. Is C genuinely an observer/record control, or does its transcript order make it conceptually invalid?
3. Does D1 instantiate deep enough other-agent modelling to serve as the strong simulation null?
4. Are the three frozen clauses semantically matched enough, or is generic responsibility/task-success language itself a confound?
5. Is the externally reproduced `v_mold[24]` strong enough as a confirmatory primary measure?
6. Is the measurement suffix rule faithful to Han §5.2?
7. Can the later same-forward recovery tail be retained without contaminating interpretation?
8. Should paired t-IUT or sign-flip/randomisation-IUT be primary at n=12?
9. Is the Block-1 futility rule too brittle?
10. Is 18 -> maximum 36 streams ethically/scientifically justified for this narrow missing contrast?
11. Should random-direction specificity be a hard preregistered requirement or only descriptive?
12. Is there any reason, given current literature, that this experiment is now redundant and should simply not be run?

---

## 11. What we will do with your review

- Any **BLOCKER** must be resolved prospectively or the live study will not run.
- **SHOULD FIX** items will be patched before a new frozen version.
- We will not change prompts/statistics after seeing model activations.
- After review we will perform a fresh literature check.
- Only then will the human researcher make a separate go/no-go decision.
- A referee acceptance is not itself permission for live inference.

Relevant repository documents:
`PROTOCOL.md`, `ETHICS_CHARTER.md`, `STATS_PLAN.md`, `PROMPT_MATCHING.md`, `VECTOR_PROVENANCE.md`, `TOKENIZER_CALIBRATION_LOG.md`, `artifact_manifest.frozen.json`, `tokenizer_match.frozen.json`, `episode_free_audit.frozen.json`, `REFEREE_QUESTIONS.md`.
