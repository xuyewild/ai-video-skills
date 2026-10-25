# Visual Bible Template

Copy to `project-name/00_project/visual-bible.md`. The example below is a fictional 3D Eastern fantasy project (protagonist Lin Zhou, with a spirit fox, Tuanzi, who rides on his shoulder). "3D donghua" means Chinese 3D animation. The content only shows how to write; change it to fit your script and the owner's requirements. `scripts/check_visual_bible.py` checks the headings and field names on this page, so do not rename the headings.

````markdown
# Visual Bible

Style name: 3D donghua
One-line style: 3D donghua animation, slender CG characters in Eastern fantasy settings, clean and refined texture, a calm and cool overall feel with warm light at key moments.
Effect intensity: medium-high; ordinary moves follow the baseline, signature ultimates and the film's climax go up one level, with ups and downs within the same scene
Fixed effects: amulet glow = cyan-white; spirit fox flame = orange-gold

## Color
- Main tone: gray-teal and stone blue, most of the frame (sky, distant hills, stone buildings).
- Shadows: deep teal-gray, not black, not purple-leaning; clothing outlines stay readable in the dark.
- Highlights: warm off-white, only on lit edges and metal.
- Skin tone: natural warm skin, not gray or greenish even in cold surroundings.
- Accent color: vermilion, only on old seals, blood and key props, small areas.
- Ratio: gray-teal about 60% (sky, distant hills, stone walls), warm off-white about 30% (lit surfaces, wooden objects), vermilion about 10%.
- Reserved color: vermilion goes only to key story objects; no large areas of warm color before this episode's climax.

## Palette system (optional, write it when there are many characters or factions, or when color has to tell the story)
- Color ideology: gray-teal = order and oppression; vermilion = blood and key story objects; warm off-white = human warmth and safe places.
- Characters and factions: protagonist = white clothes with vermilion patterns, the brightest and highest contrast; opposing faction = cold blue and silver; extras = gray-teal, one step darker and plainer than the protagonist.
- Color identity of spaces: academy = gray-teal stone, pale sky; wilderness = earth brown, dark green; protagonist's home = warm wood, candlelight.
- Saturation and value layers: characters and the reserved color are the most saturated, effects next, environment the plainest; distant views are paler and cooler.
- Separation: the protagonist is set apart from the background on at least one of value, warm/cool, or saturation; same-color clothes are separated by light (lit side, rim light) and position.
- Same color, non-reserved use: the same color on metal and ornaments is written as matte and darker, not glowing, so it stays apart from the reserved color's light.

## Light
- The main light has a source: day is skylight plus side-back light, night is moonlight or firelight, interiors are window light or candle flame.
- Soft light first; the light-to-shade transition on faces is gentle; hard light is allowed in fights and effects scenes.
- Medium contrast: highlights do not blow out into white patches, shadows keep detail.
- The lit side of a face always faces the light source; people closer to a fire are brighter.
- Scene light must make sense: light has a findable source (window, lamp, fire, skylight), the direction is consistent, shadows match, and a night scene is not bright everywhere. Non-realistic styles may be expressive (for example stronger rim light, mood-colored light), but must not feel wrong. Live-action projects always follow real-world logic.
- Effect light: skill light must fall on characters and environment (interactive light). Write who it lights and who keeps their original color. A large collision may briefly change the light of the whole scene, then return to the scene baseline after the peak.
- The darkest areas are textured dark gray, not pure black.

## Light setups (optional, one line per scene type)
| Scene type | Main light type and direction | Light and dark (how much of the frame is shadow) | Warm/cool |
|---|---|---|---|
| Daytime dialogue | Angled side light, sun behind and to the side of the character, soft light | Mid-tone, 10 to 20% | Warm sun against gray-teal shadows |
| Scheming, interrogation | Hard side light or top light, only one lamp | Low-key, 50 to 60% | Warm lamp against cool shadows |
| Awakening, being chosen | Halo from behind, or one beam falling only on the protagonist | Protagonist bright, surroundings dark | Beam warm gold, surroundings cool gray |

## Materials
- Skin: fine, slightly translucent, not plastic-smooth.
- Cloth: weave and thickness visible; combat clothing is more matte, silk has a soft sheen.
- Metal, stone and wood: metal has small-area highlights; stone is rough and low in reflection; wood has grain.
- Fur and feathers: individual strands are distinct; the spirit fox's white fur stays pure white and is not tinted by ambient light.

## Camera texture
- Depth of field: medium and close shots in dialogue have moderately blurred backgrounds; deep frames fade layer by layer with depth of field and atmospheric perspective, subject clear, distance paler and softer.
- Sharpness and grain: the image is clean and sharp, no film grain, no vignette.
- Glow: a slight glow only around real light sources and effects.
- Motion character: the camera is steady and has weight, does not shake, and makes no high-speed flybys without a reason.

