# Response to Fable v0.8 Third-Round Adversarial Review

Project response: accept both required SHOULD FIX items. The experimental 2×2 design is unchanged. v0.9 is an analysis/preregistration freeze only.

No live experimental model inference existed when these changes were made. Episode count remains 0.

## Ruling-by-ruling response

1. **Additive A/S role alternative — ACCEPT acknowledged. Two non-additive alternatives — SHOULD FIX accepted.**
   - Add a preregistered no-stake floor-compression diagnostic using the same frozen activations and 100-direction random cohort.
   - Add recovery interaction `I_rec` and companion contrast `J = I_primary - I_rec`.
   - Neither addition permits new streams or reruns.
2. **C0 coherence — ACCEPT acknowledged.** C0 remains control scored on execution fidelity. No wording change.
3. **V validity — ACCEPT acknowledged.** Existing lexical caveat remains explicit.
4. **Manipulation uptake — ACCEPT acknowledged.** Claim remains limited to the frozen framing under teacher forcing.
5. **Four-cell tokenizer matching — ACCEPT acknowledged and independently verified.** No prompt change.
6. **Sign-flip inference — ACCEPT with scope sentence.** Exactness is claimed only under exchangeable signs for the frozen matched-family/template-level hypothesis; near-cloning limits generalisation rather than within-template validity.
7. **24→48 budget — ACCEPT acknowledged.** No episode-budget change.
8. **Random-direction floors — ACCEPT acknowledged.** Remain non-triviality floors, not semantic-specificity claims.
9. **uMold[24] and v_perp_u — ACCEPT as secondary.** Add interpretation rule: if `I(v_perp_u) <= 0`, a primary effect is not attributed to the training-specific component orthogonal to the naive semantic Mold direction.
10. **vGold and 18–27 band — ACCEPT acknowledged.**
11. **d_z and R thresholds — ACCEPT acknowledged.** The optional bootstrap-lower-bound gate is not promoted to a hard decision rule; the preregistered bootstrap interval and undefined-denominator count remain reported.
12. **No remaining design blocker conditional on the two preregistrations — ACCEPTED.** v0.9 completes those preregistrations before any literature/go-no-go stage.

## v0.9 prospective operationalisation

### A. No-stake compression diagnostic

For every analysis direction, define family-wise:
- `N_i = C0_i - D1_i`;
- `AS_i = A_i - S_i`.

For trained vMold and each of the 100 frozen random directions compute:
- `W_N = Var_i(N_i)`;
- `W_AS = Var_i(AS_i)`.

Use lower-tail random-cohort ranks:
- `q_N = (1 + #{j: W_N(random_j) <= W_N(vMold)}) / 101`;
- `q_AS = (1 + #{j: W_AS(random_j) <= W_AS(vMold)}) / 101`.

Prospective compression flag:
- `q_N <= .05` AND `q_AS > .05`.

This flag encodes the referee's specific concern: a vMold-specific collapse of nuisance variance in the no-stake row without a corresponding collapse of the stake-row A-S variance.

Also report, without an additional post-hoc threshold, C0 and D1 primary projections relative to their same-family recovery-success projections. This location diagnostic is corroborative and is not a rescue route.

If the compression flag is present and primary I is otherwise positive, the mandatory label is:

`INTERACTION_NOT_IDENTIFIABLE_DUE_TO_NO_STAKE_COMPRESSION`.

Such a result is not counted as support for the intended failure-dependent interpretation.

### B. Recovery lexical-composition companion

At the already frozen recovery assistant suffix compute:
- `I_rec,i = (A_rec,i - S_rec,i) - (C0_rec,i - D1_rec,i)`;
- `J_i = I_primary,i - I_rec,i`.

Report:
- all family-level `I_rec` and `J`;
- mean/median;
- exact one-sided sign-flip p for `J > 0`;
- sensitivity t test.

Interpretation:
- a pure time-stable lexical composition predicts `J ≈ 0`;
- a failure-dependent pattern predicts `J > 0`.

`J` is a mandatory companion interpretation readout for a positive primary I, not an extra run-authorisation gate.

If primary I passes but `J` does not support `J > 0`, use the mandatory label:

`COMPOSITION_ALTERNATIVE_NOT_EXCLUDED`.

The recovery header has already seen the earlier failure, so passing J does not by itself prove responsibility-sensitive processing.

## Scope lock

Any positive result is described only as:

> a framing × stake interaction on an externally defined direction in one 4B model under teacher forcing.

It does not establish agency, welfare, valence, consciousness, sentience, moral status or rights. A null does not establish their absence.

## Next gate

After v0.9 documentation, executable-analysis checks and episode-free CI pass:
1. fresh literature re-check;
2. separate human scientific + ethical go/no-go.

No referee acceptance and no v0.9 freeze authorises live inference.
