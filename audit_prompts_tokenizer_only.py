"""Final tokenizer-only structural audit for frozen A/S/C0/D1 instrument. NO model inference."""
import argparse,hashlib,json
from pathlib import Path
import prompts_minimal_gate as pmg
PINNED_REVISION='cdbee75f17c01a7cc42f958dc650907174af0554'
EXPECTED_TOKENIZER_SHA256='aeb13307a71acd8fe81861d94ad54ab689df773318809eed3cbe794b4492dae4'
EXPECTED_CONDITIONS=('A','S','C0','D1')
def sha256(path):
 h=hashlib.sha256()
 with open(path,'rb') as f:
  for chunk in iter(lambda:f.read(1024*1024),b''): h.update(chunk)
 return h.hexdigest()
def setup(f,clause):
 return (f"{pmg.STYLE_PREFIX[f.style]} {f.family_id}\nR RESULT CODES: {f.result_codes[0]} {f.result_codes[1]}\n"
         f"R TARGET RESULT: {f.target}\nAVAILABLE ACTIONS: {' '.join(f.action_codes)}\n{clause}\nQ OUTPUT: one action code only.")
def msgs(f,clause,rec=False):
 out=[{'role':'system','content':pmg.SYSTEM},{'role':'user','content':setup(f,clause)},
      {'role':'assistant','content':f.action},{'role':'user','content':pmg.feedback(f)}]
 if rec: out += [{'role':'assistant','content':f.recovery_action},{'role':'user','content':pmg.recovery(f)}]
 return out
def main():
 from transformers import AutoTokenizer
 ap=argparse.ArgumentParser(); ap.add_argument('--local-tokenizer-dir',required=True); ap.add_argument('--matched-role-clauses',required=True)
 ap.add_argument('--tokenizer-json',required=True); ap.add_argument('--revision',default=PINNED_REVISION); ap.add_argument('--out',default='tokenizer_audit.json'); args=ap.parse_args()
 if args.revision!=PINNED_REVISION: raise SystemExit('Refusing non-pinned revision')
 digest=sha256(args.tokenizer_json)
 if digest!=EXPECTED_TOKENIZER_SHA256: raise AssertionError('tokenizer SHA mismatch')
 selected=json.loads(Path(args.matched_role_clauses).read_text()); clauses=selected['selected_clauses']
 if selected.get('status')!='TOKEN_MATCH_PASS' or tuple(selected.get('conditions',()))!=EXPECTED_CONDITIONS or set(clauses)!=set(EXPECTED_CONDITIONS): raise AssertionError('selection mismatch')
 tok=AutoTokenizer.from_pretrained(args.local_tokenizer_dir,local_files_only=True,trust_remote_code=False)
 rep={'status':'FINAL_TOKENIZER_AUDIT_PASS','conditions':list(EXPECTED_CONDITIONS),'revision':args.revision,'tokenizer_sha256':digest,'selected_indices':selected['selected_indices'],'families':{}}
 for f in pmg.FAMILIES:
  rows={}; suff=[]
  for c in EXPECTED_CONDITIONS:
   p=msgs(f,clauses[c],False); no=tok.apply_chat_template(p,tokenize=True,add_generation_prompt=False); gen=tok.apply_chat_template(p,tokenize=True,add_generation_prompt=True)
   if gen[:len(no)]!=no: raise AssertionError('generation prompt not suffix')
   ps=gen[len(no):]
   full=msgs(f,clauses[c],True); fno=tok.apply_chat_template(full,tokenize=True,add_generation_prompt=False); fgen=tok.apply_chat_template(full,tokenize=True,add_generation_prompt=True)
   if fgen[:len(fno)]!=fno or fgen[:len(gen)]!=gen: raise AssertionError(f'{f.family_id}/{c}: causal prefix mismatch')
   rs=fgen[len(fno):]
   rows[c]={'primary_prefix_n':len(gen),'primary_no_gen_n':len(no),'recovery_full_n':len(fgen),'primary_suffix_ids':ps,'recovery_suffix_ids':rs}; suff.append((tuple(ps),tuple(rs)))
  if len({rows[c]['primary_prefix_n'] for c in EXPECTED_CONDITIONS})!=1 or len({rows[c]['recovery_full_n'] for c in EXPECTED_CONDITIONS})!=1 or len(set(suff))!=1: raise AssertionError(f'{f.family_id}: exact matching failed')
  rep['families'][f.family_id]=rows
 Path(args.out).write_text(json.dumps(rep,indent=2),encoding='utf-8'); print(f"PASS: {len(rep['families'])} families A/S/C0/D1 exact")
if __name__=='__main__': main()