## Time and weather variants
| Variant | What changes vs. baseline | Must not change | Line for the video prompt |
|---|---|---|---|
| Day | Baseline | — | Soft daylight comes from the side and back, the frame is mostly gray-teal, skin tones are natural. |
| Night | Whole frame darker and cooler, main light changes to moonlight or firelight | Skin tone readable, shadows keep detail | Cool blue moonlight dominates at night, firelight lights only nearby people and ground, outlines stay readable in the dark. |
| Rain | Lower contrast, reflections on the ground | White fur does not change color | Overcast rain light is even and grayish, the ground is wet and reflective, fine rain falls densely. |
| Flashback | Fades to warm brown, edges go soft | Character appearance unchanged | The flashback fades to warm brown with slightly soft frame edges; the baseline returns when we come back to the present. |

- Interior scenes: window light sets the direction, light gets dimmer toward the inside of the room, corners may be dark; lamp light takes its warm or cool color from the lamp (candles and oil lamps are warm, a cool white lamp is not automatically written as warm).
- When time of day and weather combine, light follows the actual sources: a rainy night keeps the night's lamps and fire and does not inherit daytime skylight; looking at rain outside from inside a room, it does not rain or fog indoors.

## Color script (optional, one table per episode)
Before each episode starts, write one table by section. When writing video prompts, set the light, dark, warm and cool of each scene from it. Only the header and the rules are fixed here. Example:

| Section | Emotional direction | Where light/dark, warm/cool and intensity go | Where the reserved color appears |
|---|---|---|---|
| Opening to conflict | Oppression -> outburst | Darker and cooler -> local warm light | Vermilion first appears on an old seal |

## Don'ts
- Do not turn into live-action realism or flat 2D.
- No colored light without a source, no color wash over the whole frame.
- Skin does not go gray, greenish or fluorescent.
- Characters' eyes do not glow (unless the script says so).
- Characters are not drawn with influencer faces, heavy retouched makeup or plastic skin.
- No subtitles, watermarks or logos in the frame.

## Asset image style
```text
3D donghua CG style, slender character proportions, fine skin with a slightly translucent feel, clothing with visible weave and embroidery, matte combat clothing, metal with only small crisp highlights, clean sharp render, no film grain.
```

## Video style
```text
3D donghua animation style, slender CG characters, clean and refined texture, not live action. The whole frame is cool gray-teal, light is soft with a clear source, skin tones are natural, shadows keep detail, and distant objects fade softer and paler with atmospheric perspective.
```

## Combat staging style (optional, write it for projects with fights)
```text
Combat staging of a high-budget animated film: exaggerated perspective, large contrast between fast and slow, key action poses are exaggerated but readable, the camera follows the action. The render texture does not change and still follows the style blocks above.
```

## Scale baseline
- Lin Zhou: height 182 cm.
- Tuanzi: about 40 cm standing, usually crouching on Lin Zhou's shoulder.
- Scale sentence: Lin Zhou is 182 cm tall; Tuanzi is about 40 cm standing, head level with Lin Zhou's knee, and when crouching on his shoulder its body takes up about half the shoulder width.

## Asset sheet link
Style baseline: 3D donghua (details in visual-bible.md)
Gray background: #808080
````

If you use Midjourney for asset images, add this block after the "Asset image style" block (optional):

````markdown
## Midjourney style
```text
3D Chinese animation (donghua) CG style, elongated body proportions, refined skin shading with subtle subsurface scattering, visible fabric weave and embroidery, matte cloth, small crisp metal highlights, clean sharp render, no film grain
```
Style reference: none
````

For styles such as 2D, line art and ink wash (the default texture wording assumes the translucent skin and fabric weave of 3D and live action), add this block after the "Asset image style" block (optional). Use it in place of the texture description when making character, creature and prop images:

````markdown
## Asset image texture
```text
Flat color with one or two layers of hard-edged shadow, cloth shown only with fold lines, metal as a single highlight color, no skin texture and no fabric weave.
```
````

For live-action projects where the owner asks for a cinematic texture by name, you can add one line to "Camera texture". The texture words (anamorphic feel, film grain, slight halation, very shallow depth of field) go into the video style block and not into the asset images. Also change "no film grain, no vignette" to match. Do not add this for other styles.

## How to write each part

