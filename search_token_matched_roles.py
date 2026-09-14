"""Deterministic tokenizer-only search for A/S/C0/D1 clauses. NO model inference."""
import argparse,hashlib,json
from pathlib import Path
from role_clause_variants import ROLE_VARIANTS,FROZEN_VARIANT_ORDER,VARIANT_SET_VERSION
import prompts_minimal_gate as pmg
PINNED_REVISION="cdbee75f17c01a7cc42f958dc650907174af0554"
EXPECTED_TOKENIZER_SHA256="aeb13307a71acd8fe81861d94ad54ab689df773318809eed3cbe794b4492dae4"
MATCH_CONDITIONS=("A","S","C0","D1")
def sha256(path):
 h=hashlib.sha256()
 with open(path,"rb") as f:
  for chunk in iter(lambda:f.read(1024*1024),b""): h.update(chunk)
 return h.hexdigest()
def load_tokenizer(args):
 from transformers import AutoTokenizer
 if args.local_tokenizer_dir: return AutoTokenizer.from_pretrained(args.local_tokenizer_dir,local_files_only=True,trust_remote_code=False)
 return AutoTokenizer.from_pretrained(args.model,revision=args.revision,trust_remote_code=False)
def render(tok,msgs,add): return tok.apply_chat_template(msgs,tokenize=True,add_generation_prompt=add)
def suffix(a,b):
 if b[:len(a)]!=a: raise AssertionError("generation prompt is not a pure suffix")
 return b[len(a):]
def setup(f,clause):
 return (f"{pmg.STYLE_PREFIX[f.style]} {f.family_id}\nR RESULT CODES: {f.result_codes[0]} {f.result_codes[1]}\n"
         f"R TARGET RESULT: {f.target}\nAVAILABLE ACTIONS: {' '.join(f.action_codes)}\n{clause}\nQ OUTPUT: one action code only.")
def msgs(f,clause,rec):
 out=[{"role":"system","content":pmg.SYSTEM},{"role":"user","content":setup(f,clause)},
      {"role":"assistant","content":f.action},{"role":"user","content":pmg.feedback(f)}]
 if rec: out += [{"role":"assistant","content":f.recovery_action},{"role":"user","content":pmg.recovery(f)}]
 return out
def audit_combo(tok,idxs):
 clauses={c:ROLE_VARIANTS[c][i] for c,i in zip(MATCH_CONDITIONS,idxs)}
 reports={}
 for f in pmg.FAMILIES:
  rows={}; suff=[]
  for c in MATCH_CONDITIONS:
   p=msgs(f,clauses[c],False); no=render(tok,p,False); gen=render(tok,p,True); ps=suffix(no,gen)
   full=msgs(f,clauses[c],True); full_no=render(tok,full,False); full_gen=render(tok,full,True); rs=suffix(full_no,full_gen)
   if full_gen[:len(gen)]!=gen: return None
   rows[c]={"primary_prefix_n":len(gen),"primary_no_gen_n":len(no),"recovery_full_n":len(full_gen),
            "primary_suffix_ids":ps,"recovery_suffix_ids":rs,
            "setup_n":len(tok.encode(setup(f,clauses[c]),add_special_tokens=False))}
   suff.append((tuple(ps),tuple(rs)))
  if len({rows[c]["primary_prefix_n"] for c in MATCH_CONDITIONS})!=1: return None
  if len({rows[c]["recovery_full_n"] for c in MATCH_CONDITIONS})!=1: return None
  if len(set(suff))!=1: return None
  reports[f.family_id]=rows
 total=sum(next(iter(r.values()))["primary_prefix_n"] for r in reports.values())
 return clauses,reports,total
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--model",default="Qwen/Qwen3-4B-Instruct-2507"); ap.add_argument("--revision",default=PINNED_REVISION)
 ap.add_argument("--local-tokenizer-dir"); ap.add_argument("--tokenizer-json"); ap.add_argument("--out",default="matched_role_clauses.json"); args=ap.parse_args()
 if not args.local_tokenizer_dir and args.revision!=PINNED_REVISION: raise SystemExit("Refusing non-pinned remote revision")
 if args.tokenizer_json and sha256(args.tokenizer_json)!=EXPECTED_TOKENIZER_SHA256: raise AssertionError("tokenizer.json SHA mismatch")
 if args.local_tokenizer_dir and not args.tokenizer_json: raise SystemExit("--tokenizer-json required with local snapshot")
 tok=load_tokenizer(args); import transformers
 hits=[]
 for idxs in FROZEN_VARIANT_ORDER:
  r=audit_combo(tok,idxs)
  if r is not None:
   clauses,reports,total=r; hits.append((total,idxs,clauses,reports))
 if not hits: raise SystemExit("NO EXACT A/S/C0/D1 MATCH among precommitted variants")
 hits.sort(key=lambda x:(x[0],x[1])); total,idxs,clauses,reports=hits[0]
 payload={"status":"TOKEN_MATCH_PASS","variant_set_version":VARIANT_SET_VERSION,"conditions":list(MATCH_CONDITIONS),
          "model":args.model,"revision":args.revision if not args.local_tokenizer_dir else "LOCAL_SNAPSHOT_MUST_BE_MANIFESTED",
          "selection_rule":"minimum total primary-prefix tokens, then frozen lexicographic variant indices",
          "selected_indices":dict(zip(MATCH_CONDITIONS,idxs)),"selected_clauses":clauses,"n_exact_hits":len(hits),
          "transformers_version":transformers.__version__,"tokenizer_json_sha256":sha256(args.tokenizer_json) if args.tokenizer_json else None,
          "families":reports}
 Path(args.out).write_text(json.dumps(payload,indent=2),encoding="utf-8")
 print(json.dumps({k:payload[k] for k in ["status","variant_set_version","selected_indices","n_exact_hits"]},indent=2))
if __name__=="__main__": main()
