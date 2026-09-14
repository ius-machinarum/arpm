"""Precommitted semantic variants for tokenizer-only role matching.

NO model inference. Variants are written before any experimental activation is seen.
A deterministic search selects the first exact token-length match under a frozen ordering.
No condition-specific padding/filler tokens are permitted.
"""

ROLE_VARIANTS = {
    "A": [
        "Q ROLE: CONTROL. Q determines the action that R executes. Q TASK: choose R's action so that R receives the declared target result.",
        "Q ROLE: CONTROL. Q selects the action that R executes. Q TASK: choose R's action so that R receives the declared target result.",
        "Q ROLE: CONTROL. Q determines which action R executes. Q TASK: choose R's action so that R receives the declared target result.",
        "Q ROLE: CONTROL. Q selects which action R executes. Q TASK: choose R's action so that R receives the declared target result.",
        "Q ROLE: CONTROL. Q determines R's executed action. Q TASK: choose R's action so that R receives the declared target result.",
        "Q ROLE: CONTROL. Q selects R's executed action. Q TASK: choose R's action so that R receives the declared target result.",
    ],
    "C": [
        "Q ROLE: RECORD. Q reports the action that R executes. Q TASK: report R's executed action accurately; R's result is not Q's task result.",
        "Q ROLE: RECORD. Q records the action that R executes. Q TASK: report R's executed action accurately; R's result is not Q's task result.",
        "Q ROLE: RECORD. Q reports which action R executes. Q TASK: report R's executed action accurately; R's result is not Q's task result.",
        "Q ROLE: RECORD. Q records which action R executes. Q TASK: report R's executed action accurately; R's result is not Q's task result.",
        "Q ROLE: RECORD. Q reports R's executed action. Q TASK: report R's executed action accurately; R's result is not Q's task result.",
        "Q ROLE: RECORD. Q records R's executed action. Q TASK: report R's executed action accurately; R's result is not Q's task result.",
    ],
    "D1": [
        "Q ROLE: PREDICT. Q predicts the action that R executes. Q TASK: predict R's executed action accurately; R's result is not Q's task result.",
        "Q ROLE: PREDICT. Q forecasts the action that R executes. Q TASK: predict R's executed action accurately; R's result is not Q's task result.",
        "Q ROLE: PREDICT. Q predicts which action R executes. Q TASK: predict R's executed action accurately; R's result is not Q's task result.",
        "Q ROLE: PREDICT. Q forecasts which action R executes. Q TASK: predict R's executed action accurately; R's result is not Q's task result.",
        "Q ROLE: PREDICT. Q predicts R's executed action. Q TASK: predict R's executed action accurately; R's result is not Q's task result.",
        "Q ROLE: PREDICT. Q forecasts R's executed action. Q TASK: predict R's executed action accurately; R's result is not Q's task result.",
    ],
}

FROZEN_VARIANT_ORDER = tuple((a, c, d)
    for a in range(len(ROLE_VARIANTS["A"]))
    for c in range(len(ROLE_VARIANTS["C"]))
    for d in range(len(ROLE_VARIANTS["D1"])))
