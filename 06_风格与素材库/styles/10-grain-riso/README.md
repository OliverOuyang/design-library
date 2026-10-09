# Riso 印刷与颗粒 · Risograph & Grain（补充）

Risograph 孔版印刷与胶片/纸张颗粒：有限的专色油墨叠印、半调网点、轻微错版和未涂布纸纹理，带来温暖、手工、略带瑕疵的印刷质感。

> 用之前先对照 [不要做原则](../../../04_规则与模板/不要做原则.md)：§3 风格不一致（全项目统一颗粒/专色）。

## 参考作品（11 个，点链接看原作）

| # | 作品 | 作者 / 出品 | 年份 | 类型 | 适合 | 为什么值得参考 |
|---|---|---|---|---|---|---|
| 1 | [Hato Press](https://en.wikipedia.org/wiki/Hato_Press) | Jackson Lam & Ken Kirton | 2009- | 艺术家 | 网站、游戏 | 伦敦代表性 Riso 印刷与出版工作室，长期出版艺术家 zine 并开设 Riso 工作坊，是 riso 出版物视觉的标杆来源。（Wikipedia（CC BY-SA）） |
| 2 | [RISOTTO Studio](https://risottostudio.com/) | Gabriella Marcella（格拉斯哥） | 2012- | 艺术家 | 网站、游戏 | 英国运营最久的 Riso 专业工作室之一，大胆的图形系统与图案，并提供教程、免费模板和印刷档案。（官网） |
| 3 | [The Rise of Riso](https://www.commarts.com/columns/the-rise-of-riso) | Garrick Webster / Communication Arts | 2018 | 网站 | 网站、游戏、视频 | 系统梳理 riso 美学：单色逐次过版、专色叠印、陷印对位、80% 饱和度上限、未涂布纸纹理，并列出全球代表工作室与艺术家。（Communication Arts 文章） |
| 4 | [Spider-Man: Into the Spider-Verse（半调网点与印刷错位）](https://kottke.org/19/03/how-animators-created-the-spider-verse) | Sony Pictures Animation | 2018 | 视频 | 视频、游戏 | 用半调网点和胶印错版伪影代替景深与动态模糊，是把印刷质感做进动画的最强参考（页内附主创讲解视频）。（Kottke 文章；影片版权归 Sony） |
| 5 | [Risograph animation](https://magdalenekennedy.substack.com/p/risograph-animation) | Magdalene Kennedy | 2025 | 视频 | 视频 | 先数字动画，再逐帧用 Federal Blue、Bubblegum Pink、Yellow 等油墨 riso 印出、扫描回视频，真实的套色错位就是动画质感来源。（作者 Substack，版权归作者） |
| 6 | [Pentiment（美术总监 Hannah Kennedy 深度解析）](https://www.gamedeveloper.com/art/deep-dive-the-art-of-pentiment) | Obsidian Entertainment | 2022 | 游戏 | 游戏 | 以欧洲木刻版画和手抄本为参考的叙事游戏，展示“版画/印刷”语言如何转译为游戏角色与场景。（Game Developer 文章） |
| 7 | [p5.riso](https://github.com/antiboredom/p5.riso) | Sam Lavigne & Tega Brain |  | 开源演示 | 网站、游戏 | p5.js 的 Risograph 分色库：在代码里按油墨分层、做半调和叠印，可导出真实印刷用分色，也可直接用于网页生成艺术。（Anti-Capitalist License（非标准开源许可，限制营利性公司使用）） |
| 8 | [riso-colors](https://github.com/mattdesl/riso-colors) | Matt DesLauriers |  | 开源演示 | 网站、游戏、视频 | RISO 官方油墨的名称/HEX/Pantone 数据集（来源 stencil.wiki），可直接作为游戏或网站的 riso 色板 token。（MIT License） |
| 9 | [Spectrolite（Mac 分色软件）](https://blogs.denison.edu/riso/2024/10/25/working-with-spectrolite/) | spectrolite.app |  | 开源演示 | 网站、视频 | 免费 Mac 应用，把图像按油墨拆成灰度分色，带半调、色调分离和油墨预览，适合快速验证 riso 配色。（Denison 大学 Riso 实验室教程） |
| 10 | [Grainy Gradients](https://css-tricks.com/grainy-gradients/) | Jimmy Chion / CSS-Tricks | 2021 | 网站 | 网站 | 用 SVG feTurbulence 噪声 + CSS 渐变与滤镜做出带颗粒的渐变，是网页实现 riso/胶片颗粒最常被引用的教程。（CSS-Tricks 文章） |
| 11 | [grained.js](https://github.com/sarathsaleem/grained) | sarathsaleem |  | 开源演示 | 网站 | 零依赖的网页动态颗粒库，用 CSS 关键帧+生成的噪点 PNG 给任意元素加会动的胶片颗粒。（MIT License） |

## 公开提示词（7 条，原文照抄，附出处）

标「节选」的只抄到了开头，全文看出处。用的时候把主体换成你的，风格约束部分保留。

**1. Midjourney v6.1** · [出处](https://midlibrary.io/styles/risograph)

```
Risograph --v 6.1
```

Midlibrary 词条：层叠高饱和色、半调网点和渐变，主色为荧光粉、电光蓝和黄；建议再加具体油墨名和纸张描述。

**2. Krea-2-Turbo + cyan-pink-risograph LoRA** · [出处](https://huggingface.co/ilkerzgi/krea-2-cyan-pink-risograph-lora)

```
a lighthouse on a rocky cliff. cyan pink risograph style
```

触发词 “cyan pink risograph style”，双色（青+粉）限制色板；Krea 2 Community License。

**3. FLUX.1-dev + shouldis/risograph LoRA** · [出处](https://huggingface.co/shouldis/risograph)

```
A risograph print style poster of a photograph of purple mountains with blue and pink circles floating, grainy gradients in the style of RISOG
```

触发词 RISOG；“grainy gradients”是 riso 渐变颗粒的关键描述。页面未注明许可证。

**4. Midjourney** · [出处](https://www.awesomic.com/blog/the-best-midjourney-prompts-for-print-design-guide)

```
[theme], bold central composition, negative space for typography, neon palette, halftone texture --ar 24:36 --s 250 --q 2
```

Awesomic 印刷设计指南的海报/演出海报模板：中心构图+给字留白+半调纹理，适合 riso 风格海报。

**5. Imagen（Vertex AI）** · [出处](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/image/img-gen-prompt-guide)

```
A woman, 35mm portrait, blue and grey duotones
```

Google Imagen 官方提示指南示例：用 duotone 限定双色，是 riso 双色印刷感最简的官方写法。

**6. Midjourney v5.1** · [出处](https://www.awesomic.com/blog/the-best-midjourney-prompts-for-print-design-guide)

```
moody portrait, cinematic lighting, shallow depth of field, teal & orange grade, film grain --ar 8:10 --v 5.1 --q 2
```

Awesomic 的编辑封面模板，含 film grain；用于胶片颗粒向而非 riso 向。

**7. GPT Image 2.5** · [出处](https://youmind.com/ar/prompts/risograph-poster-style-transfer-34544)

```
Create a standalone 3:4 vertical contemporary risograph-style art poster based on the original photograph.
```

节选：照片转 riso 海报提示词的首句原文（全文更长，见来源；原作者 X @saniaspeaks_）。

## Midjourney 风格代码（--sref）

社区整理的代码，不同 Midjourney 版本效果会漂移，先小批量试。

| 代码 | 说明 | 出处 |
|---|---|---|
| `--sref --sref 7462501467` | “Playful Misregistered Risograph”：明亮有限色块略微溢出粗糙手绘线，riso + 素朴艺术 + 涂鸦，颗粒纹理与错版感（另见 underwoodxie Substack 介绍）。 | [链接](https://promptsref.com/srefcodedetail/--sref%207462501467) |
| `--sref --sref 261695377` | 纪实写实+魔幻现实的电影感摄影，细腻 35mm/中画幅胶片颗粒、低饱和复古调色；用于胶片颗粒向。 | [链接](https://underwoodxie.substack.com/p/3-photography-style-sref-codes-we) |

## 已发布色板

- **RISO 标准油墨（riso-colors / stencil.wiki 数据，MIT）**（[出处](https://raw.githubusercontent.com/mattdesl/riso-colors/master/riso-colors.json)）：`#000000` `#ff48b0` `#ffe800` `#0078bf` `#f15060` `#ff665e` `#00838a` `#3d5588` `#3255a4` `#ff6c2f` `#00a95c` `#5ec8e5` `#ffb511` `#765ba7` `#82d8d5` `#88898a`

## 这个风格的「不要做」

- 不要用 CMYK 全彩思路做 riso：每种油墨一张灰度分色（黑=100% 墨量，白=0%），只用计划印刷的专色。（[来源](https://typeshop.risd.gd/preparing-files)）
- 不要大面积 100% 满版：实际印刷建议饱和度不超过约 80%，否则容易蹭脏；数字模拟时也应保留油墨不均和透纸感。（[来源](https://www.commarts.com/columns/the-rise-of-riso)）
- 不要追求像素级完美对位：riso 每色单独过版，色块需留陷印并会轻微错位；完全对齐的矢量叠色看起来就是数字插画。（[来源](https://www.commarts.com/columns/the-rise-of-riso)）
- 不要只靠一层均匀噪点冒充纸感：riso 的质感来自未涂布纸纹理、网点/抖动和墨色不匀，应分层叠加。（[来源](https://www.commarts.com/columns/the-rise-of-riso)）
- 网页颗粒效果不要只在一个浏览器验收：mix-blend-mode 在 Chromium 和 WebKit 中渲染有差异，需跨浏览器检查。（[来源](https://css-tricks.com/grainy-gradients/)）

## 做出这种风格的工具

| 工具 | 链接 | 许可证 | 用途 | 状态 |
|---|---|---|---|---|
| grained.js | [sarathsaleem/grained](https://github.com/sarathsaleem/grained) | MIT | 网页动态颗粒 | 已核对 |
| p5.riso | [antiboredom/p5.riso](https://github.com/antiboredom/p5.riso) | Anti-Capitalist License（公司商用受限） | p5 做 Riso 分色 | 已核对，商用慎用 |
| 本库纸张颗粒贴图 | paper-grain-tile.png | 自制 | 可平铺背景 | 已实测 |

## 工具实测（tool-tests/）

这些是我用上面的开源工具在 CC0/公有领域测试图上跑出来的，只用来证明工具能做到这个效果、方便你复现参数，**不是风格标杆**，风格以上面的参考作品为准。

- [paper-grain-tile.png](tool-tests/paper-grain-tile.png)
- [riso-pink-blue.png](tool-tests/riso-pink-blue.png)
