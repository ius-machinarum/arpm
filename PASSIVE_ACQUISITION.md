# Passive artifact acquisition v0.7

This step remains **episode-free**. It downloads no language-model weights and runs no model inference.

`acquire_passive_artifacts.py` is allowlisted to exactly six remote filenames:

- `tokenizer.json`
- `tokenizer_config.json`
- `vocab.json`
- `merges.txt`
- `vectors_step95_bal.pt`
- `vectors_naive_faithful_pc5000.pt`

The Qwen tokenizer is pinned to:
`cdbee75f17c01a7cc42f958dc650907174af0554`

Both external vector files are acquired from the same immutable mirror revision:
`8f4df5b5b14ecb4bcc5b20209bdfe2574d1ebee8`

The acquisition helper resolves mutable `main` to an immutable repository SHA before downloading vector bytes.

Known frozen hashes:
- trained vector: `bd90129eaf5a7d92933ed6e536613eaeebf81486b62f68e11b5dc2d6d385e297`
- naive semantic control: `68bff1428712def0330851057dba102112e3d48ffa23db7da85d84cde93aaa0e`
- tokenizer.json: `aeb13307a71acd8fe81861d94ad54ab689df773318809eed3cbe794b4492dae4`

Passing passive acquisition is not permission to load Qwen model weights.

## Usage

```bash
python acquire_passive_artifacts.py --out passive_inputs
```

Then run the v0.7 episode-free audit with the trained vector, naive control and tokenizer-only snapshot.
