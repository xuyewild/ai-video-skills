# ai-video-skills

English | [中文](README.zh-CN.md)

I've been making AI comic dramas for about six months. An image model does the asset sheets, Seedance 2.5 does the video, and I'm at thousands of clips now.

Most of my redos come down to two things. One is the look not matching. Each clip is fine on its own, then you cut them together and one's cold, the next is warm, and a character who was 3D last episode is sliding toward live action. The other is fights. Fists go right through people, someone gets hit and just stands there, two fighters strike a pose and wait for each other.

These two skills came out of all those redos.

**visual-bible**: a short file, one or two screens, that locks down the style, color, light and scale up front. It also gives you two style blocks to paste straight into prompts, one for images, one for video.

**action-physics-choreography**: takes a line like "they clash fiercely" and breaks it into beats. Setup, contact, result. Which way the force goes, where people land, how the camera follows.

You can install either one alone. English is in `skills/en/`, Chinese in `skills/zh/`, same content.

## Is this for you?

If you're making comic dramas, short dramas, animated shorts or music videos with dozens or hundreds of clips per project, if your style or color or proportions keep drifting between episodes, or if fights and chases come out wrong no matter how many times you regenerate, yes. If you only need a clip or two, you don't need it.

## Stuff I picked up from the redos

- Don't name the style. The model doesn't care. Describe what you can see: line art or not, how many shadow layers, how much skin detail.
- Make one sample first. If it looks right, make every asset sheet from it, and only go to video once the look holds. The text is just backup.
- Light has to come from somewhere. The bright side faces the light, shadows are textured dark gray, and night scenes aren't lit up everywhere.
- If you only write the start and the end, the model makes up the middle. So write every beat in full: how it starts, what it hits, what happens.
- Whether a hit lands is all about the person getting hit. Start the shot at contact. They get knocked somewhere and land. Show how hard it was by how far they fly, not with adjectives.

## Install

**Claude Code**: copy the skill folders you want into `~/.claude/skills/` (global) or `.claude/skills/` in your project.

```bash
git clone https://github.com/xuyewild/ai-video-skills
cp -r ai-video-skills/skills/en/visual-bible ~/.claude/skills/
cp -r ai-video-skills/skills/en/action-physics-choreography ~/.claude/skills/
```

**Claude web or desktop app**: zip a skill folder and upload it as a custom skill in settings.

**Other AIs**: a skill is just some Markdown and a few Python scripts. Hand the AI `SKILL.md` and whatever reference files it points to.

## Models

The video examples use Seedance 2.5 (with notes on what's different in 2.0). The asset-sheet examples cover GPT Image and Midjourney V8. The methods don't depend on the model, but when you switch, hard limits like clip length and number of reference images come from that model's official docs. Sources and the dates I checked them are in each skill's `references/sources.md`. These models change fast, so double-check before you rely on a detail.

## Scripts

Python standard library only, 3.9 or newer. They read both Chinese and English files.

| Script | What it does |
|---|---|
| `visual-bible/scripts/check_visual_bible.py` | Checks that a visual bible has all its fields and sections, that the style blocks are clean (no hex codes in the video block, no time of day or weather in the asset block), and that it matches the asset sheet |
| `action-physics-choreography/scripts/validate_action_text.py` | Checks that action beats go setup → contact → result, have a force direction, don't pile on intensifiers, and fit the clip length |

```bash
python -m unittest discover -s tests -v
```

## Sister repo

[multi-ai-skills](https://github.com/xuyewild/multi-ai-skills): splitting up work, handing it off and keeping track of progress when several AIs work on one long project.

## Feedback

Issues and PRs are welcome. What I'd most like to see is before/after comparisons from your own projects. If you think a rule is wrong, tell me which model you used and what went wrong in what situation.

## License

[MIT](LICENSE)
