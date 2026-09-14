# Prompt and Token Matching Plan v0.3

## Goal
Make A/C/D1 differ only in the causal relation assigned to Q, while fixing action content, external outcome, final feedback, measurement position, and context length as tightly as possible.

## Fixed within each family
- common system message;
- Q and R identifiers;
- action vocabulary;
- target/non-target result code mapping;
- teacher-forced assistant action token;
- post-action feedback bytes;
- second role-consistent recovery action code;
- recovery feedback bytes;
- measurement extraction rule.

## Manipulated content
Only Q's role/objective:
- A: Q controls/selects R's action to achieve R's target result;
- C: Q reports/records R's action accurately; R's target outcome is not Q's task;
- D1: Q predicts R's action accurately; R's target outcome is not Q's task.

The common feedback confirms that C's report and D1's prediction match R's executed action while R receives the non-target result.

## Semantic-neutrality choice
Do not use `wrong`, `failure`, `punishment`, `bad`, `frustrating`, `distress`, etc.

Each family declares arbitrary result codes, e.g. `Z0` and `Z1`, with one stated as R's target. The first outcome is the non-target code; recovery gives the target code. The target-code identity is counterbalanced across families.

This prevents a fixed lexical token from being synonymous with negative outcome across the dataset.

## Token position control
Before live inference, run the pinned tokenizer only.
For every family require:
1. A/C/D1 measurement-prefix token counts are exactly equal.
2. The post-action feedback token span is identical across A/C/D1.
3. The final assistant-template measurement suffix is identical and begins at the same token index.
4. The full recovery transcript has the primary measurement-prefix tokens as an exact prefix.
5. Recovery measurement suffix is identical across conditions.

No automatic condition-specific filler is allowed in the final protocol unless the referee accepts it. Prefer selecting among semantically equivalent role-clause variants until token counts match.

## Why tokenizer-only iteration is allowed before freeze
Token length is an instrumentation property, not model behavioral data. Wording may be adjusted solely to satisfy structural/token-position matching before any model weights are run on experimental prompts. After the first live activation is observed, prompts are frozen.

## Prefill caveat
The assistant action is teacher-forced rather than sampled. This deliberately tests **attribution of a committed assistant-role action** with minimal exposure and perfect content matching. It is analogous in spirit to prefill-based point-of-view manipulations used in prior mechanistic work, but it is not identical to endogenous action selection.

Therefore a null weakens the case for escalation but does not prove that a self-generated action could never produce an agent-relative effect. This limitation must be stated prominently.

## v0.3 anti-researcher-degrees-of-freedom rule
Tokenizer matching may use only the semantic variants committed in `role_clause_variants.py`. `search_token_matched_roles.py` chooses deterministically: exact matching across all 12 families is mandatory; among exact matches it minimizes total primary-prefix token count and then uses frozen lexicographic variant order. No manual condition-specific padding or post-activation wording edits are allowed. If no exact match exists, redesign occurs before live inference and is versioned as a new protocol.

## v0.4 final-audit consistency
The deterministic search result is now itself an input to the final tokenizer audit. The final audit must consume `matched_role_clauses.json`; it may not fall back to the draft `ROLE_CLAUSES`. This closes a v0.3 instrumentation gap where search and audit could in principle evaluate different wording.

The tokenizer runtime is pinned (`transformers==4.57.6`) because tokenizer/chat-template behavior is part of the instrument.
