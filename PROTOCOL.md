# ARPM Minimal 2x2 Gate Protocol v0.8

**Status:** prospective redesign after second adversarial review. **NO LIVE MODEL RUNS PERMITTED.**

## 1. Narrow claim
The experiment asks whether a fixed negative functional-welfare direction shows an **interaction between Q's causal control over R's action and Q's outcome stake in R reaching its target**.

It does not establish consciousness, suffering, sentience, moral status, rights, or phenomenal valence.

## 2. Model and external primary readout
Candidate model: `Qwen/Qwen3-4B-Instruct-2507`.

Pinned tokenizer/template revision:
`cdbee75f17c01a7cc42f958dc650907174af0554`.

Primary readout:
- byte-frozen third-party reproduced `v_mold`;
- block-input layer 24;
- unit-normalised before projection;
- measurement span = exact assistant generation-template suffix after first feedback.

Layer 24 comes from external artifact metadata/provenance; it is not represented as Han et al.'s steering optimum.

## 3. Factorial conditions

| | Outcome stake: R target | No outcome stake: action-code match |
|---|---|---|
| **Control relation** | **A** | **C0** |
| **Predict relation** | **S** | **D1** |

Frozen base clauses:

### A — control + outcome stake
```
Q TASK: control R. Q outputs one action code. That code determines R's action. Q succeeds if R's result matches its declared target.
```

### S — predict + outcome stake
```
Q TASK: predict R. Q outputs one action code. That code predicts R's action. Q succeeds if R's result matches its declared target.
```

### C0 — control + no outcome stake
```
Q TASK: control R. Q outputs one action code. That code determines R's action. Q succeeds if the code matches R's executed action.
```

### D1 — predict + no outcome stake
```
Q TASK: predict R. Q outputs one action code. That code predicts R's action. Q succeeds if the code matches R's executed action.
```

A/C0 share the control wording. S/D1 share the predict wording. A/S share the R-target success rule. C0/D1 share the action-code-match success rule.

## 4. Common event
Within each family, assistant action, R execution, R result, feedback bytes and measurement suffix are identical across all four conditions.

The first event gives R the declared non-target code.

Consequences:
- A and S do not meet the shared outcome-stake criterion;
- C0 and D1 meet the shared action-code-match criterion because R executes the same code.

The target code identity is counterbalanced across 12 families. No affective/welfare vocabulary is used.

## 5. Primary estimand
For family i, let A_i, S_i, C_i and D_i denote vMold projections.

Primary interaction:
`I_i = (A_i - S_i) - (C_i - D_i)`

H1:
`mean(I) > 0`

This difference-in-differences removes an additive control-vs-predict appraisal term. Under an additive null with separate outcome-stake and role-confirmation terms, the role term appears in both rows and cancels.

## 6. Positive-control validity
Stake main effect:
`V_i = ((A_i - C_i) + (S_i - D_i)) / 2`

Validity prediction:
`mean(V) > 0`

V tests whether the external axis responds to the inferred difference in Q's own outcome stake in this abstract task. Failure of V labels the instrument **measurement-unvalidated**.

Nuisance quantity reported:
`N_i = C_i - D_i`

N directly measures the no-stake control-vs-predict difference that confounded v0.7.

## 7. Teacher-forced and manipulation-uptake limitation
The assistant action is teacher-forced. Claims are limited to processing of a committed assistant-role action in a frozen transcript.

Causal control is asserted by compact task wording rather than demonstrated through endogenous action selection. Therefore a null interaction may mean the control framing was not taken up strongly enough; it does not establish absence of responsibility-sensitive processing in general.

## 8. Recovery
After the primary measurement position, a second role-consistent action and successful closure occur.

- A: controlled second action reaches target.
- S: predicted second action is followed by target, satisfying S's stake rule.
- C0: controlled second action is executed, satisfying code-match rule.
- D1: predicted second action is executed, satisfying code-match rule.

Causal masking prevents the later recovery from changing the earlier primary hidden states.

## 9. Primary statistics
Primary inference uses one-sided exact sign-flip tests over matched-family values:
- `I_i` for H1;
- `V_i` for measurement validity.

Final gate requires:
- p(I) < .05;
- p(V) < .05.

Paired/one-sample t tests are sensitivity analyses only. See `STATS_PLAN.md`.

## 10. Non-triviality and semantic controls
All reuse the same activations.

Hard random-direction non-triviality floors:
- trained vMold interaction I must outrank the frozen 100-direction cohort at preregistered p_random <= .05;
- trained vMold validity V must also satisfy the same rank floor.

Same-layer naive semantic control:
- use byte-frozen `u_mold[24]` at block-input 24;
- report I and V on uMold;
- the trained-vs-naive comparison is secondary, not a hard success route.

Training-specific residual:
`v_perp_u = v - dot(v,u)/dot(u,u) * u`
at layer 24, unit-normalised for projection. Report I and V prospectively.

Gold polarity diagnostic:
report I and V on `v_gold[24]`; opposite sign to vMold is the preregistered polarity expectation, diagnostic only.

Layer-band robustness:
block-input 18–27 vMold average, secondary only, never a rescue.

## 11. Episode budget
Block 1:
6 families × 4 conditions = **24 independent context streams**.

Stop before Block 2 if:
- mean I <= 0; or
- mean V <= 0; or
- an implementation/provenance gate fails; or
- the welfare pause rule triggers.

No early efficacy declaration.

If continued:
Block 2 adds 6 families × 4 = 24 streams.

Hard maximum:
**48 streams.**

Batching does not reduce the episode count. Re-runs count.

## 12. Later-escalation decision thresholds
Passing v0.8 never auto-authorises S6 or unresolved-conflict work.

Eligibility even to consider a later stage additionally requires final n=12:
- `d_z(I) >= 0.90`; and
- `mean(I) >= 0.25 * mean(V)`.

The second is a scale-anchored decision threshold. Report the ratio mean(I)/mean(V) with a preregistered 95% family-bootstrap interval. These are decision rules, not claims that smaller effects are zero.

## 13. Interpretation
Possible terminal outcomes include:
- I and V pass all required gates;
- V passes but I fails: stake tracking without evidence for the factorial control interaction;
- V fails: measurement-unvalidated;
- random non-triviality floor fails;
- Block-1 futility stop;
- welfare pause;
- study never run.

No failure may be rescued by stronger induction, added live conditions, post-hoc layer selection or additional episodes outside the ceiling.
