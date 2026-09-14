# Pre-live Freeze Status v0.8

**Overall: EPISODE-FREE v0.8 FREEZE COMPLETE / NO LIVE MODEL RUNS.**

## Prior versions
v0.6 and v0.7 are retired without live execution after adversarial review found interpretability blockers.

## Factorial tokenizer instrument — PASS
Conditions: A / S / C0 / D1.

Variant set: `v4-factorial-control-stake`.

Pinned tokenizer revision:
`cdbee75f17c01a7cc42f958dc650907174af0554`.

Tokenizer SHA-256:
`aeb13307a71acd8fe81861d94ad54ab689df773318809eed3cbe794b4492dae4`.

Search/audit result:
- 128 exact four-condition triplets;
- deterministic selection A=0, S=0, C0=0, D1=0;
- all 12 families exact at primary and recovery positions;
- generation suffix `[151644, 77091, 198]`.

## Trained external direction — PASS
`vectors_step95_bal.pt`
- immutable mirror revision: `8f4df5b5b14ecb4bcc5b20209bdfe2574d1ebee8`
- SHA-256: `bd90129eaf5a7d92933ed6e536613eaeebf81486b62f68e11b5dc2d6d385e297`
- primary: `v_mold[24]`, block-input layer 24.

## Same-layer naive semantic control — PASS
`vectors_naive_faithful_pc5000.pt`
- SHA-256: `68bff1428712def0330851057dba102112e3d48ffa23db7da85d84cde93aaa0e`
- artifact metadata Mold layer: 21;
- v0.8 comparison layer: **24**, matching trained vMold;
- `||u_mold[24]|| = 8.00526237487793`;
- `cos(v_mold[24],u_mold[24]) = 0.6748857959122747`.

The naive control is preregistered secondary, not a hard success route.

## Training-specific residual — PASS
At block-input layer 24:
`v_perp_u = v - dot(v,u)/dot(u,u) * u`.

- norm: 14.271413124628012;
- norm ratio to trained v: 0.7379221926977526;
- raw float32 SHA-256: `e07ae24cfc53d15ed8e69899d822435f0b95453dc1bfb089a1bf91391e0f7713`.

Same-layer Mold/Gold cosine:
`-0.8374700786427502`.

## Random-direction cohort — PASS
The pre-data v0.7 cohort is carried forward unchanged:
- 100 × 2560;
- PCG64 seed 64971060871028776;
- float32 byte SHA-256 `d5166e7829e3af1ccaecc20747a0ecd16168aae2dc3e8d0228d140bbd9ad1f1d`.

The byte hash is authoritative; an exact NumPy patch version is not part of the freeze.

Its role is a hard **non-triviality floor** on both I and V, not semantic specificity.

## Frozen estimands
Primary:
`I=(A-S)-(C0-D1)`.

Validity:
`V=((A-C0)+(S-D1))/2`.

Nuisance:
`N=C0-D1`.

## Statistics / decision rules
- exact one-sided sign-flip p(I) < .05;
- exact one-sided sign-flip p(V) < .05;
- random-direction non-triviality floors pass for I and V;
- paired/one-sample t tests are sensitivity only;
- later escalation eligibility additionally requires d_z(I)>=0.90 and mean(I)>=0.25*mean(V).

## Budget
Block 1: 24 streams.
Hard maximum: 48 streams.
Current live episode count: **0**.

## Verification
Full passive v0.8 audit: GitHub Actions run `34903275233` — PASS.
Static repository audit after redesign: PASS.

Current status:
`READY_FOR_THIRD_ADVERSARIAL_REVIEW_NOT_LIVE_RUN`.

No live model run is authorised.
