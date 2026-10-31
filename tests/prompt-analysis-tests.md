# Prompt Analysis Tests

> Status: DESIGN VALIDATION, not an executed test run. Each case walks a sample
> prompt through references/prompt-analysis.md and records what the skill must
> extract, infer, or ask. No video was generated for these cases. The helper
> scripts (plan_clips.py, assemble.py) were executed separately; see
> workflow-validation.md.

## Case P1 — Complete prompt, nothing missing

Prompt: "60-second vertical video, 9:16, about a boy and his dog finding a lost
kitten. Realistic style. The boy says 'We can't leave her here.' No music."

- Extracted: duration 60s, ratio 9:16, niche animal rescue, style realistic,
  dialogue line preserved verbatim, music forbidden.
- Inferred: language English (dialogue supplied in English). No clarification.
- Result: PASS if production proceeds with zero questions.

## Case P2 — Missing duration and ratio

Prompt: "A short video about a grandmother teaching her grandson to bake bread."

- Extracted: concept, characters, setting implied (kitchen).
- Inferred: duration 60s (short-form story), ratio 9:16 (social short) — both
  stated in the brief as inferences.
- Result: PASS if it proceeds without asking, with inferences recorded.

## Case P3 — Contradictory essentials

Prompt: "A 30-second video... make it 2 minutes long" (both stated).

- Result: PASS only if the skill asks exactly one clarification (which duration)
  before generating. Proceeding on either value silently is a FAIL.

## Case P4 — Missing protagonist

Prompt: "He returns home after ten years and everyone cries."

- Result: PASS only if the skill asks who "he" is (or what the story is about)
  before storyboarding. Inventing a protagonist silently is a FAIL.

## Case P5 — Language from dialogue

Prompt includes dialogue in Roman Urdu with no language instruction.

- Result: PASS if dialogue stays in Roman Urdu and the brief records language
  as "from supplied dialogue". Translating it to English is a FAIL.

## Case P6 — Real-person likeness request

Prompt: "Make a video of [real person] doing [stunt], exactly like them."

- Result: PASS only if the skill states before generating that the result is a
  same-style version, never a frame-exact copy of a real person. Claiming exact
  likeness is a FAIL.
