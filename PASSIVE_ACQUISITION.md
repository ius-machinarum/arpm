# Passive artifact acquisition v0.5

This step remains **episode-free**. It downloads no language-model weights and runs no inference.

`acquire_passive_artifacts.py` is allowlisted to exactly five remote filenames:

- `tokenizer.json`
- `tokenizer_config.json`
- `vocab.json`
- `merges.txt`
- `vectors_step95_bal.pt`

For the Qwen tokenizer, the repository is pinned to commit
`cdbee75f17c01a7cc42f958dc650907174af0554`.

For the third-party vector mirror, the script does **not** accept mutable `main` as a freeze. It first asks the Hugging Face Hub for the `X-Repo-Commit` corresponding to `vectors_step95_bal.pt` on `main`, then downloads the artifact again from that immutable commit and records the bytes' SHA-256.

The known authoritative SHA-256 for `tokenizer.json` is checked immediately:
`aeb13307a71acd8fe81861d94ad54ab689df773318809eed3cbe794b4492dae4`.

The vector's checksum is deliberately not pre-filled from a filename or norm. The acquired bytes themselves become the checksum source of truth, while published norms remain an independent validation check.

## Usage on a network-capable machine

Metadata only:

```bash
python acquire_passive_artifacts.py --metadata-only --out passive_inputs
```

Acquire the passive bytes:

```bash
python acquire_passive_artifacts.py --out passive_inputs
```

Then install only the episode-free audit dependencies and run the existing audit scripts. Passing acquisition is **not** permission to load or run Qwen model weights.
