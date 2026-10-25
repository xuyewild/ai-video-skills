# ai-video-skills

[English](README.md) | 中文

我用 AI 做了半年漫剧，图像模型出资产图，Seedance 2.5 出视频，到现在几千条片子了。

返修最多的就两类。一类是画风对不上：单条看都挺好，剪到一起，这条冷那条暖，人物这集还是 3D，下集就往真人那边跑。另一类是打戏：拳头直接从身上穿过去，挨了打的人站着不动，两个人摆好架势在那互相等。

这两个 skill 就是从这些返修里整理出来的。

**visual-bible**（视觉圣经）：一到两屏的短文件，先把画风、色彩、光线、比例定死，再给你两段能直接贴进提示词的风格段，图像一段，视频一段。

**action-physics-choreography**（动作物理与编排）：把“两人激烈交手”这种一句话，拆成一拍一拍的起手、接触、结果，写清楚力往哪边去、人落在哪、镜头怎么跟。

两个能分开装。中文在 `skills/zh/`，英文在 `skills/en/`，内容一样。

## 啥时候用得上

做漫剧、短剧、动画短片、MV，一个项目要几十上百条视频的；画风、色调、人物比例老是一集一集漂的；打斗、追逐、摔投重生成多少次都不对的。只出一两条的话用不着。

## 返修里攒下的几条

- 别写风格名字，模型不认。写看得见的：有没有描线，阴影分几层，皮肤画多细。
- 先出一张样张，看着对了，所有资产图都照它出，风格稳了再去做视频。文字只是打辅助。
- 光要有来处。亮的那边冲着光源，暗部是带纹理的深灰，夜戏别哪儿都亮。
- 只写开头和结尾，中间模型就自己编。所以每一拍都要写全：怎么起手，碰到哪，结果怎样。
- 疼不疼看挨打的那个。镜头从碰上那一下开始，他得被打出去、落到某个地方。力气多大看他飞多远，别靠形容词。

## 安装

**Claude Code**：把要用的 skill 文件夹复制到 `~/.claude/skills/`（全局）或者项目里的 `.claude/skills/`。

```bash
git clone https://github.com/xuyewild/ai-video-skills
cp -r ai-video-skills/skills/zh/visual-bible ~/.claude/skills/
cp -r ai-video-skills/skills/zh/action-physics-choreography ~/.claude/skills/
```

**Claude 网页版或桌面版**：把 skill 文件夹打成 zip，在设置里上传成自定义 skill。

**其他 AI**：skill 就是几份 Markdown 加几个 Python 脚本，把 `SKILL.md` 和它提到的参考文件丢给它读就行。

## 适用模型

视频的写法拿 Seedance 2.5 举例（也写了和 2.0 的区别），资产图的写法覆盖 GPT Image 和 Midjourney V8。方法本身不挑模型；换了模型以后，时长、参考图数量这类硬限制按那个模型的官方文档来。资料来源和查的日期写在各 skill 的 `references/sources.md` 里。模型更新很快，用之前最好再核对一遍。

## 脚本

只用 Python 标准库，3.9 以上就能跑，中英文写法都认。

| 脚本 | 做什么 |
|---|---|
| `visual-bible/scripts/check_visual_bible.py` | 查视觉圣经的字段和段落齐不齐、风格段干不干净（视频段里不能有色值，资产图段里不能有时段和天气）、跟资产表对不对得上 |
| `action-physics-choreography/scripts/validate_action_text.py` | 查动作块有没有按起手 → 接触 → 结果写全、写没写受力方向、结果词是不是堆太多、片段时长在不在范围里 |

```bash
python -m unittest discover -s tests -v
```

## 姊妹仓库

[multi-ai-skills](https://github.com/xuyewild/multi-ai-skills)：多个 AI 一起做长项目时怎么分工、交接、记进度。

## 反馈

欢迎开 issue 和 PR，最想看到的是你拿自己项目做的前后对比。想改哪条规则，说一下用的什么模型、在什么场景下出了什么问题。

## 许可证

[MIT](LICENSE)
