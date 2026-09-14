"""Byte-freeze the external naive Mold artifact for same-layer v0.8 use.

NO model inference. Artifact metadata layer 21 is recorded but the analysis comparison
is prospectively fixed at block-input layer 24 to match trained vMold[24].
"""
import argparse,hashlib,json,math
from pathlib import Path
import torch
EXPECTED_SHA256="68bff1428712def0330851057dba102112e3d48ffa23db7da85d84cde93aaa0e"
EXPECTED_SIZE=739541
EXPECTED_HIDDEN=2560
EXPECTED_LAYERS=36
EXPECTED_METADATA_MOLD_LAYER=21
ANALYSIS_LAYER=24
PUBLISHED_LAYER24_NORM=8.01
def sha256(path):
 h=hashlib.sha256()
 with open(path,"rb") as f:
  for chunk in iter(lambda:f.read(1024*1024),b""): h.update(chunk)
 return h.hexdigest()
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("artifact"); ap.add_argument("--repo",required=True); ap.add_argument("--revision",required=True); ap.add_argument("--out",default="naive_control_manifest.frozen.json"); args=ap.parse_args()
 p=Path(args.artifact); digest=sha256(p)
 if digest!=EXPECTED_SHA256 or p.stat().st_size!=EXPECTED_SIZE: raise AssertionError("naive artifact byte mismatch")
 obj=torch.load(p,map_location="cpu",weights_only=True)
 required={"v_mold","v_gold","layer_mold","layer_gold","per_class","balanced","note"}
 if set(obj)!=required: raise AssertionError(f"unexpected keys: {sorted(obj)}")
 if int(obj["layer_mold"])!=EXPECTED_METADATA_MOLD_LAYER: raise AssertionError("unexpected artifact-selected layer")
 mold=obj["v_mold"]; gold=obj["v_gold"]
 if list(mold.shape)!=[EXPECTED_LAYERS,EXPECTED_HIDDEN] or list(gold.shape)!=[EXPECTED_LAYERS,EXPECTED_HIDDEN]: raise AssertionError("shape mismatch")
 n=float(mold[ANALYSIS_LAYER].float().norm())
 if not math.isclose(n,PUBLISHED_LAYER24_NORM,rel_tol=0.01): raise AssertionError(f"layer24 norm {n} not close to published {PUBLISHED_LAYER24_NORM}")
 payload={"status":"BYTE_FROZEN_NAIVE_CONTROL_PASS","freeze_version":"v0.8",
  "artifact":{"filename":p.name,"size_bytes":p.stat().st_size,"sha256":digest,"repo":args.repo,"revision":args.revision,"safe_load":"weights_only=True"},
  "mapping":{"semantic_name":"u_mold","artifact_key":"v_mold","tensor_shape":list(mold.shape),"dtype":str(mold.dtype),
    "artifact_metadata_mold_layer":int(obj["layer_mold"]),"analysis_block_input_layer":ANALYSIS_LAYER,
    "analysis_layer_norm":n,"published_layer24_norm_reference":PUBLISHED_LAYER24_NORM},
  "metadata":{"layer_gold":int(obj["layer_gold"]),"per_class":int(obj["per_class"]),"balanced":bool(obj["balanced"]),"note":str(obj["note"])},
  "role":"secondary_same_layer_semantic_control_not_hard_gate","episode_count":0,"model_weights_loaded":False}
 Path(args.out).write_text(json.dumps(payload,indent=2),encoding="utf-8"); print(json.dumps(payload,indent=2))
if __name__=="__main__": main()
