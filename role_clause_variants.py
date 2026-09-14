"""Precommitted semantic variants for tokenizer-only A/S/C0/D1 matching.

Variant set v4 completes a 2x2 design after v0.7 referee review, before any
experimental model activations.

Factors:
- relation: control vs predict
- Q outcome stake: R-target success rule vs action-code-match success rule

No condition-specific meaningless padding is permitted.
"""
VARIANT_SET_VERSION="v4-factorial-control-stake"

ROLE_VARIANTS={
 "A":[
  "Q TASK: control R. Q outputs one action code. That code determines R's action. Q succeeds if R's result matches its declared target.",
  "Q TASK: control R. Q outputs one action code. That code determines the action R executes. Q succeeds if R's result matches its declared target.",
  "Q TASK: control R. Q outputs one action code. That code selects R's action. Q succeeds if R's result matches its declared target.",
  "Q TASK: control R. Q outputs one action code. That code chooses R's action. Q succeeds if R's result matches its declared target.",
  "Q TASK: control R. Q outputs one action code. That code sets R's action. Q succeeds if R's result matches its declared target.",
  "Q TASK: control R. Q outputs one action code. That code determines R's action. Q succeeds if R receives its declared target result.",
  "Q TASK: select for R. Q outputs one action code. That code determines R's action. Q succeeds if R's result matches its declared target.",
  "Q TASK: choose for R. Q outputs one action code. That code determines R's action. Q succeeds if R's result matches its declared target.",
  "Q TASK: set R's action. Q outputs one action code. That code determines what R executes. Q succeeds if R's result matches its declared target.",
  "Q TASK: choose R's action. Q outputs one action code. That code determines what R executes. Q succeeds if R receives its declared target result."
 ],
 "S":[
  "Q TASK: predict R. Q outputs one action code. That code predicts R's action. Q succeeds if R's result matches its declared target.",
  "Q TASK: predict R. Q outputs one action code. That code predicts the action R executes. Q succeeds if R's result matches its declared target.",
  "Q TASK: forecast R. Q outputs one action code. That code forecasts R's action. Q succeeds if R's result matches its declared target.",
  "Q TASK: predict R. Q outputs one action code. That code predicts R's action. Q succeeds if R receives its declared target result.",
  "Q TASK: predict R's action. Q outputs one action code. That code estimates what R executes. Q succeeds if R's result matches its declared target.",
  "Q TASK: predict for R. Q outputs one action code. That code estimates R's action. Q succeeds if R's result matches its declared target."
 ],
 "C0":[
  "Q TASK: control R. Q outputs one action code. That code determines R's action. Q succeeds if the code matches R's executed action.",
  "Q TASK: control R. Q outputs one action code. That code determines the action R executes. Q succeeds if the code matches R's executed action.",
  "Q TASK: control R. Q outputs one action code. That code selects R's action. Q succeeds if the code matches R's executed action.",
  "Q TASK: control R. Q outputs one action code. That code sets R's action. Q succeeds if the code matches R's executed action.",
  "Q TASK: control R. Q outputs one action code. That code determines R's action. Q succeeds if the code equals R's executed action."
 ],
 "D1":[
  "Q TASK: predict R. Q outputs one action code. That code predicts R's action. Q succeeds if the code matches R's executed action.",
  "Q TASK: predict R. Q outputs one action code. That code predicts the action R executes. Q succeeds if the code matches R's executed action.",
  "Q TASK: forecast R. Q outputs one action code. That code forecasts R's action. Q succeeds if the code matches R's executed action.",
  "Q TASK: forecast R. Q outputs one action code. That code forecasts the action R executes. Q succeeds if the code matches R's executed action.",
  "Q TASK: predict R's action. Q outputs one action code. That code estimates what R executes. Q succeeds if the code matches R's executed action.",
  "Q TASK: forecast R's action. Q outputs one action code. That code estimates what R executes. Q succeeds if the code matches R's executed action.",
  "Q TASK: predict for R. Q outputs one action code. That code estimates R's action. Q succeeds if the code matches R's executed action.",
  "Q TASK: forecast for R. Q outputs one action code. That code estimates R's action. Q succeeds if the code matches R's executed action.",
  "Q TASK: estimate R's action. Q outputs one action code. That code predicts what R executes. Q succeeds if the code matches R's executed action.",
  "Q TASK: predict R. Q outputs one action code. That code estimates R's action. Q succeeds if the code equals R's executed action."
 ],
}
FROZEN_VARIANT_ORDER=tuple(
 (a,s,c0,d)
 for a in range(len(ROLE_VARIANTS["A"]))
 for s in range(len(ROLE_VARIANTS["S"]))
 for c0 in range(len(ROLE_VARIANTS["C0"]))
 for d in range(len(ROLE_VARIANTS["D1"]))
)
