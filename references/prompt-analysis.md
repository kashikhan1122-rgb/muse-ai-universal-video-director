# Prompt Analysis

## Goal

Turn one free-form prompt into a production brief without interrogating the user.
Extract everything the prompt already says; infer only what is safe; ask only
about what is genuinely essential and unknowable.

## Extraction checklist

Parse the prompt for each of these. Mark each as GIVEN, INFERRED (with reason),
or MISSING:

1. **Concept and story** — what happens, in what order, with what ending.
2. **Niche and genre** — animal rescue, documentary, comedy, fantasy, etc. Never
   restrict to a list; record what the prompt implies.
3. **Characters** — every recurring person, animal, creature, or animated subject,
   with all visual traits stated.
4. **Locations** — every place, its look, time of day, weather, lighting.
5. **Duration** — exact if stated (60s, 5 min, 28 min). If unstated, infer from
   platform and story weight, and say so.
6. **Aspect ratio** — 9:16, 16:9, 1:1, or other. If unstated: social/short-form
   implies 9:16; documentary/long-form implies 16:9. State the inference.
7. **Visual style** — realistic, animated, stick-figure, cinematic, smartphone-UGC,
   flat illustration, etc. If unstated, choose the style the story's tone implies.
8. **Dialogue and narration** — quoted lines preserved verbatim; narrator voice
   described if given.
9. **Language** — from explicit instruction or from supplied dialogue. Never
   default silently: record the language decision (see audio-and-voice.md).
10. **Camera** — any shot, movement, or framing instruction.
11. **Audio** — music, ambient sound, silence, sound effects.
12. **Captions** — required, forbidden, or unspecified.
13. **Platform** — where it will be posted, if stated; affects ratio and caption
    defaults only.
14. **Constraints and negatives** — anything the prompt forbids (no text, no
    extra characters, no 3D, etc.). These go into every clip prompt's negative
    block.

## Inference rules

- Infer from the prompt's own evidence, never from habit. A cooking video is not
  automatically vertical; a cooking tutorial for YouTube is horizontal, a recipe
  reel is vertical.
- One inference per missing field, stated in one line in the brief. Example:
  "Ratio: 9:16 (inferred — short-form social story, no ratio stated)."
- If two inferences conflict (prompt says "YouTube documentary" and "60-second
  reel"), that is a genuine ambiguity: ask one question, then proceed.

## When to ask (the only cases)

1. Contradictory essentials (two durations, two protagonists, two endings).
2. A story that cannot start without a missing fact (the prompt says "he returns"
   but never says who "he" is).
3. A capability limit that changes the deliverable (e.g. the prompt demands a
   real identifiable person's exact likeness — generation makes a same-style
   version, never a frame-exact copy; say so before generating).

In all three cases: ask one short question, offer concrete options where they
exist, and resume automatically on the answer. Never ask twice about the same
field.

## Output

The production brief (templates/production-brief.md). It is the contract for the
whole production: every later stage reads it, and no later stage re-invents a
decision the brief already made.
