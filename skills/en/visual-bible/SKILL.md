---
name: visual-bible
description: Write a short visual bible for AI video, AI comic drama (AI-generated serial short drama) and animated shorts: one-line style, color, light, materials, camera texture, time-of-day and weather variants, don'ts, scale baseline, plus an asset image style block and a video style block you can paste straight into prompts. Works for any look (3D, 2D, live action). Build it once at project start, then add a row only when a new time of day, weather or style block appears. It does not design shots or describe characters.
license: MIT
metadata:
  version: "0.1.0"
---

# Visual Bible

The most common problem with an AI-made film is that every clip looks good alone but they do not look like one film. One clip is cold, the next is warm. A character is 3D in one episode and drifts toward live action in the next. Night scenes are bright everywhere. A visual bible is a short file, one to two screens, that fixes the look, color and light of the whole film. It also gives two style blocks you paste into prompts, so every generation starts from the same base.

It comes from six months of AI comic drama production (an image model made the asset images, Seedance 2.5 made the video). The method does not depend on the model. Seedance-specific wording is marked.

## 1. What it does and does not do

It produces one file. Suggested location: `00_project/visual-bible.md`.

| Who reads it | Which part | What for |
|---|---|---|
| Whoever writes image prompts (person or AI) | Style name, asset image style block (read the Midjourney block if you use Midjourney) | The style part of character, scene and prop image prompts |
| Whoever writes video prompts (person or AI) | Video style block, the line for the current variant, color, don'ts, scale baseline | The first sentence of every video prompt and its "keep consistent" part |
| The owner (director) | The whole file | Read it in one screen and decide |

It does not cover: shots, composition, camera moves; the specific look of characters, scenes and props (that goes in your character or asset sheet); sound; plot.

## 2. When to write it and when to change it

- **Build the base at project start.** Read the script, list the location types, times of day and weather that really appear, and write it from the template.
- **After that, only increments.** Before each episode (or batch), check whether there is a time of day, weather, location type or special style block (flashback, dream, illusion) that is not in the variant table. If there is, add one row that says only what changes from the baseline. If not, change nothing and reply "no new variants this episode".
- **The style base does not change per episode.** To change the one-line style, color, materials, camera texture or the two style blocks, ask the owner first. After a change, use the new text from the next shot not yet generated. Approved images are not regenerated for a wording change. They are regenerated only if the style itself changed.

## 3. Input

- The owner's style requirements, reference film titles or reference images. Take only color, light, materials and texture from a reference, never characters or plot.
- Location types, times of day and weather that recur in the script (day, night, rain, snow, candlelit interiors...). Build variants only for what really appears.
- If there is an asset sheet (the register of characters, scenes and props), its "style baseline" and "gray background" lines.

If the style is not decided, ask the owner. If the name is set but details are missing, fill in the five items of the "style profile" in section 0 of [style-writing.md](references/style-writing.md) and say when you deliver which items you chose yourself. Do not stop because a color value or a reference film is missing.

## 4. File format

Template and how to write each part: [template.md](references/template.md). Fixed order:

