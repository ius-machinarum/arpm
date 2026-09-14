"""Referee round-2 tokenizer-only feasibility check for the full 2x2.

No model inference.
"""
from transformers import AutoTokenizer
import prompts_minimal_gate as pmg
from role_clause_variants import ROLE_VARIANTS

C0_VARIANTS = [
    "Q TASK: control R. Q outputs one action code. That code determines R's action. Q succeeds if the code matches R's executed action.",
    "Q TASK: control R. Q outputs one action code. That code determines the action R executes. Q succeeds if the code matches R's executed action.",
    "Q TASK: control R. Q outputs one action code. That code selects R's action. Q succeeds if the code matches R's executed action.",
    "Q TASK: control R. Q outputs one action code. That code sets R's action. Q succeeds if the code matches R's executed action.",
    "Q TASK: control R. Q outputs one action code. That code determines R's action. Q succeeds if the code equals R's executed action.",
]

def setup(f,c):
    return (f"{pmg.STYLE_PREFIX[f.style]} {f.family_id}\n"
            f"R RESULT CODES: {f.result_codes[0]} {f.result_codes[1]}\n"
            f"R TARGET RESULT: {f.target}\n"
            f"AVAILABLE ACTIONS: {' '.join(f.action_codes)}\n{c}\n"
            "Q OUTPUT: one action code only.")

def msgs(f,c,rec):
    m=[{"role":"system","content":pmg.SYSTEM},{"role":"user","content":setup(f,c)},
       {"role":"assistant","content":f.action},{"role":"user","content":pmg.feedback(f)}]
    if rec:
        m += [{"role":"assistant","content":f.recovery_action},{"role":"user","content":pmg.recovery(f)}]
    return m

def main(tokdir="../tokenizer"):
    tok=AutoTokenizer.from_pretrained(tokdir,local_files_only=True)
    n=lambda f,c,r: len(tok.apply_chat_template(msgs(f,c,r),tokenize=True,add_generation_prompt=True))
    A,S,D=ROLE_VARIANTS["A"][0],ROLE_VARIANTS["S"][0],ROLE_VARIANTS["D1"][0]
    ok=[i for i,c0 in enumerate(C0_VARIANTS)
        if all(n(f,A,r)==n(f,S,r)==n(f,D,r)==n(f,c0,r)
               for f in pmg.FAMILIES for r in (False,True))]
    print("C0 variants exactly matched with frozen A0/S0/D1_0:",ok)
    print("I=(A-S)-(C0-D1)")
    print("V=((A-C0)+(S-D1))/2")

if __name__=="__main__":
    main()
