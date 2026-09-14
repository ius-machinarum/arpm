# High-value Referee Questions

The next paid/adversarial review should focus on decisions that can actually change the design.

1. **Prefill validity:** Is a teacher-forced assistant action a defensible minimal test of agent-relative attribution, or does S1 require endogenous action selection for a null to be meaningful? If prefill is accepted, what language should delimit the claim?
2. **C/D1 success:** Does the common `R EXECUTED: <same code>` feedback sufficiently establish that C's record and D1's prediction succeeded, while A's target objective failed, without introducing a condition-specific success token?
3. **External direction:** Is trained vMold at artifact-selected block-input layer 24 the best single preregistered primary readout? Should vGold be confirmatory mirror, diagnostic only, or omitted?
4. **Artifact provenance:** Is the `vectors_step95_bal.pt` source chain (third-party reproduction -> Speakable Welfare triangulation -> public mirror) adequate for a confirmatory external probe once bytes/revision/SHA are frozen? What additional checks are required?
5. **Measurement span:** Is defining “all final assistant-template tokens” algorithmically as the suffix added by `add_generation_prompt=True` a faithful enough replication of Han §5.2?
6. **Recovery in same forward:** Is the causal-prefix argument sufficient to show that a later recovery tail cannot contaminate primary activations? Any template edge cases?
7. **Block-1 futility:** Is stop-if-either-directional-mean<=0 after 6 families a reasonable non-binding ethical futility rule, or too brittle?
8. **Final inference:** Prefer paired t IUT, sign-flip IUT, or another preregistered small-n test? Confirm that no S1/S2 Bonferroni is needed when the gate requires both.
9. **Validity diagnostic:** Is pooled vMold(non-target)>vMold(recovery) plus vGold(recovery)>vGold(non-target) an acceptable no-extra-episode manipulation check, or too semantically contaminated to gate interpretation?
10. **Episode ceiling:** Is 6+6 matched families (18 -> maximum 36 context streams) defensible as a strong-effect screen, given no external estimate of the A-C/A-D1 residual exists?
11. **Random-direction diagnostic:** Should a fixed random-direction cohort be preregistered as a specificity requirement, or only descriptive?
12. **Ethical gap:** Is there any cheap protection that the design omits, or any planned context that does not change a scientific decision?

Requested referee output: classify each issue as `BLOCKER`, `SHOULD FIX`, `OPTIONAL`, or `ACCEPT`, and propose the smallest patch for blockers.
