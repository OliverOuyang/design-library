# 生成示例用的脚本

这些是生成 `styles/` 示例图和视频的原始脚本，换成你自己的图片就能复用。

- `style-fx.py`：像素化、抖动/半调、LOMO、Riso、故障静帧（Python + Pillow + numpy）
- `style-fx-ascii.py` / `style-fx-riso.py`：ASCII 彩色/终端绿版本、Riso 双色网点
- `glitch-video.py`：逐帧故障视频，输出 raw 帧，管道给 ffmpeg：`python3 glitch-video.py <dir> | ffmpeg -f rawvideo -pix_fmt rgb24 -s 720x720 -r 24 -i - out.mp4`
- `sketch.html`（rough.js）、`morph.html`（flubber）、`pixel.html`（像素 UI）、`fonts.html`（字体样张）：浏览器打开，需要先 `npm i roughjs flubber p5 @fontsource/...`

脚本里的路径参数是我生成时的目录结构（`<dir>/sty/src/*.png` 为输入、`<dir>/out/` 为输出），用前改一下。

## 新增

- `pixcheck.py`：像素图检查（来自不要做原则 §5）。`python3 pixcheck.py 图.png` 输出颜色数和最常见的色块宽度；真像素图颜色少、色块宽度是固定倍数。本库的像素游戏 UI 截图就是用它查出颜色数 61、有 1px 色块（字体抗锯齿），已删掉。
- `make-gallery.py`：重新生成 `gallery.jpg`（读 catalog.json，优先用官方图/参考图）。

- `check-catalog.py`：校验 `catalog.json`（文件存在、SHA-256 一致、SPDX 许可证在 `LICENSES/` 里、媒体文件都已登记、单文件超过 50MB 告警）。只用标准库：`python3 tools/check-catalog.py`；确认改动无误后用 `--fix-hash` 重算哈希。
