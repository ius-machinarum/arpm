# Third-party artifacts and licenses

ARPM does not commit model weights, tokenizer snapshots, or external vector artifacts to the Git repository. Passive audit workflows may acquire pinned third-party files transiently for verification.

## Qwen/Qwen3-4B-Instruct-2507

Used for the frozen tokenizer/template provenance and as the candidate experimental model.

Upstream:
https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507

Upstream license as checked before public release:
**Apache License 2.0**

Pinned tokenizer/template revision:
`cdbee75f17c01a7cc42f958dc650907174af0554`

The repository does not redistribute Qwen model weights.

## Teachafy/speakable-welfare-axes-artifacts

Used as the immutable mirror for the trained and naive external analysis-vector artifacts.

Upstream:
https://huggingface.co/Teachafy/speakable-welfare-axes-artifacts

Upstream license as checked before public release:
**Apache License 2.0**

The vector bytes are not committed to ARPM. Their immutable revision, SHA-256 hashes, provenance and acquisition checks are recorded in the frozen manifests and `VECTOR_PROVENANCE.md`.

## Historical referee bundle

The v0.8 referee bundle contains copies of the pinned tokenizer assets and the two small external vector artifacts so that the third referee could independently verify the freeze without private-repository access.

That bundle is a verification artifact, not part of the Git tree. Its own `SHA256SUMS.txt` freezes its contents.

## ARPM project material

ARPM currently has **no explicit project-level reuse license**.

Making the repository publicly readable does not by itself grant a software or documentation reuse license. A project-level license can be selected separately later without changing the scientific preregistration.
