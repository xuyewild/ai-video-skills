# 资料来源

口径：以 Seedance 2.5 为准；2.0 资料只作参考并标明；只用 2026 年资料。查询日期 2026-10。模型更新很快，用之前请重新核对。

版本标签：**2.5 官方** = 字节/火山/即梦官方文档或发布稿；**2.5 教程** = 明确针对 2.5 的第三方指南；**2.5 实测** = 有生成结果的测试；**2.0 参考** = 针对 2.0 的资料。

| 编号 | 来源 | 日期 | 版本 | 本 skill 用到的结论 |
|---|---|---|---|---|
| S1 | 火山引擎《Doubao Seedance 2.5 提示词指南》 https://docs.volcengine.com/docs/82379/2607689 | 2026（页面未显示日期） | 2.5 官方 | 秒级时间戳；时间段内容过多会过度剪切或遗漏剧情；官方案例里有“先……然后……”的复合运镜（“一个镜头一种运镜”出自 2.0 指南，2.5 没有）；复杂任务拆小；动作优先概括性描述，只在少数有记忆点的动作上写细节。页面靠脚本渲染，直接抓取常失败 |
| S2 | 火山方舟官方提示词优化 Skill `sd25-pe 0.1.1` | 取得 2026-10-09 | 2.5 官方 | 时间段是事件预算，不是帧级剪辑点；事件过密时减少阶段而不是继续细分；先呈现触发原因再呈现反应 |
| S3 | ByteDance Seed《Seedance 2.5 正式发布》 https://seed.bytedance.com/en/blog/one-take-creation-flexible-referencing-introducing-seedance-2-5 | 2026-07-31 | 2.5 官方 | 官方承认“复杂动作的物理合理性”和“多主体交互场景的稳定性”仍有改进空间 |
| S4 | 即梦 Seedance 2.5 官方使用手册（XiaoHu 英文转述） https://best.xiaohu.ai/en/article/dreamina-seedance-25-guide/ | 2026-08-03 | 2.5 官方（转述） | 武侠案例要求避免“动作拖沓杂乱、肢体穿模扭曲”；机甲案例强调高速中的重心转移；滞空写 Slow Motion；背景人物拉开间距、不出现复制人；主体 1–8 个最稳 |
| S5 | 字节官方 2.5 提示词指南（XiaoHu 中文解读） https://best.xiaohu.ai/article/seedance-25-prompt-guide/ | 2026-08-02 | 2.5 官方（转述） | “动作优先概括主要过程，只为关键动作写细节，同一动作别重复描述” |
| S6 | 小云雀《Seedance 2.5 使用手册》 https://www.xiaoyunque.com/tutorials/seedance-2-5 | 页面只标“8 月 14 日”，按 2.5 发布时间推定 2026 | 2.5 官方产品教程 | “指定时间段内容过多，则会导致过度剪切或剧情遗漏”；30 秒“建议拆成 4-6 个时间段”；不用时间戳控制频率；早期版本有“多参考重复人”；用负向约束兜底（多余肢体、漂浮物） |
| S7 | Luma《Seedance 2.5 Complete Guide》 https://lumalabs.ai/learning-center/articles/seedance-2-5-complete-guide | 2026-07-30 | 2.5 教程 | 叙事内容约每 15 秒 3–4 个有效节拍；重要动作写方向、距离、速度、接触、反应，背景动作不必 |
| S8 | Higgsfield《Seedance 2.5 Complete Prompting Guide》 https://higgsfield.ai/blog/seedance-2-5-prompting-guide | 2026-08-13 | 2.5 教程 | 打击要有重量、反冲、随势；“no floaty wire-fu”；决定性反击一拍慢动作约 2 秒；剑只用劈、刃先到、不刺，保持一种出招；限定每人在画面中只出现一次 |
| S9 | Picsart《Seedance 2.5 prompting guide》 https://picsart.com/blog/seedance-2-5-prompting-guide/ | 2026-08-14 | 2.5 教程 | “Describe cause first, then the resulting motion”；顺序告诉模型因果 |
| S10 | Kapwing《How to Prompt Seedance 2.5》 https://www.kapwing.com/resources/how-to-prompt-seedance-2-5-a-guide-for-ai-video-creators/ | 2026-08-21 | 2.5 教程 | 只给起止状态模型会自己编过渡；动作不要都写成同时发生；已发生的动作再写一遍会重复、抖动；约束写“无肢体变形、无空中凭空变向、无漂浮武器” |
| S11 | OpenArt《Seedance 2.5 Prompt Guide》 https://openart.ai/blog/seedance-2-5-prompt-guide/ | 2026-08-10 | 2.5 教程 | 每个时间段一个清楚动作，塞太多会丢拍；每拍一个运镜；时间戳不是计数器 |
| S12 | ClipDance《Seedance 2.0 vs 2.5 fighting test》 https://clipdance.ai/blog/seedance-2-vs-seedance-2-5-fighting-test | 2026-08-05 | 2.5 实测（对比 2.0） | 2.5 快动作时衣袍、肢体、刃口发软，2.0 更锐利；2.5 尝试更密的连续交手；建议只在最快一下允许方向性模糊、动作后立即恢复清晰、关键姿态轮廓可读；用“接近—格挡—反击—分开—停一秒”的有限序列代替“史诗打斗” |
| S13 | MindStudio《Seedance 2.5 Review》 https://www.mindstudio.ai/blog/seedance-2-5-review-guide | 2026-08-06 | 2.5 实测 | 快速动作段仍有形变、失去连贯；放大修不好；避免快切指令；2.0 的提示词直接用在 2.5 上出现破碎结果 |
| S14 | Kapwing《Is Seedance 2.5 Actually Better Than 2.0?》 https://www.kapwing.com/resources/is-seedance-2-5-actually-better-than-2-0-heres-what-i-found/ | 2026-09-09 | 2.5 实测（对比 2.0） | 2.5 追逐中主角像慢动作而旁人正常速度；2.0 只生成 15 秒；2.0 更严格执行镜头指令；2.0 更愿意做风格化变形，2.5 更贴近原主体 |
| S15 | 网易号《180 秒直出！Seedance2.5 实测》 https://www.163.com/dy/article/L36S4OF105567EZL.html | 2026-07-31 | 2.5 实测 | 30 秒打斗后半段“两个人一直在滚”，动作设计简单时长段落单调 |
| S16 | 网易号《Seedance2.5 来了，字节能打败自己吗？》 https://www.163.com/dy/article/L3949A750531MRZO.html | 2026-08-01 | 2.5 实测 | 双人剑斗流畅、换镜不变脸；延长时没有顺着结尾姿态推进动作，像拼接新段落 |
| S17 | Atlas Cloud《Seedance 2.5 anime prompts》 https://www.atlascloud.ai/blog/tips/seedance-2.5-anime-prompts-style-control | 2026-08-07 | 2.5 教程（动漫） | 冲击帧、速度线写法；风格锚点最多两个；肢体扭曲用姿态参考图约束 |
| S18 | 作者的 AI 漫剧生产实测记录（不公开） | 2026-10 | 2.5 实测 | 受击方不在画面里就不会被打到；“不躲不挡抬掌”被加护盾；方向词写具体；大型静态结构受击位移做不出来；受击反馈单独一镜 |
| S19 | seeddance2.app《How to Do Fighting Scenes in Seedance 2.0》 https://seeddance2.app/blog/seedance-2-fight-scene-guide | 2026-07-02 | 2.0 参考 | 一条一个主招式；双人交手拆成攻方、受击、反击；拳穿过目标最常见，命中单独一镜并写随势；武器写进主体；用简单招式减少快动作变形；约 5 秒一拍 |
| S20 | ComfyUI 文档 ByteDance2ReferenceNode https://docs.comfy.org/zh/built-in-nodes/ByteDance2ReferenceNode | 页面未标日期 | 2.0 参考 | 2.0 参考图 ≤9、参考视频 ≤3、时长 4–15 秒。只用来佐证 S14 的“2.0 只生成 15 秒” |
| S21 | 第三方实测打斗提示词 37 份（私下分享，不公开） | 2026-10 收到 | 2.5 第三方实测（作者自称出片好、无对照；十几份出自同一两套模板） | 起手-接触-结果加地面痕迹；位移差表现强弱；同一击两种反应；碰撞三级与受力传导；镜头只在接触时沿受力方向震；攻击带战术目的；力竭时动作变慢变重。未采纳：小数秒、帧级要求、30 秒 20 拍以上、通用负面清单 |
| S22 | Luma《Seedance 2.5 Prompting Guide》 https://lumalabs.ai/learning-center/articles/seedance-2-5-prompting-guide | 2026-07-30 | 2.5 教程 | 按方向、距离、速度、接触、反应写动作；“0–5s 事件+镜头+声音”的时间段写法；每 15 秒 3–4 个关键节拍 |
| S23 | seedance.tv《Seedance 2.5 fight scene prompt》 https://www.seedance.tv/zh/blog/seedance-2-5-fight-scene-prompt | 2026-08-29 | 2.5 教程（第三方站） | 先全景交代站位；同一时刻一人主动；具体招式名比“迅捷史诗”有效；人物粘连时拉大初始间距；特写只给一次关键受击 |
| S24 | seedance.tv《Seedance slow motion video guide 2026》 https://www.seedance.tv/blog/seedance-slow-motion-video-guide-2026 | 2026-06-28 | 2.5 教程（第三方站） | 变速写明“先正常速度、在某一刻转入慢动作”，切换点不准要多抽；慢动作词叠多会整段冻住；快动作强行慢放手脸易变形 |
| S25 | invideo《Why do AI video models struggle with physical contact》 https://invideo.io/faq/why-do-ai-video-models-struggle-with-physical-contact/ | 2026-07-27 | 2.5 参考（厂商自述，跨模型） | 模型没有骨骼与碰撞概念，多人接触最容易崩；约 3 次出 1 个可用接触镜头 |
| S26 | Higgsfield《Seedance 2.5 Complete Prompting Guide》 https://higgsfield.ai/blog/seedance-2-5-prompting-guide | 2026-08-13 | 2.5 教程 | 写实打斗“不是戏剧化、不是吊威亚式摆姿势”；出招交换处用快切和甩镜 |
| S27 | CometAPI《How to prompt Seedance 2.5》 https://www.cometapi.com/how-to-prompt-seedance-2-5/ | 2026-08-10（09-03 更新） | 2.5 教程 | 用参考视频控制编排 |
| S28 | Atlas Cloud 打斗测试（Wan 3.0 / MiniMax H3） https://www.atlascloud.ai/blog/tips/wan-3.0-fight-scene | 2026-08-27 | 2.5 参考（跨模型，非 Seedance） | 手臂被躯干挡住消失、镜头在接触时躲开；对策：侧面角度、全身在画面内 |
| S29 | 一位 AI 动作设计师的教学视频《AI 动作设计：让打斗连续起来》（私下分享） | 2026-10 收到 | 2.5 教程（未标模型版本，无对照） | 打斗拆成人物动作、镜头路线、周围反应三件事并按此检查；开场就在交手；上一招收势时下一招已开始，接不上就减招；速度靠具体移动方式、写方向落点；快不等于全程模糊 |
| S30 | 第三方打斗提示词 6 份（私下分享） | 2026-10 收到 | 2.5 实测（第三方，作者称出片好，无对照） | 敌人持续冲锋补位、不围观；两个对手打法不同；扇、法杖类动作词；下腰旋步、抬膝顶腹、法器柄反砸等组合。未采纳：小数秒 |
| S31 | 第三方战斗提示词 13 份（私下分享） | 2026-10 收到 | 2.5 实测（第三方，作者称出片好，无对照） | 折扇、流星锤、长枪、巨刃、伞刃、巨笔的动作语法与物理；战斗链；长兵控距短兵抢内圈；反作用力接下一招；借倒塌柱、飞石、对方武器换轨迹；场地推进线与战损递进；单人展示用场景物当落点；人对巨兽。未采纳：0.2–0.5 秒疯切、25 机位、小数秒、帧数、8K、定格和收白收黑结尾、以参考图作首帧（除小数秒、帧数外，其余是“未验证”而非“无效”） |
| S33 | 第三方战斗提示词 5 份（私下分享） | 2026-10 收到 | 2.5 实测（第三方，无对照；和上一行出自同一套模板） | 敌群按种类分工（远程压制、巨型掷物、小只扑咬、精英合击）；蓄力时能量沿发力链从脚到兵器逐节亮起；真空里声音只剩身体传导的低频，大爆之后留一个清楚的小声音（收刀“咔哒”）。未采纳：三级碰撞特效包和 0.05 秒抽帧、每 0.2–0.3 秒换位、1.2 / 1.5 秒小数秒镜头、UE5 / 8K / 胶片型号、核爆蘑菇云卫星视角当通用升级、伪技术词（“800+ 骨骼节点逐帧调整”）、视频停在命中前定格让下一条接着炸、IP 角色名和“雾山五行”画风名（除小数秒、帧数外，其余是“未验证”而非“无效”） |
| S32 | super-i.cn《用AI制作冲击帧：让打斗更有力量感》 https://www.super-i.cn/info-3090.html | 2026-10-07 | 2.5 教程（即梦 Seedance 2.5 成片，作者逐帧查看） | 角色要从容强大时，用小幅、准确、轻松的出招表现控制力，威力靠目标和环境的变化表现；成片里蓄力和短幅双斩在同一个特写里完成 |

