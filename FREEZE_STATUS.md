# Pre-live Freeze Status v0.4

**Overall: NOT FROZEN / NO LIVE MODEL RUNS.**

## Verified from public sources
- Candidate model: `Qwen/Qwen3-4B-Instruct-2507`.
- Pinned tokenizer/template revision: `cdbee75f17c01a7cc42f958dc650907174af0554` (Qwen commit updating `tokenizer_config.json`).
- Official Hugging Face file metadata reports `tokenizer.json` SHA-256 `aeb13307a71acd8fe81861d94ad54ab689df773318809eed3cbe794b4492dae4`.
- The pinned 2507 chat template ends a generation prompt with the ordinary assistant header and contains no Qwen3 thinking-template machinery.
- External-vector target: `vectors_step95_bal.pt`, mirrored by `Teachafy/speakable-welfare-axes-artifacts`, with stated upstream provenance `nickmahdavi/functional-welfare` (third-party reproduction of Han et al. 2026).
- Published independent methodology fixes the trained treatment positions to Mold block-input layer 24 and Gold block-input layer 21, with reported norms about 19.34 and 12.10 respectively.

## Not yet byte-frozen
- exact `vectors_step95_bal.pt` bytes / local SHA-256 / byte size;
- exact mirror repository revision used to acquire those bytes;
- object-key/index mapping inside that `.pt` file;
- local `tokenizer_config.json` SHA-256;
- A/C/D1 exact token-match result.

The current environment cannot fetch the required Hugging Face/Xet bytes into the container and does not contain `transformers`/`tokenizers`. This is an instrumentation limitation, **not a pass**.

## v0.4 completion route
`run_episode_free_audit.py` now orchestrates the remaining gates using only a vector artifact and tokenizer-only snapshot. It rejects model-weight-like files in the tokenizer snapshot and emits `episode_free_audit.json` only if:
1. tokenizer bytes and pinned `tokenizer.json` hash pass;
2. vector structure can be safe-loaded with `weights_only=True`;
3. explicit Gold/Mold mapping reconciles dimension/layer/norm references;
4. a role-clause triplet is found solely among the precommitted variants;
5. the final tokenizer audit re-checks **that exact selected triplet** across all 12 families.

A passing output status is `READY_FOR_ADVERSARIAL_REVIEW_NOT_LIVE_RUN`. It is deliberately not authority to load the language model.

## v0.5 acquisition status
A deterministic passive acquisition helper is now included. In the current ChatGPT execution environment, direct Hugging Face/Xet byte downloads and package installation are network-blocked, so the helper itself has been statically tested but the remote bytes have **not** been falsely marked acquired. The next legitimate state transition occurs only when `passive_acquisition_manifest.json` is produced on a network-capable environment and the downstream byte/token audits pass.
