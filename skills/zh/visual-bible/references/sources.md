# 资料来源

读取日期均为 2026-10-09。火山引擎文档页直接打开只有 JavaScript 外壳，正文要经官方文档接口读取，日期取接口返回的首发/更新时间。模型和平台更新很快，用之前请重新核对。

| 号 | 来源 | 日期 | 版本 | 采纳了什么 |
|---|---|---|---|---|
| S1 | [Doubao Seedance 2.5 提示词指南（火山方舟）](https://docs.volcengine.com/docs/82379/2607689) | 首发 2026-08-07，更新 2026-10-09 | Seedance 2.5（含与 2.0 差异） | 一句话概述含“题材/风格”、结尾补充贯穿始终的氛围；“参考图片 1 的光影和滤镜”“色温、光影、亮度参考图片”写法；“顶级3D国漫仙侠”例子；参考用法与 2.0 一致；2.5 与 2.0 美学差异大、混用不连贯、用 2.0 视频做延长并选 MOV 保留风格；2.0 宽高比固定 6 档、不响应时间戳 |
| S2 | 火山方舟官方提示词优化 Skill `sd25-pe` | 2026-10-09 取得 | sd25-pe 0.1.1 / Seedance 2.5 | 模板“画面呈现<视觉风格或情绪>”；长提示词压缩重复风格词、不设字数上限；素材映射优先级 |
| S3 | [Doubao Seedance 2.0 系列提示词指南（火山方舟）](https://docs.volcengine.com/docs/ark/seedance-2-0-prompt-guide) | 首发 2026-04-02，更新 2026-09-22 | Seedance 2.0（2.5 冲突时以 2.5 为准；本条与 2.5 无冲突） | “风格漂移”：写实参考图 + 未强调风格会漂成真人写实，加“3D国风漫画”等约束词，或先把参考图转成目标风格；“3D 国漫 CG 仙侠风格”例子；风格示例词 |
| S4 | [Seedance 2.5 官方发布稿（字节跳动 Seed）](https://seed.bytedance.com/zh/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5) | 2026-07-31 | Seedance 2.5 | 画质优化“更接近实拍的影视质感”（据此判断 2.5 默认偏写实） |
| S5 | [Midjourney V8 Alpha（官方更新）](https://updates.midjourney.com/v8-alpha/) | 2026-03-17 | Midjourney V8 | 个性化、sref、Moodboard 表现；向后兼容 V7 的档案、Moodboard、sref；长而具体的提示词表现更好；`--raw` |
| S6 | [Midjourney 文档：Version](https://docs.midjourney.com/hc/en-us/articles/32199405667853-Version) | 页面无日期；内容写到 V8.2 于 2026-07-24 成为默认 | Midjourney V8.1 / V8.2 | 版本日期；V8.1/V8.2 支持 sref、`--sw`、风格码、Moodboard、Raw；不支持 `--oref`、Draft Mode、Quality；V8.2 Edit Model 取代 Omni/Character Reference |
| S7 | [Midjourney 文档：Style Reference](https://docs.midjourney.com/hc/en-us/articles/32180011136653-Style-Reference) | 页面无日期 | V6 及以后（V8 支持见 S6） | `--sw` 0—1000 默认 100；只取整体风格不取物体人物；文字保持简单、不写冲突风格词 |
| S8 | [Blake Crosley：Midjourney Sref Codes Are Version-Bound](https://blakecrosley.com/blog/midjourney-sref-library-strategy)（第三方） | 2026-08-04 | V8 系列 | 风格码绑定算法版本，图片链接更耐用 |
| S9 | [塔猴：3D国漫风AI漫剧全套指令](https://www.tahou.com/article/204170532137259013)（第三方） | 2026-04-22 | 未注明模型 | 常见风格词组合“3D写实渲染与国漫仙侠美学”“CG渲染，电影级光影” |
| S10 | [创建视频生成任务 API（火山方舟）](https://docs.volcengine.com/docs/ark/create-video-generation-task-api) | 更新 2026-10-08 | Seedance 2.5 / 2.0 | 参考素材上限：2.5 图 0—30、视频 0—10、音频 0—10；2.0 图 0—9、视频 0—3、音频 0—3 |
| S11 | [Codex 官方 imagegen skill（openai/codex 仓库）](https://github.com/openai/codex/blob/main/codex-rs/skills/src/assets/samples/imagegen/SKILL.md) | 2026-10-09 读 main | GPT Image 系 | 提示词结构（用途 → 输入图 → 主体 → 风格 → 构图 → 光线 → 色彩 → 材质 → 约束）；写短、只补有实质帮助的细节；多张参考图按编号写用途；编辑时写明只改什么、每轮重复不变项 |
| S12 | 非公开的第三方打斗提示词样本 13 份；[Segmind《Advanced Seedance 2.5 Prompts》](https://blog.segmind.com/advanced-seedance-2-5-prompts-5-expert-patterns-tested-2026/)；[Venice《Seedance 2.5 Prompt Tips》](https://venice.ai/blog/seedance-2-5-prompt-tips)；[Higgsfield《Seedance 2.5 Prompting Guide》](https://higgsfield.ai/blog/seedance-2-5-prompting-guide) | 样本 2026-10 收到；Segmind 2026-09-25；Venice 2026-08-06；Higgsfield 2026-08-13 | Seedance 2.5 | 样本把渲染风格、战斗演出风格和画质词混写；Segmind：cinematic、hyper-detailed、8K 作用很小（无成对对照）；Venice：画质形容词只占字数；Higgsfield：全局风格写胶片或数字质感、类型、调色，并写明不要的样子 |
| S13 | 第三方 skill：casting-lookbook 公开版（作者 luckdvr，GPT Image 系定妆流程）；另两份私下分享的第三方 skill（日系自然主义电影提示词、彩色漫画导演） | 2026-08 至 09 | Midjourney／gpt-image-2，作者未实测 | 风格指纹写法（技法、材质、边缘、色彩、造型语言）；光按实际光源走：窗光向屋内衰减、冷白灯不变暖、雨夜不继承天光、室内不下雨；彩色漫画按部位分色。只吸收思路、用自己的话写，未搬原文 |
| S14 | [Atlas Cloud《Mastering Seedance 2.5 Anime: Prompts, Aesthetics, and Style Control》](https://www.atlascloud.ai/blog/guides/seedance-2.5-anime-prompts-style-control) | 2026-08-04 | Seedance 2.5（第三方，无对照测试） | 2D 动漫用描线、赛璐璐平涂这类具体写法，不用“电影光”；风格锚点不超过两个，多了会漂；反向写不要 3D 渲染、体积光、次表面散射、柔和渐变阴影；权重语法未经验证，不采用 |

## 查过但没有找到的

- Seedance 2.5 官方没有给风格段的字数建议，也没有“参考图与文字风格冲突时听谁”的明确规则；本 skill 的“参考图为主，文字为辅”和 40—80 字是作者的判断。
- 没有找到 2026 年 Midjourney V8 官方关于 `--sv` 默认值的说明（Style Reference 页只列了 V6、V7）。
- 没有找到 2026 年针对“3D 国漫风”在 Seedance 2.5 上的系统实测。
