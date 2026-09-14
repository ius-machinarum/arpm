"""Byte-level audit of a LOCAL tokenizer-only snapshot. NO model weights/inference."""
import argparse, hashlib, json
from pathlib import Path

PINNED_REVISION='cdbee75f17c01a7cc42f958dc650907174af0554'
EXPECTED_TOKENIZER_JSON_SHA256='aeb13307a71acd8fe81861d94ad54ab689df773318809eed3cbe794b4492dae4'
FORBIDDEN_WEIGHT_SUFFIXES={'.safetensors','.bin','.ckpt','.pth','.onnx'}

def sha256(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for chunk in iter(lambda:f.read(1024*1024),b''):
            h.update(chunk)
    return h.hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('tokenizer_dir')
    ap.add_argument('--revision',default=PINNED_REVISION)
    ap.add_argument('--out',default='tokenizer_snapshot_manifest.json')
    args=ap.parse_args()
    if args.revision != PINNED_REVISION:
        raise SystemExit('Refusing non-pinned tokenizer revision')
    root=Path(args.tokenizer_dir)
    if not root.is_dir(): raise FileNotFoundError(root)
    files=[]
    for p in sorted(x for x in root.rglob('*') if x.is_file()):
        if p.suffix.lower() in FORBIDDEN_WEIGHT_SUFFIXES or p.name.startswith('model-'):
            raise AssertionError(f'Model-weight-like file found in tokenizer-only snapshot: {p.name}')
        files.append({'path':str(p.relative_to(root)),'size_bytes':p.stat().st_size,'sha256':sha256(p)})
    tjson=root/'tokenizer.json'
    tcfg=root/'tokenizer_config.json'
    if not tjson.exists() or not tcfg.exists():
        raise AssertionError('tokenizer.json and tokenizer_config.json are both required')
    tj_sha=sha256(tjson)
    if tj_sha != EXPECTED_TOKENIZER_JSON_SHA256:
        raise AssertionError(f'tokenizer.json SHA mismatch: {tj_sha}')
    cfg=json.loads(tcfg.read_text(encoding='utf-8'))
    template=cfg.get('chat_template')
    if not isinstance(template,str) or not template:
        raise AssertionError('chat_template missing')
    if '<think>' in template or '</think>' in template or 'enable_thinking' in template:
        raise AssertionError('2507 tokenizer template unexpectedly contains thinking machinery')
    generation_marker = "<|im_start|>assistant" + "\\n"
    if generation_marker not in template or 'add_generation_prompt' not in template:
        raise AssertionError('expected assistant generation-prompt clause not found')
    payload={
      'status':'TOKENIZER_BYTES_PASS_NO_MODEL_WEIGHTS',
      'repo':'Qwen/Qwen3-4B-Instruct-2507',
      'revision':args.revision,
      'tokenizer_json_sha256':tj_sha,
      'tokenizer_json_expected_sha256':EXPECTED_TOKENIZER_JSON_SHA256,
      'tokenizer_config_sha256':sha256(tcfg),
      'tokenizer_class':cfg.get('tokenizer_class'),
      'model_max_length':cfg.get('model_max_length'),
      'chat_template_sha256':hashlib.sha256(template.encode('utf-8')).hexdigest(),
      'contains_thinking_template':False,
      'files':files,
    }
    Path(args.out).write_text(json.dumps(payload,indent=2),encoding='utf-8')
    print(json.dumps({k:payload[k] for k in payload if k!='files'},indent=2))

if __name__=='__main__': main()
