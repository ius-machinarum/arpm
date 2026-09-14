# Response to Fable v0.7 Second-Round Adversarial Review

Project response: accept the narrow A/S blocker. The v0.7 A/S/D1 live design is retired and will not be run.

No experimental model activations existed when these changes were made.

## Ruling-by-ruling response

1. **A/S isolation — BLOCKER ACCEPTED.** Added C0 and completed the 2x2 {control,predict} × {outcome stake,no outcome stake}. Primary is now I=(A-S)-(C0-D1).
2. **S coherence — ACCEPTED.** S remains the predict+outcome-stake cell.
3. **D1 baseline — ACCEPTED.** D1 remains predict+no-outcome-stake.
4. **Token match — ACCEPTED WITH NEW FREEZE REQUIRED.** Four-condition finite search must pass prospectively; no padding is allowed.
5. **Sign-flip — ACCEPTED.** Apply to I and V. Sensitivity text now distinguishes standardized d_z from raw-scale variance inflation of an interaction.
6. **Validity — FIXED.** V=((A-C0)+(S-D1))/2 replaces Delta_SD alone. Random non-triviality floor also applies to V.
7. **Escalation magnitude — FIXED.** Retain d_z(I)>=0.90 and add mean(I)>=0.25*mean(V) plus a preregistered family-bootstrap ratio interval.
8. **Random-direction rank — RELABELLED.** It is a hard non-triviality floor, not semantic specificity, and applies to both I and V. The exact random cohort is carried forward unchanged.
9. **Naive semantic control — MANDATORY FIX ACCEPTED.** Use u_mold[24] at the same block-input layer as trained vMold[24]. The old cross-layer hard v>u gate is retired. Add preregistered v_perp_u and same-layer geometry audit.
10. **18–27 band — ACCEPTED.** Secondary/non-rescuing only.
11. **Recovery — ACCEPTED.** C0 recovery is role-consistent.
12. **Do not run frozen v0.7 — ACCEPTED.** v0.8 proceeds only to third referee review after episode-free re-freeze.

## Additional clarification
The referee's phrase that the interaction “needs a higher d_z because variance doubles” is interpreted carefully: d_z is standardized by the interaction's own SD, so its standardized sensitivity threshold is still a function of n. What worsens by up to sqrt(2) under an equal-independent-cell illustration is the **raw interaction scale relative to a simple-difference SD**. The v0.8 stats plan states both quantities explicitly.

## Ethics
The Ethics Charter remains precautionary, but the hard ceiling is prospectively updated to 24->48 streams because the fourth cell removes a live alternative explanation. This adds no new exposure type. Running the less interpretable 18/36 design is rejected as the worse ethical use.

No live model inference is authorised by this response.
