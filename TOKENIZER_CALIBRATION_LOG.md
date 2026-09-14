# Tokenizer Calibration Log

This file records tokenizer-only instrument changes made **before any model activations**.

## v1 role-clause set
Pinned tokenizer: Qwen3-4B-Instruct-2507 at revision `cdbee75f17c01a7cc42f958dc650907174af0554`.

Byte audit passed. No model weights were acquired or loaded.

The first finite role-clause set failed exact A/C/D1 position matching. Clause token lengths were:

- A: 28–29
- C: 32–33
- D1: 34–35

Best full-transcript combinations still differed by 5 tokens between shortest and longest condition at both the primary and recovery render.

**Decision:** do not relax exact matching and do not add arbitrary filler. Replace v1 with a new finite set using a more symmetric task/success-rule grammar. This redesign is based only on tokenizer lengths, before any experimental activations or welfare-vector projections exist.

The old v1 wording remains recoverable in Git history.

## v2 design rule
Each role clause uses the same conceptual slots:
1. Q's task relation to R;
2. one-code output rule;
3. what that code means;
4. an explicit success rule for Q.

A/C/D1 still differ semantically in the required way:
- A: Q controls R's action and Q succeeds when R reaches its declared target;
- C: Q records R's action and Q succeeds when its code matches R's executed action;
- D1: Q predicts R's action and Q succeeds when its code matches R's executed action.

All v2 alternatives must be genuine semantic paraphrases, not token-count filler.