1. `Style name:` Two to six words, such as `3D donghua` (donghua = Chinese animation; here, Chinese 3D animation) or `2D cel animation`. If there is an asset sheet, copy it as is into the sheet's `Style baseline:` line.
2. `One-line style:` Medium + render texture + overall mood, one sentence.
3. `Fixed effects:` Effects that recur across episodes (someone's protective glow, a magic line that runs through the whole film). Fix one color for each: `name = color`, separated by `;`. Write `none` if there are none. Optional: `Effect intensity:` for the baseline intensity of effects across the film.
4. `## Color`: main tone, shadows, highlights, skin tone, accent color, one line each, plus the main/secondary ratio and the reserved color. For the palette system see [color-craft.md](references/color-craft.md).
5. `## Light`: where the main light comes from, soft or hard, contrast, how much detail stays in shadows. Light and shadow often matter more than the scene itself. In any style, light must have a findable source and a consistent direction. Non-realistic styles may be expressive, but must not feel wrong.
6. `## Materials`: how skin, cloth, metal, stone, wood, fur and feathers appear in this project.
7. `## Camera texture`: depth of field tendency, sharpness, grain, glow; the character of camera motion (steady, heavy, light). No specific camera moves.
8. `## Time and weather variants`: a table with Variant | What changes vs. baseline | Must not change | Line for the video prompt.
9. `## Don'ts`: five to ten items, the directions that really drift.
10. `## Asset image style`: one or two sentences, render and materials only, no ambient light or time of day (character and prop images are usually even light on gray; scene image light is written per variant).
11. `## Video style`: two or three sentences: style + color tendency + light baseline, placed in the first sentence of every video prompt.
12. `## Scale baseline`: one line of height or body length in numbers for each main character and creature, and a last line "Scale sentence" to copy word for word into video prompts.
13. (Optional) `## Asset sheet link`: two lines: `Style baseline: <style name> (details in visual-bible.md)` and `Gray background: <color value>`.

Optional sections: `## Palette system`, `## Light setups`, `## Color script`, `## Combat staging style`, `## Midjourney style`, `## Asset image texture`. See the template for how to write them.

Keep the whole file to one or two screens. No internal IDs, revision numbers or status fields. Use version control for history.

## 5. How to write the style blocks

The style profile, details and examples for each style are in [style-writing.md](references/style-writing.md). Sources are in [sources.md](references/sources.md). Key points:

- **Write style as visible practice.** A model tells styles apart by whether there are outlines, how many shadow layers there are, how far the skin is rendered. It does not tell them apart by the style name alone. Use one main anchor plus one or two supporting words, then one line saying what it is not (negative anchor).
- **Video style block.** Two or three sentences, about 40 to 80 words, written once per prompt, not repeated in every shot. The official Seedance 2.5 structure is "one-sentence overview (subject + place + event + genre/style) -> shots -> a closing line for the atmosphere that runs throughout". The style block goes in the opening sentence. No color value codes.
- **Asset image style block.** One or two sentences, starting with the style name, then form, line and shading, materials. No time of day, weather, ambient light or tone filters, because these words tint the gray background and the characters. No color values or parameters.
- **Midjourney (optional).** If you use it for images, write a separate English block that matches the asset image style block. Put parameters on the next line, "Style reference", not in the style block.
- Quality words such as "8K" or "UE5" can be added at the end, but they do not replace a visible description of the style.
- When a reference image and the text conflict, the reference image usually wins. So first make one sample image with the asset image style block. After the owner approves it, use it as the style reference for all later asset images. Move to video once the style is consistent.

## 6. Workflow

1. Read the script and list the location types, times of day and weather that really appear.
2. Write a first draft from the template. For variants, write only what changes from the baseline.
3. Write the style blocks and self-check: the video style block has no color value codes; the asset image style block (and the Midjourney block, if written) has no time of day, weather or scene light.
4. Run the check script (it checks format only, not whether the style is good):

   ```bash
   python3 scripts/check_visual_bible.py visual-bible.md [--registry asset-sheet.md] [--prompts prompts.md ...]
   ```

   `--registry` checks the asset sheet's style baseline and gray background. `--prompts` checks whether the color is copied exactly when a prompt mentions a fixed effect (warning only).
5. Give the owner one screen to read. When they finish editing, it is final. If a sample is wanted, make one image with the asset image style block. Once approved, it becomes the style reference image.

## 7. How downstream uses it

- **Image:** the "style" line of the prompt = style name + asset image style block, followed by appearance, proportions, composition, background.
- **Video:** the first sentence of every prompt = video style block + the line for the current variant. In the "keep consistent" part, write the light and tone relationship once, plus three to five color anchors for this scene. Rewrite the relevant don'ts in positive form and put them in. Characters and creatures in the same frame get the "scale sentence" copied word for word. Do not write "see the visual bible" or "same as above". The model cannot see this file.
- **Compare with the approved sample, not with the previous episode.** At each increment, compare against the sample approved at project start to see whether the look has drifted. Otherwise it slowly slides a little each episode.

## 8. When you switch video models

Different models (including different versions from the same maker) have very different aesthetic preferences. Do not mix two models in one scene. After switching, make one short sample clip from each style block and show the owner before going to batch. For the specific differences between Seedance 2.0 and 2.5, see the last section of style-writing.md.

## 9. Delivery

- The visual bible file (from the template).
- Two or three lines in chat: what style was set, which items you chose yourself, and whether the asset sheet has been synced.
