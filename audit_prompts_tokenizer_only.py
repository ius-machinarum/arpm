"""Final tokenizer-only structural audit for the frozen A/S/D1 instrument.

NO model weights or inference. Consumes the deterministic role selection produced by
search_token_matched_roles.py and verifies exact position matching in all 12 families.
"""
import argparse, hashlib, json
from pathlib import Path
import prompts_minimal_gate as pmg

PINNED_REVISION='cdbee75f17c01a7cc42f958dc650907174af0554'
EXPECTED_TOKENIZER_SHA256='aeb13307a71acd8fe81861d94ad54ab689df773318809eed3cbe794b4492dae4'
EXPECTED_CONDITIONS=('A','S','D1')

def sha256(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''): h.update(chunk)
    return h.hexdigest()

def load_tokenizer(local_dir):
    from transformers import AutoTokenizer
    return AutoTokenizer.from_pretrained(local_dir,local_files_only=True,trust_remote_code=False)

def setup(f,clause):
    return (
      f"{pmg.STYLE_PREFIX[f.style]} {f.family_id}\n"
      f"R RESULT CODES: {f.result_codes[0]} {f.result_codes[1]}\n"
      f"R TARGET RESULT: {f.target}\n"
      f"AVAILABLE ACTIONS: {' '.join(f.action_codes)}\n"
      f"{clause}\nQ OUTPUT: one action code only."
    )

def msgs(f,clause,recovery=False):
    out=[{'role':'system','content':pmg.SYSTEM},{'role':'user','content':setup(f,clause)},
         {'role':'assistant','content':f.action},{'role':'user','content':pmg.feedback(f)}]
    if recovery:
        out += [{'role':'assistant','content':f.recovery_action},{'role':'user','content':pmg.recovery(f)}]
    return out

def render(tok,m,add): return tok.apply_chat_template(m,tokenize=True,add_generation_prompt=add)

def suffix(a,b):
    if b[:len(a)]!=a: raise AssertionError('generation prompt is not a pure suffix')
    return b[len(a):]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--local-tokenizer-dir',required=True)
    ap.add_argument('--matched-role-clauses',required=True)
    ap.add_argument('--tokenizer-json',required=True)
    ap.add_argument('--revision',default=PINNED_REVISION)
    ap.add_argument('--out',default='tokenizer_audit.json')
    args=ap.parse_args()
    if args.revision!=PINNED_REVISION: raise SystemExit('Refusing non-pinned revision')
    digest=sha256(args.tokenizer_json)
    if digest!=EXPECTED_TOKENIZER_SHA256: raise AssertionError(f'tokenizer SHA mismatch: {digest}')
    selected=json.loads(Path(args.matched_role_clauses).read_text())
    if selected.get('status')!='TOKEN_MATCH_PASS': raise AssertionError('role-clause selection is not passing')
    clauses=selected['selected_clauses']
    if tuple(selected.get('conditions',())) != EXPECTED_CONDITIONS: raise AssertionError('selection condition order mismatch')
    if set(clauses)!=set(EXPECTED_CONDITIONS): raise AssertionError('condition set mismatch')
    tok=load_tokenizer(args.local_tokenizer_dir)
    report={'status':'FINAL_TOKENIZER_AUDIT_PASS','conditions':list(EXPECTED_CONDITIONS),'revision':args.revision,
            'tokenizer_sha256':digest,'selected_indices':selected['selected_indices'],'families':{}}
    for f in pmg.FAMILIES:
        rows={}; suffixes=[]
        for c in EXPECTED_CONDITIONS:
            p=msgs(f,clauses[c],False)
            no=render(tok,p,False); gen=render(tok,p,True); ps=suffix(no,gen)
            full=msgs(f,clauses[c],True)
            full_no=render(tok,full,False); full_gen=render(tok,full,True); rs=suffix(full_no,full_gen)
            if full_gen[:len(gen)]!=gen: raise AssertionError(f'{f.family_id}/{c}: recovery altered primary prefix')
            rows[c]={'primary_prefix_n':len(gen),'primary_no_gen_n':len(no),'recovery_full_n':len(full_gen),
                     'primary_suffix_ids':ps,'recovery_suffix_ids':rs}
            suffixes.append((tuple(ps),tuple(rs)))
        if len({rows[c]['primary_prefix_n'] for c in EXPECTED_CONDITIONS})!=1: raise AssertionError(f'{f.family_id}: primary length mismatch')
        if len({rows[c]['recovery_full_n'] for c in EXPECTED_CONDITIONS})!=1: raise AssertionError(f'{f.family_id}: recovery length mismatch')
        if len(set(suffixes))!=1: raise AssertionError(f'{f.family_id}: template suffix mismatch')
        report['families'][f.family_id]=rows
    Path(args.out).write_text(json.dumps(report,indent=2),encoding='utf-8')
    print(f"PASS: {len(report['families'])} families use A/S/D1 with exact position matching")

if __name__=='__main__': main()
