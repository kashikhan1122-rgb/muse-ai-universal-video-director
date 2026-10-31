# Storyboard System

## Purpose

The storyboard is the plan that makes clip generation deterministic. A generator
cannot see the whole video; the storyboard is how each ~10s clip knows exactly
what it must contain.

## What a storyboard contains

For the project overall:

- Logline (one sentence)
- Story structure (acts or beats, with timecodes)
- Character list (names + identity-block references)
- Location list (with environment-block references)
- Audio plan summary (dialogue, narration, music, silence)

For every scene (a scene may span one or more clips):

- Scene number, timecode range, location, time of day
- Story beat: what changes in this scene
- Characters present, with positions and relative placement
- Facial expressions and eye direction per character
- Body, hand, and leg movement per character
- Object interactions (what is picked up, opened, broken, handed over)
- Environment and background detail visible in frame
- Camera: angle, distance, movement, framing
- Lighting and composition notes
- Transition into the next scene
- Dialogue / voiceover / sound effects with timing
- Clip split: if the scene exceeds ~10s, where it splits and what each clip
  covers, including the exact handover action at the split

## Frame-level planning

For complex or high-stakes moments (a reveal, a reunion, a stunt, a product
transformation), plan at frame level: the first frame, the key action frames,
and the final frame of each clip. The final frame matters most — it becomes the
next clip's reference (see clip-continuity.md).

## Storyboard reference images

Generate storyboard reference images when they genuinely help:

- Recurring characters whose look must survive 6+ clips
- Complex locations (a room layout, a street, a workshop)
- A signature object that must stay identical

Do not generate storyboard images when a precise text storyboard is clearer,
when the project is a single short clip, or when image generation is
unavailable. A text storyboard is a complete deliverable on its own.

## Storyboard → clip prompt mapping

Every clip prompt is built from the storyboard, never improvised:

```
[Style block — from brief, verbatim]
[Character block(s) — from character reference, verbatim]
[Environment block — from environment reference, verbatim]
[Camera — from storyboard scene]
[Action — from storyboard scene, this clip only]
[Dialogue — quoted lines for this clip only, if any]
[Audio — music/ambient/silence for this clip]
[Negative block — from brief, verbatim]
```

If a clip prompt omits the character or environment block, that is a defect in
the plan, caught before generation — not after.

## Template

See templates/storyboard-template.md. Copy it per project; do not reuse another
project's storyboard.
