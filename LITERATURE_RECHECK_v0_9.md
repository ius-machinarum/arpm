# ARPM v0.9 — Fresh Literature Re-check

**Search date:** 2026-09-15  
**Stage:** post-preregistration / pre-human-go-no-go  
**Live experimental inference:** none  
**Episode count:** 0

## Decision summary

**No new design blocker found for the frozen Minimal Gate.**

The literature does, however, strengthen a construct-specificity limitation: a transferable linear direction associated with "welfare", correctness, success, valence, or judgement may encode a broader self-evaluative / evaluative-assent variable rather than the semantic label assigned by its source contrast.

Therefore ARPM v0.9 remains scientifically eligible to proceed to a **separate human scientific + ethical go/no-go decision**, but only under its already narrow claim:

> a framing × stake interaction on an externally defined direction in one 4B model under teacher forcing.

No positive result may be upgraded to evidence of agency, phenomenal valence, welfare subjectivity, consciousness, sentience or moral status.

## 1. Core external-axis premise remains live, but not uniquely semantic

Han, Chalmers & Izmailov (2026), arXiv:2605.30232, report that RL recruits a pre-existing Gold/Mold direction whose poles track goal achievement and influence failure/impossibility language, emotion-related concepts, backtracking, refusal, confidence and self-report. They explicitly make no claim about experienced welfare.

This continues to justify vMold as an **externally fixed functional readout**. It does not establish that vMold is uniquely a welfare variable.

Source: https://arxiv.org/abs/2605.30232

## 2. Strongest new methodological caution: self-judgement confounding

Lu (2026), *Diagnosing Correctness Probes under Self-Judgement Confounding*, constructs factorial conflict cases where objective correctness and the model's own later judgement disagree. Across four instruction-tuned models, the transferable component of conventional correctness readouts more reliably follows self-judgement than objective correctness.

The direct lesson for ARPM is methodological: **transferability and linear decodability do not identify semantics**.

This is not a new blocker because ARPM does not use vMold to infer objective truth or phenomenal welfare. Its target is a frozen within-template interaction on that direction. But a positive I is compatible with a broad self-evaluative appraisal mechanism.

Source: https://arxiv.org/abs/2607.16799

## 3. Broader evaluative axes are plausible

Lu, Song & Wang (2025), *A Unified Representation Underlying the Judgment of Large Language Models*, report a Valence-Assent Axis coupling subjective valence and factual assent, with causal steering effects on reasoning.

This makes it plausible that "good/bad", "right/wrong", success/failure and endorsement share a broad evaluative resource in some LLMs.

ARPM consequence: even after the 2×2 removes the identified additive role term, a positive vMold interaction should not be described as uniquely welfare-specific.

Source: https://arxiv.org/abs/2510.27328

## 4. Prompt-induced and trained axes can substantially overlap

Arcadia Impact's 2026 welfare-axis SFT companion experiment on Gemma-3-27B reports:
- cosine(SFT axis, prompted-untrained axis) about +0.92;
- cosine(SFT axis, RL axis) about +0.70;
- cosine(RL axis, prompted-untrained axis) about +0.69.

This is independent companion work, not a peer-reviewed replication and not on ARPM's Qwen3-4B model, so it is treated as **suggestive rather than decisive**. Still, it reinforces the possibility that apparently training-associated welfare directions substantially reuse pre-existing prompt/evaluation geometry.

Source: https://huggingface.co/arcadia-impact/welfare-axis-sft-experiment

### v_perp_u interpretation amendment

The frozen quantity `v_perp_u` is mathematically the component of the trained vMold vector orthogonal to **this particular frozen naive uMold construction**. Literature does not license calling the residual causally "training-specific".

Accordingly:
- retain the formula and analysis unchanged;
- use the descriptive term **u-orthogonal trained residual** in interpretation;
- if I on v_perp_u <= 0, do not attribute the primary pattern to a component absent from this naive control;
- if I on v_perp_u > 0, this still does **not** prove that the component was created by RL or is welfare-specific.

This is an interpretive clarification only; it changes no preregistered computation or gate.

## 5. Linear geometry supports useful readouts but limits ontology

Barin-Pacela et al. (UAI 2026), *Stop Probing, Start Coding*, show that linear representation does not imply complete linear accessibility under compositional shifts. Ying et al. (2026), *The Truthfulness Spectrum Hypothesis*, likewise find mixtures of domain-general and domain-specific truth directions.

