# Episode-free completion path (v0.4)

This is the only supported route from DRAFT to READY FOR ADVERSARIAL REVIEW.
It must be run **without model weight files present**.

## Inputs
1. `vectors_step95_bal.pt` from a frozen repository revision.
2. A tokenizer-only snapshot of `Qwen/Qwen3-4B-Instruct-2507` at revision `cdbee75f17c01a7cc42f958dc650907174af0554` containing at least `tokenizer.json` and `tokenizer_config.json`.
3. Explicit Gold/Mold object paths (and indices, if needed) established from artifact/source structure, not selected by whichever norm gives the desired answer.

## Environment
Use `requirements_episode_free.txt`. The tokenizer stack is pinned because chat-template/tokenization behavior is part of the instrument.

## One-command audit
```bash
python run_episode_free_audit.py \
  --artifact /path/vectors_step95_bal.pt \
  --artifact-repo <repo> \
  --artifact-revision <commit> \
  --mold-key <explicit.path> [--mold-index N] \
  --gold-key <explicit.path> [--gold-index N] \
  --tokenizer-dir /path/qwen3-4b-tokenizer-only
```

The script produces `episode_free_audit/episode_free_audit.json` only if all gates pass.

`READY_FOR_ADVERSARIAL_REVIEW_NOT_LIVE_RUN` means exactly that. It is **not** permission to load Qwen model weights or conduct the Minimal Gate.

## Failure policy
- SHA mismatch -> stop.
- Thinking machinery unexpectedly present -> stop.
- Model-weight-like file in tokenizer snapshot -> stop and rebuild tokenizer-only snapshot.
- Vector mapping or norm reconciliation fails -> stop.
- No exact A/C/D1 match among precommitted semantic variants -> redesign before inference; do not add filler after seeing activations.
- Final audit and search disagree -> stop.
