# 设计素材库 · 总索引

给游戏、独立站、AI 视频共用。**风格以真实作品为准**：每种风格都附上了业内公认的参考作品（链接到原作）和从公开来源原文抄来的提示词（附出处）；我自己用工具跑的图只放在 `tool-tests/`，仅用来证明工具能做到、方便复现。

使用前先读 [不要做原则](../04_规则与模板/不要做原则.md)，每个文件夹的 README 开头都标了对应的条款。

- 总览图：[gallery.jpg](gallery.jpg)
- 机器可读清单：[catalog.json](catalog.json)（v3：每个文件都有来源、作者、许可证、SPDX 标识、SHA-256、`ai_used`；结构见 [catalog.schema.json](catalog.schema.json)）
- 许可证全文：[LICENSES/](LICENSES/)（按 SPDX 标识命名）；需要署名的素材汇总在 [ATTRIBUTION.md](ATTRIBUTION.md)
- 脚本：[tools/](tools/README.md)，含像素图检查 `pixcheck.py` 和清单校验 `check-catalog.py`
- 调研与改进路线：[项目治理/11_素材库结构调研与改进.md](../项目治理/11_素材库结构调研与改进.md)

> 在本仓库中的定位：本目录是“风格参考 + 可复用素材”层，状态整体为 `candidate`。可直接放进项目的只有 `kind: asset` 且许可证允许的文件；`official/`、`refs/` 是参考，不是可再分发素材（见 [分类法、来源与版权合同](../项目治理/02_分类法来源与版权合同.md)）。

## 其他项目怎么用

| 场景 | 做法 |
|---|---|
| 只想查风格、抄提示词 | 直接打开 `styles/<风格>/README.md` |
| 某个项目要用几个素材 | 复制文件，同时把 `catalog.json` 里对应条目的作者、许可证抄进项目的致谢页；CC BY 的看 [ATTRIBUTION.md](ATTRIBUTION.md) |
| 多个项目长期共用 | 推到 GitHub 后，在项目里 `git subtree add --prefix design-lib <仓库地址> main --squash`（项目里看得到文件、不需要额外命令）；要严格锁版本再用 `git submodule` |
| 只拉这一个目录 | `git clone --filter=blob:none --sparse <仓库地址>` 然后 `git sparse-checkout set 06_风格与素材库` |
| 程序读取 | 读 `catalog.json`，按 `kind`、`spdx`、`ai_used` 过滤 |

改动文件后跑一次 `python3 tools/check-catalog.py`，它会检查哈希、许可证和漏登记的文件。

更新：2026-10-09（并入本地仓库：补 SPDX、哈希、许可证全文、署名清单、校验脚本）

## styles/ · 按视觉风格

| 文件夹 | 风格 | 参考作品 | 公开提示词 | sref | 本地参考图 |
|---|---|---|---|---|---|
| [01-ascii-pixel](styles/01-ascii-pixel/README.md) | ASCII 与像素 · ASCII & Pixels | 12 | 7 | 0 | 0 |
| [02-sketch-scribble](styles/02-sketch-scribble/README.md) | 手绘涂鸦 · Sketch & Scribble | 12 | 6 | 6 | 1 |
| [03-digital-impressionism](styles/03-digital-impressionism/README.md) | 数字印象派 · Digital Impressionism | 11 | 7 | 6 | 0 |
| [04-morphing-objects](styles/04-morphing-objects/README.md) | 形变物体 · Morphing Objects | 10 | 6 | 2 | 0 |
| [05-lomo-imagery](styles/05-lomo-imagery/README.md) | LOMO 胶片感 · Lomo Imagery | 12 | 6 | 0 | 0 |
| [06-generative-art](styles/06-generative-art/README.md) | 生成艺术 · Generative Art | 12 | 5 | 0 | 2 |
| [07-shades-of-off-white](styles/07-shades-of-off-white/README.md) | 米白层次 · Shades of Off-white | 10 | 4 | 0 | 0 |
| [08-dither-halftone](styles/08-dither-halftone/README.md) | 抖动与半调 · Dither & Halftone（补充） | 10 | 5 | 1 | 1 |
| [09-glitch-crt](styles/09-glitch-crt/README.md) | 故障与 CRT · Glitch & CRT（补充） | 10 | 6 | 0 | 1 |
| [10-grain-riso](styles/10-grain-riso/README.md) | Riso 印刷与颗粒 · Risograph & Grain（补充） | 11 | 7 | 2 | 0 |

## library/ · 按素材类型

| 文件夹 | 内容 | 官方展示图 | 可直接用的文件 |
|---|---|---|---|
| [01-web-motion](library/01-web-motion/README.md) | 网页动效（视频里推荐的 4 个） | 3 | 1 |
| [02-icons](library/02-icons/README.md) | 图标 | 2 | 7 |
| [03-emoji-stickers](library/03-emoji-stickers/README.md) | 3D / 动态 Emoji 贴纸 | 1 | 10 |
| [04-game-assets](library/04-game-assets/README.md) | 游戏素材（3D 角色 / 场景 / 游戏图标） | 11 | 6 |
| [05-fonts](library/05-fonts/README.md) | 字体（全部可商用） | 6 | 2 |
| [06-illustrations](library/06-illustrations/README.md) | 插画 | 0 | 0 |
| [07-video-kits](library/07-video-kits/README.md) | 视频素材包与配方 | 0 | 1 |

## 文件类型说明

- `official/`：各项目 GitHub 仓库里的官方展示图，代表素材本来的质量
- `refs/`：参考作品图，只收开源仓库里允许转载的；其他作品版权在原作者，README 里只放链接
- `tool-tests/`：本库用开源工具跑的测试，不是风格标杆

## 许可证要点

- 随便用：CC0（KayKit、Kenney、Poly Haven）、MIT / ISC
- 要署名：CC BY（game-icons 3.0、Noto 动态 emoji 4.0）
- 有限制：React Bits（不可转卖组件）、GSAP（不能做与 Webflow 竞争的建站工具）、p5.riso（反资本主义许可，公司商用受限）、Hydra（AGPL）、didder（GPL）、部分 LoRA（非商用，见各风格提示词备注）、**Animated Fluent Emojis（仅限个人使用）**
- 字体全是 OFL：可商用可嵌入，不能单独卖字体文件
- 参考作品只用于学习风格，不要直接拿原图做素材

## 状态说明

- **已实测**：下载并实际跑过
- **已核对**：看过仓库和许可证，没实际跑
- **未测**：网站从云端打不开，只给链接
