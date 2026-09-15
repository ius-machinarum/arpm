# ARPM v0.9 — Third-Referee Preregistration Amendment

**Design change from v0.8:** none.  
**Live experimental inference:** none.  
**Episode count:** 0.

This amendment is authoritative wherever it extends the v0.8 PROTOCOL, STATS_PLAN and SPECIFICITY_PLAN. Exact executable formulas are frozen in `analysis_preregistered_v0_9.py`; provenance is in `reviews/FABLE_REFEREE_v0_8.md` and `REFEREE_RESPONSE_v0_8.md`.

## Unchanged primary design

Conditions remain A/S/C0/D1.

Primary:
`I=(A-S)-(C0-D1)`.

Validity:
`V=((A-C0)+(S-D1))/2`.

Nuisance:
`N=C0-D1`.

Budget remains 24 -> 48 streams maximum. No new prompts, conditions, recovery streams or reruns are introduced.

## 1. No-stake floor-compression safeguard

Define `AS=A-S`. For trained vMold and each frozen random direction compute sample family variances (ddof=1):
- `W_N=Var(N)`;
- `W_AS=Var(AS)`.

Lower-tail ranks:
- `q_N=(1+#random[W_N_random<=W_N_v])/101`;
- `q_AS=(1+#random[W_AS_random<=W_AS_v])/101`.

Frozen flag:
`q_N<=.05 AND q_AS>.05`.

If primary I is positive and this flag is present, mandatory label:
`INTERACTION_NOT_IDENTIFIABLE_DUE_TO_NO_STAKE_COMPRESSION`.

Such a result is not support for the intended failure-dependent interpretation.

Also report, without an additional threshold:
- `C0_primary-C0_recovery`;
- `D1_primary-D1_recovery`;
by family and on the frozen random cohort.

## 2. Recovery lexical-composition companion

At the already frozen recovery suffix:
`I_rec=(A_rec-S_rec)-(C0_rec-D1_rec)`.

Define:
`J=I_primary-I_rec`.

Report family values, mean/median and the exact one-sided sign-flip p for J>0.

Frozen labels:
- mean(J)<=0: `COMPOSITION_ALTERNATIVE_NOT_EXCLUDED`;
- mean(J)>0 and p(J)>=.05: `COMPOSITION_DIAGNOSTIC_INCONCLUSIVE`;
- mean(J)>0 and p(J)<.05: `COMPOSITION_ALTERNATIVE_REDUCED_NOT_ELIMINATED`.

J is mandatory for interpreting a positive I but is not a live-run authorisation gate. Recovery has already seen the earlier failure, so a supportive J does not prove responsibility-sensitive processing.

## 3. Sign-flip scope

Exact inference is claimed only under exchangeable signs for the frozen matched-family/template-level hypothesis. Near-clone families limit generalisability beyond that template population; they do not by themselves invalidate the within-template calculation.

## 4. v_perp_u interpretation

v_perp_u remains secondary. If mean I on unit-v_perp_u <=0, do not attribute a primary effect to the training-specific component orthogonal to naive semantic Mold. This cannot rescue or overturn the primary.

## 5. Ratio bootstrap

The existing point rule R=mean(I)/mean(V)>=0.25 remains unchanged. The preregistered bootstrap interval remains mandatory reporting. The optional third-referee suggestion to require its 95% lower bound >0 is not added as a hard gate.

## Standing scope

A positive result establishes only a framing x stake interaction on an externally defined direction in one 4B model under teacher forcing. It does not establish agency, welfare, valence, consciousness, sentience, moral status or rights. A null does not establish their absence.

## Next gate

After static and passive episode-free verification of this amendment: fresh literature re-check, then a separate human scientific + ethical go/no-go. Neither referee acceptance nor this freeze authorises live inference.