## 查不到的

- **灵兽与人的抓、摔、托举**：没有找到针对 Seedance 2.5 或 2.0 的专门资料或实测。相关规则按身体力学和尺度基线写，属于判断。
- **Q 版夸张动作**：没有找到 Seedance 的专门资料。写法用“标进标出”和按时间段分别写比例，属于判断。
- **受力方向反**：没有找到专门实测；只有作者方向写反的记录（S18）。
- **武器交接丢失**：2.5 没有专门资料；只有 2.0 的“武器在帧间消失”（S19）和 2.5 教程的“锁定一种出招”（S8）。
- **群战与一对一的差别**：没有直接对比；依据官方承认的多主体交互弱项（S3）和主体数量稳定区（S4）推出。
- **一条视频的动作拍数上限**：没有官方数字；S7、S6 给出的是节拍密度观察，不折算成公式。

## 动作设计手艺资料（非 Seedance，用于 body-and-contact 第 11–13 节）

- Dyabin《Separation / Compensation Principle in Strikes Animation》，80.lv，2021-12-10，https://80.lv/articles/separation-compensation-principle-in-strikes-animation/ ：身体先停、肢体后出才有重量。
- PlayStation Blog《God of War Ragnarök》战斗设计，2022-10-04，https://blog.playstation.com/?p=370399 ：受击姿态大变、挥击大弧线强跟随、主动降低震屏换可读性、声音补冲击。
- Jan Willem Nijman（Vlambeer）game feel 演讲整理，2013-10-22，https://infovore.org/?p=5275 ：命中短暂冻结、沿攻击方向击退、镜头沿攻击方向踢一下再衰减。
- 樱井政博谈 hitstop，Source Gaming 译，2015-11-11，https://sourcegaming.info/2015/11/11/thoughts-on-hitstop-sakurais-famitsu-column-vol-490-1/ ：双方同时停住、受方抖动、时长随伤害增加。
- No Film School《Jackie Chan's 9 principles of action comedy》，2014-12-03，https://nofilmschool.com/2014/12/jackie-chans-9-principles-action-comedy ：镜头清楚、动作与反应同框、让人感到节奏、从劣势开始、痛让人物有人性。
- RogerEbert.com 访 Gareth Evans、Iko Uwais，2014-03-25，https://www.rogerebert.com/features/the-art-of-controlled-chaos-with-gareth-evans-and-iko-uwais-of-the-raid-2-berandal ：每个人物有自己的节奏，受方不提前动。
- 香港01《寫實vs寫意：武打片的動作設計》，2018（2025 更新），https://www.hk01.com/武備志/149832/ ：北派大开大合与写实拳种设计。
- 新华社访袁和平，2026-02-19，https://www.news.cn/20260219/233171a833994189bfdc6aa4d20e003b/c.html ：兵器差异即人物性格差异。
- 机核《动作游戏的打击感》，2018-05-22，https://www.gcores.com/articles/97115 ：招式越高阶反馈越强，前摇后摇。
- 澎湃评《雾山五行》，2020-08-10，https://www.thepaper.cn/newsDetail_forward_8657966 ：打斗有起承转合、实写兵器配虚写特效（记者分析）。

