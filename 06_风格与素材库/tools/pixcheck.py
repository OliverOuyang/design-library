# 像素图检查（来自 04_规则与模板/不要做原则.md §5）
# 用法: python3 pixcheck.py 图片.png
import sys
from collections import Counter
from PIL import Image
im = Image.open(sys.argv[1]).convert("RGBA")
w, h = im.size
px = im.load()
n_colors = len(im.getcolors(maxcolors=w * h))
runs = Counter()
for y in range(0, h, max(1, h // 64)):
    n = 1
    for x in range(1, w):
        if px[x, y] == px[x - 1, y]:
            n += 1
        else:
            runs[n] += 1; n = 1
print(f"尺寸 {w}x{h}  颜色数 {n_colors}")
print("最常见的色块宽度(像素:次数):", runs.most_common(5))
