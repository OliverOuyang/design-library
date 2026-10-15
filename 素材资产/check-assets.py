#!/usr/bin/env python3
"""校验 素材资产/assets-manifest.js：条目文件存在、哈希一致、许可证有原文、没有漏登记的素材。
用法：python3 素材资产/check-assets.py   （任意目录下运行均可）
只用标准库，退出码非 0 表示有问题，CI 会在每次 push / PR 时运行。"""
import hashlib, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
LICENSE_DIR = os.path.join('..', '06_风格与素材库', 'LICENSES')
SUPPORT = {'动效/motion.css'}  # 动效样本共用的样式表，不单独作为素材登记

src = open('assets-manifest.js', encoding='utf-8').read()
integrity = dict(re.findall(r'"([^"]+)":"([0-9a-f]{64})"', src))
# 音效条目由数组 map 生成，路径模板形如 音效/按压/${file}.wav，需要展开
paths, licenses = set(re.findall(r'path:"([^"$]+)"', src)), set(re.findall(r'license:"([^"]+)"', src))
for names, tmpl in re.findall(r'\.\.\.\[([^\]]+)\]\.map\(.*?path:`([^`]+)`', src):
    for n in re.findall(r'"([^"]+)"', names):
        paths.add(tmpl.replace('${file}', n))

errs = []
for p in sorted(paths - integrity.keys()):
    errs.append(f'{p}: 有条目但 INTEGRITY 里没有哈希')
for p in sorted(integrity.keys() - paths):
    errs.append(f'{p}: INTEGRITY 有哈希但 items 里没有条目')
for p, h in sorted(integrity.items()):
    if not os.path.isfile(p):
        errs.append(f'{p}: 文件不存在'); continue
    if hashlib.sha256(open(p, 'rb').read()).hexdigest() != h:
        errs.append(f'{p}: sha256 不一致（文件被改过？同步更新 assets-manifest.js 和 素材清单与许可.md）')
for s in sorted(licenses):
    if not os.path.isfile(os.path.join(LICENSE_DIR, s + '.txt')):
        errs.append(f'license={s} 在 06_风格与素材库/LICENSES/ 里没有原文')
for d in ('音效', '动效'):
    for root, _, files in os.walk(d):
        for fn in files:
            p = os.path.join(root, fn).replace(os.sep, '/')
            if fn.startswith('LICENSE') or p in SUPPORT: continue
            if p not in integrity:
                errs.append(f'{p}: 素材文件没有登记进 assets-manifest.js')
if not os.path.isfile('音效/LICENSE-Kenney-CC0-1.0.txt'):
    errs.append('音效/LICENSE-Kenney-CC0-1.0.txt: 上游许可证原文缺失')

for x in errs: print('错误', x)
print(f'检查 {len(integrity)} 个素材：{len(errs)} 个错误')
sys.exit(1 if errs else 0)
