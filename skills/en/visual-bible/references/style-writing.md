# Writing the Style Blocks: Video Style, Asset Image Style and Midjourney

The [Sx] after a conclusion points to [sources.md](sources.md). Items with no tag are the author's judgment from production; adjust them to what you actually generate. The video part uses Seedance 2.5 as the example. Other video models have the same structure; for exact wording follow that model's official guide.

## 0. Set the style profile first (the same for any style)

Any look works: 3D donghua (Chinese 3D animation), 2D anime, thick-paint painterly, ink wash, color comics, live action. All follow the same method. The style name is only a label. A model tells styles apart by visible practice. A third-party casting-lookbook skill writes a style as a fingerprint of "technique, material, edge, color" plus "form language" [S13]. Atlas Cloud also advises that 2D anime use concrete wording such as outlines and flat color in place of "cinematic" [S14]. At project start, the owner and you settle five items and write them into the one-line style, the asset image style block and the video style block:

| Item | What to write | Example: 3D donghua | Example: 2D cel animation |
|---|---|---|---|
| 1 Style name (main anchor) | Medium plus style, one main anchor | 3D donghua animation | 2D Japanese animation, cel shading |
| 2 Form language | Head-to-body tendency; eye size and shape; how nose and mouth are simplified; hair in clumps or strand by strand; how far skin is rendered | Slender proportions; eyes slightly larger than real, nose bridge kept; hair in volumetric clumps; fine skin, no pores | Big eyes, nose done in one stroke; hair in large chunks; no skin texture |
| 3 Line and shading | Outlines or not, line weight; flat color, cel shading, thick paint or realistic rendering; how many shadow layers, hard or soft edges | No outlines, soft gradient shading | Clean black outlines of even weight; flat color plus one or two layers of hard-edged shadow |
| 4 Materials | How skin, cloth, metal and hair appear in this way of drawing | Cloth with visible weave, metal with small-area highlights | Cloth shown only with fold lines, metal as a single highlight color |
| 5 Negative anchor | One sentence pointing at the direction that drifts most easily | Not live action | Not a 3D render, no volumetric light and no soft gradient shadows |

- Light is not part of the style profile. Light is written in "Light" and "Time and weather variants", and asset images use even light on gray.
- Seedance 2.5 leans realistic by default [S4]. For non-realistic styles, write items 2 and 3 as specifically as you can, and point item 5 at realism or 3D.
- Whether item 2 helps for 3D donghua has not been compared yet. Take one character and make one image with the sentence added to the asset image style block and one without. If it helps, write it into the project.
- The 2D cel animation column in the table is a writing example, not tested by the author. The first time you use a new style, follow section 4C.

## 1. Video style block (Seedance 2.5 as the example)

### Where it goes

- The official basic structure: a one-sentence overview "subject + place + event + genre/style", then shots, and at the end a supplement of visual detail and atmosphere that runs throughout [S1]. The style block goes in the first sentence of the prompt, and the light and tone relationship is written once more in the "keep consistent" part.
- The official prompt optimization skill's template writes "the picture presents <visual style or mood>", and for long prompts it requires "compress repeated style words and repeated constraints", with no word limit [S2]. So the style block is written once per prompt, not repeated in shot lines.
- Length: the author set two or three sentences, about 40 to 80 words. The official guide gives no number.

### What to write

1. Medium and style name (style profile item 1), for example `3D donghua animation style`. The wording in official examples includes "top-tier 3D guoman xianxia" (3D Chinese animation, immortal-hero fantasy), "3D guoman CG xianxia style" and "3D guofeng comic" [S1][S3].
2. Form and shading (style profile items 2 to 4; pick the one or two that best tell this style apart): for example slender CG proportions or chibi (head-to-body numbers go in the asset sheet, not in the style block), outlines or not, skin and cloth texture.
3. One negative anchor line (style profile item 5).
4. Color tendency: main tone + skin protection, one sentence.
5. Light baseline: has a source, soft or hard, shadows.
6. The line for the current time of day and weather (from the variant table), joined at the end.
7. Photographic texture (optional): lens inertia, motion blur, depth of field, atmospheric perspective, written as something visible ("the camera has real inertia and a slight handheld feel, with correctly directed motion blur at high speed"). Reference works can be used to communicate, but in the prompt they must be broken down into visible conditions like these.

Do not write: color value codes. Quality and engine words such as "8K" or "UE5" may be added at the end.

### Write the render style and the combat staging style separately

Fight prompts circulating online often mix "semi-realistic 3D animated film feel" (render) with "Japanese anime sakuga combat staging" (performance) in one sentence, then pile on UE5, 8K, masterpiece, ultra-detailed [S12]. Split them:

