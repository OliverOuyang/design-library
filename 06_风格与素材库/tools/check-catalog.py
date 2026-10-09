#!/usr/bin/env python3
"""校验 catalog.json：文件存在、哈希一致、许可证可识别、没有漏登记的媒体文件。
用法：python3 tools/check-catalog.py        （在 06_风格与素材库/ 下运行，或传入目录）
      python3 tools/check-catalog.py --fix-hash  （确认改动无误后，重算 sha256/bytes）
只用标准库，退出码非 0 表示有问题，可以直接放进 git pre-commit 或 CI。"""
import hashlib, json, os, sys

ROOT = next((a for a in sys.argv[1:] if not a.startswith('--')), os.path.join(os.path.dirname(__file__), '..'))
os.chdir(ROOT)
FIX = '--fix-hash' in sys.argv
MEDIA = {'.png', '.jpg', '.jpeg', '.webp', '.gif', '.svg', '.mp4', '.webm', '.mov', '.glb', '.gltf',
         '.ttf', '.otf', '.woff', '.woff2', '.wav', '.mp3', '.ogg', '.json', '.gz'}
SKIP = {'catalog.json', 'catalog.schema.json'}
REQ = ['path', 'kind', 'title', 'license', 'spdx', 'sha256', 'bytes', 'ai_used']
KNOWN_NON_TEXT = {'GPL-3.0-only', 'AGPL-3.0-only'}  # 只登记参考图，不随库分发许可全文
WARN_BYTES = 50 * 1024 * 1024  # GitHub 对 >50MB 的文件告警，>100MB 拒收

c = json.load(open('catalog.json', encoding='utf-8'))
errs, warns, seen = [], [], set()
licenses = {f[:-4] for f in os.listdir('LICENSES') if f.endswith('.txt')} if os.path.isdir('LICENSES') else set()
for e in c['entries']:
    for f in e.get('files', []):
        p = f.get('path', '?'); seen.add(p)
        for k in REQ:
            if k not in f: errs.append(f'{p}: 缺字段 {k}')
        if not os.path.isfile(p):
            errs.append(f'{p}: 文件不存在'); continue
        b = open(p, 'rb').read(); h = hashlib.sha256(b).hexdigest()
        if FIX: f['sha256'], f['bytes'] = h, len(b)
        elif f.get('sha256') != h: errs.append(f'{p}: sha256 不一致（文件被改过？确认后用 --fix-hash）')
        s = f.get('spdx', '')
        if not (s.startswith('LicenseRef-') or s in licenses or s in KNOWN_NON_TEXT):
            errs.append(f'{p}: spdx={s} 不在 LICENSES/ 里')
        if f.get('kind') == 'asset' and f.get('spdx', '').startswith('CC-BY') and not f.get('source_url') and not f.get('author'):
            errs.append(f'{p}: CC-BY 素材必须有作者或来源，才能署名')
        if len(b) > WARN_BYTES: warns.append(f'{p}: {len(b)//1048576}MB，超过 50MB，考虑 Git LFS 或外链')
for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in ('.git', 'LICENSES', 'node_modules')]
    for fn in files:
        p = os.path.relpath(os.path.join(root, fn), '.').replace(os.sep, '/')
        if p in SKIP or p == 'gallery.jpg' or p.startswith('tools/'): continue
        if os.path.splitext(fn)[1].lower() in MEDIA and p not in seen:
            errs.append(f'{p}: 媒体文件没有登记进 catalog.json')
if FIX:
    json.dump(c, open('catalog.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('已重算哈希')
for w in warns: print('警告', w)
for x in errs: print('错误', x)
print(f'检查 {len(seen)} 个文件：{len(errs)} 个错误，{len(warns)} 个警告')
sys.exit(1 if errs else 0)
