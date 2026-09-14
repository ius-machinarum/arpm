"""Orchestrate the full v0.7 episode-free pre-referee audit.

Requires only passive tokenizer/vector artifacts. No language-model weights are loaded.
A PASS means ready for adversarial review, not permission to run the Minimal Gate.
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
    ap.add_argument('--naive-artifact',required=True)
    ap.add_argument('--artifact-repo',required=True)
    ap.add_argument('--artifact-revision',required=True)
    ap.add_argument('--mold-key',default='v_mold')
    ap.add_argument('--gold-key',default='v_gold')
    ap.add_argument('--mold-index',type=int,default=24)
    ap.add_argument('--gold-index',type=int,default=21)
    ap.add_argument('--tokenizer-dir',required=True)
    ap.add_argument('--out-dir',default='episode_free_audit')
    args=ap.parse_args()

    root=Path(__file__).resolve().parent
    out=Path(args.out_dir); out.mkdir(parents=True,exist_ok=True)
    py=sys.executable
    tok_json=Path(args.tokenizer_dir)/'tokenizer.json'

    run([py,str(root/'tokenizer_snapshot_audit.py'),args.tokenizer_dir,'--out',str(out/'tokenizer_snapshot_manifest.json')])
    run([py,str(root/'inspect_vector_artifact.py'),args.artifact,'--out',str(out/'vector_structure_audit.json')])

    run([
      py,str(root/'freeze_vector_artifact.py'),args.artifact,
      '--repo',args.artifact_repo,'--revision',args.artifact_revision,
      '--mold-key',args.mold_key,'--gold-key',args.gold_key,
      '--mold-index',str(args.mold_index),'--gold-index',str(args.gold_index),
      '--out',str(out/'artifact_manifest.frozen.json')
    ])

    run([
      py,str(root/'freeze_naive_artifact.py'),args.naive_artifact,
      '--repo',args.artifact_repo,'--revision',args.artifact_revision,
      '--out',str(out/'naive_control_manifest.frozen.json')
    ])

    run([py,str(root/'specificity_controls.py'),'--out',str(out/'random_direction_freeze.json')])

    run([
      py,str(root/'search_token_matched_roles.py'),
      '--local-tokenizer-dir',args.tokenizer_dir,
      '--tokenizer-json',str(tok_json),
      '--out',str(out/'matched_role_clauses.json')
    ])

    run([
      py,str(root/'audit_prompts_tokenizer_only.py'),
      '--local-tokenizer-dir',args.tokenizer_dir,
      '--tokenizer-json',str(tok_json),
      '--matched-role-clauses',str(out/'matched_role_clauses.json'),
      '--out',str(out/'tokenizer_audit.json')
    ])

    components={
      'tokenizer_snapshot':load(out/'tokenizer_snapshot_manifest.json'),
      'vector_structure':load(out/'vector_structure_audit.json'),
      'vector_freeze':load(out/'artifact_manifest.frozen.json'),
      'naive_control_freeze':load(out/'naive_control_manifest.frozen.json'),
      'random_direction_freeze':load(out/'random_direction_freeze.json'),
      'role_match':load(out/'matched_role_clauses.json'),
      'tokenizer_audit':load(out/'tokenizer_audit.json'),
    }

    statuses=[
      components['tokenizer_snapshot']['status'],
      components['vector_freeze']['status'],
      components['naive_control_freeze']['status'],
      components['random_direction_freeze']['status'],
      components['role_match']['status'],
      components['tokenizer_audit']['status'],
    ]
    expected=[
      'TOKENIZER_BYTES_PASS_NO_MODEL_WEIGHTS',
      'BYTE_FROZEN_VECTOR_PASS',
      'BYTE_FROZEN_NAIVE_CONTROL_PASS',
      'RANDOM_DIRECTION_FREEZE_PASS',
      'TOKEN_MATCH_PASS',
      'FINAL_TOKENIZER_AUDIT_PASS',
    ]
    if statuses != expected:
        raise AssertionError((statuses,expected))

    payload={
      'status':'READY_FOR_ADVERSARIAL_REVIEW_NOT_LIVE_RUN',
      'freeze_version':'v0.7',
      'conditions':['A','S','D1'],
      'episode_count':0,
      'model_weights_loaded':False,
      'components':components,
    }
    Path(out/'episode_free_audit.json').write_text(json.dumps(payload,indent=2),encoding='utf-8')
    print(json.dumps({'status':payload['status'],'freeze_version':'v0.7','episode_count':0,'model_weights_loaded':False},indent=2))

if __name__=='__main__': main()
