# Episode-free completion path v0.7

This is the supported route from redesign to adversarial re-review. It must run **without language-model weight files present**.

## Inputs
1. frozen trained artifact `vectors_step95_bal.pt`;
2. frozen naive-control artifact `vectors_naive_faithful_pc5000.pt`;
3. tokenizer-only snapshot of `Qwen/Qwen3-4B-Instruct-2507` at revision `cdbee75f17c01a7cc42f958dc650907174af0554`;
4. the committed finite A/S/D1 variant set;
5. the committed deterministic random-direction specification.

## Environment
Use `requirements_episode_free.txt`.

## One-command audit

```bash
python run_episode_free_audit.py \
  --artifact /path/vectors_step95_bal.pt \
  --naive-artifact /path/vectors_naive_faithful_pc5000.pt \
  --artifact-repo Teachafy/speakable-welfare-axes-artifacts \
  --artifact-revision 8f4df5b5b14ecb4bcc5b20209bdfe2574d1ebee8 \
  --tokenizer-dir /path/qwen3-4b-tokenizer-only
```

The audit verifies:
- tokenizer bytes/template and absence of model weights;
- trained vector bytes, mapping and norms;
- naive u_mold bytes, explicit mapping and artifact-selected layer;
- deterministic 100-direction random control hash;
- exact A/S/D1 tokenizer matching;
- final 12-family position audit.

A passing status is:

`READY_FOR_ADVERSARIAL_REVIEW_NOT_LIVE_RUN`

It is **not** permission to run Qwen.

## Failure policy
- any byte/hash mismatch -> stop;
- any model-weight-like file in tokenizer snapshot -> stop;
- unexpected vector keys/shapes/layers -> stop;
- random-control byte hash mismatch -> stop;
- no exact A/S/D1 match -> stop and redesign before activations;
- search/final tokenizer audit disagreement -> stop.

No failed episode-free gate is bypassed by hand editing after seeing model activations.
