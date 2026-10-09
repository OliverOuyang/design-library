# ASCII 与像素 · ASCII & Pixels

以严格像素网格或等宽字符为最小单位、限定调色板、靠手工逐点排布来表达形体与光影的低分辨率风格。

> 用之前先对照 [不要做原则](../../../04_规则与模板/不要做原则.md)：§5 像素图是假像素、§1 AI 味严重。

## 参考作品（12 个，点链接看原作）

| # | 作品 | 作者 / 出品 | 年份 | 类型 | 适合 | 为什么值得参考 |
|---|---|---|---|---|---|---|
| 1 | [Celeste](https://www.celestegame.com/) | Maddy Makes Games（像素美术 Pedro "Saint11" Medeiros / Amora B.） | 2018 | 游戏 | 游戏、网站 | 现代独立游戏像素美术标杆：小角色+高可读性动画，配色克制，适合平台跳跃类参考。 |
| 2 | [Hyper Light Drifter](https://www.heartmachine.com/hyper-light-drifter) | Heart Machine | 2016 | 游戏 | 游戏、视频 | 高饱和限定色+大面积留白的像素氛围画面，示范像素风也能做出电影感构图。 |
| 3 | [Eastward](https://www.eastwardgame.com/) | Pixpil（Chucklefish 发行） | 2021 | 游戏 | 游戏、视频 | 极致细腻的手绘像素场景与光照，是“高密度像素场景”的上限参考。 |
| 4 | [Dwarf Fortress](http://www.bay12games.com/dwarves/) | Bay 12 Games（Tarn & Zach Adams） | 2006 | 游戏 | 游戏 | 最具代表性的 ASCII 文字图形游戏，Classic 模式完全用字符表达世界。（官方页说明 Premium 版可在图形与 Classic（ASCII）模式间切换） |
| 5 | [Caves of Qud](https://www.cavesofqud.com/) | Freehold Games | 2024 | 游戏 | 游戏、网站 | ASCII/字符瓦片 roguelike 的美学代表，展示字符画如何做出统一的色彩体系。 |
| 6 | [eBoy](https://www.eboy.com/) | eBoy（1997 年至今） | 1997 | 艺术家 | 网站、视频 | 等距像素城市插画的开山团队，适合做网站主视觉、海报类像素插画参考。 |
| 7 | [Paul Robertson（Pirate Baby's Cabana Battle Street Fight 2006 / Kings of Power 4 Billion% / Scott Pilgrim 游戏）](https://en.wikipedia.org/wiki/Paul_Robertson_(animator)) | Paul Robertson | 2006 | 艺术家 | 视频、游戏 | 像素动画大师，其像素短片是“像素风动画/MV”最常被引用的参考。 |
| 8 | [Pixel Art Tutorials（Saint11）](https://saint11.art/blog/pixel-art-tutorials/) | Pedro Medeiros |  | 艺术家 | 游戏 | Celeste 美术本人的系列像素教程，可直接当作团队的像素规范教材。（免费访问，© Pedro Medeiros，未声明开放许可） |
| 9 | [Lospec Palette List](https://lospec.com/palette-list) | Lospec 社区 |  | 网站 | 游戏、网站、视频 | 4000+ 套免费限定调色板（可按颜色数筛选），是锁定 4/8/16/32 色色板的首选来源。 |
| 10 | [Play — ASCII Art playground（play.core）](https://play.ertdfgcvb.xyz/) | Andreas Gysin（ertdfgcvb） |  | 开源演示 | 网站、视频 | 浏览器内实时 ASCII 动画的代表作，适合网站做 ASCII 动效/字符渲染。（源码 github.com/ertdfgcvb/play.core，Apache-2.0） |
| 11 | [three.js webgl_effects_ascii（AsciiEffect）](https://github.com/mrdoob/three.js/blob/dev/examples/webgl_effects_ascii.html) | three.js / mrdoob |  | 开源演示 | 网站 | 官方示例：把 3D 场景实时渲染成字符（字符集 ' .:-+*=%@#'），网站接入 ASCII 3D 的最短路径。（three.js 为 MIT 许可） |
| 12 | [Aseprite](https://www.aseprite.org/) | Igara Studio |  | 开源演示 | 游戏 | 业界标准像素绘制/动画工具，支持像素完美笔触、调色板编辑、抖动笔刷与精灵表导出。 |

## 公开提示词（7 条，原文照抄，附出处）

标「节选」的只抄到了开头，全文看出处。用的时候把主体换成你的，风格约束部分保留。

**1. Midjourney v4** · [出处](https://aituts.com/midjourney-pixel-art/)

```
clean pixel art, post apocalyptic city, style of metal slug 1996 --ar 3:2 --v 4
```

用具体游戏+年份锁定像素密度与美术流派，比泛泛的“pixel art”更可控。

**2. Midjourney v4** · [出处](https://aituts.com/midjourney-pixel-art/)

```
house in the trees, top down 2d game, pixel art, style of Legend of Zelda: A Link to the Past (SNES, Game Boy Color) 1991 --v 4
```

指定视角（top down）+平台（SNES）+年代，适合生成游戏地图概念。

**3. Midjourney v4** · [出处](https://aituts.com/midjourney-pixel-art/)

```
clean pixel art, greek temple with statue of apollo, style of castlevania 1986 --v 4
```

8-bit 时代参照，适合低色数场景。

**4. SDXL + Pixel Art XL LoRA（nerijs）** · [出处](https://huggingface.co/nerijs/pixel-art-xl)

```
pixel art, a cute corgi, simple, flat colors
```

官方用法：出图后用最近邻缩小 8 倍得到真像素；LCM 版负面词为 "3d render, realistic"。许可 creativeml-openrail-m。

**5. Retro Diffusion（RD Tile/Plus，经 Scenario）** · [出处](https://help.scenario.com/en/articles/retro-diffusion-models-the-essentials/)

```
top-down forest path with trees and rocks, classic JRPG map
```

专为真像素训练（≤256×256）；可传入调色板图限制颜色，RD Tile 经典 RPG 瓦片为 32×32。

**6. Retro Diffusion（RD Animation，经 Scenario）** · [出处](https://help.scenario.com/en/articles/retro-diffusion-models-the-essentials/)

```
small pirate character with parrot, walking animation, pixel art
```

行走动画风格固定 48×48，小精灵 32×32；尺寸要匹配游戏格子。

**7. FLUX.1-dev + ASCII Art v1 LoRA（martintomov）** · [出处](https://huggingface.co/martintomov/ascii-flux-v1)

```
ASCII art, a small boat on a calm lake, surrounded by trees
```

触发词 "ascii art"；许可为 flux-1-dev-non-commercial，商用需注意。网站正式使用建议改用 play.core/AsciiEffect 等真字符渲染。

## 这个风格的「不要做」

- 不要混用不同像素尺寸（mixels）：同一画面/同一图层内像素大小必须一致，背景层若放大须整层统一。（[来源](https://community.flowlab.io/t/mini-rant-stop-using-mixels/38287)）
- 不要非整数缩放：放大只用整数倍+最近邻，否则像素宽窄不一、模糊。（[来源](https://emulation.gametechwiki.com/index.php/Scaling)）
- 避免错误抗锯齿（过多导致发糊）、锯齿乱点（jaggies）、色带对齐（banding）和沿轮廓的枕形明暗（pillow shading）。（[来源](https://pixeljoint.com/forum/forum_posts.asp?TID=11299)）
- 颜色不要过多、不要用模糊/涂抹工具、不要存 JPG：高色数通常是“脏”像素的信号，应锁定限定色板。（[来源](https://pixeljoint.com/forum/forum_posts.asp?TID=11299)）
- AI 出图不要直接当像素用：须按原生分辨率生成并用最近邻缩回网格；超出原生尺寸放大会产生像素重复与颜色渗色（假像素）。（[来源](https://help.scenario.com/en/articles/retro-diffusion-models-the-essentials/)）

## 做出这种风格的工具

| 工具 | 链接 | 许可证 | 用途 | 状态 |
|---|---|---|---|---|
| ascii-image-converter | [TheZoraiz/ascii-image-converter](https://github.com/TheZoraiz/ascii-image-converter) | Apache-2.0 | 命令行图片转 ASCII（彩色/盲文） | 已核对 |
| Pixelorama | [Orama-Interactive/Pixelorama](https://github.com/Orama-Interactive/Pixelorama) | MIT | 免费像素画编辑器（动画/图层） | 已核对 |
| pixelit | [giventofly/pixelit](https://github.com/giventofly/pixelit) | MIT | 网页里把图片像素化 | 已核对 |
| 融合像素字体 | [TakWolf/fusion-pixel-font](https://github.com/TakWolf/fusion-pixel-font) | OFL | 中文像素字体 | 已实测 |
| Lospec 调色板库 | https://lospec.com/palette-list | — | 像素调色板合集 | 未测 |
| React Bits：ASCIIText / PixelBlast / LetterGlitch / PixelTrail | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | MIT + Commons Clause | 网页直接用的同风格组件 | 已核对 |

## 工具实测（tool-tests/）

这些是我用上面的开源工具在 CC0/公有领域测试图上跑出来的，只用来证明工具能做到这个效果、方便你复现参数，**不是风格标杆**，风格以上面的参考作品为准。

- [ascii-astronaut.txt](tool-tests/ascii-astronaut.txt)
- [ascii-chelsea.txt](tool-tests/ascii-chelsea.txt)
- [ascii-color-astronaut.png](tool-tests/ascii-color-astronaut.png)
- [ascii-color-chelsea.png](tool-tests/ascii-color-chelsea.png)
- [ascii-green-astronaut.png](tool-tests/ascii-green-astronaut.png)
- [ascii-green-chelsea.png](tool-tests/ascii-green-chelsea.png)
- [pixel-pico8-astronaut.png](tool-tests/pixel-pico8-astronaut.png)
- [pixel-pico8-chelsea.png](tool-tests/pixel-pico8-chelsea.png)
