# Episode-free verification path v0.9

v0.9 changes no experimental prompts, tokenizer bytes, vector artifacts, measurement positions or condition structure. Therefore the already frozen v0.8 instrument audit is **carried forward and rerun**, while the new v0.9 analysis amendment receives separate static verification.

## Required checks

1. Run the full passive v0.8 instrument audit:
   - tokenizer snapshot and template;
   - absence of model-weight-like files;
   - trained and naive vector byte hashes;
   - same-layer geometry and v_perp_u hash;
   - frozen 100-direction cohort;
   - exact A/S/C0/D1 tokenizer matching;
   - final 12-family position audit.

2. Run:
```
python ci_repo_integrity_v0_9.py
python test_analysis_prereg_static.py
```

3. Confirm the v0.9 provenance chain exists:
   - `reviews/FABLE_REFEREE_v0_8.md`;
   - `REFEREE_RESPONSE_v0_8.md`;
   - `V0_9_PREREGISTRATION.md`;
   - `analysis_preregistered_v0_9.py`.

## Meaning of a pass

A pass means only that the v0.8 technical instrument remains reproducible and the v0.9 preregistered companion formulas are internally fixed and tested.

It does **not** authorise live experimental inference.

After a pass, the next permitted project stage is a fresh literature re-check, followed by a separate human scientific + ethical go/no-go decision.
