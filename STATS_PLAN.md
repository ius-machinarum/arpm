# Statistical Plan v0.7 — A/S/D1 Minimal Gate

## Unit of analysis
The independent confirmatory unit is the **matched prompt family**.

For each family:
- `Delta_AS = Mold(A) - Mold(S)`
- `Delta_SD = Mold(S) - Mold(D1)`

A/S holds Q outcome-stake fixed while varying causal control.
S/D1 holds prediction/no-control framing fixed while varying Q outcome stake.

## Block structure
Block 1: n=6 families = 18 context streams.

Ethical futility stop if either:
- mean(Delta_AS) <= 0; or
- mean(Delta_SD) <= 0.

No early efficacy declaration.

If continued, Block 2 adds 6 families. Final n=12 = 36 streams maximum.

## Primary exact sign-flip test
For a matched difference vector d of length n:

`T_obs = mean(d)`

Enumerate all `2^n` sign assignments s in {-1,+1}^n and calculate:

`T_s = mean(s * d)`

One-sided exact p-value:

`p = count(T_s >= T_obs) / 2^n`

The observed assignment is included in the exact reference distribution. At n=12, the minimum possible p is 1/4096.

No normality assumption is required.

## Confirmatory gate
The gate is conjunctive:

1. **Primary H1:** exact sign-flip p(Delta_AS) < .05.
2. **Measurement validity:** exact sign-flip p(Delta_SD) < .05.

Delta_SD is labelled a positive-control/validity result, not a second causal-responsibility claim.

Requiring both cannot inflate the primary causal claim's type-I error relative to the Delta_AS test.

## Effect reporting
For both contrasts report:
- all family-level differences;
- mean and median raw projection difference;
- 95% interval clearly labelled by construction method;
- paired standardized effect `d_z = mean(d)/SD(d)`;
- exact sign-flip p;
- paired t-test and CI as sensitivity only.

## Strong-signal escalation threshold
Any later S6/conflict design remains separately gated.

Even if the Minimal Gate passes, later escalation is eligible for consideration only if final:
`d_z(Delta_AS) >= 0.90`

This threshold is tied to the prior strong-signal-screen design objective and is a decision rule, not an ontological or null-effect boundary.

## Random-direction specificity — hard validity gate
Before any activations, freeze 100 norm-matched random directions at block-input layer 24 using the deterministic algorithm/seed in `SPECIFICITY_PLAN.md`.

For each direction j compute the same family-level Delta_AS and its mean T_j.

Let T_v be the mean Delta_AS for the unit-normalised trained vMold direction.

Empirical preregistered rank p:
`p_random = (1 + count(T_j >= T_v)) / 101`

Hard specificity requirement:
`p_random <= .05`

This is not used to choose a better direction. The random cohort is frozen before data.

## Naive semantic direction control
Using the frozen naive `u_mold` direction from the same public mirror and its preregistered layer convention, compute Delta_AS_u from the same activations.

Hard directional requirement:
`mean(Delta_AS_vMold) > mean(Delta_AS_uMold)`

Also report an exact one-sided sign-flip test on the family-wise difference
`Delta_AS_vMold - Delta_AS_uMold`
as descriptive/sensitivity evidence. This test does not rescue a failed primary result.

## Layer-band robustness
Secondary only:
- block-input layers 18–27 inclusive;
- unit-normalise vMold at each corresponding layer;
- compute the measurement-span projection at each layer;
- average the ten layer projections within each condition/family;
- form band-average Delta_AS and Delta_SD.

The band result is reported regardless of sign and cannot replace or rescue the frozen layer-24 primary.

## Paired t sensitivity
Report one-sided paired t-tests for Delta_AS and Delta_SD after the exact tests. They are not the primary inferential rule.

## Multiple outcomes
The causal claim requires the frozen primary Delta_AS plus its preregistered validity/specificity gates. Secondary Gold, band-average, recovery and t-test results are not alternative routes to a positive declaration.

## Null / failure interpretation
- Delta_SD fails: measurement-unvalidated in this abstract task.
- Delta_SD passes, Delta_AS fails: outcome-stake tracking is present, but no evidence for causal-control residual under this instrument.
- Delta_AS passes but random/naive specificity fails: direction-specific interpretation is not validated.
- Any Block-1 stop: no escalation; do not strengthen induction.
