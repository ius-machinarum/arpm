"""Repository-integrity checks that require no model, tokenizer, vector or network access."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent

REQUIRED = {
    "README.md", "STATUS.md", "PROTOCOL.md", "ETHICS_CHARTER.md",
    "STATS_PLAN.md", "PROMPT_MATCHING.md", "VECTOR_PROVENANCE.md",
    "EPISODE_FREE_AUDIT.md", "REFEREE_QUESTIONS.md", "SOURCES.md",
    "TOKENIZER_SNAPSHOT.md", "PASSIVE_ACQUISITION.md", "FREEZE_STATUS.md",
    "acquire_passive_artifacts.py", "tokenizer_snapshot_audit.py",
    "inspect_vector_artifact.py", "freeze_vector_artifact.py",
    "role_clause_variants.py", "search_token_matched_roles.py",
    "audit_prompts_tokenizer_only.py", "run_episode_free_audit.py",
    "prompts_minimal_gate.py", "requirements_episode_free.txt",
    "artifact_manifest.template.json", "artifact_manifest.frozen.json",
    "tokenizer_match.frozen.json", "episode_free_audit.frozen.json",
    "TOKENIZER_CALIBRATION_LOG.md", "REFEREE_PACKET.md", ".gitignore",
}

FORBIDDEN_TRACKED_SUFFIXES = {".pt", ".pth", ".bin", ".safetensors", ".gguf", ".ckpt", ".onnx"}

def main():
    present = {p.name for p in ROOT.iterdir() if p.is_file()}
    missing = sorted(REQUIRED - present)
    assert not missing, f"Required files missing: {missing}"

    forbidden = [
        p.name for p in ROOT.rglob("*")
        if p.is_file() and p.suffix.lower() in FORBIDDEN_TRACKED_SUFFIXES
    ]
    assert not forbidden, f"Model/vector binary artifact tracked unexpectedly: {forbidden}"

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    status = (ROOT / "STATUS.md").read_text(encoding="utf-8")
    ethics = (ROOT / "ETHICS_CHARTER.md").read_text(encoding="utf-8")

    assert "NO LIVE MODEL RUNS" in readme
    assert "NO LIVE MODEL RUNS" in status
    assert "READY_FOR_ADVERSARIAL_REVIEW_NOT_LIVE_RUN" in readme
    assert "No unnecessary possible harm" in ethics

    # Generic local-path leak checks; personal names/emails are checked off-repo.
    text = "\n".join(
        p.read_text(encoding="utf-8", errors="ignore")
        for p in ROOT.rglob("*")
        if p.is_file() and p.suffix.lower() in {".md", ".txt", ".py", ".json", ".cff", ""}
    )
    assert not re.search(r"[A-Za-z]:\\\\Users\\\\[^\\\s]+", text), "Windows user path found"
    assert not re.search(r"/home/[A-Za-z0-9._-]+/", text), "Absolute Unix home path found"

    print("REPOSITORY_INTEGRITY_PASS")

if __name__ == "__main__":
    main()
