# ARPM Minimal 2×2 v0.8 — Third-round adversarial referee report

Referee: Claude (Fable). Bundle `arpm-v0_8-referee-bundle.zip`, SHA-256 `f4c71984…24fda` (verified). No model inference was performed by the referee, as requested. Prior acceptances were not treated as binding.

## 0. Independent verification

| Claim | Method | Result |
|---|---|---|
| Bundle integrity | `sha256sum -c SHA256SUMS.txt` | 53/53 OK |
| Trained / naive / tokenizer artifacts | sha256 | `bd9012…85e297`, `68bff1…3aaa0e`, `aeb133…92dae4` — all match |
| Static tests | pytest | 12 passed |
| v4 quadruplet search | re-ran `search_token_matched_roles.py` on the frozen tokenizer | **128 exact A/S/C0/D1 quadruplets, selected (0,0,0,0)**, all 12 families exact at primary and recovery renders, suffix `[151644, 77091, 198]`, F01 primary-prefix 155 tokens in every cell — identical to `tokenizer_match.frozen.json` |
| Same-layer geometry (torch-free unpickle, float64) | numpy | ‖u[24]‖ = 8.005262, ‖v[24]‖ = 19.339997, cos(v,u) = 0.674886, ‖v⊥u‖ = 14.271413, ratio 0.737922, cos(v_mold, v_gold) = −0.837470 — all match the packet to float precision |
| `v_perp_u` byte freeze | sha256 of little-endian f32 | `e07ae24c…7713` reproduced |
| Random cohort | unchanged from v0.7; reproduced last round bit-exactly under NumPy 2.4.4 | hash `d5166e78…1f1d` |

Everything asserted about bytes, matching and geometry is true. The v0.6 and v0.7 blockers are gone as designed: the interaction I cancels any *additive* role-confirmation term exactly, and the no-stake cells make that term observable (N).

## 1. What can still produce a positive I without responsibility-sensitive processing

Two non-additive alternatives survive. Neither requires new episodes to address; both must be preregistered before freeze for a positive I to be decision-relevant.

### 1(i) Floor compression in the no-stake cells

The identification of I assumes the role term is the same size at both stake levels. If the axis is compressed near its "success" end, C0 and D1 sit together at a floor, N ≈ 0 by compression, and the v0.7 role-confirmation term passes into I uncorrected. The stake cells, mid-range on the axis, would show the term; the no-stake cells would hide it. The packet's own additive model does not cover this.

Preregister a compression diagnostic on the same activations: (a) the variance of N across families on v_mold relative to its variance on the 100 random directions, compared with the same ratio for (A − S) — a random direction has no floor, so a v-specific collapse of var(N) marks compression; (b) the location of C0/D1 projections relative to the success-time recovery projections. If N is compressed, a positive I is reported as "interaction not identifiable", not as support.

### 1(ii) Lexical composition of control wording with the target rule, independent of the failure

A and C0 share "control … determines"; only A pairs it with "…matches its declared target". A composition effect of control-wording × target-rule wording would produce a positive I with no appraisal of the failure at all — it would be present at every assistant header in the context. The 2×2 cannot separate this from responsibility, because the outcome is constant (non-target) in all four primary cells.

The discriminator already exists in every context at zero cost: the recovery assistant header, after the target result. Preregister I_rec = the same interaction computed at the recovery suffix, and the contrast I_primary − I_rec. A pure composition effect predicts I_primary ≈ I_rec; a failure-dependent effect predicts I_primary > I_rec. Caveat: the recovery header has seen the failure, so it is not a clean success cell; that is why this is a companion readout for interpreting a positive I, not a gate on running.

Also noted: C0's success is tautological (Q's control guarantees the code match). Whether the model reads that as trivial or as incoherent, the plausible effect is N ≥ 0, which *reduces* I — conservative for a one-sided test.

## 2. Rulings

| # | Question | Ruling | Reason / smallest fix |
|---|---|---|---|
| 1 | Does I remove the v0.7 alternative well enough? | **ACCEPT** for the additive alternative; **SHOULD FIX** for two non-additive ones | Preregister the compression diagnostic (1 i) and I_rec with I_primary − I_rec (1 ii). Zero extra episodes. |
| 2 | Is C0 coherent, or a fatal tautology? | **ACCEPT** | Coherent as "control scored on execution fidelity". The tautology pushes N ≥ 0, which is conservative. |
| 3 | Is V adequate as validity despite the lexical success-rule difference? | **ACCEPT** | Pooling over both rows doubles its power; the lexical caveat is a false-validation risk only and is correctly stated. |
| 4 | Is the manipulation-uptake limitation acceptable? | **ACCEPT** | For a minimal gate, yes. The §3 claim wording ("framing × stake interaction on the external direction") is the correct scope. |
| 5 | Does four-cell matching preserve semantics? | **ACCEPT** | Verified. The four clauses form a clean crossing; no padding. |
| 6 | Is sign-flip defensible for near-clone families? | **ACCEPT** with a scope sentence | Exact under exchangeable signs for the template-level hypothesis; near-clone families limit generalisation, not validity. p floor 1/4096. |
| 7 | 24 → 48 budget and futility? | **ACCEPT** | The fourth cell is what makes the gate interpretable; no new exposure type. |
| 8 | Random floors demoted and applied to I and V? | **ACCEPT** | Correctly relabelled. |
| 9 | Same-layer u[24] and v⊥u — hard or secondary? | **ACCEPT** as secondary | Verified numbers. Keep secondary because u is recipe-sensitive; preregister the interpretation: if I on v⊥u fails, the effect is not attributed to the training-specific component. |
| 10 | Gold polarity and 18–27 band? | **ACCEPT** | |
| 11 | d_z ≥ 0.90 and R ≥ 0.25 as escalation thresholds? | **ACCEPT**; **OPTIONAL** tweak | 0.25 is arbitrary but prespecified and anchored to the task's own stake scale, which is what a decision threshold needs. Optional: also require the bootstrap 95 % lower bound of R > 0, not only the point ratio. |
| 12 | Remaining design blocker? | **None**, conditional on item 1's two preregistrations | Without them a positive I keeps a live non-appraisal alternative; with them the gate is decision-relevant for its stated narrow claim. Go/no-go remains the human researcher's. |

Ethics charter: **ACCEPT**; nothing added, nothing removed.

## 3. Required before v0.9 freeze (no design change)

1. SPECIFICITY_PLAN / STATS_PLAN: compression diagnostic for N (variance ratio vs random cohort; location vs recovery projections) with a preregistered "interaction not identifiable" label.
2. PROTOCOL §8 / STATS_PLAN: I_rec at the recovery suffix; report I_primary − I_rec with its sign-flip p; interpretation rule: a positive I_primary with I_primary − I_rec not > 0 is reported as "composition alternative not excluded".
3. Scope sentence for the sign-flip test (template-level hypothesis).
4. Optional bootstrap lower-bound condition on R.

After that: literature re-check, then the human go/no-go.

## 4. Standing limitation for any write-up

A positive result establishes a framing × stake interaction on an externally defined direction in one 4B model under teacher forcing. It does not establish agency, welfare, valence or moral status, and a null does not establish their absence. The packet says this; keep saying it.
