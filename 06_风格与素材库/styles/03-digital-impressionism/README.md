# 数字印象派 · Digital Impressionism

用数字手段再现印象派式的可见笔触、破碎色块与光色变化，画面像会动的油画或水彩，重光影氛围而轻精确轮廓。

> 用之前先对照 [不要做原则](../../../04_规则与模板/不要做原则.md)：§1 AI 味严重、§2 物理逻辑、§3 风格不一致。

## 参考作品（11 个，点链接看原作）

| # | 作品 | 作者 / 出品 | 年份 | 类型 | 适合 | 为什么值得参考 |
|---|---|---|---|---|---|---|
| 1 | [Loving Vincent（至爱梵高）](https://en.wikipedia.org/wiki/Loving_Vincent) | Dorota Kobiela, Hugh Welchman | 2017 | 视频 | 视频 | 65000帧全部由125位画师手绘油画完成，获欧洲电影奖最佳动画、奥斯卡提名，是'会动的梵高笔触'的终极参照。 |
| 2 | [The Old Man and the Sea（老人与海）](https://en.wikipedia.org/wiki/The_Old_Man_and_the_Sea_(1999_film)) | Aleksandr Petrov | 1999 | 视频 | 视频 | 玻璃油彩动画，获奥斯卡最佳动画短片，展示了笔触在镜头运动中如何流动变形。 |
| 3 | [David Hockney: The Arrival of Spring, Normandy, 2020](https://www.royalacademy.org.uk/exhibition/david-hockney) | David Hockney / Royal Academy of Arts | 2020 | 作品 | 网站、游戏、视频 | 116幅在iPad上'绘制'后打印的作品，是真正意义上的数字印象派：明亮色块、简洁笔触、光线变化。 |
| 4 | [The Wild Robot（荒野机器人）](https://en.wikipedia.org/wiki/The_Wild_Robot_(film)) | Chris Sanders / DreamWorks Animation | 2024 | 视频 | 视频、游戏 | 导演称目标是'宫崎骏森林里的莫奈画'，让成片保持概念画的笔触感，是3D绘画化渲染的当代标杆。 |
| 5 | [Arcane（双城之战）](https://en.wikipedia.org/wiki/Arcane_(TV_series)) | Fortiche / Riot Games | 2021 | 视频 | 视频、游戏 | 2D/3D混合、每帧像手绘概念画，两获艾美奖最佳动画节目，可参考绘画质感贴图与光影。 |
| 6 | [GRIS](https://nomada.studio/gris) | Nomada Studio（Conrad Roset 联合创办） | 2018 | 游戏 | 游戏、网站 | 水彩感的柔和色块与渐变，配合色彩逐步回归的叙事，是绘画风独立游戏的代表。 |
| 7 | [Dordogne](https://en.wikipedia.org/wiki/Dordogne_(video_game)) | Un Je Ne Sais Quoi / Umanimation | 2023 | 游戏 | 游戏 | 整体画面像水彩画的叙事游戏，适合参考水彩印象风的场景与UI。 |
| 8 | [Eastshade](https://en.wikipedia.org/wiki/Eastshade) | Eastshade Studios | 2019 | 游戏 | 游戏 | 扮演画家在岛上作画的第一人称游戏，3D世界以温暖、绘画般的光色呈现，适合'画中世界'题材参考。 |
| 9 | [Ōkami（大神）](https://en.wikipedia.org/wiki/%C5%8Ckami) | Clover Studio / Capcom | 2006 | 游戏 | 游戏 | 受水墨与浮世绘启发的卡通渲染，'天之笔'让绘画本身成为玩法，是东方笔触数字化的经典。 |
| 10 | [On Crafting Painterly Shaders](https://blog.maximeheckel.com/posts/on-crafting-painterly-shaders/) | Maxime Heckel | 2024 | 开源演示 | 网站、游戏 | 从基础到各向异性 Kuwahara 滤镜的实时WebGL绘画化着色器教程，网站和游戏可直接借鉴实现。 |
| 11 | [Painterly Rendering with Curved Brush Strokes of Multiple Sizes](https://mrl.cs.nyu.edu/publications/painterly98/) | Aaron Hertzmann | 1998 | 开源演示 | 游戏、网站 | SIGGRAPH 98 经典论文：由粗到细多层曲线笔触重绘照片，是程序化印象派笔触的算法源头。 |

## 公开提示词（7 条，原文照抄，附出处）

标「节选」的只抄到了开头，全文看出处。用的时候把主体换成你的，风格约束部分保留。

**1. Gemini 2.5 Flash Image (Nano Banana)** · [出处](https://developers.googleblog.com/en/how-to-prompt-gemini-2-5-flash-image-generation-for-the-best-results/)

```
Transform the provided photograph of a modern city street at night into the artistic style of Vincent van Gogh's 'Starry Night'. Preserve the original composition of buildings and cars, but render all elements with swirling, impasto brushstrokes and a dramatic palette of deep blues and bright yellows.
```

Google官方风格迁移示例：保留构图、指定笔触类型（swirling, impasto）和调色板，适合把游戏截图/实拍转成印象派。

**2. Sora 2** · [出处](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide)

```
Style: Hand-painted 2D/3D hybrid animation with soft brush textures, warm tungsten lighting, and a tactile, stop-motion feel. The aesthetic evokes mid-2000s storybook animation — cozy, imperfect, full of mechanical charm. Subtle watercolor wash and painterly textures; warm–cool balance in grade; filmic motion blur for animated realism.
```

OpenAI Sora 2 官方提示指南中的 Style 段落，可作为AI视频'绘画感动画'的风格块整体复用。

**3. Morphic 图像生成** · [出处](https://morphic.com/resources/images/impressionism-images)

```
A wide riverside boating party at golden hour, women in summer dresses, men in straw boaters, broken reflections across the water, rowboats moored under willow.
```

雷诺阿式河畔聚会，'broken reflections' 强调破碎笔触倒影。

**4. Morphic 图像生成** · [出处](https://morphic.com/resources/images/impressionism-images)

```
A poppy field in afternoon wind, two figures with parasols moving down a path through scarlet flecks, breezy cobalt sky with high white cloud, soft painterly horizon.
```

莫奈《罂粟花田》式构图，'scarlet flecks' 指定点状色块。

**5. Morphic 图像生成** · [出处](https://morphic.com/resources/images/impressionism-images)

```
A green-painted Japanese-style garden bridge arcing over a pond of water lilies, willows reflected in broken daubs, soft mauve and rose-pink flowers, afternoon haze.
```

莫奈睡莲日本桥，'broken daubs' 是关键笔触词。

**6. Midjourney** · [出处](https://openart.ai/blog/post/midjourney-prompts-for-art-style)

```
Impressionist style landscape with soft, diffused light, capturing the essence of a serene countryside.
```

OpenArt 艺术风格提示词，较简短，可作为基础模板再补充笔触描述。

**7. Midjourney** · [出处](https://openart.ai/blog/post/midjourney-prompts-for-art-style)

```
Post-impressionist still life with vibrant colors, bold brushstrokes, and a focus on form.
```

后印象派静物，强调粗笔触与形体，适合道具/物件图。

## Midjourney 风格代码（--sref）

社区整理的代码，不同 Midjourney 版本效果会漂移，先小批量试。

| 代码 | 说明 | 出处 |
|---|---|---|
| `--sref 3342922409` | Soft Impressionist：柔焦、可见笔触，玫瑰/鼠尾草绿/大地色的油画感。 | [链接](https://moodboard.beehiiv.com/p/10-more-styles-to-steal) |
| `--sref 3176460494` | Psychedelic Swirl：高饱和、梵高式厚涂旋涡笔触。 | [链接](https://moodboard.beehiiv.com/p/10-more-styles-to-steal) |
| `--sref 151289788` | Poetic Impressionism（社区上传）。 | [链接](https://sref-midjourney.com/style/impressionism) |
| `--sref 1650724867` | Melancholic Impressionism：忧郁色调的印象派。 | [链接](https://sref-midjourney.com/style/impressionism) |
| `--sref 3397305952` | Dreamy Impressionism：梦幻柔和印象派。 | [链接](https://sref-midjourney.com/style/impressionism) |
| `--sref 772318403` | Classical Oil Painting：可见笔触、传统光影的厚重油画（偏古典，可与印象派sref混合）。 | [链接](https://moodboard.beehiiv.com/p/10-midjourney-style-codes-you-can-copy-paste) |

## 这个风格的「不要做」

- 不写明笔触技法（如 broken brushwork、visible short strokes）时，模型常给出平滑渐变，看起来像普通数字插画而不是印象派。（[来源](https://morphic.com/resources/images/impressionism-images)）
- 基础方形 Kuwahara 滤镜会产生'方块状'笔触，核尺寸过大时画面会严重失真；做实时绘画化着色器要用圆形/各向异性版本并控制核大小。（[来源](https://blog.maximeheckel.com/posts/on-crafting-painterly-shaders/)）
- AI视频里风格描述不要放在最后或只写一个词；要在提示开头就确立风格并用具体视觉词，否则后续镜头会漂回写实。（[来源](https://developers.openai.com/cookbook/examples/sora/sora2_prompting_guide)）
- 不要把'印象派'等同于'加个油画滤镜'：参考作品（Loving Vincent、荒野机器人）都是让笔触服务光线和氛围，而不是均匀铺满纹理。（[来源](https://en.wikipedia.org/wiki/The_Wild_Robot_(film))）

## 做出这种风格的工具

| 工具 | 链接 | 许可证 | 用途 | 状态 |
|---|---|---|---|---|
| primitive | [fogleman/primitive](https://github.com/fogleman/primitive) | MIT | 用几何图形逐步重建图片（可出过程帧） | 已实测 |
| Geometrize | [Tw1ddle/geometrize-haxe](https://github.com/Tw1ddle/geometrize-haxe) | 宽松许可（见仓库） | 同类工具，有网页版 | 已核对 |
| p5.brush | [acamposuribe/p5.brush](https://github.com/acamposuribe/p5.brush) | MIT | p5.js 真实笔刷/水彩 | 已核对（npm 安装失败，未渲染） |
| ImageMagick -paint | https://imagemagick.org | Apache-2.0 风格 | 一键油画滤镜 | 已实测 |

## 工具实测（tool-tests/）

这些是我用上面的开源工具在 CC0/公有领域测试图上跑出来的，只用来证明工具能做到这个效果、方便你复现参数，**不是风格标杆**，风格以上面的参考作品为准。

- [magick-oilpaint-coffee.png](tool-tests/magick-oilpaint-coffee.png)
- [primitive-buildup-rocket.mp4](tool-tests/primitive-buildup-rocket.mp4)
- [primitive-ellipses-chelsea.png](tool-tests/primitive-ellipses-chelsea.png)
- [primitive-triangles-coffee.png](tool-tests/primitive-triangles-coffee.png)
