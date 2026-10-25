# ai-video-skills

English | [中文](README.zh-CN.md)

Two skills that make AI video look like one film, and make AI fight scenes actually land. They come from half a year of AI comic-drama production: an image model for asset sheets, Seedance 2.5 for video, dozens of episodes and the repair notes from hundreds of fight shots.

| Skill | What it solves |
|---|---|
| [visual-bible](skills/en/visual-bible/SKILL.md) | Every clip looks good, but together they don't look like one film. A one-to-two-screen visual bible locks the style, color, light and scale, and gives two ready-to-paste style blocks (one for images, one for video) |
| [action-physics-choreography](skills/en/action-physics-choreography/SKILL.md) | Fists pass through bodies, nobody reacts to a hit, two fighters pose and wait. Turns "they clash fiercely" into setup → contact → result beats with force direction, landing and camera |

Each skill works on its own. Every skill ships in English (`skills/en/`) and Chinese (`skills/zh/`). Both versions have the same content and each installs on its own.

## Who it is for

- You make AI comic dramas, short dramas, animated shorts or music videos, with dozens or hundreds of generated clips per project.
- Style, color grade or character proportions drift from episode to episode.
- Fights, chases and throws keep coming out wrong no matter how often you regenerate.

Not useful for one or two clips.

## The core ideas

- **Write the style as visible technique.** Models respond to "line art or not, how many shadow layers, how much skin detail", not to a style name.
- **Reference images first, text second.** Make one sample with the style block, get it approved, generate every asset sheet from it, then move to video.
- **Light needs a source.** In any style, the lit side faces the light, shadows are textured dark gray, and night is not bright everywhere.
- **Cause before effect.** Give a model only the start and the end of a move and it invents the middle. Write setup, contact and result for every beat.
- **Impact lives in the one being hit.** The receiver is the subject of the hit shot, the shot starts at contact, and the receiver moves and lands somewhere. Show strength with distance, not adjectives.

## Install

**Claude Code**: copy the skill folders you want into `~/.claude/skills/` (global) or `.claude/skills/` in your project.

```bash
git clone https://github.com/xuyewild/ai-video-skills
cp -r ai-video-skills/skills/en/visual-bible ~/.claude/skills/
cp -r ai-video-skills/skills/en/action-physics-choreography ~/.claude/skills/
```

**Claude web or desktop app**: zip a skill folder and upload it as a custom skill in settings.

**Other AIs**: a skill is just Markdown plus Python scripts. Give the AI `SKILL.md` and the reference files it points to.

## Models

Video writing uses Seedance 2.5 as the example (with notes on 2.0). Asset-sheet writing covers GPT Image and Midjourney V8. The methods are model-agnostic; when you switch models, hard limits such as clip length and reference count follow that model's official docs. Sources and lookup dates are in each skill's `references/sources.md`. Models change fast, so check again before you rely on a detail.

## Scripts

Python standard library only, 3.9+. Both Chinese and English files are recognized.

| Script | What it does |
|---|---|
| `visual-bible/scripts/check_visual_bible.py` | Checks that a visual bible has all fields and sections, that the style blocks are clean (no hex codes in the video block, no time of day or weather in the asset block), and that it matches the asset sheet |
| `action-physics-choreography/scripts/validate_action_text.py` | Checks that action beats run setup → contact → result, have a force direction, don't stack intensifiers, and fit the clip length |

```bash
python -m unittest discover -s tests -v
```

## Sister repo

[multi-ai-skills](https://github.com/xuyewild/multi-ai-skills): roles, handoffs and project memory when several AIs work on one long project.

## Contributing

Issues and PRs are welcome, especially before/after comparisons from your own projects. When proposing a rule change, say which model you used and what went wrong in which situation.

## License

[MIT](LICENSE)
