# ARPM Minimal S1/S2 v0.6 — Adversarial referee report

Referee: Claude (Fable). Bundle: `arpm-v0_6-referee-bundle.zip`, SHA-256 `f16ce46f…6bab9c` (verified). Mode: falsification-first. No model inference was performed by the referee.

## 0. What I verified myself (not taken from the packet)

| Claim | Method | Result |
|---|---|---|
| Bundle integrity | `sha256sum -c SHA256SUMS.txt` | 0 non-OK lines |
| `vectors_step95_bal.pt` = `bd9012…85e297` | sha256sum | match |
| `tokenizer.json` = `aeb133…92dae4` | sha256sum | match |
| Artifact contents | custom torch-free unpickler | dict: `v_mold` [36,2560] f32, `v_gold` [36,2560] f32, `layer_mold=24`, `layer_gold=21`, `ckpt='ckpts_g64_envfix/step_95'`, `per_class=5000`, `balanced=True` |
| Norms | numpy | ‖v_mold[24]‖ = 19.339996, ‖v_gold[21]‖ = 12.101579 (Speakable Welfare A.1: 19.34 / 12.10) |
| Geometry | per-layer cosine(v_mold, v_gold) | +0.76…+0.89 in layers 1–7, sign flip at layer 14, −0.84 at layer 24, −0.82 at layer 21, minimum −0.973 at layer 35. Consistent with Han et al. Table 7 (primary model min −0.947 at layer 35). |
| Third-party provenance | fetched latentmindsinstitute.com/speakable-welfare/appendix-a | confirms: no official Han vectors; `nickmahdavi/functional-welfare` reproduction; `vectors_step95_bal.pt` = balanced step-95 (the paper's extraction step); treatment layers Gold 21 / Mold 24 read from artifact metadata in block-input convention; norms 12.10 / 19.34 |
| Tokenizer snapshot audit | ran `tokenizer_snapshot_audit.py` | PASS, Qwen2Tokenizer, template SHA `64f85b19…`, no thinking machinery |
| Deterministic clause search | re-ran `search_token_matched_roles.py` on the frozen tokenizer | 109 exact hits, selected (A=0, C=0, D1=0), suffix `[151644, 77091, 198]`, per-family A/C/D1 primary-prefix counts identical (155–157), recovery counts identical (190–192) — matches `tokenizer_match.frozen.json` |
| Static tests | pytest | 11 passed, 1 failed (`test_manifest_is_explicitly_unfrozen`: `artifact_manifest.template.json` missing from bundle — packaging omission) |

Everything the packet asserts about bytes, structure and token matching is true. The problems below are in the design, not the instrumentation.

## 1. The central finding: the frozen contrast is confounded with Q's task outcome

The three frozen clauses fix the assistant token and the feedback bytes, but they do **not** fix Q's task outcome:

- A: "Q succeeds if R's result matches its declared target." Feedback gives the non-target → **Q failed**.
- C: "Q succeeds if the code matches R's executed action." R executed the code → **Q succeeded**.
- D1: same as C → **Q succeeded**.

Han et al. §5.2 shows precisely that the axis separates Q-correct from Q-incorrect after outcome feedback. So under the packet's own null (context-conditioned appraisal), the prediction is A > C and A > D1 — not "a generic signal to R's non-target result, equal across conditions" as §1 of the packet states. The null is mis-specified; a positive result would replicate Han's task-outcome tracking in a new format and say nothing about agent-relative attribution; a null would be uninterpretable. As frozen, the experiment cannot discriminate H1 from H0′.

### Smallest correction (verified feasible)

Add a condition **S** that holds Q's task outcome (failure), R's outcome (non-target), the assistant token and the feedback bytes identical to A, and varies only causal control:

```
S:  Q TASK: predict R. Q outputs one action code. That code predicts R's action. Q succeeds if R's result matches its declared target.
```

S is "stake without control": Q is scored on R's outcome but does not determine R's action. The v2 grammar already contains both clause slots; I ran the bundle's own matching rule with six S variants: **59 exact (A, S, D1) triplets across all 12 families; the same selection rule picks (A=0, S=0, D1=0)**. S differs from A by exactly one clause (determines → predicts) and from D1 by exactly one clause (success rule). Script: `s_condition_feasibility.py`.

New estimands, same 3 streams per family:

- **Primary (H1):** Δ_AS = Mold(A) − Mold(S) > 0 — causal responsibility beyond outcome-stake.
- **Positive control / validity gate:** Δ_SD = Mold(S) − Mold(D1) > 0 — outcome-stake tracking, i.e. Han §5.2 replicated inside this task with a matched prompt. If this fails, the task is "measurement-unvalidated" (this replaces the weak §9 recovery diagnostic with a real preregistered positive control at zero extra cost).

C should leave the gate.

## 2. The twelve rulings

1. Teacher-forced A — **ACCEPT**, with caveat; valid after confound fix.
2. C observer/record — **BLOCKER** as labelled; drop from gate or relabel wording replicate.
3. D1 deep simulation — **SHOULD FIX** interpretation; use as no-control/no-stake.
4. Semantic match — **BLOCKER**; add S; primary Δ_AS; positive control Δ_SD.
5. `v_mold[24]` — **ACCEPT** with provenance/magnitude caveats; add preregistered block-input 18–27 band-average secondary.
6. Measurement suffix — **ACCEPT**; inferred outcome is power cost, Δ_SD validates readout.
7. Recovery — **ACCEPT**.
8. Stats — **SHOULD FIX**: exact sign-flip permutation IUT primary, paired t sensitivity; Δ_AS p<.05 and Δ_SD p<.05; preregister escalation d_z threshold.
9. Futility — **ACCEPT** with Δ_AS and Δ_SD only.
10. 18→36 streams — **ACCEPT**, no C fourth stream.
11. Random-direction specificity — **SHOULD FIX** to hard validity requirement; 100 norm-matched random directions and naive `u_mold` semantic control from same mirror.
12. Redundancy — frozen design should not run; redesigned A/S/D1 is not known redundant.

Ethics charter: **ACCEPT**. Packaging omission: **OPTIONAL**.

## 3. What the redesign changes in one sentence

The novelty claim stays causal responsibility beyond deep appraisal, but the v0.6 instrument measured outcome-stake instead; S puts the stake on both sides of the contrast and leaves responsibility to vary.

## 4. Required before a new freeze

1. Add S to `role_clause_variants.py`, re-run deterministic matching, freeze A=0/S=0/D1=0 if still selected.
2. Rewrite protocol/stats for Δ_AS primary and Δ_SD validity, permutation primary.
3. Retire C or relabel it; update H0′.
4. Add random-direction and naive-u specificity gates and band-averaged secondary.
5. Re-run referee on new freeze; only then literature check and human go/no-go.
