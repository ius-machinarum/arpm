"""Static repository-integrity checks for the v0.9 preregistration freeze."""
from pathlib import Path
ROOT=Path(__file__).resolve().parent
REQUIRED=[
 "README.md","STATUS.md","VERSION","V0_9_PREREGISTRATION.md",
 "analysis_preregistered_v0_9.py","test_analysis_prereg_static.py",
 "REFEREE_RESPONSE_v0_8.md","reviews/FABLE_REFEREE_v0_8.md",
 "PROTOCOL.md","STATS_PLAN.md","SPECIFICITY_PLAN.md","ETHICS_CHARTER.md",
 "episode_free_audit.frozen.json","tokenizer_match.frozen.json",
 "specificity_geometry.frozen.json","random_direction_freeze.frozen.json"
]
FORBIDDEN={".pt",".pth",".bin",".safetensors",".gguf",".ckpt",".onnx"}

def main():
    missing=[p for p in REQUIRED if not (ROOT/p).is_file()]
    assert not missing,missing
    bad=[str(p.relative_to(ROOT)) for p in ROOT.rglob("*")
         if p.is_file() and p.suffix.lower() in FORBIDDEN]
    assert not bad,bad
    readme=(ROOT/"README.md").read_text()
    status=(ROOT/"STATUS.md").read_text()
    amendment=(ROOT/"V0_9_PREREGISTRATION.md").read_text()
    assert "v0.9" in readme and "v0.9" in status
    assert "Episode count remains **0**" in status
    assert "No live experimental inference was performed." in readme
    assert "No live inference is authorised." in status
    assert "HUMAN_ETHICAL_NO_GO_V0_9_NO_LIVE_RUN" in readme
    assert "HUMAN_ETHICAL_NO_GO_V0_9_NO_LIVE_RUN" in status
    assert (ROOT/"HUMAN_DECISION_v0_9.md").is_file()
    assert "INTERACTION_NOT_IDENTIFIABLE_DUE_TO_NO_STAKE_COMPRESSION" in amendment
    assert "COMPOSITION_ALTERNATIVE_NOT_EXCLUDED" in amendment
    print("REPOSITORY_INTEGRITY_V0_9_PASS")

if __name__=="__main__":
    main()
