# External Vector Provenance v0.7

## Primary trained direction — frozen
Artifact:
`vectors_step95_bal.pt`

Mirror:
`Teachafy/speakable-welfare-axes-artifacts`

Immutable mirror revision:
`8f4df5b5b14ecb4bcc5b20209bdfe2574d1ebee8`

SHA-256:
`bd90129eaf5a7d92933ed6e536613eaeebf81486b62f68e11b5dc2d6d385e297`

The artifact explicitly contains:
- `v_mold` [36,2560], float32;
- `v_gold` [36,2560], float32;
- `layer_mold=24`;
- `layer_gold=21`;
- `ckpt=ckpts_g64_envfix/step_95`;
- `per_class=5000`;
- `balanced=True`.

Primary: unit-normalised `v_mold[24]` at block-input layer 24.

The layer is artifact-selected by the third-party reproduction / Speakable Welfare provenance. It is not represented as Han et al.'s steering optimum. Block-input 24 corresponds to block-output 23 and lies within the effective mid/late band discussed in prior work; no direct magnitude comparison to Han is licensed.

## Why this can still be confirmatory
The primary vector, bytes, key, sign and layer were fixed by external work and frozen before any ARPM activation data. The project does not select a layer or direction after observing A/S/D1 results.

## Band-average robustness
Prospectively secondary:
block-input layers 18–27 inclusive, using the corresponding vMold vector at each layer, each unit-normalised before projection. Average across the ten layers within family/condition.

This is robustness only and cannot rescue layer-24 failure.

## Naive semantic control — pending byte freeze
Fable requested a same-mirror naive Mold control:
`vectors_naive_faithful_pc5000.pt`

The project will acquire it only through the passive allowlist, resolve the mirror to an immutable revision, hash the bytes, inspect it safely, freeze the explicit object/layer mapping, and include it in the v0.7 referee bundle.

Until that manifest exists, the v0.7 specificity gate is **not frozen**.

## Random directions
The 100 random directions are not learned artifacts. Their generation algorithm, norm target, dimension, seed and expected byte hash are prospectively fixed in `SPECIFICITY_PLAN.md` / `specificity_controls.py` before any activations.

## Model compatibility
Current model: `Qwen/Qwen3-4B-Instruct-2507`, hidden size 2560.
The old 8B pilot path is retired.
