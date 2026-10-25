---
name: action-physics-choreography
description: Action physics and choreography. Use when a script or AI video prompt has complex action such as fights, chases, throws, weapons, group battles, falls from height, or people interacting with animals or monsters. Turns a line like "the two fight fiercely" into a visible process chain (setup, contact, result, force direction, landing point) and gives beat-by-beat wording and camera cooperation that an AI video model (Seedance 2.5 as the example) can execute. It does not decide who wins, the plot, or effects details.
license: MIT
metadata:
  version: "0.1.0"
---

# Action Physics and Choreography

Fights in AI video fail in three common ways: the punch passes through the body, nobody moves after the hit, or two people hold their poses and wait for each other. The cause is almost always the prompt. It says "an intense exchange" or "one punch sends him flying". The model gets only the start and the ending, and invents the process itself.

This skill breaks action into a cause-and-effect chain the model can execute: **who starts from where with which hand → what part of the opponent it touches → where the opponent is pushed back, where they land, and what stops them**. It comes from the rework records of several hundred fight shots made over half a year of AI comic-drama production, plus general craft from the action-design industry. The video wording uses Seedance 2.5 as the example. The principles apply to other video models too.

## When to use it

| Use | Do not use |
|---|---|
| Throws, grappling, weapons (including handoffs and disarms), real contact between two or more people, height differences and falls, people interacting with animals or monsters (pounce, grab, lift, ride, fling), actions limited by injury, parts of a group battle, chases, chibi-style exaggerated fights | Walking to a mark, turning the head, handing over an object, sitting down; simple actions the script already makes clear |

## Input

The original action text for the current scene; the participants, their abilities and injuries; the body size and relative height of the characters (required reading for people-and-animal interaction; if a visual bible exists, take its "scale baseline"); the location layout of the scene; and, when continuing from the previous video, the last frame of the previous clip. If the injured side, a size, or a direction is missing and would change the action, list the gap. Do not invent it.

## What it does not handle

Who wins and where they end up, injury facts, character arcs, dialogue locked by the author, shot size and camera plan, and how effects spread and fade. How the fight is played (who strikes first, which move, what terrain is used) can be redesigned. See section 19 of [body-and-contact.md](references/body-and-contact.md).

## Two output formats

**When writing a script: a process-chain passage.** Write one natural paragraph in this order: preparation → contact (what grabs, what steps on what) → force → center of gravity → path → inertia → result of the force → aftermath (hair, clothing, props). It directly replaces the original action sentence. A charging character does not stop to wait for a line of dialogue. A character who is able to save the situation must act effectively.

Put `[Action passage]` at the head of the passage so it can be checked. Remove the marker when writing it back into the script. Leave no blank lines inside the passage.

**When writing a video prompt: beat-by-beat action blocks.** One block for each action beat:

```text
[Action] <name> | clip <N>s | beat <k>/<M>
Setup: <who, which hand or foot, where the force builds> (one sentence)
Contact: <which body part touches which part of the opponent> (one sentence)
Result: <how the struck side moves, where they land, what posture, what is left on the ground, what steadies them> (one sentence)
Impact: <light / heavy / finisher> | Environment: <how the force travels out: feet → ground → nearby objects> | Shake: <small jolt / clear shake / violent shake / none>
Force direction: <from frame X toward frame Y / backward and upward>
Camera: <cut: split into 2-3 short shots, give shot size, camera move and subject for each; or one continuous take: one line per exchange, giving the camera move and the shake level>
```

One beat = setup, contact, result. A "clip" is the length of one generated video. The "Impact" line only sets feedback strength. In the prompt, write only the feedback that can be seen, never labels such as "heavy" or "finisher". The action block is a design draft. In the final prompt, merge the three sentences into the camera description and drop the labels.

For examples see [action-templates.md](references/action-templates.md).

## Action types

| Type | Must write | Most common failure |
|---|---|---|
| Bare-handed | Supporting foot, striking side, the body part that lands, the recovery after the hit | Fist passes through the body, nobody moves after the hit |
| Weapon | "Holds the sword with both hands" goes into the subject; blade line direction; one kind of attack (only chop or only thrust) | Weapon disappears, deforms, changes hands |
| Throw | Grip point → break the balance → one kind of force (swing / back throw / trip) → landing order | Flies without being grabbed, landing point has no source |
| Chase | Each side's direction, who is faster, terrain obstacles | Background moves but the person does not, the lead turns into slow motion |
| Fall from height | What support is lost → fall → which body part lands first → resting posture | Falls from nowhere, changes direction in the air |
| People with animals or monsters | Relative height (write numbers); the specific body part grabbed or lifted; who bears the weight | Scale drift, hand sinks into the fur, the animal shrinks |
| Group battle | Only one pair in main contact per beat; everyone else does one thing each | Everyone brawls at random, cloned people, clipping through each other |
| Chibi exaggeration | Mark the entry and exit; exaggerate with deformation and pauses, not extra moves | Proportions do not switch back, too many moves in the chibi part |

