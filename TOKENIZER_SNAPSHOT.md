# Tokenizer snapshot instrument

The tokenizer/chat template is part of the experimental instrument, not incidental preprocessing.

## Pin
- repo: `Qwen/Qwen3-4B-Instruct-2507`
- revision: `cdbee75f17c01a7cc42f958dc650907174af0554`
- official `tokenizer.json` SHA-256: `aeb13307a71acd8fe81861d94ad54ab689df773318809eed3cbe794b4492dae4`
- tokenizer runtime for the offline audit: `transformers==4.57.6`

The Qwen commit at this revision changes `tokenizer_config.json`; therefore pinning only `tokenizer.json` is insufficient. `tokenizer_snapshot_audit.py` hashes `tokenizer_config.json` and the chat-template string locally as well.

## Safety/instrumentation rule
The tokenizer-only directory may not contain `.safetensors`, `.bin`, `.ckpt`, `.pth`, `.onnx`, or `model-*` weight-like files. A violation stops the episode-free audit.

This rule is intentionally stronger than technically necessary: it makes it easy to verify that the pre-referee stage did not accidentally acquire or load a language model.
