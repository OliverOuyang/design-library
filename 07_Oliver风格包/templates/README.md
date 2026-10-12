# 封面和图集模板

两个 HTML 模板，文字、截图、圈哪里都写在网址参数里，用 `render.js` 一条命令出 PNG。风格来自上级的 `tokens.css`。

| 文件 | 出什么 | 尺寸 |
|---|---|---|
| `cover.html` | 套餐 / 商品封面：大标题 + 荧光笔词 + 真实截图 + 手绘圈和手写批注，可选右下角头像 | Fiverr 1280×769 · Upwork 1000×750 · 闲鱼 800×800（方图自动改成上下排） |
| `gallery.html?v=ba` | 图集：以前 / 现在对比 | 1280×769 |
| `gallery.html?v=get` | 图集：你会拿到什么（手写对勾清单 + 3 张缩略图，可标一张为视频） | 1280×769 |
| `render.js` | 把模板渲染成 PNG（需要 Playwright） | |
| `placeholder-shot.svg` | 占位截图，**只用来看排版，上架前必须换成真实截图** | |
| `examples/` | 上面各种用法的效果图 | |

## 用法

```bash
cd templates
node render.js "cover.html?w=1280&h=769&title=Your sales report, sent [every Monday]&sub=Google Sheets + Apps Script&tag=Sample · fictional shop&shot=my-dashboard.png&circle=0.52,0.12,0.22,0.22&note=compared with last week" out.png
node render.js "cover.html?w=800&h=800&lang=zh&title=每周一[自动]发销售周报&sub=表格自动化&shot=my-dashboard.png&note=和上周自动对比" xianyu.png
node render.js "gallery.html?v=get&items=Your working sheet::In your own Google account|A video walkthrough::Every package&thumbs=guide.png,email.png,video.jpg&play=3&note=the video comes with every order" get.png
```

- 标题里用 `[方括号]` 包住要涂荧光笔的那个词，每张图只涂一个。
- `circle=x,y,宽,高` 按截图的比例（0–1）填，圈住截图里最关键的一个数字或按钮；`note` 写 2–6 个词，会放在圈的上方。
- `lang=zh` 换中文字体：标题正文用思源黑体，手写用平方江南体（本机装了或加 `font=private` 时）或马善政。
- `avatar=头像.jpg` 只在 Fiverr 封面上用。
- 截图要用真实结果；样品要带 `tag=Sample · fictional shop`（中文 `示例 · 虚构店铺`）。

## 不要
- 不放工具 logo 墙、徽章、星级、“#1”“guaranteed”、联系方式。
- 不用 AI 画的截图、人像或“手写字”冒充真的。
