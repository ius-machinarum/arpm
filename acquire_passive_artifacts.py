"""Acquire ONLY the passive inputs for the ARPM episode-free audit.

Safety boundary:
- Downloads tokenizer metadata/files and one welfare-vector artifact only.
- Refuses model-weight-like filenames and any non-allowlisted remote path.
- Never imports transformers or loads a language model.
- Resolves the vector mirror's mutable `main` ref to the server-reported immutable
  commit BEFORE accepting the artifact into the audit inputs.

This helper is intentionally usable with Python's standard library only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import ssl
import sys
import tempfile
import urllib.error
import urllib.request
from pathlib import Path
from typing import Dict, Tuple

MODEL_REPO = "Qwen/Qwen3-4B-Instruct-2507"
MODEL_REVISION = "cdbee75f17c01a7cc42f958dc650907174af0554"
VECTOR_REPO = "Teachafy/speakable-welfare-axes-artifacts"
VECTOR_FILENAME = "vectors_step95_bal.pt"
EXPECTED_TOKENIZER_JSON_SHA256 = "aeb13307a71acd8fe81861d94ad54ab689df773318809eed3cbe794b4492dae4"
TOKENIZER_FILES = (
    "tokenizer.json",
    "tokenizer_config.json",
    "vocab.json",
    "merges.txt",
)
FORBIDDEN_SUFFIXES = {".safetensors", ".bin", ".ckpt", ".pth", ".onnx", ".gguf"}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def assert_passive_name(filename: str) -> None:
    p = Path(filename)
    low = p.name.lower()
    if p.suffix.lower() in FORBIDDEN_SUFFIXES or low.startswith("model-"):
        raise AssertionError(f"Refusing model-weight-like file: {filename}")
    allowed = set(TOKENIZER_FILES) | {VECTOR_FILENAME}
    if filename not in allowed:
        raise AssertionError(f"Remote path is not allowlisted: {filename}")


def hf_resolve(repo: str, revision: str, filename: str) -> str:
    assert_passive_name(filename)
    return f"https://huggingface.co/{repo}/resolve/{revision}/{filename}"


def request(url: str, method: str = "GET") -> urllib.request.Request:
    headers = {"User-Agent": "arpm-episode-free-audit/0.5"}
    token = os.environ.get("HF_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return urllib.request.Request(url, headers=headers, method=method)


def remote_metadata(url: str) -> Dict[str, str]:
    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, req, fp, code, msg, headers, newurl):
            return None

    opener = urllib.request.build_opener(NoRedirect)
    try:
        with opener.open(request(url, "GET"), timeout=45) as r:
            headers = r.headers
    except urllib.error.HTTPError as e:
        if e.code not in (301, 302, 303, 307, 308):
            raise
        headers = e.headers
    return {k.lower(): v for k, v in headers.items()}


def resolved_commit_for_main(repo: str, filename: str) -> Tuple[str, Dict[str, str]]:
    meta = remote_metadata(hf_resolve(repo, "main", filename))
    commit = meta.get("x-repo-commit")
    if not commit or len(commit) < 12:
        raise RuntimeError("Hub did not provide X-Repo-Commit; refusing mutable main freeze")
    return commit, meta


def download(url: str, dest: Path) -> Dict[str, str]:
    dest.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(request(url), timeout=120) as r:
        headers = {k.lower(): v for k, v in r.headers.items()}
        fd, tmp_name = tempfile.mkstemp(prefix=dest.name + ".", suffix=".partial", dir=str(dest.parent))
        try:
            with os.fdopen(fd, "wb") as f:
                shutil.copyfileobj(r, f, length=1024 * 1024)
            os.replace(tmp_name, dest)
        except Exception:
            try:
                os.unlink(tmp_name)
            except FileNotFoundError:
                pass
            raise
    return headers


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="passive_inputs")
    ap.add_argument("--metadata-only", action="store_true", help="Resolve immutable revisions but do not download bytes")
    args = ap.parse_args()

    out = Path(args.out)
    tok_dir = out / "tokenizer_only"
    vec_dir = out / "vector"
    out.mkdir(parents=True, exist_ok=True)

    vector_commit, vector_main_meta = resolved_commit_for_main(VECTOR_REPO, VECTOR_FILENAME)
    manifest = {
        "status": "PASSIVE_METADATA_RESOLVED" if args.metadata_only else "PASSIVE_BYTES_ACQUIRED_NOT_YET_AUDITED",
        "episode_count": 0,
        "model_weights_loaded": False,
        "model_repo": MODEL_REPO,
        "model_revision": MODEL_REVISION,
        "vector_repo": VECTOR_REPO,
        "vector_revision_resolved_from_main": vector_commit,
        "vector_main_response": {
            k: vector_main_meta.get(k)
            for k in ("x-repo-commit", "x-xet-hash", "etag", "x-linked-etag", "content-length")
            if vector_main_meta.get(k) is not None
        },
        "files": [],
    }

    if not args.metadata_only:
        for filename in TOKENIZER_FILES:
            dest = tok_dir / filename
            headers = download(hf_resolve(MODEL_REPO, MODEL_REVISION, filename), dest)
            row = {
                "role": "tokenizer",
                "filename": filename,
                "repo": MODEL_REPO,
                "revision": MODEL_REVISION,
                "size_bytes": dest.stat().st_size,
                "sha256": sha256(dest),
                "response_x_repo_commit": headers.get("x-repo-commit"),
                "response_x_xet_hash": headers.get("x-xet-hash"),
            }
            manifest["files"].append(row)
        tjson = tok_dir / "tokenizer.json"
        got = sha256(tjson)
        if got != EXPECTED_TOKENIZER_JSON_SHA256:
            raise AssertionError(f"tokenizer.json SHA256 mismatch: {got}")

        vec_dest = vec_dir / VECTOR_FILENAME
        headers = download(hf_resolve(VECTOR_REPO, vector_commit, VECTOR_FILENAME), vec_dest)
        manifest["files"].append({
            "role": "external_vector",
            "filename": VECTOR_FILENAME,
            "repo": VECTOR_REPO,
            "revision": vector_commit,
            "size_bytes": vec_dest.stat().st_size,
            "sha256": sha256(vec_dest),
            "response_x_repo_commit": headers.get("x-repo-commit"),
            "response_x_xet_hash": headers.get("x-xet-hash"),
        })

        for p in tok_dir.rglob("*"):
            if p.is_file() and (p.suffix.lower() in FORBIDDEN_SUFFIXES or p.name.lower().startswith("model-")):
                raise AssertionError(f"Forbidden file appeared in tokenizer-only snapshot: {p}")

    (out / "passive_acquisition_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(json.dumps({
        "status": manifest["status"],
        "vector_revision": vector_commit,
        "episode_count": 0,
        "model_weights_loaded": False,
    }, indent=2))


if __name__ == "__main__":
    main()
