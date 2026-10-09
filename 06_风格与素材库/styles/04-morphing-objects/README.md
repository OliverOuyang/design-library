# 形变物体 · Morphing Objects

物体之间连续无剪辑地变形转化——液态金属、软体团块、矢量形状插值与面孔融合，强调平滑过渡和一个贯穿始终的视觉锚点。

> 用之前先对照 [不要做原则](../../../04_规则与模板/不要做原则.md)：§2 物理逻辑、§8 AI 视频专项、§7 减少动效。

## 参考作品（10 个，点链接看原作）

| # | 作品 | 作者 / 出品 | 年份 | 类型 | 适合 | 为什么值得参考 |
|---|---|---|---|---|---|---|
| 1 | [Black or White（Michael Jackson）面孔融合段落](https://en.wikipedia.org/wiki/Black_or_White) | John Landis（导演）/ Pacific Data Images | 1991 | 视频 | 视频 | 史上最著名的面孔 morph 序列之一，由 Pacific Data Images 制作，定义了'连续换脸'的视觉语言。 |
| 2 | [Cry（Godley & Creme）音乐录像带](https://en.wikipedia.org/wiki/Cry_(Godley_%26_Creme_song)) | Godley & Creme | 1985 | 视频 | 视频 | 用溶解与擦除把一张张面孔连续融合，获MTV VMA提名，是前数字时代的模拟 morph 鼻祖。 |
| 3 | [T-1000 液态金属（终结者2）](https://en.wikipedia.org/wiki/T-1000) | Industrial Light & Magic / Stan Winston | 1991 | 视频 | 视频 | ILM的液态金属CG变形，至今仍是'液体铬/汞'变形的标杆参照。 |
| 4 | [Inside — The Huddle](https://en.wikipedia.org/wiki/Inside_(video_game)) | Playdead | 2016 | 游戏 | 游戏 | 终章可操控的肉团'Huddle'是游戏中软体变形角色的经典，获TGA最佳美术指导。 |
| 5 | [flubber](https://github.com/veltman/flubber) | Noah Veltman | 2017 | 开源演示 | 网站、游戏 | 2D形状之间平滑插值的JS库，支持任意SVG路径互相变形，网站动效可直接使用。（MIT） |
| 6 | [GSAP MorphSVGPlugin](https://gsap.com/docs/v3/Plugins/MorphSVGPlugin/) | GreenSock (GSAP) |  | 开源演示 | 网站 | 业界最常用的SVG路径变形插件，提供 shapeIndex、rotational 等控制，适合精细的网页图形变形。 |
| 7 | [Blobmixer](https://tympanus.net/codrops/?p=102907) | 14islands |  | 网站 | 网站 | 基于WebGL的3D软体'blob'生成玩具，可实时调节形变与材质，是网页液态变形的优秀交互范例。 |
| 8 | [Igloo Inc](https://www.awwwards.com/annual-awards-2024/site-of-the-year) | abeto | 2024 | 网站 | 网站 | Awwwards 2024年度网站，沉浸式3D与滚动叙事结合，可参考滚动驱动的形体/粒子转化。 |
| 9 | [Lusion](https://lusion.co/) | Lusion（英国Bristol） |  | 艺术家 | 网站、视频 | 以3D视觉叙事和沉浸式网站著称的获奖工作室，作品常含流体、软体与形体变形。 |
| 10 | [Andreas Wannerstedt — Oddly Satisfying 系列](https://www.andreaswannerstedt.se/) | Andreas Wannerstedt |  | 艺术家 | 视频、网站 | 瑞典3D动态设计师，'Oddly Satisfying' 系列循环动画是物体运动与形变节奏的高质量参考。 |

## 公开提示词（6 条，原文照抄，附出处）

标「节选」的只抄到了开头，全文看出处。用的时候把主体换成你的，风格约束部分保留。

**1. Midjourney v7** · [出处](https://sureprompts.com/prompt-libraries/midjourney-v7/897940eb-c55c-4b3f-b8f0-70c2f2fbf7a1)

```
Abstract sculpture of liquid chrome morphing into impossible organic form, mercury-like surface reflecting distorted environment in funhouse mirror effect, flowing between solid and liquid states simultaneously, studio black background with three-point lighting creating multiple highlight reflections, form suggesting both human figure and ocean wave without being either, photorealistic material rendering with surreal impossible physics, contemporary art gallery installation aesthetic --ar 1:1 --s 500 --chaos 40 --v 7 --no text
```

液态铬雕塑静帧，黑底三点布光强化反射；可作为AI视频首帧。

**2. Kling 2.5** · [出处](https://magichour.ai/templates/details/cmpve9o6300fcwy0zn4xygx58-metallic-flow-mutation)

```
Liquid chrome begins forming at the fingertips and slowly travels across the subject's body. The reflective metal flows like living mercury, coating every surface while maintaining realistic body movement. Sections of the body temporarily liquefy and reshape before hardening into polished metallic structures. The transformation concludes with the subject becoming a sleek biomechanical form. Cinematic realism, unchanged environment.
```

Magic Hour 模板'Metallic Flow Mutation'：从指尖起始、逐段液化再硬化，并锁定'unchanged environment'作为锚点。

**3. Morphic 视频生成** · [出处](https://morphic.com/resources/videos/morph-videos)

```
A rose morphing into a songbird, soft window light
```

最简 morph 结构：起点主体 + 终点主体 + 统一光线。

**4. Morphic 视频生成** · [出处](https://morphic.com/resources/videos/morph-videos)

```
Tight tabletop shot of a steaming coffee cup that slowly morphs into a blooming flower, the rim opening into petals and the steam curling into a stem, warm window light, shallow depth of field.
```

把杯沿对应花瓣、蒸汽对应花茎——用形状对应关系让变形可信。

**5. Morphic 视频生成** · [出处](https://morphic.com/resources/videos/morph-videos)

```
A single portrait holds dead center while the face morphs from childhood through old age, skin texture, hair color, and bone structure shifting in one unbroken take, soft even key light, slow push-in.
```

以画面中心为固定锚点的面孔老化 morph，致敬 Black or White 式换脸。

**6. Seedream** · [出处](https://picsart.com/blog/best-prompts-for-ai-video-generators/)

```
Abstract shapes transforming into birds and dissolving into mist. Soft, flowing animation.
```

抽象形状→鸟→雾的多段转化，适合网站 hero 背景循环。

## Midjourney 风格代码（--sref）

社区整理的代码，不同 Midjourney 版本效果会漂移，先小批量试。

| 代码 | 说明 | 出处 |
|---|---|---|
| `--sref 4573` | Fluid Chrome Elegance：流动铬金属质感（社区上传）。 | [链接](https://sref-midjourney.com/style/liquid) |
| `--sref 597333` | Molten Heartscape：熔融液态形体。 | [链接](https://sref-midjourney.com/style/liquid) |

## 这个风格的「不要做」

- 没有共同锚点（画面中心、地平线、视线、统一光线）时，变形会被读成硬切而不是平滑 morph。（[来源](https://morphic.com/resources/videos/morph-videos)）
- 起点和终点主体描述含糊会让变形失控；要明确写出从什么变成什么，以及变化的质感（融化、液化、旋转中重塑）。（[来源](https://morphic.com/resources/videos/morph-videos)）
- 网页SVG变形时，两条路径点位不对应会产生中途'打结'；用 shapeIndex 对齐起点，复杂形状拆成多条路径分别变形，必要时用 rotational 类型。（[来源](https://gsap.com/docs/v3/Plugins/MorphSVGPlugin/)）
- flubber 的 interpolate() 只取第一个外轮廓，带孔洞或复合路径的形状会被忽略；maxSegmentLength 越小越平滑但更耗性能。（[来源](https://github.com/veltman/flubber)）

## 做出这种风格的工具

| 工具 | 链接 | 许可证 | 用途 | 状态 |
|---|---|---|---|---|
| flubber | [veltman/flubber](https://github.com/veltman/flubber) | MIT | 任意 SVG 形状之间平滑插值 | 已实测 |
| GSAP MorphSVG | [greensock/GSAP](https://github.com/greensock/GSAP) | GSAP 免费许可 | SVG 路径变形（现已免费） | 已核对 |
| blobs | [g-harel/blobs](https://github.com/g-harel/blobs) | MIT | 随机有机 blob 及其动画 | 已核对 |
| three.js morph targets | [mrdoob/three.js](https://github.com/mrdoob/three.js) | MIT | 3D 网格变形 | 已核对 |
| React Bits：MetaBalls / Ferrofluid / LiquidChrome / Orb | [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits) | MIT + Commons Clause | 网页直接用的同风格组件 | 已核对 |

## 工具实测（tool-tests/）

这些是我用上面的开源工具在 CC0/公有领域测试图上跑出来的，只用来证明工具能做到这个效果、方便你复现参数，**不是风格标杆**，风格以上面的参考作品为准。

- [flubber-morph-frame.png](tool-tests/flubber-morph-frame.png)
- [flubber-morph.mp4](tool-tests/flubber-morph.mp4)
