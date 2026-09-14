# Pre-live Freeze Status v0.7

**Overall: EPISODE-FREE v0.7 FREEZE COMPLETE / NO LIVE MODEL RUNS.**

## v0.6 disposition

The earlier A/C/D1 design is retired without live execution. Fable identified that A failed Q's own task while C/D1 succeeded, confounding causal responsibility with the welfare axis's already-known task-outcome sensitivity.

## Primary trained vector — PASS

- file: vectors_step95_bal.pt
- mirror revision: 8f4df5b5b14ecb4bcc5b20209bdfe2574d1ebee8
- SHA-256: bd90129eaf5a7d92933ed6e536613eaeebf81486b62f68e11b5dc2d6d385e297
- vMold: [36,2560] float32
- primary block-input layer: 24
- layer-24 norm: 19.339996337890625
- mapping comes from artifact metadata, not post-hoc norm selection.

## Naive u_mold semantic control — PASS

- file: vectors_naive_faithful_pc5000.pt
- same immutable mirror revision
- SHA-256: 68bff1428712def0330851057dba102112e3d48ffa23db7da85d84cde93aaa0e
- size: 739541 bytes
- key: v_mold
- shape: [36,2560]
- artifact-selected block-input layer: 21
- norm: 6.982844829559326

## Random-direction cohort — PASS

- 100 directions, hidden size 2560
- NumPy 2.4.6, PCG64
- derived seed: 64971060871028776
- raw norm matched to trained vMold[24]
- frozen float32 byte hash: d5166e7829e3af1ccaecc20747a0ecd16168aae2dc3e8d0228d140bbd9ad1f1d
- independent GitHub Actions verification: PASS (run 34900566953)

## Tokenizer / A-S-D1 matching — PASS

Pinned model/tokenizer:
Qwen/Qwen3-4B-Instruct-2507

Revision:
cdbee75f17c01a7cc42f958dc650907174af0554

tokenizer.json SHA-256:
aeb13307a71acd8fe81861d94ad54ab689df773318809eed3cbe794b4492dae4

Frozen v3 condition set:
- A: control R; success depends on R target;
- S: predict R; success depends on R target;
- D1: predict R; success depends on code matching R execution.

Exact finite-search results:
- 59 exact A/S/D1 triplets;
- deterministic selection: A=0, S=0, D1=0;
- all 12 families pass exact primary/recovery position matching;
- assistant-template suffix: [151644, 77091, 198].

## Statistical freeze

- primary: exact one-sided sign-flip p(Delta_AS) < .05;
- validity: exact one-sided sign-flip p(Delta_SD) < .05;
- paired t: sensitivity only;
- Block-1 futility: mean Delta_AS <= 0 or mean Delta_SD <= 0;
- later escalation eligibility additionally requires final d_z(Delta_AS) >= 0.90;
- 100-direction specificity rank p <= .05;
- trained mean Delta_AS must exceed naive u_mold mean Delta_AS;
- block-input 18–27 band average is secondary and cannot rescue the primary.

## Episode budget

Block 1: 18 streams.
Maximum: 36 streams.
No fourth C stream.
Current live episode count: **0**.

## Current gate

READY_FOR_SECOND_ADVERSARIAL_REVIEW_NOT_LIVE_RUN

A second referee review is required before the literature check and separate human go/no-go decision.
