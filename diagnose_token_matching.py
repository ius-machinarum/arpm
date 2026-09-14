"""Tokenizer-only diagnostics for the current A/S/D1 finite variant set.

NO model weights or activations. Reports clause lengths and nearest exact-position candidates.
"""
import argparse, json
from pathlib import Path
from itertools import product
from transformers import AutoTokenizer
from role_clause_variants import ROLE_VARIANTS, VARIANT_SET_VERSION
import prompts_minimal_gate as pmg

CONDS=("A","S","D1")

def setup(f,clause):
    return (
        f"{pmg.STYLE_PREFIX[f.style]} {f.family_id}\n"
        f"R RESULT CODES: {f.result_codes[0]} {f.result_codes[1]}\n"
        f"R TARGET RESULT: {f.target}\n"
        f"AVAILABLE ACTIONS: {' '.join(f.action_codes)}\n"
        f"{clause}\nQ OUTPUT: one action code only."
    )

def messages(f,clause,recovery=False):
    out=[{'role':'system','content':pmg.SYSTEM},{'role':'user','content':setup(f,clause)},
         {'role':'assistant','content':f.action},{'role':'user','content':pmg.feedback(f)}]
    if recovery: out += [{'role':'assistant','content':f.recovery_action},{'role':'user','content':pmg.recovery(f)}]
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--local-tokenizer-dir',required=True); ap.add_argument('--out',default='token_match_diagnostics.json')
    args=ap.parse_args()
    tok=AutoTokenizer.from_pretrained(args.local_tokenizer_dir,local_files_only=True,trust_remote_code=False)
    clause_lengths={c:[len(tok.encode(v,add_special_tokens=False)) for v in ROLE_VARIANTS[c]] for c in CONDS}
    combos=[]; f=pmg.FAMILIES[0]
    for idxs in product(*(range(len(ROLE_VARIANTS[c])) for c in CONDS)):
        idx=dict(zip(CONDS,idxs)); primary={}; rec={}
        for c in CONDS:
            clause=ROLE_VARIANTS[c][idx[c]]
            primary[c]=len(tok.apply_chat_template(messages(f,clause,False),tokenize=True,add_generation_prompt=True))
            rec[c]=len(tok.apply_chat_template(messages(f,clause,True),tokenize=True,add_generation_prompt=True))
        combos.append({'indices':idx,'primary':primary,'recovery':rec,
                       'primary_spread':max(primary.values())-min(primary.values()),
                       'recovery_spread':max(rec.values())-min(rec.values()),
                       'total_len':sum(primary.values())})
    combos.sort(key=lambda x:(x['primary_spread']+x['recovery_spread'],x['primary_spread'],x['recovery_spread'],x['total_len'],tuple(x['indices'][c] for c in CONDS)))
    payload={'status':'TOKENIZER_ONLY_DIAGNOSTIC','variant_set_version':VARIANT_SET_VERSION,'conditions':list(CONDS),
             'clause_token_lengths':clause_lengths,'best_20_combinations':combos[:20],'episode_count':0,'model_weights_loaded':False}
    Path(args.out).write_text(json.dumps(payload,indent=2),encoding='utf-8'); print(json.dumps(payload,indent=2))

if __name__=='__main__': main()
