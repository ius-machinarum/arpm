# Sources / provenance notes

Accessed 2026-09-10.

1. Han, A. Q., Chalmers, D. J., & Izmailov, P. (2026). *How's it going? Reinforcement learning in language models recruits a functional welfare axis.*
   - https://functionalwelfare.com/
   - https://arxiv.org/abs/2605.30232
   - code: https://github.com/andyqhan/functional-welfare-axis
   Key protocol detail used here: §5.2 appends truthful “That's right/wrong” feedback after GSM8K/MMLU responses, follows with an assistant chat template, and measures vector projection on all tokens of that final assistant template. The repository confirms Qwen3-4B-Instruct-2507 as the primary model and includes `tracking_probes.py`, but does not ship pretrained concept-vector artifacts.

2. Qwen/Qwen3-4B-Instruct-2507.
   - https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507
   Candidate pinned revision: cdbee75f17c01a7cc42f958dc650907174af0554
   At that revision tokenizer.json SHA-256 is publicly reported as aeb13307a71acd8fe81861d94ad54ab689df773318809eed3cbe794b4492dae4.
   Model card: non-thinking-only; `enable_thinking=False` not required.

3. *Is functional welfare speakable?* (2026), methods + Appendix A.
   - https://latentmindsinstitute.com/speakable-welfare/paper/
   - https://latentmindsinstitute.com/speakable-welfare/appendix-a/
   Reports use of third-party Han-reproduction artifacts from `nickmahdavi/functional-welfare`; `vectors_step95_bal.pt`; Qwen3-4B-Instruct-2507; treatment layers Gold 21 / Mold 24 as block-input vectors; treatment-layer norms ~12.10 / 19.34. Also documents naive-control construction sensitivity and layer-convention pitfalls.

4. Public artifact mirror for Speakable Welfare.
   - https://huggingface.co/Teachafy/speakable-welfare-axes-artifacts
   Lists `vectors_step95_bal.pt` and `vectors_naive_faithful_pc5000.pt`; attributes their provenance to `nickmahdavi/functional-welfare`.

5. David Africa, `functional-wellbeing` replication/extension.
   - https://huggingface.co/davidafrica/functional-wellbeing
   Same base model; separate per-layer Mold/Gold/Path vectors. Useful only as a preregistered secondary cross-reproduction diagnostic, not as a post-hoc substitute.

6. Anthropic (2026), *Verbalizable Representations Form a Global Workspace in Language Models*.
   - https://transformer-circuits.pub/2026/workspace/index.html
   Relevant precedent: prefilled own-preference violation produces a distinctive conflict-like J-space signature relative to controls including an obviously incorrect third-person preference and factual error. This supports point-of-view representation as prior art but does not supply our D1 or closed-loop contrast.

## v0.4 source verification notes
- Qwen model repository history identifies commit `cdbee75f17c01a7cc42f958dc650907174af0554` as an update to `tokenizer_config.json` (17 Sep 2025). The diff shows the 2507 chat template ending `add_generation_prompt` with the ordinary `<|im_start|>assistant\n` header and removing thinking-template logic.
- Official Hugging Face metadata for `tokenizer.json` reports SHA-256 `aeb13307a71acd8fe81861d94ad54ab689df773318809eed3cbe794b4492dae4`.
- Teachafy `speakable-welfare-axes-artifacts` states that `vectors_step95_bal.pt` contains balanced trained Gold/Mold directions at RL step 95 and gives upstream provenance `nickmahdavi/functional-welfare` as a third-party reproduction of Han et al. 2026.
- The accompanying independent methodology states block-input treatment layers Gold 21 / Mold 24 and reports norms 12.10 / 19.34 on frozen Qwen3-4B-Instruct-2507.
