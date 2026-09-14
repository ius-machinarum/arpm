from pathlib import Path
ROOT=Path(__file__).resolve().parent
def test_no_model_loader_in_episode_free_tools():
 files=['tokenizer_snapshot_audit.py','inspect_vector_artifact.py','freeze_vector_artifact.py','freeze_naive_artifact.py',
        'specificity_controls.py','specificity_geometry_audit.py','search_token_matched_roles.py','audit_prompts_tokenizer_only.py','run_episode_free_audit.py']
 banned={'AutoModel','AutoModelForCausalLM','pipeline','from_pretrained_model'}
 for fn in files:
  txt=(ROOT/fn).read_text()
  for b in banned: assert b not in txt,(fn,b)
def test_orchestrator_status_is_not_live_permission():
 txt=(ROOT/'run_episode_free_audit.py').read_text()
 assert 'READY_FOR_THIRD_ADVERSARIAL_REVIEW_NOT_LIVE_RUN' in txt
 assert "'conditions':['A','S','C0','D1']" in txt
 assert 'specificity_geometry' in txt and 'random_direction_freeze' in txt
 assert "'episode_count':0" in txt and "'model_weights_loaded':False" in txt
def test_final_tokenizer_audit_consumes_search_selection():
 txt=(ROOT/'audit_prompts_tokenizer_only.py').read_text()
 assert '--matched-role-clauses' in txt and "selected['selected_clauses']" in txt
def test_tokenizer_snapshot_rejects_weights():
 txt=(ROOT/'tokenizer_snapshot_audit.py').read_text()
 assert '.safetensors' in txt and '.bin' in txt and 'Model-weight-like file found' in txt
def test_pins_consistent():
 rev='cdbee75f17c01a7cc42f958dc650907174af0554'; sha='aeb13307a71acd8fe81861d94ad54ab689df773318809eed3cbe794b4492dae4'
 for fn in ['search_token_matched_roles.py','audit_prompts_tokenizer_only.py','tokenizer_snapshot_audit.py']:
  txt=(ROOT/fn).read_text(); assert rev in txt,fn; assert sha in txt,fn
if __name__=='__main__':
 for n,v in sorted(globals().items()):
  if n.startswith('test_') and callable(v): v()
 print('PASS')
