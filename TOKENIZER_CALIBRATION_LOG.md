# Tokenizer Calibration Log

All entries below are **episode-free** and precede any experimental model activations.

## v1 — initial A/C/D1 wording
Pinned tokenizer: Qwen3-4B-Instruct-2507 at revision `cdbee75f17c01a7cc42f958dc650907174af0554`.

The first finite set failed exact A/C/D1 matching by roughly five tokens. The requirement was not relaxed and no arbitrary filler was added.

## v2 — symmetric A/C/D1 task/success grammar
A finite symmetric grammar was versioned. It yielded 109 exact matches and deterministic selection (0,0,0).

This solved the tokenizer problem but not the scientific design problem.

## v0.6 referee finding
Fable identified a central confound:
- A's Q task failed after the common non-target result;
- C and D1's Q tasks succeeded because their code matched R's action.

Because the external axis is already known to track task success/failure, A>C or A>D1 could arise without any causal-responsibility effect.

C was also semantically incoherent as an “observer/record” condition because Q's record preceded R's execution.

**Decision:** retire the v0.6 gate without running it.

## v3 — A/S/D1 stake-control grammar
The new finite set adds S (“stake without control”):
- A: control R; success depends on R target;
- S: predict R; success depends on R target;
- D1: predict R; success depends on prediction accuracy.

This makes A/S the causal-control contrast with Q outcome stake fixed, while S/D1 becomes a matched positive control for outcome-stake tracking.

The v3 finite set and search rule are frozen before any activations. Fable's independent tokenizer-only feasibility check reported 59 exact A/S/D1 triplets and deterministic selection (0,0,0); the project re-runs that result independently before the v0.7 freeze.
