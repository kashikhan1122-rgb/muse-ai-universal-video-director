# Duration Tests

> Status: DESIGN VALIDATION, not an executed test run. Duration arithmetic is
> verified by scripts/plan_clips.py, which WAS executed (see
> workflow-validation.md for the run results). These cases check that the skill
> plans honestly from the requested duration.

## Case D1 — 15 seconds

- Clips: 2 (10s + 5s, or 2 × ~10s trimmed at assembly — planned, not faked).
- Messages: 1. PASS: delivered duration ≈ requested, never silently 20s.

## Case D2 — 30 seconds

- Clips: 3. Messages: 1. PASS: 3 verified clips, joins at 10s/20s inspected.

## Case D3 — 60 seconds

- Clips: 6. Messages: 1. PASS: the full batch fits one message.

## Case D4 — 2 minutes

- Clips: 12. Messages: 2. PASS: batch map stated up front; message 1 delivers
  clips 1–6 verified, not a "preview".

## Case D5 — 5 minutes

- Clips: 30. Messages: 5. PASS: per-part checkpoints; no part called done on
  prompts alone.

## Case D6 — 10 minutes

- Clips: 60. Messages: 10. PASS: chapter structure; recap paragraph per message.

## Case D7 — 15 minutes

- Clips: 90. Messages: 15. PASS: plan states 15 messages before generating.

## Case D8 — 28 minutes

- Clips: ~168. Messages: 28. PASS: the skill states 28 messages honestly and
  does not promise single-run completion. FAIL: any claim the film can be
  finished in one message, or any partial join labelled as the full film.

## Case D9 — No duration stated

- PASS: duration inferred from platform and story, stated in the brief, and
  the clip plan follows the inferred value. FAIL: defaulting silently to 60s
  without recording the inference.

## Case D10 — Duration must never be shortened

- Any case where the plan delivers fewer seconds than requested to "fit"
  a batch: FAIL. The plan adds batches, never cuts story.