- **Render style** (what it looks like): this is the video style block, one main anchor plus one or two supporting words, unchanged across the film. English anchor words (anime cinematic CG) carry no more information than the equivalent wording in your own language. Write the block in the same language as the rest of your prompts; do not mix.
- **Combat staging style** (how it performs): perspective, fast/slow contrast, key-frame poses, camera follow. This belongs to action and camera, and goes in the optional "Combat staging style" section of the template. Attach it after the style block only for fight and ultimate-move shots. Write Japanese-style "sakuga" as what it means on screen, not as the word.
- **Quality words and engine names** (UE5, 8K, PBR, masterpiece): outside sources disagree. The official prompt optimization skill does not add them on its own; Segmind and Venice say they do little; third-party fight samples that came out well almost all include them [S12]. There is no side-by-side test. You may add them at the end of the style block, but they do not replace visible description, so still write the five items of the style profile.

### When the reference image and the text style conflict

- The official prompt optimization skill's mapping priority: user's explicit instruction > prompt description > asset content > file name > upload order [S2]. This is a priority for asset roles, and does not guarantee that text can beat the reference image's look.
- Official 2.5 examples include wording such as "the generated video's color temperature, light and brightness reference the characters and scene in the image" and "the light and filter of reference image 1" [S1]. A reference image carries its light and tone into the result.
- The 2.5 release notes say the image quality direction is "closer to the cinematic texture of live shooting" [S4]. From this I conclude that 2.5 leans realistic by default, so non-realistic styles must be stated in the style block and supported by the style of the asset images themselves.

So: **the reference image leads, the text supports.** Make all asset images with the same asset image style block, and go to video once the style is consistent. The style block states the style name. Gray-background asset images do not carry light; light comes from the style block and the variant line.

## 2. Asset image style block (any image model)

Asset images (costume and look images of characters, scenes and props) can be made with GPT Image, Midjourney or another image model. Paste the style block as is into the "style" line of the prompt.

### How image models read a prompt (GPT Image as the example)

- The prompt structure of OpenAI Codex's official imagegen skill: purpose -> input images (say what image 1 and image 2 each do) -> subject -> style/medium -> composition -> light -> color -> materials -> constraints/avoid. It asks you to "write short and add only details that really help the result" [S11].
- With several input images, say each one's role by number. When editing, say "change only X, leave the rest", and repeat the unchanged items every round [S11].

### How to write it

