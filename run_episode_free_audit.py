"""Orchestrate the full v0.8 episode-free pre-referee audit.

Requires only passive tokenizer/vector artifacts. No language-model weights are loaded.
A PASS means ready for third adversarial review, not permission for live inference.
"""
import argparse,json,subprocess,sys
from pathlib import Path
def run(cmd):
 p=subprocess.run(cmd,text=True,capture_output=True)
 if p.returncode:
  sys.stderr.write(p.stdout+p.stderr); raise SystemExit(p.returncode)
 return p.stdout
def load(p): return json.loads(Path(p).read_text())
def main():
 ap=argparse.ArgumentParser()
 ap.add_argument('--artifact',required=True); ap.add_argument('--naive-artifact',required=True)
 ap.add_argument('--artifact-repo',required=True); ap.add_argument('--artifact-revision',required=True)
 ap.add_argument('--tokenizer-dir',required=True); ap.add_argument('--out-dir',default='episode_free_audit')
 args=ap.parse_args(); root=Path(__file__).resolve().parent; out=Path(args.out_dir); out.mkdir(parents=True,exist_ok=True); py=sys.executable
 tok_json=Path(args.tokenizer_dir)/'tokenizer.json'
 run([py,str(root/'tokenizer_snapshot_audit.py'),args.tokenizer_dir,'--out',str(out/'tokenizer_snapshot_manifest.json')])
 run([py,str(root/'inspect_vector_artifact.py'),args.artifact,'--out',str(out/'vector_structure_audit.json')])
 run([py,str(root/'freeze_vector_artifact.py'),args.artifact,'--repo',args.artifact_repo,'--revision',args.artifact_revision,
      '--mold-key','v_mold','--gold-key','v_gold','--mold-index','24','--gold-index','21','--out',str(out/'artifact_manifest.frozen.json')])
 run([py,str(root/'freeze_naive_artifact.py'),args.naive_artifact,'--repo',args.artifact_repo,'--revision',args.artifact_revision,
      '--out',str(out/'naive_control_manifest.frozen.json')])
 run([py,str(root/'specificity_geometry_audit.py'),'--trained',args.artifact,'--naive',args.naive_artifact,'--out',str(out/'specificity_geometry.json')])
 run([py,str(root/'specificity_controls.py'),'--out',str(out/'random_direction_freeze.json')])
 run([py,str(root/'search_token_matched_roles.py'),'--local-tokenizer-dir',args.tokenizer_dir,'--tokenizer-json',str(tok_json),'--out',str(out/'matched_role_clauses.json')])
 run([py,str(root/'audit_prompts_tokenizer_only.py'),'--local-tokenizer-dir',args.tokenizer_dir,'--tokenizer-json',str(tok_json),
      '--matched-role-clauses',str(out/'matched_role_clauses.json'),'--out',str(out/'tokenizer_audit.json')])
 components={
  'tokenizer_snapshot':load(out/'tokenizer_snapshot_manifest.json'),
  'vector_freeze':load(out/'artifact_manifest.frozen.json'),
  'naive_control_freeze':load(out/'naive_control_manifest.frozen.json'),
  'specificity_geometry':load(out/'specificity_geometry.json'),
  'random_direction_freeze':load(out/'random_direction_freeze.json'),
  'role_match':load(out/'matched_role_clauses.json'),
  'tokenizer_audit':load(out/'tokenizer_audit.json')}
 statuses=[components[k]['status'] for k in ['tokenizer_snapshot','vector_freeze','naive_control_freeze','specificity_geometry','random_direction_freeze','role_match','tokenizer_audit']]
 expected=['TOKENIZER_BYTES_PASS_NO_MODEL_WEIGHTS','BYTE_FROZEN_VECTOR_PASS','BYTE_FROZEN_NAIVE_CONTROL_PASS','SPECIFICITY_GEOMETRY_PASS','RANDOM_DIRECTION_FREEZE_PASS','TOKEN_MATCH_PASS','FINAL_TOKENIZER_AUDIT_PASS']
 if statuses!=expected: raise AssertionError((statuses,expected))
 payload={'status':'READY_FOR_THIRD_ADVERSARIAL_REVIEW_NOT_LIVE_RUN','freeze_version':'v0.8',
          'conditions':['A','S','C0','D1'],'episode_count':0,'model_weights_loaded':False,'components':components}
 Path(out/'episode_free_audit.json').write_text(json.dumps(payload,indent=2),encoding='utf-8')
 print(json.dumps({'status':payload['status'],'freeze_version':'v0.8','episode_count':0,'model_weights_loaded':False},indent=2))
if __name__=='__main__': main()
