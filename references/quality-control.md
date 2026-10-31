# Quality Control Engine

## When QC runs

Twice: per clip (before it enters the manifest as verified) and on the final
assembly (joins, beginning, ending, total duration, audio continuity).

## Per-clip checklist

- [ ] Character identity matches the identity block (face, eyes, hair/fur,
      clothing, proportions)
- [ ] Facial consistency and readable expressions
- [ ] Anatomy: no extra limbs, fingers, or distorted bodies
- [ ] Natural movement; no impossible physics
- [ ] Object interactions behave (hands hold things, doors open the right way)
- [ ] Background continuity with the previous clip
- [ ] Lighting consistency (time of day, light direction)
- [ ] Camera continuity (position, framing vs the continuity log)
- [ ] Lip-sync: the speaking character's mouth moves with their line
- [ ] Dialogue timing: lines complete, not clipped mid-sentence
- [ ] Audio present and intelligible; music never overpowers dialogue
- [ ] No visual defects: no garbled text, no watermarks, no stray objects
- [ ] No unexpected or unwanted characters
- [ ] Scene transition matches the storyboard

## Assembly checklist

- [ ] Clips in story order, no clip missing or duplicated
- [ ] Total duration matches the request (±0.5s per join rounding, stated)
- [ ] Aspect ratio matches the request on the final file
- [ ] No black gaps, frozen frames, or missing audio at any join
- [ ] Beginning hooks as storyboarded; ending lands as storyboarded
- [ ] Captions (if required) timed, readable, correctly spelled

## Verdicts

- **PASS** — clip enters the manifest.
- **RETRY** — defect is fixable by re-prompting (stronger continuation, clearer
  action, corrected identity block). Counts against the 3-attempt budget.
- **ACCEPT WITH NOTE** — minor variation that does not break the story
  (slight background detail shift). Recorded in the QC report, not hidden.
- **FAIL** — after 3 attempts, or a defect that cannot be fixed by re-prompting
  (e.g. a generation refusal). Recorded in the failed-generation report; the
  project continues without it or with the best acceptable alternative.

## Rules

1. Measure, don't eyeball, duration, resolution, frame rate, and audio
   presence (ffprobe). A clip that fails measurement is not "close enough".
2. Never silently accept a major defect: identity change, teleport, wrong
   ratio, missing audio, garbled on-screen text.
3. The QC report is part of the delivery package. If it is empty of defects,
   say the check ran and passed — do not invent defects, and do not invent a
   report that was not written.

Template: templates/quality-control-template.md.
