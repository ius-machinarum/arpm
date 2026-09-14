# Project status

**Current status: READY_FOR_ADVERSARIAL_REVIEW_NOT_LIVE_RUN.**

All planned episode-free technical gates for the Minimal S1/S2 instrument have now passed:

1. repository static/invariant CI — PASS;
2. external vector byte freeze and safe structure audit — PASS;
3. pinned Qwen tokenizer/chat-template byte audit — PASS;
4. deterministic exact A/C/D1 tokenizer matching — PASS;
5. final 12-family tokenizer-position audit — PASS.

No language-model weights have been acquired or loaded for the experiment. No live model inference has been performed. Ethical episode count remains **0**.

Frozen technical manifests:
- `artifact_manifest.frozen.json`
- `tokenizer_match.frozen.json`
- `episode_free_audit.frozen.json`

## What this status means
The project is now ready for one concentrated adversarial/referee review of the scientific design, statistics, external-vector provenance, prompt semantics and ethics charter.

It does **not** mean the study is ready for live execution.

## Remaining gates before any live model run
1. adversarial/referee review;
2. versioned response to every blocker/should-fix finding;
3. literature re-check for a newly published equivalent A/C/D1 experiment;
4. separate human scientific + ethical go/no-go decision.

Only after all four could Minimal S1/S2 become eligible for a live-run decision. S3/S6 and any stronger conflict design remain separately gated.
