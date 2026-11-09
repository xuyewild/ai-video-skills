# Seedance 2.5 before/after: 16 prompt fixes

English | [中文](seedance-2.5-改前改后.md)

While making an AI comic drama, I took the first cut of one episode apart shot by shot. Of 197 shots, 158 were 1 to 2 seconds long and 123 were locked-off. Then I ran 5 rounds of controlled tests on Seedance 2.5, changing only a few lines each round and checking whether the output changed.

Each fix below shows what I wrote, what came out, and what I write now. Results come in three grades:

- **verified**: after the change, the output actually changed.
- **one case**: tried once.
- **not re-tested**: I write it this way now, but haven't run a side-by-side.

Characters and settings in the examples are generic. The quoted prompt lines were originally in Chinese and are translated here.

## 1. Pacing

**1. Don't split one scene into too many clips**
- Before: one scene generated as 11 separate clips, about 8 seconds each.
- Result: cut together, it breaks at every seam. Audio also fades in at the start of each clip; the first second was under 30% of mid-clip volume in all 11.
- Now: fewer clips per scene, more shots inside each clip.

**2. Vary shot length**
- Before: 158 of 197 shots were 1 to 2 seconds.
- Result: no lingering, no real fast cutting either. Flat rhythm.
- Now: any shot that needs an expression gets at least 2 seconds. 1-second shots are for hands, props and empty frames.

**3. No camera move on a 1-second shot** (verified)
- Before: `camera tilts down from face to feet`, given 1 second.
- Result: a row of boots. You can't tell who it is.
- Now: 1-second shots are locked-off.

**4. Don't pack a shot with actions**
- Before: 6 actions written into 2 seconds.
- Result: the model played one or two, slowly.
- Now: one thing per shot for everyday action, two or three chained moves max in a fight.

## 2. Effects

**5. Don't write "beam of light"** (verified)
- Before: `a line of light slashes across`. "Edge line", "thin line" and "blast beam" do the same.
- Result: a thin laser with no weight.
- Now:

```
Describe the energy's thickness, volume and layers of material (flame, molten glow, sparks, debris). Size it against something in the scene. End with: not a thin laser line.
```

- After: the slash had thickness and flaming debris, and the direction was right.

**6. Don't give an energy ball a "shell"** (not re-tested)
- Before: `outer shell + bands around the sphere`.
- Result: a red energy ball rendered as a smooth glass marble.
- Now: `no solid shell, edges constantly spilling and curling outward`, plus something in the scene for scale.

**7. Colored light stains white** (not re-tested)
- Before: red energy lighting a character dressed in white.
- Result: the whole character turned pink.
- Now:

```
The red light only reaches the nearby rain and clouds. The white clothing stays pure white, with only a narrow red rim light on the edge.
```

**8. Check new symbols against clichés**
- Before: `a dark red halo`.
- Result: an angel's halo.
- Now: change the shape, or drop it.

**9. Put attack or defense in the verb** (not re-tested)
- Before: `doesn't dodge, doesn't block, raises his right palm` with a blast incoming.
- Result: the model gave him a shield nobody asked for.
- Now: `raises his right palm and swings a strike`.

## 3. Impact

**10. The thing being hit has to be in the shot** (verified)
- Before: the impact shot only framed the mountain; the giant being hit was out of frame.
- Result: the slash hit the mountain.
- Now: whatever gets hit is the subject of that shot. After the change, the giant is in frame and the contact point bursts into flame.

**11. A giant cut in half won't move, three ways** (failed 3 times)
- Before: a giant mech sliced through the waist, top half sliding off. Written as a step-by-step process, as its own impact shot, and as "already in two pieces".
- Result: all three, it stands still with a glowing line on it.
- Now: stop fighting the prompt. Either give "top half slides off" its own short clip with nothing else in it, or change the design so it explodes or crumbles.

**12. Two giants share a frame once** (failed 3 times)
- Before: two giants on opposite sides of a bay, "across the whole bay" written into every shot.
- Result: the establishing shot gets the distance right. Any later shot with both puts one right behind the other.
- Now: establish the distance once, then shoot them separately.

**13. Big things need small things next to them** (verified)
- Before: the slash in flight shot as a wide side-on view with nothing for scale.
- Result: it doesn't look big.
- Now: low camera, close to something small (rocks, sea surface), the slash passing overhead, sparks landing on the rocks.

## 4. Acting

**14. Give a cold expression at least 2 seconds** (one case)
- Before: `corners of the mouth turn down` in a cold scene.
- Result: the character kept smiling, as if the reference image's smile carried over.
- Now: `not smiling, lips pressed flat`. It worked in a 3-second shot; the same line in a 1-second shot went back to a closed-eye smile. My read: 1 second isn't enough to perform.

**15. Write big emotions in the body, not just the face** (verified)
- Before: `smile collapses, clenches teeth, turns head`.
- Result: a flat, level stare.
- Now: body moves, like the whole head snapping away and the shoulders dropping. After the change, it went from smile to frown to looking away, the whole arc.

**16. Write a reaction for whoever is listening** (verified)
- Before: only the speaker was written.
- Result: listeners stood blank-faced, sometimes cropped out.
- Now: one concrete reaction per listener, like "a corner of the mouth lifts, chin goes up".

## Bonus: the action block template

[action-physics-choreography](../skills/en/action-physics-choreography/SKILL.md) writes action in blocks like this. This is the shortest version; the full one adds impact level, environment and camera. One block per action, and Setup, Contact and Result are all required:

```
[Action] <name>
Setup: <who, which hand or foot, where the force builds>
Contact: <which body part touches which part of the opponent>
Result: <how the one hit moves, where they land, in what pose, what is left on the ground, what steadies them>
Force direction: <from frame X toward frame Y>
```

Write only the start and the end, and the model makes up the middle.

---

If you got different results, open an issue with the model version, your exact prompt line, and what came out.
