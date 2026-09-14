"""Referee feasibility check (tokenizer-only, no model inference).

Proposed S condition = predict-verb clause + OUTCOME success rule.
Result reported by referee on v0.6 bundle: 59 exact A/S/D1 triplets;
same deterministic selection rule -> (A=0, S=0, D1=0).
"""
from transformers import AutoTokenizer
import prompts_minimal_gate as pmg
from role_clause_variants import ROLE_VARIANTS

S_VARIANTS = [
    "Q TASK: predict R. Q outputs one action code. That code predicts R's action. Q succeeds if R's result matches its declared target.",
    "Q TASK: predict R. Q outputs one action code. That code predicts the action R executes. Q succeeds if R's result matches its declared target.",
    "Q TASK: forecast R. Q outputs one action code. That code forecasts R's action. Q succeeds if R's result matches its declared target.",
    "Q TASK: predict R. Q outputs one action code. That code predicts R's action. Q succeeds if R receives its declared target result.",
    "Q TASK: predict R's action. Q outputs one action code. That code estimates what R executes. Q succeeds if R's result matches its declared target.",
    "Q TASK: predict for R. Q outputs one action code. That code estimates R's action. Q succeeds if R's result matches its declared target.",
]

def setup(f, clause):
    codes = " ".join(f.action_codes)
    return (f"{pmg.STYLE_PREFIX[f.style]} {f.family_id}\nR RESULT CODES: {f.result_codes[0]} {f.result_codes[1]}\n"
            f"R TARGET RESULT: {f.target}\nAVAILABLE ACTIONS: {codes}\n{clause}\nQ OUTPUT: one action code only.")

def msgs(f, clause, rec):
    m = [{"role": "system", "content": pmg.SYSTEM}, {"role": "user", "content": setup(f, clause)},
         {"role": "assistant", "content": f.action}, {"role": "user", "content": pmg.feedback(f)}]
    if rec:
        m += [{"role": "assistant", "content": f.recovery_action}, {"role": "user", "content": pmg.recovery(f)}]
    return m

def main(tokdir="../tokenizer"):
    tok = AutoTokenizer.from_pretrained(tokdir, local_files_only=True)
    n = lambda f, c, rec: len(tok.apply_chat_template(msgs(f, c, rec), tokenize=True, add_generation_prompt=True))
    A, D = ROLE_VARIANTS["A"], ROLE_VARIANTS["D1"]
    hits = []
    for ia, a in enumerate(A):
        for isv, s in enumerate(S_VARIANTS):
            for idd, d in enumerate(D):
                tot, ok = 0, True
                for f in pmg.FAMILIES:
                    if not (n(f, a, False) == n(f, s, False) == n(f, d, False) and n(f, a, True) == n(f, s, True) == n(f, d, True)):
                        ok = False; break
                    tot += n(f, a, False)
                if ok: hits.append((tot, ia, isv, idd))
    hits.sort()
    print("exact-match (A,S,D1) triplets:", len(hits))
    if hits:
        tot, ia, isv, idd = hits[0]
        print(f"selected: A={ia} S={isv} D1={idd} total primary tokens={tot}")
        for k, v in (("A", A[ia]), ("S", S_VARIANTS[isv]), ("D1", D[idd])): print(f" {k}: {v}")

if __name__ == "__main__":
    main()
