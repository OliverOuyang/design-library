# 视频素材包与配方

把上面的素材直接合成短视频的配方：Fluent 3D Emoji + 得意黑 + 霞鹜文楷，ffmpeg 一条命令出竖屏片段。

## 适合用在

抖音/小红书竖屏、AI 视频的片头片尾和字幕条。

## 工具 / 资源

| 工具 | 链接 | 许可证 | 用途 | 状态 |
|---|---|---|---|---|
| ffmpeg | https://ffmpeg.org | LGPL/GPL | 合成、加字、转码 | 已实测 |
| Playwright 录屏 | [microsoft/playwright](https://github.com/microsoft/playwright) | Apache-2.0 | 把网页动效录成视频素材 | 已实测 |

## 怎么复现示例

示例命令见 `make-vertical.sh`（把 3 张 PNG 叠在纯色背景上上下浮动，加标题和副标题）。

## 按「不要做原则」使用

对应 [不要做原则](../../../04_规则与模板/不要做原则.md)。

- 短镜头、一个镜头一个动作；字幕和 logo 后期加。（§8）
- 成片 0.25 倍速完整看一遍再发。（§0 第 4 条）

## 可直接用的素材文件

- [make-vertical.sh](make-vertical.sh)

## 工具实测（tool-tests/）

我测试时做的拼图、录屏和截图，证明素材能用、方便复现，不代表素材本身的最好效果。

- [all-assets-contact-sheet.png](tool-tests/all-assets-contact-sheet.png)
- [contact-sheet-source.html](tool-tests/contact-sheet-source.html)
- [vertical-emoji-title.mp4](tool-tests/vertical-emoji-title.mp4)
