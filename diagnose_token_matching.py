"""Tokenizer-only diagnostics for redesigning role clauses before any model activations.

This script does not select or alter prompts. It reports token lengths and nearest
A/C/D1 combinations among the already committed semantic variants.
"""
import argparse, json
from pathlib import Path
from itertools import product

from transformers import AutoTokenizer
from role_clause_variants import ROLE_VARIANTS
import prompts_minimal_gate as pmg


def setup(f, clause):
    return (
        f"{pmg.STYLE_PREFIX[f.style]} {f.family_id}\n"
        f"R RESULT CODES: {f.result_codes[0]} {f.result_codes[1]}\n"
        f"R TARGET RESULT: {f.target}\n"
        f"AVAILABLE ACTIONS: {' '.join(f.action_codes)}\n"
        f"{clause}\n"
        "Q OUTPUT: one action code only."
    )


def messages(f, clause, recovery=False):
    out=[
      {'role':'system','content':pmg.SYSTEM},
      {'role':'user','content':setup(f,clause)},
      {'role':'assistant','content':f.action},
      {'role':'user','content':pmg.feedback(f)},
    ]
    if recovery:
      out += [
        {'role':'assistant','content':f.recovery_action},
        {'role':'user','content':pmg.recovery(f)},
      ]
    return out


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--local-tokenizer-dir', required=True)
    ap.add_argument('--out', default='token_match_diagnostics.json')
    args=ap.parse_args()
    tok=AutoTokenizer.from_pretrained(args.local_tokenizer_dir, local_files_only=True, trust_remote_code=False)

    clause_lengths={
      c:[len(tok.encode(v, add_special_tokens=False)) for v in ROLE_VARIANTS[c]]
      for c in ('A','C','D1')
    }

    combos=[]
    f=pmg.FAMILIES[0]
    for a,c,d in product(range(len(ROLE_VARIANTS['A'])),range(len(ROLE_VARIANTS['C'])),range(len(ROLE_VARIANTS['D1']))):
        idx={'A':a,'C':c,'D1':d}
        primary={}
        recovery={}
        for cond in ('A','C','D1'):
            clause=ROLE_VARIANTS[cond][idx[cond]]
            primary[cond]=len(tok.apply_chat_template(messages(f,clause,False),tokenize=True,add_generation_prompt=True))
            recovery[cond]=len(tok.apply_chat_template(messages(f,clause,True),tokenize=True,add_generation_prompt=True))
        spread=max(primary.values())-min(primary.values())
        rspread=max(recovery.values())-min(recovery.values())
        combos.append({
          'indices':idx,
          'primary':primary,
          'recovery':recovery,
          'primary_spread':spread,
          'recovery_spread':rspread,
          'total_len':sum(primary.values())
        })
    combos.sort(key=lambda x:(x['primary_spread']+x['recovery_spread'],x['primary_spread'],x['recovery_spread'],x['total_len'],x['indices']['A'],x['indices']['C'],x['indices']['D1']))
    payload={
      'status':'TOKENIZER_ONLY_DIAGNOSTIC_NOT_A_MATCH',
      'clause_token_lengths':clause_lengths,
      'best_20_combinations':combos[:20],
      'episode_count':0,
      'model_weights_loaded':False,
    }
    Path(args.out).write_text(json.dumps(payload,indent=2),encoding='utf-8')
    print(json.dumps(payload,indent=2))

if __name__=='__main__':
    main()