没找到 3D 国漫动作导演的一手访谈，也没找到字节官方的 Seedance 2.5 动作指南。
- R 系列（body-and-contact 第 14 节）：HK01《寫實vs寫意 武打片的動作設計》2018（2025 更新）https://www.hk01.com/武備志/149832/ ；HK01《京劇與香港武打電影》2018-01-02 https://www.hk01.com/article/146022 ；HK01 访谷垣健治 2026-06-10 https://global.hk01.com/电影/60358249/ ；HK01 访武指梁博恩 2020-12-30 https://www.hk01.com/武備志/568223/ ；人民日报副刊（硬僵身）2023-06-01 https://paper.people.com.cn/rmrb/html/2023-06/01/nw.D110000renmrb_20230601_2-20.htm ；GIGAZINE 转述 Vox 特技协调访谈（借位）2023-08-03 https://gigazine.net/gsc_news/en/20230803-punches-real/ ；Bordwell《A glance at blows》2008-12-28 https://davidbordwell.net/blog/2008/12/28/a-glance-at-blows/ ；界面访林魂 2023-08-11 https://www.jiemian.com/article/9911131.html ；澎湃《镖人贰》2026-06-14 https://m.thepaper.cn/newsDetail_forward_33369819 ；澎湃评《雾山五行》2020-08-25 https://www.thepaper.cn/newsDetail_forward_8871996 。
- 打点、卡点、起势、收势、受招、过招、身法这几个行话本轮没找到可引用的定义，没有写进第 14 节。3D 国漫（《凡人修仙传》《斗罗大陆》）仍没有动作设计的一手访谈。
