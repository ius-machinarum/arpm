"""Create a byte-level vector freeze manifest. NO model inference.

The artifact key mapping must be supplied explicitly. This script refuses to infer
which tensor is Gold or Mold from convenient norms after seeing the object.
"""
import argparse, hashlib, json, math
from pathlib import Path
import torch

REF_MOLD=19.34
REF_GOLD=12.10
HIDDEN=2560

def sha256(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""):
            h.update(chunk)
    return h.hexdigest()

def get_path(obj,path):
    cur=obj
    for part in path.split('.'):
        if part.isdigit(): cur=cur[int(part)]
        else: cur=cur[part]
    return cur

def summary(x):
    return {"shape":list(x.shape),"dtype":str(x.dtype),"norm":float(x.float().norm())}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("artifact")
    ap.add_argument("--repo",required=True)
    ap.add_argument("--revision",required=True)
    ap.add_argument("--mold-key",required=True,help="Explicit dot path to the Mold tensor/array at block-input layer 24, or to a layer stack used with --mold-index")
    ap.add_argument("--gold-key",required=True)
    ap.add_argument("--mold-index",type=int,default=None)
    ap.add_argument("--gold-index",type=int,default=None)
    ap.add_argument("--norm-rtol",type=float,default=0.03)
    ap.add_argument("--out",default="artifact_manifest.frozen.json")
    args=ap.parse_args()
    p=Path(args.artifact)
    digest=sha256(p)
    obj=torch.load(p,map_location="cpu",weights_only=True)
    mold=get_path(obj,args.mold_key); gold=get_path(obj,args.gold_key)
    if args.mold_index is not None: mold=mold[args.mold_index]
    if args.gold_index is not None: gold=gold[args.gold_index]
    if not isinstance(mold,torch.Tensor) or not isinstance(gold,torch.Tensor):
        raise TypeError("explicit key mapping did not resolve to tensors")
    if mold.numel()!=HIDDEN or gold.numel()!=HIDDEN:
        raise AssertionError(f"direction dimension mismatch: mold={mold.shape}, gold={gold.shape}, expected {HIDDEN}")
    mn=float(mold.float().norm()); gn=float(gold.float().norm())
    if not math.isclose(mn,REF_MOLD,rel_tol=args.norm_rtol):
        raise AssertionError(f"Mold norm {mn} does not reconcile with {REF_MOLD}")
    if not math.isclose(gn,REF_GOLD,rel_tol=args.norm_rtol):
        raise AssertionError(f"Gold norm {gn} does not reconcile with {REF_GOLD}")
    payload={
      "status":"BYTE_FROZEN_VECTOR_PASS",
      "artifact":{"filename":p.name,"size_bytes":p.stat().st_size,"sha256":digest,"repo":args.repo,"revision":args.revision},
      "mapping":{"mold_key":args.mold_key,"mold_index":args.mold_index,"block_input_layer":24,
                 "gold_key":args.gold_key,"gold_index":args.gold_index,"gold_block_input_layer":21},
      "mold":summary(mold),"gold":summary(gold),
      "norm_reference":{"mold":REF_MOLD,"gold":REF_GOLD,"rtol":args.norm_rtol},
      "safe_load":"weights_only=True",
    }
    Path(args.out).write_text(json.dumps(payload,indent=2),encoding="utf-8")
    print(json.dumps(payload,indent=2))

if __name__=="__main__": main()