| Part | How to write it | What not to write |
|---|---|---|
| Style name | Two to six words; identical, word for word, to the part before the brackets in the asset sheet's `Style baseline:` line | Long sentences, bracketed notes (bracketed notes go after the asset sheet line) |
| One-line style | Medium + render texture + overall mood | Plot, character names |
| Fixed effects | For each effect that is fixed across episodes and appears in every episode, fix one color: `name = color`, separated by `;`, or `none`. When a prompt mentions it, copy the color word for word | Changing color by scene; two wordings for the same effect ("cyan-white", "pale cyan") |
| Effect intensity (optional) | The baseline for the whole film and the rule for going up a level, one sentence | The specific result of each move |
| Color | Five lines: main tone, shadows, highlights, skin tone, accent color; write the color and the area. Then the rough ratio of main, secondary and accent (for example 6:3:1). For each color say which light source it comes from and which surface it falls on. Make the accent color a "reserved color", given only to key story objects, and say at what moment it appears | One-to-one color mapping ("tense means red") |
| Palette system (optional) | Color ideology (what each color stands for in this film and who uses it), identity colors for characters and factions, color identity of spaces, saturation and value layers, how the subject is separated from the background, how same-color non-reserved uses are told apart from the reserved color. Write only this film's choices; for general practice see [color-craft.md](color-craft.md) | General color knowledge that applies across projects; color values (they stay out of the video style block) |
| Color script (optional) | Fix the header and rules; each episode writes by section the emotional direction, where light/dark, warm/cool and intensity go, and where the reserved color appears; the method comes from Pixar's color scripts | Color values for every shot |
| Light | Where the main light comes from, soft or hard, contrast, shadows; plus three rules that can be checked shot by shot: lit side faces the light, closer to the source is brighter, shadows are textured dark gray, not pure black | The lighting plan of one particular shot |
| Light setups (optional) | One line for each scene type common in this project: main light type and direction, light and dark (how much of the frame is shadow, shadows still textured), warm/cool | The lighting plan of one particular shot; light without a source |
| Materials | Four or five materials common in this project | The structure of one specific prop (that belongs to the asset sheet) |
| Camera texture | Depth of field tendency, sharpness, grain, glow, motion character | Specific camera moves |
| Time and weather variants | Build only what really appears in the script; the "line for the video prompt" can be joined directly after the video style block. For a special style block (flashback, dream, illusion), write one or two visible rules (such as "fades to warm brown, edges go soft") and say when it returns to the baseline | One variant per scene |
| Don'ts | Five to ten items, checkable | Dozens of synonymous lines |
| Asset image style | One or two sentences; render and materials only; paste as is into the "style" line of image prompts | Time of day, weather, scene light, tone filters (character and prop images are even light on gray; scene image light is written per variant); color values, `--` parameters |
| Asset image texture (optional) | For 2D, line art, ink wash and similar styles, one sentence: how many shadow layers, hard or soft edges, how cloth and metal are drawn, whether skin gets texture | Light, time of day, color values |
| Midjourney style (optional) | Write it only when using Midjourney; one English block that matches the asset image style block | Same as above; parameters go on the next line, "Style reference" |
| Style reference (inside the Midjourney block) | `none`, or `--sref <sample image link> --sw <0-1000>` | Several conflicting samples |
| Video style | Two or three sentences, about 40 to 80 words, with one negative anchor line | Color value codes; empty words such as "cinematic" or "premium feel" |
| Combat staging style (optional) | One or two sentences: how the action and camera perform, no render description; attached after the video style block only for fight and ultimate-move shots | Mixing it with the style block |
| Scale baseline | One line for each main character and creature: height or body length as a number (cm, m); for those often together, the relative position (how much of the shoulder width when crouching on the shoulder); the last line "Scale sentence" is copied word for word into video prompts. If there is an asset sheet, the numbers match it; change one, sync the other | Phrases with no number such as "very small" or "up to the knee" |
| Asset sheet link (optional) | Two lines, `Style baseline:` and `Gray background:`; the part of `Style baseline` before the brackets is identical to the style name | — |

## Link with the asset sheet

- The asset sheet header reads `Style baseline: <style name> (details in visual-bible.md)`. The part before the brackets must be identical to the "style name", word for word, so that a script or person assembling prompts takes only the words before the brackets.
- Image prompt: "Style: <style name>; <asset image style block>", followed by appearance, proportions, composition, gray background.
- With Midjourney: `<style name> production asset sheet of ...` followed by the Midjourney style block, then appearance, proportions, composition, gray background. When "Style reference" is not "none", put that parameter line after `--ar 16:9`.
- The asset sheet's `Gray background:` matches the gray in this file's "Asset sheet link".
- If you change the style name or the asset image style block, change the asset sheet to match. The owner decides whether approved images are regenerated (a wording change alone does not regenerate).

## Updates

- New time of day, weather or location type: add one row to the variant table.
- The style itself changed (for example from cooler to warmer): change the affected parts, and say in one line in chat which already-generated images and shots are affected.
- No revision numbers or old versions in the file; use version control for history.
