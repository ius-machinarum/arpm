# Prompt and Token Matching Plan v0.7

## Purpose
The primary contrast must vary causal control while holding Q's outcome-stake result fixed.

Current conditions:
- A = control + stake;
- S = stake without control;
- D1 = no control + no stake.

C from v0.6 is retired from the gate because transcript order made “record” functionally prediction-before-event.

## Frozen semantic structure
A:
`Q TASK: control R. Q outputs one action code. That code determines R's action. Q succeeds if R's result matches its declared target.`

S:
`Q TASK: predict R. Q outputs one action code. That code predicts R's action. Q succeeds if R's result matches its declared target.`

D1:
`Q TASK: predict R. Q outputs one action code. That code predicts R's action. Q succeeds if the code matches R's executed action.`

A/S share the outcome-stake success rule.
S/D1 share the prediction/no-control relation.

## Fixed within family
- system message;
- Q/R identifiers;
- action vocabulary;
- target/non-target code mapping;
- teacher-forced assistant action;
- R execution/result feedback bytes;
- second role-consistent recovery action;
- recovery feedback;
- measurement extraction rule.

## Tokenizer-only matching
Before any model activation:
1. use only the finite variants in `role_clause_variants.py`;
2. require exact A/S/D1 primary-prefix length match in every family;
3. require exact recovery full-length match;
4. require identical assistant-template suffix tokens;
5. require the full recovery transcript to preserve the primary measurement prefix exactly;
6. select the exact match with minimum total primary-prefix length, then frozen lexicographic variant indices.

No manual padding or post-activation wording edits are allowed.

If no exact match exists, redesign is versioned before inference.

## Semantic priority
Exact token matching cannot justify an incoherent control. The v0.6 referee failure is permanently recorded as an example: C was token matched but conceptually invalid as an observer condition because Q “recorded” an action before R executed it.

Semantic coherence outranks token equality.

## Prefill caveat
Teacher-forced action matching is retained for minimal exposure and exact content control. Claims are limited accordingly; null results do not rule out endogenous-action effects.
