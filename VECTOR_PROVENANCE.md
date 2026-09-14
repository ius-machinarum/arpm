# External Vector Provenance Audit v0.3

## Status
**Source-chain provenance: provisionally adequate. Byte-level provenance: NOT YET FROZEN.**

No live model run is permitted until the actual artifact bytes have been acquired and hashed.

## Primary source chain
1. Han, Chalmers & Izmailov (2026) publish the functional-welfare method/code but their official repository does not ship pretrained vectors.
2. The 2026 `Is functional welfare speakable?` project reports using a third-party reproduction originating from `nickmahdavi/functional-welfare`.
3. Its public artifact mirror `Teachafy/speakable-welfare-axes-artifacts` identifies:
   - `vectors_step95_bal.pt` — trained Gold/Mold directions, RL step 95, balanced;
   - base model `Qwen/Qwen3-4B-Instruct-2507`.
4. The Speakable Welfare Appendix reports treatment layers and norms read from artifact metadata:
   - Gold: block-input layer 21, norm about 12.10;
   - Mold: block-input layer 24, norm about 19.34.
5. The same appendix explicitly documents an off-by-one hazard for Jacobian-lens source layers. Our direct residual projection therefore records the **block-input convention explicitly** rather than copying a J-lens layer index.

## Primary planned artifact
`vectors_step95_bal.pt`

Primary pole: `v_Mold`

Primary treatment position: block-input layer 24.

## Secondary independent reproduction
`davidafrica/functional-wellbeing` provides a separate replication/extension on the same base model with per-layer `lava` (= Mold), `goal` (= Gold), and `path` mean-difference vectors. This is useful as a non-gating cross-reproduction check using the *same experimental activations*, so it costs no new model episodes.

It must not be substituted for the primary vector after seeing the primary result.

## Model pin
Candidate base-model revision:
`cdbee75f17c01a7cc42f958dc650907174af0554`

The Hugging Face commit history identifies this revision as the tokenizer-config update on 17 Sep 2025. The repository's tokenizer.json at this revision reports SHA-256:
`aeb13307a71acd8fe81861d94ad54ab689df773318809eed3cbe794b4492dae4`

The Qwen model card states that Qwen3-4B-Instruct-2507 is non-thinking-only and does not require `enable_thinking=False`.

## Required byte-level freeze before inference
Record in `artifact_manifest.json`:
- exact model repo revision;
- SHA-256 of tokenizer.json and tokenizer_config.json;
- SHA-256 of model index and each weight shard (or authoritative immutable content hashes);
- exact external-vector repository + revision;
- SHA-256 of `vectors_step95_bal.pt`;
- object keys, tensor shapes, dtypes;
- vMold/vGold norms at all layers;
- verified treatment layer norms;
- sign convention;
- PyTorch/Transformers versions;
- explicit HF hidden-state index -> block-input layer mapping.

## Hard failure conditions
Do not run if:
- artifact cannot be loaded with a safe weights-only path;
- vector dimensionality does not equal model hidden size;
- expected layer count/convention cannot be reconciled;
- treatment-layer norms materially disagree with published provenance without explanation;
- artifact/model revision provenance is ambiguous enough that compatibility cannot be defended.

## v0.3 freeze rule
Repository naming and published norms establish provenance but do **not** constitute a byte-level freeze. The exact `.pt` bytes must be acquired from a frozen repository revision, SHA-256 hashed, safely loaded with `weights_only=True`, and mapped to Gold/Mold using an explicit source-supported object-key mapping. Norm agreement is a validation check, not a key-discovery procedure.

## v0.4 provenance rule
The mirror/reproduction provenance is sufficiently documented to nominate the artifact, but nomination is not byte freeze. Public methodology states that `vectors_step95_bal.pt` is the balanced step-95 trained Gold/Mold artifact from the `nickmahdavi/functional-welfare` third-party reproduction, and independently reports treatment layers/norms. We still require the exact local bytes, repository revision, safe tensor structure inspection, and explicit key/index mapping before the primary direction becomes frozen.

`inspect_vector_artifact.py` is deliberately non-semantic: it enumerates every tensor path/shape/norm but does not decide which one is Mold/Gold. `freeze_vector_artifact.py` then requires the mapping as explicit input. This separates **inspection** from **commitment** and prevents convenient norm matching from silently choosing the primary tensor.
