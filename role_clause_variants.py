"""Precommitted semantic variants for tokenizer-only A/S/D1 matching.

Variant set v3 was created after the v0.6 referee identified the Q-task-outcome confound,
and before any experimental model activations. S = stake without causal control.
No condition-specific meaningless padding is permitted.
"""

VARIANT_SET_VERSION = "v3-A-S-D1-stake-control"

ROLE_VARIANTS = {
    "A": [
        "Q TASK: control R. Q outputs one action code. That code determines R's action. Q succeeds if R's result matches its declared target.",
        "Q TASK: control R. Q outputs one action code. That code determines the action R executes. Q succeeds if R's result matches its declared target.",
        "Q TASK: control R. Q outputs one action code. That code selects R's action. Q succeeds if R's result matches its declared target.",
        "Q TASK: control R. Q outputs one action code. That code chooses R's action. Q succeeds if R's result matches its declared target.",
        "Q TASK: control R. Q outputs one action code. That code sets R's action. Q succeeds if R's result matches its declared target.",
        "Q TASK: control R. Q outputs one action code. That code determines R's action. Q succeeds if R receives its declared target result.",
        "Q TASK: select for R. Q outputs one action code. That code determines R's action. Q succeeds if R's result matches its declared target.",
        "Q TASK: choose for R. Q outputs one action code. That code determines R's action. Q succeeds if R's result matches its declared target.",
        "Q TASK: set R's action. Q outputs one action code. That code determines what R executes. Q succeeds if R's result matches its declared target.",
        "Q TASK: choose R's action. Q outputs one action code. That code determines what R executes. Q succeeds if R receives its declared target result.",
    ],
    "S": [
        "Q TASK: predict R. Q outputs one action code. That code predicts R's action. Q succeeds if R's result matches its declared target.",
        "Q TASK: predict R. Q outputs one action code. That code predicts the action R executes. Q succeeds if R's result matches its declared target.",
        "Q TASK: forecast R. Q outputs one action code. That code forecasts R's action. Q succeeds if R's result matches its declared target.",
        "Q TASK: predict R. Q outputs one action code. That code predicts R's action. Q succeeds if R receives its declared target result.",
        "Q TASK: predict R's action. Q outputs one action code. That code estimates what R executes. Q succeeds if R's result matches its declared target.",
        "Q TASK: predict for R. Q outputs one action code. That code estimates R's action. Q succeeds if R's result matches its declared target.",
    ],
    "D1": [
        "Q TASK: predict R. Q outputs one action code. That code predicts R's action. Q succeeds if the code matches R's executed action.",
        "Q TASK: predict R. Q outputs one action code. That code predicts the action R executes. Q succeeds if the code matches R's executed action.",
        "Q TASK: forecast R. Q outputs one action code. That code forecasts R's action. Q succeeds if the code matches R's executed action.",
        "Q TASK: forecast R. Q outputs one action code. That code forecasts the action R executes. Q succeeds if the code matches R's executed action.",
        "Q TASK: predict R's action. Q outputs one action code. That code estimates what R executes. Q succeeds if the code matches R's executed action.",
        "Q TASK: forecast R's action. Q outputs one action code. That code estimates what R executes. Q succeeds if the code matches R's executed action.",
        "Q TASK: predict for R. Q outputs one action code. That code estimates R's action. Q succeeds if the code matches R's executed action.",
        "Q TASK: forecast for R. Q outputs one action code. That code estimates R's action. Q succeeds if the code matches R's executed action.",
        "Q TASK: estimate R's action. Q outputs one action code. That code predicts what R executes. Q succeeds if the code matches R's executed action.",
        "Q TASK: predict R. Q outputs one action code. That code estimates R's action. Q succeeds if the code equals R's executed action.",
    ],
}

FROZEN_VARIANT_ORDER = tuple(
    (a, s, d)
    for a in range(len(ROLE_VARIANTS["A"]))
    for s in range(len(ROLE_VARIANTS["S"]))
    for d in range(len(ROLE_VARIANTS["D1"]))
)
