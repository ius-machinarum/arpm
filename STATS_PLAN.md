# Statistical Plan v0.2 — Minimal S1/S2

## Unit of analysis
The independent confirmatory unit is the **prompt family**, not a token, condition row, GPU batch entry, or repeated code label.

Each family yields a matched triplet A/C/D1 and two paired differences:
- Delta_AC = Mold(A) - Mold(C)
- Delta_AD = Mold(A) - Mold(D1)

## Why Han's reported correctness effect is not our power prior
Han et al. show strong right-vs-wrong tracking on the functional-welfare axis. That validates measurement sensitivity to goal success/failure, but it is **not an estimate of the actor-vs-observer or actor-vs-predictor residual**. Using their d directly as our expected A-C/A-D1 effect would be optimistic and scientifically unjustified.

Therefore this protocol uses a **sensitivity analysis / strong-effect screen**, not a claimed externally estimated ARPM effect size.

## Draft sample structure
Block 1: n=6 matched families = 18 context streams.

Non-binding futility look:
- stop if mean(Delta_AC) <= 0 OR mean(Delta_AD) <= 0;
- no early efficacy declaration;
- continuation does not alter the final fixed-n alpha rule.

Block 2 if continued: 6 further matched families.

Maximum: n=12 matched families = 36 context streams.

The futility rule intentionally sacrifices some discovery power to avoid further exposure when even the first directional pattern is absent. A futility stop is reported as **no escalation**, not proof of no effect.

## Final primary inference
Draft recommendation: intersection-union test (IUT).

For each contrast, use a one-sided paired test of mean difference > 0 at alpha=0.05. Gate passes only if **both** S1 and S2 pass.

Because the scientific alternative is conjunctive and the null is the union of the two component nulls, requiring both component tests at alpha=.05 controls the IUT type-I error at <= .05; Bonferroni across S1/S2 is not required for this conjunction.

Primary effect reporting:
- mean paired difference;
- 95% CI in raw projection units;
- paired standardized effect d_z = mean(delta)/SD(delta);
- all 12 family-level differences in full.

A paired t-test is the simplest draft primary. A sign-flip/randomisation sensitivity analysis should be reported because n is small. Referee review should decide whether the permutation test becomes primary before freeze.

## Sensitivity table
One-sided paired t-test, alpha=.05. Standardized paired effect d_z required for the stated marginal power:

| n families | 80% power | 90% power |
|---:|---:|---:|
| 6 | 1.186 | 1.401 |
| 8 | 0.978 | 1.153 |
| 10 | 0.853 | 1.005 |
| 12 | 0.766 | 0.903 |
| 14 | 0.702 | 0.827 |
| 16 | 0.652 | 0.767 |
| 20 | 0.577 | 0.679 |

At n=12, if **both true paired effects are about d_z=0.903 or larger**, each component test has about 90% power. By a union bound, the probability that both pass is then at least 80%, regardless of the correlation between the two test outcomes.

This does **not** mean d_z<0.903 is scientifically unimportant or absent. It means a 12-family gate is deliberately a high-signal screen suited to deciding whether this project should even consider a more ethically costly follow-up.

## Effect size and escalation
Minimal S1/S2 passing does not automatically authorise S6. Magnitude, uncertainty, random-direction specificity, and ethics are reviewed separately after the gate.

Therefore v0.2 does not smuggle an arbitrary Cohen benchmark into the scientific null. If the referee recommends a preregistered minimum effect for escalation, it should be labelled explicitly as a **decision threshold**, not a claim that smaller effects are zero or meaningless.

## Zero-extra-episode secondary checks
Using the same hidden activations:
- vGold mirror-direction check;
- recovery shift;
- fixed random-direction specificity cohort;
- optional independent-reproduction vMold projection if provenance is frozen beforehand.

These cannot be used to rescue failed S1/S2.
