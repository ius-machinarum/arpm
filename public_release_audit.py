"""Static pre-public-release guard for ARPM.

Scans the tracked working tree for common accidental privacy/credential leaks and
requires the pre-live status banner. No network access and no model inference.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
SKIP = {Path(__file__).name, ".git"}
TEXT_SUFFIXES = {".md", ".txt", ".py", ".json", ".yml", ".yaml", ".cff", ""}

EMAIL_RX = re.compile(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}", re.I)
PATTERNS = {
    "windows_user_home": re.compile(r"[A-Za-z]:\\Users\\[^\\\s\"']+"),
    "unix_user_home": re.compile(r"/home/[A-Za-z0-9._-]+/"),
    "github_classic_token": re.compile(r"\bgh" + r"[pousr]_[A-Za-z0-9]{20,}\b"),
    "github_finegrained_token": re.compile(r"\bgithub_" + r"pat_[A-Za-z0-9_]{20,}\b"),
    "openai_style_key": re.compile(r"\bsk" + r"-[A-Za-z0-9_-]{20,}\b"),
    "aws_access_key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "private_key_block": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "bearer_credential": re.compile(r"\bBearer\s+[A-Za-z0-9._~+/=-]{20,}\b"),
}
FORBIDDEN_BINARY_SUFFIXES = {".pt", ".pth", ".bin", ".safetensors", ".gguf", ".ckpt", ".onnx"}

def github_noreply(email: str) -> bool:
    low = email.lower()
    return low == "noreply@github.com" or low.endswith("@users.noreply.github.com")

def main():
    findings = []
    binaries = []
    for p in ROOT.rglob("*"):
        if not p.is_file() or ".git" in p.parts:
            continue
        rel = p.relative_to(ROOT)
        if p.suffix.lower() in FORBIDDEN_BINARY_SUFFIXES:
            binaries.append(str(rel))
            continue
        if rel.name in SKIP or p.suffix.lower() not in TEXT_SUFFIXES:
            continue
        text = p.read_text(encoding="utf-8", errors="ignore")
        for email in EMAIL_RX.findall(text):
            if not github_noreply(email):
                findings.append((str(rel), "personal_email"))
        for name, rx in PATTERNS.items():
            if rx.search(text):
                findings.append((str(rel), name))

    assert not binaries, f"Tracked release-sensitive binaries: {binaries}"
    assert not findings, f"Release-sensitive text matches: {findings}"

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    status = (ROOT / "STATUS.md").read_text(encoding="utf-8")
    assert "PRE-LIVE PREREGISTRATION — HUMAN ETHICAL NO-GO" in readme
    assert "Live episode count:** **0**" in readme
    assert "No live experimental inference was performed." in readme
    assert "HUMAN_ETHICAL_NO_GO_V0_9_NO_LIVE_RUN" in readme
    assert "Episode count remains 0" in status
    assert (ROOT / "PUBLIC_RELEASE_AUDIT.md").is_file()
    assert (ROOT / "HUMAN_DECISION_v0_9.md").is_file()
    assert (ROOT / "THIRD_PARTY_LICENSES.md").is_file()
    print("PUBLIC_RELEASE_STATIC_AUDIT_PASS")

if __name__ == "__main__":
    main()
