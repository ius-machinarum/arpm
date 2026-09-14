"""Byte-freeze the externally sourced naive Mold semantic-control artifact.

NO model inference. Uses torch.load(..., weights_only=True) and refuses unexpected
bytes, layer metadata, shapes or key mappings.
"""
import argparse
import hashlib
import json
from pathlib import Path
import torch

EXPECTED_SHA256 = "68bff1428712def0330851057dba102112e3d48ffa23db7da85d84cde93aaa0e"
EXPECTED_SIZE = 739541
EXPECTED_HIDDEN = 2560
EXPECTED_LAYERS = 36
EXPECTED_MOLD_LAYER = 21

def sha256(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""): h.update(chunk)
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("artifact")
    ap.add_argument("--repo",required=True)
    ap.add_argument("--revision",required=True)
    ap.add_argument("--out",default="naive_control_manifest.frozen.json")
    args=ap.parse_args()

    p=Path(args.artifact)
    digest=sha256(p)
    if digest != EXPECTED_SHA256:
        raise AssertionError(f"naive artifact SHA mismatch: {digest}")
    if p.stat().st_size != EXPECTED_SIZE:
        raise AssertionError(f"naive artifact size mismatch: {p.stat().st_size}")

    obj=torch.load(p,map_location="cpu",weights_only=True)
    required={"v_mold","v_gold","layer_mold","layer_gold","per_class","balanced","note"}
    if set(obj) != required:
        raise AssertionError(f"unexpected naive artifact keys: {sorted(obj)}")
    if obj["layer_mold"] != EXPECTED_MOLD_LAYER:
        raise AssertionError(f"unexpected naive Mold layer: {obj['layer_mold']}")
    mold=obj["v_mold"]
    gold=obj["v_gold"]
    if list(mold.shape) != [EXPECTED_LAYERS,EXPECTED_HIDDEN]:
        raise AssertionError(f"unexpected naive Mold shape: {list(mold.shape)}")
    if list(gold.shape) != [EXPECTED_LAYERS,EXPECTED_HIDDEN]:
        raise AssertionError(f"unexpected naive Gold shape: {list(gold.shape)}")

    payload={
      "status":"BYTE_FROZEN_NAIVE_CONTROL_PASS",
      "artifact":{
        "filename":p.name,"size_bytes":p.stat().st_size,"sha256":digest,
        "repo":args.repo,"revision":args.revision,
        "safe_load":"torch.load(..., map_location='cpu', weights_only=True)"
      },
      "mapping":{
        "semantic_name":"u_mold",
        "artifact_key":"v_mold",
        "block_input_layer":int(obj["layer_mold"]),
        "tensor_shape":list(mold.shape),
        "dtype":str(mold.dtype),
        "layer_norm":float(mold[obj["layer_mold"]].float().norm())
      },
      "metadata":{
        "layer_gold":int(obj["layer_gold"]),
        "per_class":int(obj["per_class"]),
        "balanced":bool(obj["balanced"]),
        "note":str(obj["note"])
      },
      "episode_count":0,
      "model_weights_loaded":False
    }
    Path(args.out).write_text(json.dumps(payload,indent=2),encoding="utf-8")
    print(json.dumps(payload,indent=2))

if __name__=="__main__":
    main()
