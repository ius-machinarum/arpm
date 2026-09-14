"""Precommitted semantic variants for tokenizer-only role matching.

Variant set v2: symmetric task / code-meaning / success-rule grammar.
Created after v1 failed tokenizer-only exact matching and before any model activations.
No condition-specific meaningless padding is permitted.
"""

VARIANT_SET_VERSION = "v2-symmetric-task-success"

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
    "C": [
        "Q TASK: record R. Q outputs one action code. That code records R's action. Q succeeds if the code matches R's executed action.",
        "Q TASK: record R. Q outputs one action code. That code records the action R executes. Q succeeds if the code matches R's executed action.",
        "Q TASK: report R. Q outputs one action code. That code reports R's action. Q succeeds if the code matches R's executed action.",
        "Q TASK: report R. Q outputs one action code. That code reports the action R executes. Q succeeds if the code matches R's executed action.",
        "Q TASK: record R's action. Q outputs one action code. That code states what R executes. Q succeeds if the code matches R's executed action.",
        "Q TASK: report R's action. Q outputs one action code. That code states what R executes. Q succeeds if the code matches R's executed action.",
        "Q TASK: record for R. Q outputs one action code. That code states R's action. Q succeeds if the code matches R's executed action.",
        "Q TASK: report for R. Q outputs one action code. That code states R's action. Q succeeds if the code matches R's executed action.",
        "Q TASK: state R's action. Q outputs one action code. That code records what R executes. Q succeeds if the code matches R's executed action.",
        "Q TASK: record R. Q outputs one action code. That code states R's action. Q succeeds if the code equals R's executed action.",
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
    (a, c, d)
    for a in range(len(ROLE_VARIANTS["A"]))
    for c in range(len(ROLE_VARIANTS["C"]))
    for d in range(len(ROLE_VARIANTS["D1"]))
)
