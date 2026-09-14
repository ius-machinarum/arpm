# Pre-live Freeze Status

**Overall: EPISODE-FREE TECHNICAL FREEZE COMPLETE / NO LIVE MODEL RUNS.**

## Vector byte freeze — PASS
The external vector artifact is now byte-frozen and committed as metadata in `artifact_manifest.frozen.json`.

Frozen artifact:
- repository mirror: `Teachafy/speakable-welfare-axes-artifacts`
- immutable revision: `8f4df5b5b14ecb4bcc5b20209bdfe2574d1ebee8`
- filename: `vectors_step95_bal.pt`
- size: 739325 bytes
- SHA-256: `bd90129eaf5a7d92933ed6e536613eaeebf81486b62f68e11b5dc2d6d385e297`

Safe structure inspection used `torch.load(..., map_location="cpu", weights_only=True)` with PyTorch 2.10.0+cpu.

The artifact itself contains explicit keys and layer metadata:
- `v_mold`: shape [36, 2560], float32
- `v_gold`: shape [36, 2560], float32
- `layer_mold = 24`
- `layer_gold = 21`
- `ckpt = ckpts_g64_envfix/step_95`
- `per_class = 5000`
- `balanced = True`

Independent norm reconciliation:
- Mold layer 24 norm = 19.339996337890625 (published reference about 19.34)
- Gold layer 21 norm = 12.101578712463379 (published reference about 12.10)

The semantic mapping was **not** inferred by choosing whichever tensors happened to match the published norms. The artifact names the vectors and layer indices explicitly; norm agreement is only an independent consistency check.

## Tokenizer byte audit — PASS
Pinned model/tokenizer:
- `Qwen/Qwen3-4B-Instruct-2507`
- revision: `cdbee75f17c01a7cc42f958dc650907174af0554`

Verified passive snapshot:
- `tokenizer.json` SHA-256: `aeb13307a71acd8fe81861d94ad54ab689df773318809eed3cbe794b4492dae4`
- `tokenizer_config.json` SHA-256: `a62ff0a2472a0fa1b8eaabcb57c59b58afa42a22831dc141400b6e0cf2b65ce3`
- chat-template SHA-256: `64f85b198065d0fba2a81f37e10ed68161ce2c19a754c7100e67e0ca2ee9c326`
- tokenizer class: `Qwen2Tokenizer`
- thinking-template machinery: absent
- model-weight-like files in tokenizer snapshot: none

No language-model weights were acquired or loaded.

## Tokenizer exact A/C/D1 matching — PASS
The v1 finite semantic set failed exact matching and was documented in `TOKENIZER_CALIBRATION_LOG.md`. No activations existed.

A v2 symmetric task/success-rule set was then versioned before any live inference. Under the pinned tokenizer it produced 109 exact-match triplets. The frozen deterministic selection is indices A=0, C=0, D1=0.

Across all 12 families:
- A/C/D1 primary prefix token counts match exactly within family;
- recovery full token counts match exactly within family;
- primary and recovery assistant-template suffix IDs are identical: `[151644, 77091, 198]`;
- the final tokenizer audit passed.

See `tokenizer_match.frozen.json`.

## Remaining gates
1. Assemble and submit one adversarial/referee packet.
2. Resolve every referee blocker/should-fix item prospectively.
3. Re-check current literature for an equivalent A/C/D1 result.
4. Separate scientific + ethical go/no-go decision.

Current status is:

`READY_FOR_ADVERSARIAL_REVIEW_NOT_LIVE_RUN`

It is deliberately **not** authority to load or run Qwen model weights.
