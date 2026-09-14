"""Orchestrate ALL remaining pre-referee checks without loading model weights.

Requires only:
  1) vectors_step95_bal.pt
  2) a local tokenizer-only snapshot for Qwen3-4B-Instruct-2507
  3) explicit artifact key/index mapping from source metadata inspection

If every stage passes, writes episode_free_audit.json. PASS means READY FOR REFEREE,
not permission to run a language model.
"""
import argparse, json, subprocess, sys
from pathlib import Path

def run(cmd):
    p=subprocess.run(cmd,text=True,capture_output=True)
    if p.returncode:
        sys.stderr.write(p.stdout+p.stderr)
        raise SystemExit(p.returncode)
    return p.stdout

def load(p): return json.loads(Path(p).read_text())

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--artifact',required=True)
    ap.add_argument('--artifact-repo',required=True)
    ap.add_argument('--artifact-revision',required=True)
    ap.add_argument('--mold-key',required=True)
    ap.add_argument('--gold-key',required=True)
    ap.add_argument('--mold-index',type=int)
    ap.add_argument('--gold-index',type=int)
    ap.add_argument('--tokenizer-dir',required=True)
    ap.add_argument('--out-dir',default='episode_free_audit')
    args=ap.parse_args()
    root=Path(__file__).resolve().parent
    out=Path(args.out_dir); out.mkdir(parents=True,exist_ok=True)
    py=sys.executable
    tok_json=Path(args.tokenizer_dir)/'tokenizer.json'

    run([py,str(root/'tokenizer_snapshot_audit.py'),args.tokenizer_dir,'--out',str(out/'tokenizer_snapshot_manifest.json')])
    run([py,str(root/'inspect_vector_artifact.py'),args.artifact,'--out',str(out/'vector_structure_audit.json')])
    cmd=[py,str(root/'freeze_vector_artifact.py'),args.artifact,'--repo',args.artifact_repo,'--revision',args.artifact_revision,'--mold-key',args.mold_key,'--gold-key',args.gold_key,'--out',str(out/'artifact_manifest.frozen.json')]
    if args.mold_index is not None: cmd += ['--mold-index',str(args.mold_index)]
    if args.gold_index is not None: cmd += ['--gold-index',str(args.gold_index)]
    run(cmd)
    run([py,str(root/'search_token_matched_roles.py'),'--local-tokenizer-dir',args.tokenizer_dir,'--tokenizer-json',str(tok_json),'--out',str(out/'matched_role_clauses.json')])
    run([py,str(root/'audit_prompts_tokenizer_only.py'),'--local-tokenizer-dir',args.tokenizer_dir,'--tokenizer-json',str(tok_json),'--matched-role-clauses',str(out/'matched_role_clauses.json'),'--out',str(out/'tokenizer_audit.json')])

    components={
      'tokenizer_snapshot':load(out/'tokenizer_snapshot_manifest.json'),
      'vector_structure':load(out/'vector_structure_audit.json'),
      'vector_freeze':load(out/'artifact_manifest.frozen.json'),
      'role_match':load(out/'matched_role_clauses.json'),
      'tokenizer_audit':load(out/'tokenizer_audit.json'),
    }
    statuses=[components['tokenizer_snapshot']['status'],components['vector_freeze']['status'],components['role_match']['status'],components['tokenizer_audit']['status']]
    expected=['TOKENIZER_BYTES_PASS_NO_MODEL_WEIGHTS','BYTE_FROZEN_VECTOR_PASS','TOKEN_MATCH_PASS','FINAL_TOKENIZER_AUDIT_PASS']
    if statuses!=expected: raise AssertionError((statuses,expected))
    payload={
      'status':'READY_FOR_ADVERSARIAL_REVIEW_NOT_LIVE_RUN',
      'episode_count':0,
      'model_weights_loaded':False,
      'components':components,
    }
    Path(out/'episode_free_audit.json').write_text(json.dumps(payload,indent=2),encoding='utf-8')
    print(json.dumps({'status':payload['status'],'episode_count':0,'model_weights_loaded':False},indent=2))

if __name__=='__main__': main()
