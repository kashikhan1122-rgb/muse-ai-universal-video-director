# Character Consistency

## Principle

There are no permanently fixed characters in this skill. Characters are defined
by the user's prompt, per project. Once defined, a character's identity is
frozen for the whole video — except for story-driven changes the prompt
explicitly requires.

## The character identity block

For every recurring subject (person, animal, creature, animated character),
write one block and reuse it verbatim in every clip prompt:

- Name / identifier
- Face or head structure (shape, proportions)
- Eyes (shape, colour, size, spacing)
- Hair or fur (style, colour, length, texture, distinctive pattern)
- Skin / coat / surface colour and texture
- Distinctive markings (scars, spots, accessories that never leave the body)
- Body proportions and relative size vs other characters
- Clothing (every item, colour, fit, condition)
- Accessories (hat, glasses, bag, weapon, tool — with colour and position)
- Gait, posture, and signature gestures
- Voice identity (if dialogue: tone, pace, accent — see audio-and-voice.md)

Template: templates/character-reference-template.md.

## Character reference sheets

When a character recurs across many clips, or the project is long-form, build a
reference sheet: a front view, a side view, key expressions (neutral, happy,
sad, angry, surprised, determined), and any signature pose. The sheet is a
production aid, not a deliverable the user asked for — include it in the package
only if it was created.

## Rules

1. **Verbatim repetition.** The identity block goes into every clip prompt
   unchanged. Paraphrasing it between clips is how faces drift.
2. **Reference images where supported.** When the generator accepts an image
   reference, pass the character sheet or a prior clip's frame. A reference
   image improves consistency; it does not guarantee it.
3. **Story-driven changes are explicit.** Wet fur, dusty clothing, a torn sleeve,
   an emotional expression — allowed only when the story requires them, and
   written as a temporary change on top of the frozen block, never as a rewrite
   of it.
4. **No accidental additions.** No extra characters, no extra limbs or fingers,
   no changed heights, no swapped clothing between characters.
5. **Check every clip.** Identity is a QC item (quality-control.md). A clip
   where the protagonist's face, clothing, or proportions visibly change is a
   failed clip: retry within budget, else report.

## Honest limit

Generation renders each clip anew. Even with verbatim blocks and reference
images, small drift (eye shape, clothing shade, proportions) can occur. The
skill's job is to minimise drift, catch it in QC, and never claim a drifted
clip is identical to the reference. For a user-supplied real person's likeness,
state before generating: the result is a same-style version, never a
frame-exact copy of that person.
