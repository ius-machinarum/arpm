"""Safely enumerate a welfare-vector artifact without making semantic assignments.

NO model inference. This is deliberately descriptive: it reports hashes, object paths,
shapes, dtypes and norms, but does not guess which tensor is Gold or Mold.
"""
import argparse, hashlib, json
from pathlib import Path
import torch

def sha256(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for chunk in iter(lambda:f.read(1024*1024), b''):
            h.update(chunk)
    return h.hexdigest()

def walk(obj, path=''):
    rows=[]
    if isinstance(obj, torch.Tensor):
        rows.append({
            'path': path or '<root>',
            'shape': list(obj.shape),
            'dtype': str(obj.dtype),
            'numel': int(obj.numel()),
            'norm_f32': float(obj.float().norm().item()),
        })
    elif isinstance(obj, dict):
        for k,v in obj.items():
            p=f'{path}.{k}' if path else str(k)
            rows.extend(walk(v,p))
    elif isinstance(obj,(list,tuple)):
        for i,v in enumerate(obj):
            rows.extend(walk(v,f'{path}.{i}' if path else str(i)))
    return rows

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('artifact')
    ap.add_argument('--out',default='vector_structure_audit.json')
    args=ap.parse_args()
    p=Path(args.artifact)
    try:
        obj=torch.load(p,map_location='cpu',weights_only=True)
    except TypeError as e:
        raise RuntimeError('Refusing unsafe pickle load: PyTorch must support weights_only=True') from e
    payload={
        'status':'STRUCTURE_ONLY_NO_SEMANTIC_MAPPING',
        'filename':p.name,
        'size_bytes':p.stat().st_size,
        'sha256':sha256(p),
        'top_level_type':type(obj).__name__,
        'top_level_keys':list(obj.keys()) if isinstance(obj,dict) else None,
        'tensors':walk(obj),
    }
    Path(args.out).write_text(json.dumps(payload,indent=2),encoding='utf-8')
    print(json.dumps(payload,indent=2))

if __name__=='__main__': main()
