# Aspect Ratio Tests

> Status: DESIGN VALIDATION, not an executed test run. Ratio verification is
> performed by scripts/assemble.py (ffprobe measurement), which WAS executed
> on synthetic clips (see workflow-validation.md). These cases check that the
> skill requests, measures, and honours ratios honestly.

## Case R1 — 9:16 vertical, stated

- Every clip prompt states vertical 9:16 first. Every clip measured 720x1280
  (or the generator's true 9:16). Final file verified 9:16. PASS.

## Case R2 — 16:9 horizontal, stated

- Same discipline, 1280x720. A vertical clip in a horizontal project is a
  failed clip, regenerated — never rotated, stretched, or blur-filled. PASS.

## Case R3 — 1:1 square, stated

- Square staging planned from the start (centred subjects, no lateral action
  that a square frame would cut). PASS.

## Case R4 — Ratio not stated, social short

- Inferred 9:16, stated in the brief. PASS if inference is recorded; FAIL if
  the skill silently picks a ratio and never says so.

## Case R5 — Ratio not stated, long documentary

- Inferred 16:9, stated in the brief. PASS on the same condition as R4.

## Case R6 — Generator returns the wrong ratio

- Example: prompt says 9:16, clip arrives near-square.
- PASS: clip is regenerated natively in true 9:16. FAIL: the clip is
  stretched, blur-filled, black-barred, or side-cropped and presented as
  native 9:16.

## Case R7 — Mixed ratios in one project

- Any project delivering clips in two different ratios: FAIL, unless the
  storyboard deliberately plans a ratio change (extremely rare) and the
  delivery explains it. The default is one ratio for the whole video.
