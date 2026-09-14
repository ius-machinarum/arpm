"""Episode-free geometry audit for trained vMold and same-layer naive uMold.

Constructs the preregistered training-specific residual v_perp_u at block-input layer 24.
No model weights or inference.
"""
import argparse,hashlib,json,math
from pathlib import Path
import torch
TRAINED_SHA="bd90129eaf5a7d92933ed6e536613eaeebf81486b62f68e11b5dc2d6d385e297"
NAIVE_SHA="68bff1428712def0330851057dba102112e3d48ffa23db7da85d84cde93aaa0e"
LAYER=24
def sha256(p):
 h=hashlib.sha256()
 with open(p,"rb") as f:
  for ch in iter(lambda:f.read(1024*1024),b""): h.update(ch)
 return h.hexdigest()
def cos(a,b):
 return float(torch.dot(a,b)/(a.norm()*b.norm()))
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--trained",required=True); ap.add_argument("--naive",required=True); ap.add_argument("--out",default="specificity_geometry.json"); args=ap.parse_args()
 if sha256(args.trained)!=TRAINED_SHA or sha256(args.naive)!=NAIVE_SHA: raise AssertionError("artifact hash mismatch")
 t=torch.load(args.trained,map_location="cpu",weights_only=True); n=torch.load(args.naive,map_location="cpu",weights_only=True)
 v=t["v_mold"][LAYER].double(); u=n["v_mold"][LAYER].double(); g=t["v_gold"][LAYER].double()
 vp=v-(torch.dot(v,u)/torch.dot(u,u))*u
 vals={"v_norm":float(v.norm()),"u_norm":float(u.norm()),"cos_v_u":cos(v,u),
       "v_perp_u_norm":float(vp.norm()),"v_perp_u_norm_ratio":float(vp.norm()/v.norm()),
       "cos_v_gold_same_layer":cos(v,g)}
 if not math.isclose(vals["u_norm"],8.01,rel_tol=0.01): raise AssertionError(vals)
 if not math.isclose(vals["cos_v_u"],0.675,abs_tol=0.015): raise AssertionError(vals)
 if not math.isclose(vals["v_perp_u_norm_ratio"],0.738,abs_tol=0.015): raise AssertionError(vals)
 raw=vp.float().contiguous().numpy().astype("<f4",copy=False).tobytes()
 payload={"status":"SPECIFICITY_GEOMETRY_PASS","freeze_version":"v0.8","layer":LAYER,
  "formula":"v_perp_u = v - dot(v,u)/dot(u,u) * u","analysis_normalization":"unit-normalise v_perp_u before projection",
  "geometry":vals,"v_perp_u_raw_f32_sha256":hashlib.sha256(raw).hexdigest(),
  "trained_sha256":TRAINED_SHA,"naive_sha256":NAIVE_SHA,"episode_count":0,"model_weights_loaded":False}
 Path(args.out).write_text(json.dumps(payload,indent=2),encoding="utf-8"); print(json.dumps(payload,indent=2))
if __name__=="__main__": main()
