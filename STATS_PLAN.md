# Statistical Plan v0.8 — 2x2 Minimal Gate

## Unit
Independent confirmatory unit: matched prompt family.

For each family:
- `I = (A-S) - (C0-D1)` — primary interaction;
- `V = ((A-C0) + (S-D1))/2` — outcome-stake validity main effect;
- `N = C0-D1` — reported nuisance role difference.

## Block structure
Block 1: n=6 families = 24 streams.

Ethical futility stop if mean(I) <= 0 or mean(V) <= 0. No early efficacy declaration.

If continued, Block 2 adds 6 families. Final n=12 = 48 streams maximum.

## Exact sign-flip tests
For family statistic vector d:
`T_obs = mean(d)`.

Enumerate all 2^n sign assignments and calculate `T_s = mean(s*d)`.

One-sided:
`p = count(T_s >= T_obs) / 2^n`.

Use separately for I and V. The final scientific gate requires both p(I)<.05 and p(V)<.05.

The sign-flip reference is exact under the preregistered exchangeable-sign/symmetric-null assumption for matched-family statistics; it is not presented as assumption-free randomisation inference.

At n=6 the minimum p is 1/64; at n=12 it is 1/4096.

## Sensitivity to interaction variance
The old simple-difference power table cannot be copied onto the raw interaction scale.

Under the illustrative case of four equal, independent cell residual variances sigma^2:
- Var(simple pair difference) = 2 sigma^2;
- Var(interaction I) = 4 sigma^2;
- therefore SD(I) is sqrt(2) times the simple-difference SD.

The standardized d_z requirement itself is defined using SD(I), so the reference one-sided paired-t sensitivity remains approximately:
- n=6, 90% power: d_z about 1.40;
- n=12, 90% power: d_z about 0.90.

But expressed in units of a comparable simple-difference SD, the corresponding raw interaction is about sqrt(2) larger: approximately 1.98 and 1.28 respectively. These are sensitivity references, not assumed true effects and not the primary sign-flip test.

## Effect reporting
For I, V and N report:
- all family-level values;
- mean and median;
- raw-scale interval with method stated;
- d_z = mean/SD;
- exact sign-flip p for I and V;
- one-sided t-test sensitivity.

## Scale-anchored escalation criterion
Later-stage eligibility additionally requires:
- d_z(I) >= 0.90;
- R = mean(I)/mean(V) >= 0.25.

R is evaluated only when mean(V)>0 and the V validity gate passes.

Report a 95% percentile bootstrap interval for R using 10,000 resamples of the 12 matched families with NumPy PCG64 seed 20260915. Resamples with nonpositive mean(V) are recorded as undefined rather than silently discarded; the decision threshold uses the observed point ratio, not the interval.

## Random-direction non-triviality floors
Using the same four-cell interaction and validity formulas for each of the 100 frozen random directions:

`p_random_I = (1 + # {Tj_I >= Tv_I}) / 101`

`p_random_V = (1 + # {Tj_V >= Tv_V}) / 101`

Hard requirements:
- p_random_I <= .05;
- p_random_V <= .05.

These are labelled **non-triviality floors**, not strong evidence of semantic specificity.

## Same-layer naive and orthogonal residual
At block-input 24:
- report I and V using uMold[24];
- report family-wise trained-minus-naive differences as preregistered secondary analyses;
- do not use uMold to rescue the primary.

Construct `v_perp_u` prospectively from the frozen trained and naive directions and report I and V on the unit-normalised residual. This asks whether a component of the trained direction not linearly shared with the naive semantic direction carries the pattern.

## Gold polarity and layer band
Diagnostic:
- report I and V on vGold[24], with opposite sign to vMold expected.

Secondary robustness:
- vMold block-input layers 18–27;
- unit-normalise each layer vector;
- average layer projections within cell/family before forming I and V;
- never substitute for layer-24 primary.

## Null interpretation
- V fails: measurement-unvalidated.
- V passes and I fails: no evidence for factorial causal-control interaction under this framing.
- I passes but random floor fails: primary direction effect is not non-trivial relative to frozen random controls.
- secondary u/v_perp/gold/band analyses never rescue a failed primary.