For the full list of how the body moves see [body-and-contact.md](references/body-and-contact.md).

## 14 rules for writing to the video model

For the basis and the original wording see [seedance-rules.md](references/seedance-rules.md) and [sources.md](references/sources.md).

1. **Cause before effect.** Write setup → contact → result in full. Do not give only the start and the ending. If you give only both ends, the model invents the process.
2. **Beat length follows the action.** A beat is an action, not a shot. One beat can be cut into several shots, the shortest about 0.25 seconds. One time segment, one main action. In fights and effect chains you can write 2-3 in a row. In everyday shots, one shot does one thing.
3. **A hit must show the receiver.** The receiver is the frame subject, the camera is front or side, and the shot starts on the contact. Write it as displacement with a before and after. A charge does not stop before contact to wait for a line.
4. **Be specific about direction.** "A horizontal slash from frame right to the left", and keep the direction locked and consistent for the whole passage.
5. **State the intent.** Attack or defense. Writing only "does not dodge or block, raises a palm" makes the model add a shield.
6. **Fast actions blur.** Allow motion blur only on the fastest instant, and write "face, hands, and weapon are sharp again as soon as the action ends". Use simple moves.
7. **Multi-person contact is a weak point.** One pair of contact per beat. Before contact, write the distance between the two and which hand each uses.
8. **Slow motion is only for the deciding beat.** Mark its entry and exit, and write that everyone else "stays at normal speed". If you do not mark it, the lead alone plays in slow motion. A whole-clip slow motion where everyone in the shot has the same speed is the exception.
9. **The camera moves with the event.** The camera move is triggered by the action ("as the blade falls, the camera tilts down quickly to follow the blade tip"). One shot can combine moves, written in order.
10. **Do not stack result words.** Replace "fiercely" and "tremendous impact force" with body part, direction, displacement, landing point.
11. **Write continuation in the progressive tense.** When continuing from the previous clip, write "is sliding half a step to the left". Do not write it as a new move. Otherwise the model replays it or stutters.
12. **Write results down to the marks and the way they stop.** "Slides back three steps, boot soles plow two grooves, braces against a stone pillar and steadies". Strength comes from the difference in displacement ("backs off five steps" against "slides back three steps"), and from two reactions to the same hit ("A kneels, B does not move").
13. **Some light, some heavy, each with a purpose.** Contact is light, heavy, or finisher, and most of it is light or heavy. The camera shakes along the force direction only at the instant of contact, and some beats are left without shake. Give every hit a purpose (block the path, force the opponent to change direction, interrupt a charge-up).
14. **Force comes from timing contrast and the receiver.** Slow charge-up, fast strike, large reaction from the receiver, and the attacker also takes recoil. A near miss leaves small evidence (a lock of hair cut off). Open in the middle of the exchange. The recoil is the setup of the next move. Write by three things (the action, the camera path, the reaction around it), and also check by those three things.

## Differences in Seedance 2.0

A 2.0 clip is 4-15 seconds. Split a two-person exchange into one shot for the attacker, one for the hit, one for the counter, and split into as many clips as you can. About 5 seconds per beat, one main move per clip. Motion is sharper, but fists passing through the target are common, so write the hit as its own shot.

## Self-check

1. Every action beat has the three sentences setup, contact, result, in that order. Key contact beats pass the "seven questions" (section 19 of body-and-contact).
2. Every beat states the force direction, and the direction is consistent with the lock for the whole passage.
3. The struck side is the subject of the hit shot, is visible, and the shot starts from the contact. It has displacement and a landing point. A charge does not stop before contact. The setup is written only once.
4. The weapon is written into the subject. The holding hand and the blade line never change. A handoff shows both people gripping at the same time, then one lets go.
5. People-and-animal interaction states the relative height and the weight-bearing point.
6. The injured side bears no weight and does not use full force, and the compensation can be seen.
7. No result words without a process. Results are written down to displacement, marks, and the way they stop. Contact is a mix of light and heavy, and shake happens only at the instant of contact.
8. Slow motion and chibi both have an entry and an exit marker.
9. Run the check script on the design draft and get no errors (it only checks the writing, not whether the physics is reasonable):

   ```bash
   python3 scripts/validate_action_text.py design-draft.md            # checks [Action] and [Action passage] blocks
   python3 scripts/validate_action_text.py script-excerpt.md --prose   # also checks untagged body paragraphs
   ```
