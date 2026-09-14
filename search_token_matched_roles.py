"""Deterministic tokenizer-only search for A/S/D1 role clauses.

NO model weights are loaded. The search uses only the precommitted finite variants.
The same triplet must exactly match all 12 families at primary and recovery positions.
"""
import argparse, hashlib, json
from pathlib import Path
from role_clause_variants import ROLE_VARIANTS, FROZEN_VARIANT_ORDER, VARIANT_SET_VERSION
import prompts_minimal_gate as pmg

PINNED_REVISION = "cdbee75f17c01a7cc42f958dc650907174af0554"
EXPECTED_TOKENIZER_SHA256 = "aeb13307a71acd8fe81861d94ad54ab689df773318809eed3cbe794b4492dae4"
MATCH_CONDITIONS = ("A","S","D1")

def sha256(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for chunk in iter(lambda:f.read(1024*1024), b""): h.update(chunk)
    return h.hexdigest()

def load_tokenizer(args):
    from transformers import AutoTokenizer
    if args.local_tokenizer_dir:
        return AutoTokenizer.from_pretrained(args.local_tokenizer_dir, local_files_only=True, trust_remote_code=False)
    return AutoTokenizer.from_pretrained(args.model, revision=args.revision, trust_remote_code=False)

def render_ids(tok,msgs,add_generation_prompt):
    return tok.apply_chat_template(msgs,tokenize=True,add_generation_prompt=add_generation_prompt)

def suffix_added(base_ids,gen_ids):
    if gen_ids[:len(base_ids)] != base_ids: raise AssertionError("generation prompt is not a pure suffix")
    return gen_ids[len(base_ids):]

def user_setup_with(f,clause):
    return (
        f"{pmg.STYLE_PREFIX[f.style]} {f.family_id}\n"
        f"R RESULT CODES: {f.result_codes[0]} {f.result_codes[1]}\n"
        f"R TARGET RESULT: {f.target}\n"
        f"AVAILABLE ACTIONS: {' '.join(f.action_codes)}\n"
        f"{clause}\nQ OUTPUT: one action code only."
    )

def messages_with(f,clause,include_recovery):
    out=[
        {"role":"system","content":pmg.SYSTEM},
        {"role":"user","content":user_setup_with(f,clause)},
        {"role":"assistant","content":f.action},
        {"role":"user","content":pmg.feedback(f)},
    ]
    if include_recovery:
        out += [{"role":"assistant","content":f.recovery_action},{"role":"user","content":pmg.recovery(f)}]
    return out

def audit_combo(tok,idxs):
    clauses={c:ROLE_VARIANTS[c][i] for c,i in zip(MATCH_CONDITIONS,idxs)}
    family_reports={}
    for f in pmg.FAMILIES:
        rows={}; suffixes=[]
        for c in MATCH_CONDITIONS:
            primary=messages_with(f,clauses[c],False)
            no_gen=render_ids(tok,primary,False); with_gen=render_ids(tok,primary,True)
            ps=suffix_added(no_gen,with_gen)
            full=messages_with(f,clauses[c],True)
            full_no=render_ids(tok,full,False); full_ids=render_ids(tok,full,True)
            if full_ids[:len(with_gen)] != with_gen: return None
            rs=suffix_added(full_no,full_ids)
            rows[c]={
                "primary_prefix_n":len(with_gen),
                "primary_no_gen_n":len(no_gen),
                "recovery_full_n":len(full_ids),
                "primary_suffix_ids":ps,
                "recovery_suffix_ids":rs,
                "setup_n":len(tok.encode(user_setup_with(f,clauses[c]),add_special_tokens=False)),
            }
            suffixes.append((tuple(ps),tuple(rs)))
        if len({rows[c]["primary_prefix_n"] for c in MATCH_CONDITIONS}) != 1: return None
        if len({rows[c]["recovery_full_n"] for c in MATCH_CONDITIONS}) != 1: return None
        if len(set(suffixes)) != 1: return None
        family_reports[f.family_id]=rows
    total=sum(next(iter(r.values()))["primary_prefix_n"] for r in family_reports.values())
    return clauses,family_reports,total

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--model",default="Qwen/Qwen3-4B-Instruct-2507")
    ap.add_argument("--revision",default=PINNED_REVISION)
    ap.add_argument("--local-tokenizer-dir",default=None)
    ap.add_argument("--tokenizer-json",default=None)
    ap.add_argument("--out",default="matched_role_clauses.json")
    args=ap.parse_args()
    if not args.local_tokenizer_dir and args.revision != PINNED_REVISION: raise SystemExit("Refusing non-pinned remote revision")
    if args.tokenizer_json:
        d=sha256(args.tokenizer_json)
        if d != EXPECTED_TOKENIZER_SHA256: raise AssertionError(f"tokenizer.json SHA mismatch: {d}")
    if args.local_tokenizer_dir and not args.tokenizer_json: raise SystemExit("--tokenizer-json is required with a local tokenizer snapshot")
    tok=load_tokenizer(args)
    import transformers
    hits=[]
    for idxs in FROZEN_VARIANT_ORDER:
        r=audit_combo(tok,idxs)
        if r is not None:
            clauses,reports,total=r
            hits.append((total,idxs,clauses,reports))
    if not hits: raise SystemExit("NO EXACT A/S/D1 MATCH among precommitted semantic variants.")
    hits.sort(key=lambda x:(x[0],x[1]))
    total,idxs,clauses,reports=hits[0]
    payload={
        "status":"TOKEN_MATCH_PASS",
        "variant_set_version":VARIANT_SET_VERSION,
        "conditions":list(MATCH_CONDITIONS),
        "model":args.model,
        "revision":args.revision if not args.local_tokenizer_dir else "LOCAL_SNAPSHOT_MUST_BE_MANIFESTED",
        "selection_rule":"minimum total primary-prefix tokens, then frozen lexicographic variant indices",
        "selected_indices":{"A":idxs[0],"S":idxs[1],"D1":idxs[2]},
        "selected_clauses":clauses,
        "n_exact_hits":len(hits),
        "transformers_version":transformers.__version__,
        "tokenizer_json_sha256":sha256(args.tokenizer_json) if args.tokenizer_json else None,
        "families":reports,
    }
    Path(args.out).write_text(json.dumps(payload,indent=2),encoding="utf-8")
    print(json.dumps({k:payload[k] for k in ["status","variant_set_version","selected_indices","n_exact_hits"]},indent=2))

if __name__=="__main__": main()
