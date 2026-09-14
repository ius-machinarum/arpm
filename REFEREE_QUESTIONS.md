# v0.7 Second-Round Adversarial Referee Questions

Please review the redesign as a fresh freeze, not as a request to defend v0.6.

Classify each material issue as `BLOCKER`, `SHOULD FIX`, `OPTIONAL`, or `ACCEPT`.

1. Does A/S now isolate causal control from Q outcome stake adequately?
2. Is S semantically coherent as “stake without control,” or does the success rule create another hidden confound?
3. Is D1 correctly limited to a no-control/no-stake positive-control baseline rather than “deep simulation”?
4. Does the exact A/S/D1 tokenizer matching preserve semantic coherence without introducing padding artifacts?
5. Is exact one-sided sign-flip testing the correct primary small-n inference?
6. Is Delta_SD an adequate positive-control/measurement-validity gate for inferred task outcome?
7. Is the d_z >= 0.90 later-escalation threshold defensible as an explicit decision threshold?
8. Is the frozen 100-direction rank criterion an appropriate hard specificity gate?
9. Is the naive u_mold control specified strongly enough without making the gate circular?
10. Is block-input 18–27 band-average a defensible secondary robustness definition?
11. Does the recovery remain role-consistent for S and ethically useful?
12. After these fixes, is any blocker still strong enough that the 18->36 live Minimal Gate should not be run?

A second-round ACCEPT does not authorise live inference. Fresh literature review and a separate human go/no-go decision remain mandatory.
