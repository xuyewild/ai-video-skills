# ai-video-skills

[English](README.md) | 中文

让 AI 视频“像一部片”、让 AI 打斗“打得到人”的两个 skill。来自半年 AI 漫剧生产：图像模型出资产图，Seedance 2.5 出视频，几十集、几百条打斗镜头的返修记录。

| skill | 解决什么 |
|---|---|
| [visual-bible](skills/zh/visual-bible/SKILL.md) | 每条都好看、放一起不像一部片：用一份一到两屏的视觉圣经写死画风、色彩、光线、尺度，再给两段可直接粘贴的风格段（图像、视频各一段） |
| [action-physics-choreography](skills/zh/action-physics-choreography/SKILL.md) | 拳穿过身体、打完没人动、两人摆架势互相等：把“激烈交手”拆成起手 → 接触 → 结果的逐拍写法，写明受力方向、落点和镜头配合 |

两个 skill 可以单独用。每个都有中文版 `skills/zh/` 和英文版 `skills/en/`，内容一致，各自完整可装。

## 适合谁

- 用 AI 做漫剧、短剧、动画短片、MV，一个项目要生成几十上百条视频
- 画风、色调、人物比例总是一集一集漂
- 打斗、追逐、摔投这类动作戏反复生成都不对

只生成一两条视频用不上。

## 核心几句

- **风格写成看得见的做法。** 模型认的是“有没有描线、阴影几层、皮肤画到什么程度”，不是风格名。
- **参考图为主，文字为辅。** 先用风格段出一张样张，认可后所有资产图都照它出，风格一致了再进视频。
- **光要找得到来源。** 不论什么画风，亮侧朝光源、暗部是有纹理的深灰、夜里不处处亮。
- **动作先因后果。** 只给开头和结局，过程就由模型乱编。每拍写全起手、接触、结果。
- **打击感看受方。** 受方是画面主体、从接触那一下起幅、有位移和落点；强弱靠位移差，不靠形容词。

## 安装

**Claude Code**：把要用的 skill 文件夹复制到 `~/.claude/skills/`（全局）或项目里的 `.claude/skills/`。

```bash
git clone https://github.com/xuyewild/ai-video-skills
cp -r ai-video-skills/skills/zh/visual-bible ~/.claude/skills/
cp -r ai-video-skills/skills/zh/action-physics-choreography ~/.claude/skills/
```

**Claude 网页版或桌面版**：把 skill 文件夹打成 zip，在设置里上传为自定义 skill。

**其他 AI**：skill 就是 Markdown 加 Python 脚本，把 `SKILL.md` 和用到的参考文件交给它读即可。

## 适用模型

视频写法以 Seedance 2.5 为例（含与 2.0 的差异），资产图写法覆盖 GPT Image 和 Midjourney V8。方法本身与模型无关；换模型时，时长、参考图数量等硬限制以该模型官方文档为准。资料来源和查询日期写在各 skill 的 `references/sources.md`，模型更新很快，用之前请重新核对。

## 脚本

只用 Python 标准库，3.9 以上。中英文写法都认。

| 脚本 | 做什么 |
|---|---|
| `visual-bible/scripts/check_visual_bible.py` | 检查视觉圣经的字段和段落是否齐全、风格段是否干净（视频段无色值、资产图段无时段天气）、与资产表是否一致 |
| `action-physics-choreography/scripts/validate_action_text.py` | 检查动作块是否按起手 → 接触 → 结果写全、有没有受力方向、结果词是否堆砌、片段时长是否在范围内 |

```bash
python -m unittest discover -s tests -v
```

## 姊妹仓库

[multi-ai-skills](https://github.com/xuyewild/multi-ai-skills)：多个 AI 一起做长项目时的分工、交接和项目记忆。

## 贡献

欢迎 issue 和 PR，尤其是你在自己项目里用过之后的出片对比。改规则请说明用的是哪个模型、在什么场景出过什么问题。

## 许可证

[MIT](LICENSE)
