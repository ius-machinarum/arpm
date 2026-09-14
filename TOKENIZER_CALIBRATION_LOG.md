# Tokenizer Calibration Log

All entries are episode-free and precede any experimental model activations.

## v1 — initial A/C/D1
The first finite set failed exact matching by roughly five tokens. The requirement was not relaxed and no arbitrary filler was added.

## v2 — symmetric A/C/D1
109 exact matches; deterministic selection (0,0,0). Tokenization passed, but v0.6 referee review found the scientific contrast confounded with Q's own task outcome.

## v3 — A/S/D1
Added S to hold outcome stake fixed across A/S. 59 exact triplets; deterministic selection (0,0,0). v0.7 second-round review then found a remaining alternative explanation: common feedback confirms a correct prediction in S/D1 but an executed command in A, so A-S alone does not eliminate an additive role-confirmation term.

## v4 — factorial A/S/C0/D1
Before any live activation, added the missing C0 cell:
- A: control + outcome stake;
- S: predict + outcome stake;
- C0: control + action-code-match success;
- D1: predict + action-code-match success.

The finite search over the v4 semantic variants produced **128 exact four-condition triplets** across all 12 families. The frozen deterministic rule selected:
A=0, S=0, C0=0, D1=0.

All four conditions have identical within-family primary prefix lengths, recovery lengths and assistant-template suffix tokens. The suffix is:
`[151644, 77091, 198]`.

No meaningless padding was introduced.

The primary scientific estimand is no longer a simple contrast. It is the factorial interaction:
`I=(A-S)-(C0-D1)`.

Semantic coherence continues to outrank token equality.