- One or two sentences, starting with the style name (such as `3D donghua CG style`), followed by the style profile's form, line and shading, and materials. The default texture wording assumes 3D and live action; for 2D, line art and ink wash, write one more block, `## Asset image texture`, and use it in place of the texture description when making images. Its content corresponds one to one with the Midjourney block (if written); do not start a different style.
- Do not write time of day, weather, ambient light or tone filters. Asset images are even light on gray, and these words tint the background and the characters.
- Do not write color values (the gray background is written once in the asset sheet) or parameters.
- Style sample: make one image with the asset image style block. After the owner approves it, use it as the style reference image for later asset images (in the prompt's "reference image" line write "use for: render and materials; do not take: character, clothing, composition").

## 3. Midjourney style block (optional)

Write it only when you use Midjourney for asset images. The heading is `## Midjourney style`.

### Versions and features (official, read 2026-10)

- V8 alpha 2026-03-17; V8.1 released 2026-04-14; V8.2 has been the default version since 2026-07-24 [S5][S6].
- V8.1/V8.2 support: Style Reference, Style Weight, Style Reference Codes, Image Prompts, Personalization, Moodboards, Raw, Stylize. Not supported: Omni Reference (`--oref`), Multi-Prompting, the Quality parameter, Draft Mode. V8.2's Edit Model replaces Omni Reference, Character Reference and Retexture [S6].
- V8 follows long, specific descriptions better; `--raw` removes the default stylization and follows the text more closely [S5][S6].
- `--sw` ranges 0 to 1000, default 100. A style reference takes only the overall style (color, medium, texture, light) and does not copy objects or people. Keep the text prompt simple and avoid style words that conflict with the reference image [S7].

### How to write it

- One English block for render and materials: start with the style name (such as `3D Chinese animation (donghua) CG style`), followed by the style profile's form, line and shading, and materials.
- Do not write time of day, weather, ambient light or tone filters.
- Style reference: first make one sample with the style block. After the owner approves it, use it as the `--sref` image. An image link is more durable than a style code: a third-party article says numeric style codes are bound to the algorithm version that produced them [S8]. Start `--sw` at 100. The sample's colors may bleed into the gray background, so when checking images, see whether the gray is still the one in the asset sheet.
- Parameters (`--ar 16:9`, the style reference line) all go at the end of the prompt. Do not write parameters in the style block.

## 4. Example: common descriptions for a 3D donghua look

| Aspect | Plain wording (video and asset image style blocks) | Midjourney wording |
|---|---|---|
| Style name | 3D donghua animation style; 3D donghua CG | 3D Chinese animation (donghua) CG style |
| Characters | Slender CG character proportions; refined facial features | elongated CG body proportions, refined facial features |
| Skin | Fine, slightly translucent skin, not plastic-smooth | refined skin shading, subtle subsurface scattering |
| Cloth | Cloth with visible weave and thickness, silk with a soft sheen | visible fabric weave, soft silk sheen |
| Light | Soft light with a clear source (video block only) | soft directional light (samples only, not in the asset style block) |
| Render | Clean, refined image | clean sharp render, no film grain |

Third-party tutorials often use combinations such as "3D realistic rendering with guoman xianxia aesthetics" and "CG rendering, cinematic light" [S9]. Of these, "8K ultra HD" and "ultimate quality" do not change the image and are not adopted. The English words in the table are the author's wording and have not been tested at scale.

## 4A. A few general rules for style blocks

- **One main anchor plus one or two supporting words.** "3D donghua animation style" or "period live-action film style" is the main anchor; after it add only one or two texture words. With more words the image tends to turn generic [S14].
- **One negative anchor line.** After the main anchor add one "not X" sentence. For 3D write "not live action"; for live action write "not a 3D render, no CG plastic feel". Write only one line and do not expand it into a list (some advise using only positive wording; the two views conflict, so only one line is kept).
- **Do not mix words from different looks.** A 3D block does not mention live shooting or film grain; a live-action block does not mention CG, rendering or donghua; a 2D block does not mention volumetric light, subsurface scattering or realistic skin.
- **Light-and-color samples (optional).** For each main variant, make one image with the scene asset that includes light, and use it as a reference image in the video prompt, writing "use only for color temperature, light and brightness; do not take characters or composition". The official 2.5 example uses one such "color temperature, light and brightness reference image" [S1]. Gray-background asset images stay as they are; the sample is made separately. Effect still to be tested.
- **Compare with the approved sample, not with the previous episode.** At each episode's increment, compare against the sample approved at project start to see whether the look has drifted. Otherwise it slowly slides a little each episode.

## 4B. Example: live-action realism

Use this set when the owner has chosen live action; the rest of the structure is unchanged:

- Style name: for example "period live action". Write the one-line style as "period live-action film style, realistic photographic texture".
- Materials: write skin down to real pores and slight color variation; write cloth, metal, wood and stone as real objects.
- Camera texture: may have fine film grain and soft highlight roll-off; by default write only "film stock texture" and no film format. When the owner asks by name for a strong cinematic texture, this is an exception to "only one or two texture words after the main anchor": you may add a block of texture words (anamorphic feel, film grain, slight halation, very shallow depth of field, low saturation with just a touch of warm color), and a sound block that lists only on-set sounds (list each sound wanted, and say no music, narration or subtitles). The texture words go in the video style block, not in asset images. Do not add them for non-realistic styles.
- Asset image style block: write it like a costume still or production still ("period costume still, natural soft light, real skin texture").
- Video style block example:

```text
Period live-action film style, realistic photographic texture, not a 3D render. Real skin with visible pores, fine film grain, soft highlight roll-off; a single main light with a source, shadows keep texture.
```

Basis: the Seedance 2.5 official guide's example "period mystery fantasy live-action film style, cinematic realistic texture" [S1].

## 4C. The first time you use a new style

For styles other than 3D donghua and live action (2D anime, thick paint, ink wash, color comics, clay...), the first time:

1. Settle the style name and references with the owner (film titles or images; take only the way of drawing, not characters or plot).
2. Search online for recent examples and wording of this style made with your video model and image model. Fill in the five items of the style profile, and record the sources in sources.
3. A starting point you can borrow: the casting-lookbook anchor library has fingerprints for ink wash, thick paint, line art, watercolor, clay, anime-style 3D and other styles [S13]. Pick the closest as a starting point (it was tested once with gpt-image-2, so re-verify in your project). A method you can borrow for color comics: assign color by part (large main color, contrast color, small accent color), let outlines carry structure and color areas carry the big relationships, and write non-natural-colored shadows as paint color areas, not as colored lamps shining on them [S13].
4. Verify: make one costume image with the asset image style block and one low-resolution short clip with the video style block. Use them in batch only after the owner approves. If not approved, change items 2, 3 and 5 and try again.
5. One more thing changes with the style: the asset image texture (the optional template block).

## 5. Differences between Seedance 2.0 and 2.5

- Aesthetic difference: 2.5 and 2.0 differ a lot in aesthetic preference. The same reference images and prompt produce clearly different looks, and mixing them is not continuous. To keep the 2.0 look in 2.5, the official advice is to give the 2.0-generated video as input to an extension task and choose MOV as the output format [S1]. Rule: use one model per scene.
- Reference limits: 2.0 all-modal reference is 0 to 9 images, 0 to 3 videos, 0 to 3 audio clips; 2.5 is 0 to 30, 0 to 10, 0 to 10 [S10].
- Aspect ratio: 2.0 has only 6 fixed options; 2.5 supports any ratio in [0.4, 2.5] [S1]. 16:9 works in both.
- 2.0 drifts toward realism more often: a realistic reference image with no emphasis on style drifts into live-action realism. Add style constraint words, or first convert the reference image to the target style [S3].