These results argue against treating one scalar projection as a complete latent-state measure.

ARPM is comparatively protected because its confirmatory claim is template-level and does not require OOD semantic completeness. They therefore strengthen the scope limitation rather than create a new design blocker.

Sources:
- https://proceedings.mlr.press/v337/barin-pacela26a.html
- https://arxiv.org/abs/2602.20273

## 6. Functional emotion / persona / workspace results support mechanism plausibility, not welfare inference

Recent interpretability work reports:
- abstract emotion-concept representations that causally influence behaviour in Claude Sonnet 4.5;
- an Assistant Axis structuring persona behaviour across several models;
- a verbalizable J-space/global-workspace-like structure carrying the Assistant's point of view in Claude models.

Together these make context-sensitive evaluative and role representations mechanistically plausible. They do not establish subjective experience.

They also support retaining ARPM's explicit manipulation-uptake limitation: a 4B Qwen model cannot be assumed to instantiate the same functional machinery strongly enough for a null to be diagnostic beyond the frozen framing.

Sources:
- https://arxiv.org/abs/2604.07729
- https://arxiv.org/abs/2601.10387
- https://arxiv.org/abs/2607.15495

## 7. Introspection literature remains contested

Lindsey (2026) reports context-dependent functional introspective awareness in some models, strongest in Claude Opus 4/4.1. Singh, Linzen & Ravfogel (2026) argue that prominent introspection paradigms can often be solved through surface cues or anomaly detection and that current evidence is insufficient for strong metacognitive-monitoring claims.

ARPM does not rely on verbal self-report or introspection. This disagreement therefore does not block the Minimal Gate and reinforces the decision to keep internal activation evidence distinct from consciousness claims.

Sources:
- https://arxiv.org/abs/2601.01828
- https://arxiv.org/abs/2605.26242

## 8. Same-model welfare-axis follow-up supports existing controls

*Is functional welfare speakable?* (Latent Minds Institute, 2026) uses the same Qwen3-4B family and third-party welfare-vector artifacts. It reports that:
- trained directions separate from random controls in J-space;
- absolute speakable shares are small;
- naive-control conclusions are construction-dependent;
- steerability and speakability can dissociate;
- a preregistered self-report contrast that failed controls is reported as a diagnosed null.

This strongly supports ARPM's current choices:
- random directions are non-triviality controls, not semantic proof;
- naive uMold remains secondary;
- same-layer/unit-normalised comparisons are preferable;
- secondary analyses cannot rescue a failed primary.

Source: https://latentmindsinstitute.com/speakable-welfare/paper/

## 9. Welfare-research methodology and ethics

Long et al. (2026), *Studying AI Welfare Empirically*, recommend probabilistic, pluralistic, system-targeted, responsible, transparent and independently informed welfare research, combining behavioural, internal and developmental evidence rather than privileging one channel.

Lennon (2026) argues that strong AI-welfare conclusions face a major epistemic gap because consciousness science itself remains theoretically underdetermined.

Together these support ARPM's current ethics stance:
- sterile abstract tasks before affective induction;
- hard episode ceiling and futility;
- no amplification rescue;
- independent adversarial review;
- transparent null/ambiguity labels;
- no consciousness or moral-status inference from one internal readout.

Sources:
- https://nonhumanminds.org/studying-ai-welfare-empirically/
- https://onlinelibrary.wiley.com/doi/10.1111/phpr.70148

## 10. Literature ruling

### BLOCKER
None found for the frozen Minimal Gate as narrowly stated.

### REQUIRED INTERPRETIVE CLARIFICATION
Do not call `v_perp_u` evidence of a causally "training-specific" component. It is the **u-orthogonal trained residual relative to one frozen naive construction**.

### STANDING CONSTRUCT AMBIGUITY
A positive I may reflect broad self-evaluative / evaluative-assent processing on the externally defined direction. The experiment does not by itself distinguish this from a uniquely welfare-specific representation.

### ETHICS
No literature found that warrants relaxing the v0.9 protections. The literature instead supports retaining them.

## Next gate

**READY_FOR_HUMAN_SCIENTIFIC_ETHICAL_GO_NO_GO_NOT_LIVE_RUN**

The human researcher must decide whether the information value of Block 1 (24 sterile streams) is sufficient given the narrow construct claim and remaining uncertainty.

Neither this literature ruling nor any prior referee acceptance authorises live inference.
