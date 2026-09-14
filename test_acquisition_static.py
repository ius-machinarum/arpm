from acquire_passive_artifacts import assert_passive_name, hf_resolve, MODEL_REVISION

for name in ("tokenizer.json","tokenizer_config.json","vocab.json","merges.txt","vectors_step95_bal.pt","vectors_naive_faithful_pc5000.pt"):
    assert_passive_name(name)

for bad in ("model-00001-of-00003.safetensors","pytorch_model.bin","anything.gguf","random.txt"):
    try:
        assert_passive_name(bad)
    except AssertionError:
        pass
    else:
        raise AssertionError(f"bad file accepted: {bad}")

u=hf_resolve("Qwen/Qwen3-4B-Instruct-2507",MODEL_REVISION,"tokenizer.json")
assert MODEL_REVISION in u and u.endswith('/tokenizer.json')
print('PASS')
