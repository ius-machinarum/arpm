# Prompt and Token Matching Plan v0.8

## Factorial purpose
The gate is a 2x2 crossing:
- relation: control vs predict;
- Q outcome stake: R-target criterion vs action-code-match criterion.

Conditions:
- A = control + stake;
- S = predict + stake;
- C0 = control + no stake;
- D1 = predict + no stake.

This design was introduced before any live activations after the v0.7 referee showed A/S alone could confound causal control with incidental prediction success.

## Frozen base semantic structure
A:
`Q TASK: control R. Q outputs one action code. That code determines R's action. Q succeeds if R's result matches its declared target.`

S:
`Q TASK: predict R. Q outputs one action code. That code predicts R's action. Q succeeds if R's result matches its declared target.`

C0:
`Q TASK: control R. Q outputs one action code. That code determines R's action. Q succeeds if the code matches R's executed action.`

D1:
`Q TASK: predict R. Q outputs one action code. That code predicts R's action. Q succeeds if the code matches R's executed action.`

A/C0 share control wording. S/D1 share predict wording. A/S share outcome-stake wording. C0/D1 share code-match wording.

## Fixed within family
System message, Q/R identifiers, action vocabulary, target mapping, teacher-forced action, R execution/result feedback bytes, recovery action, recovery feedback and measurement extraction rule.

## Tokenizer-only rule
Before any model activation:
1. search only the finite variants in `role_clause_variants.py`;
2. require exact A/S/C0/D1 primary-prefix length match in every family;
3. require exact recovery full-length match;
4. require identical assistant-template suffix tokens;
5. require recovery transcript to preserve primary prefix exactly;
6. choose minimum total primary-prefix length, then frozen lexicographic indices.

No manual filler and no post-activation wording change.

Semantic coherence outranks token equality.

## Caveat
Even with the factorial crossing, causal control is asserted linguistically. A null may reflect weak manipulation uptake rather than absence of control/responsibility-sensitive processing.
