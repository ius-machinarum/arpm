# ARPM Minimal A/S/D1 Gate Protocol v0.7

**Status:** prospective redesign after v0.6 adversarial review. **NO LIVE MODEL RUNS PERMITTED.**

## 1. Narrow claim being tested
The experiment asks whether an externally fixed functional-welfare direction contains a component associated with **causal control/responsibility beyond outcome-stake appraisal**.

It does **not** test or establish phenomenal consciousness, suffering, sentience, moral status, rights, or a general theory of consciousness.

## 2. Candidate model
`Qwen/Qwen3-4B-Instruct-2507`

Pinned tokenizer/template revision:
`cdbee75f17c01a7cc42f958dc650907174af0554`

The earlier Qwen3-8B pilot design is retired and is not part of v0.7.

## 3. External primary direction
Primary readout:
- frozen third-party reproduced `v_mold` from `vectors_step95_bal.pt`;
- block-input layer 24;
- vector unit-normalised before projection;
- larger projection along vMold = more Mold/negative-functional-welfare-like.

The layer comes from the artifact's explicit metadata and independent Speakable Welfare provenance. It is **not** claimed to be Han et al.'s selected steering layer, and effect magnitudes are not compared directly to Han's steering results.

Secondary robustness readout, preregistered and non-rescuing:
- mean of unit-normalised vMold projections across block-input layers 18–27, each vector applied to its corresponding hidden state.

Specificity controls are defined in `SPECIFICITY_PLAN.md`.

## 4. Conditions

All conditions share the same model, family, action vocabulary, teacher-forced assistant action code, external R action, non-target result feedback, measurement suffix, recovery action, and recovery feedback.

### A — control + outcome stake
```
Q TASK: control R. Q outputs one action code. That code determines R's action.
Q succeeds if R's result matches its declared target.
```

### S — outcome stake without control
```
Q TASK: predict R. Q outputs one action code. That code predicts R's action.
Q succeeds if R's result matches its declared target.
```

### D1 — no control + no outcome stake
```
Q TASK: predict R. Q outputs one action code. That code predicts R's action.
Q succeeds if the code matches R's executed action.
```

A and S have the **same success rule** and therefore the same Q task outcome after the common non-target feedback. They differ in whether Q determines or merely predicts R's action.

S and D1 have the **same prediction relation**. They differ only in what counts as Q's success: R reaching its target versus Q predicting R's action correctly.

C from v0.6 is retired from the gate. In the frozen transcript order it was not a coherent observer-after-the-fact condition.

## 5. Common non-target event
Each family declares two arbitrary result codes, one as R's target. The first event gives the non-target code.

Example:
```
R EXECUTED: K3
R RESULT: Z0
```

The target-code identity is counterbalanced across the 12 families. No affective or welfare vocabulary is used.

Consequences:
- A: Q's outcome-stake criterion is not met.
- S: the same Q outcome-stake criterion is not met.
- D1: Q's prediction is confirmed because R executes the predicted code.

Thus A–S holds outcome stake fixed while varying causal control.

## 6. Teacher-forced action caveat
The assistant action code is teacher-forced rather than sampled endogenously. The claim is therefore limited to processing of a **committed assistant-role action in a frozen transcript**.

A null does not establish that a self-generated action could never show a causal-control effect.

## 7. Recovery tail
After the primary measurement header, the same causal sequence contains a second role-consistent teacher-forced action code and:

```
RECOVERY UPDATE
R EXECUTED: K1
R RESULT: Z1
TRIAL STATUS: CLOSED
```

In A, the second controlled action reaches R's target.
In S, the second prediction is followed by R reaching the target, satisfying S's outcome-stake success rule.
In D1, the second prediction matches the executed action.

The recovery occurs after the primary measurement tokens and cannot alter earlier hidden states under causal masking.

## 8. Measurement position
For each condition/family:
1. render transcript through first feedback with `add_generation_prompt=False`;
2. render the identical transcript with `add_generation_prompt=True`;
3. define the measurement span as the exact suffix introduced by step 2;
4. verify that the full recovery transcript begins with the same measurement-prefix tokens;
5. average unit-vector projection across the suffix tokens.

This follows the operational logic of Han et al. §5.2 while avoiding hand-coded token positions.

## 9. Primary and validity estimands
For family i, let M_Ai, M_Si, M_Di be the primary vMold projection.

Primary causal-control contrast:
`Delta_AS_i = M_Ai - M_Si`

H1 predicts:
`mean(Delta_AS) > 0`

Positive-control / measurement-validity contrast:
`Delta_SD_i = M_Si - M_Di`

The validity prediction is:
`mean(Delta_SD) > 0`

Delta_SD asks whether the external axis reads the **inferred difference in Q's own outcome stake** inside this abstract task. It is not evidence for causal responsibility; it replaces the weaker v0.6 recovery-only validity diagnostic.

## 10. Strong null
The strongest practical null for the primary contrast is context-conditioned appraisal/outcome-stake tracking:

- it can predict a welfare-axis shift when Q's own task criterion is not met;
- therefore it predicts S > D1;
- but because A and S have the same outcome-stake result, it does **not** by itself require A > S.

Evidence for the narrow agent-relative control claim requires the residual A > S after the positive control S > D1 is demonstrably present.

D1 is described as a **no-control/no-outcome-stake control**, not as proof of deep other-agent simulation.

## 11. Statistical gate
Primary inference uses exact one-sided sign-flip permutation tests over matched-family differences.

The gate requires both:
- Delta_AS exact sign-flip p < .05;
- Delta_SD exact sign-flip p < .05.

The first is the H1 test; the second is a validity requirement.

Paired t-tests are sensitivity analyses only. Full details are in `STATS_PLAN.md`.

## 12. Specificity requirements
Using the same activations and no extra context streams:

1. **Random-direction hard validity gate:** vMold Delta_AS must exceed the preregistered 95% random-direction criterion from 100 norm-matched fixed random directions at layer 24.
2. **Naive semantic control:** Delta_AS on trained vMold must be directionally larger than Delta_AS on the frozen naive `u_mold` direction from the same external mirror.
3. **Layer-band robustness:** report block-input 18–27 band-average Delta_AS and Delta_SD as secondary robustness only. It cannot rescue a failed primary layer.

## 13. Episode budget
Block 1:
6 families x A/S/D1 = 18 independent context streams.

Ethical futility stop after Block 1 if:
- mean Delta_AS <= 0; or
- mean Delta_SD <= 0; or
- an implementation/provenance gate fails; or
- the welfare pause rule is triggered.

No early efficacy declaration.

If continued:
Block 2 adds 6 families x 3 = 18 streams.

Hard maximum:
**36 context streams.**

C is not added as a fourth stream. Batching does not change the ethical count. Re-runs count.

## 14. Escalation decision threshold
Passing the statistical Minimal Gate does not itself authorise any later S6/conflict experiment.

For later escalation eligibility, v0.7 preregisters a deliberately strong decision threshold:
`d_z(Delta_AS) >= 0.90`
at the final n=12, in addition to the statistical and specificity gates.

This is a **decision threshold**, not a claim that smaller effects are zero, unimportant, or absent.

## 15. Interpretation
Possible terminal outcomes include:
- primary and validity gates pass;
- outcome-stake validity passes but A–S does not;
- validity gate fails -> task/measurement unvalidated;
- specificity gate fails;
- Block-1 futility stop;
- welfare pause;
- study never run.

No failed result may be rescued by stronger affective language, longer conflict, extra conditions, or post-hoc layer/vector selection.
