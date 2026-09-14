"""Artifact-only welfare-vector audit. NO model inference.

This intentionally does not download anything. Pass a locally acquired artifact after
its repository revision has been frozen. PyTorch >=2.1 recommended for weights_only=True.
"""
import argparse, hashlib, json
from pathlib import Path

EXPECTED = {
    "mold_block_input_layer": 24,
    "gold_block_input_layer": 21,
    "mold_norm_reference": 19.34,
    "gold_norm_reference": 12.10,
    "hidden_size": 2560,
    "n_layers": 36,
}

def sha256(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for chunk in iter(lambda:f.read(1024*1024), b""):
            h.update(chunk)
    return h.hexdigest()

def tensor_summary(x):
    return {"shape":list(x.shape),"dtype":str(x.dtype),"norm":float(x.float().norm().item())}

def walk(obj,prefix=""):
    out={}
    try:
        import torch
        Tensor=torch.Tensor
    except Exception:
        Tensor=()
    if isinstance(obj, Tensor):
        out[prefix or "<root>"]=tensor_summary(obj)
    elif isinstance(obj, dict):
        for k,v in obj.items(): out.update(walk(v, f"{prefix}.{k}" if prefix else str(k)))
    elif isinstance(obj,(list,tuple)):
        for i,v in enumerate(obj): out.update(walk(v, f"{prefix}[{i}]"))
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("artifact")
    ap.add_argument("--out", default="vector_audit.json")
    ap.add_argument("--expected-sha256", default=None)
    args=ap.parse_args()
    digest=sha256(args.artifact)
    if args.expected_sha256 and digest != args.expected_sha256:
        raise AssertionError("vector artifact SHA mismatch")
    import torch
    try:
        obj=torch.load(args.artifact,map_location="cpu",weights_only=True)
    except TypeError as e:
        raise RuntimeError("PyTorch build lacks weights_only=True; do not load untrusted pickle unsafely") from e
    report={"artifact":str(Path(args.artifact).resolve()),"sha256":digest,"expected":EXPECTED,"tensors":walk(obj)}
    Path(args.out).write_text(json.dumps(report,indent=2),encoding="utf-8")
    print(json.dumps(report,indent=2))

if __name__=="__main__": main()
