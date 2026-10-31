# Workflow Validation — All 12 Master-Instruction Scenarios

> Status: DESIGN VALIDATION, not an executed production run. Each scenario
> below walks the skill's pipeline (SKILL.md + references) against one of the
> 12 scenarios required by master instruction section 23, and records the
> checks the skill must pass. **No video was generated for these scenarios,
> and no scenario is claimed to have been executed.** The only executed tests
> in this skill are the helper scripts, whose real run results are recorded
> at the end of this document.

## Validation checklist (applied to every scenario)

For each scenario, verify the skill:

1. Understands the prompt (prompt analysis, no interrogation).
2. Imposes no fixed duration or aspect ratio.
3. Imposes no fixed niche or style.
4. Creates a suitable production structure (not a forced scene count).
5. Maintains character consistency (verbatim identity blocks).
6. Maintains environment consistency (verbatim environment blocks).
7. Plans clip continuity (final-frame reference + continuity log).
8. Uses the Muse AI workflow only (no other platform).
9. Handles failures properly (max 3 retries, then report and continue).
10. Produces an appropriate final deliverable plan (video + package, only
    files actually created).

## Scenario results (design walkthrough)

### TEST 1 — 30-second vertical animal rescue video
- 3 clips, 1 batch, 9:16, realistic or as prompted. Hook in first 3s.
- Checks 1–10: PASS by design (see examples/short-video-example.md).

### TEST 2 — 60-second realistic family storytelling video
- 6 clips, 1 batch, realistic style (not cinematic by default), dialogue
  preserved, family characters with identity blocks.
- Checks 1–10: PASS by design.

### TEST 3 — 5-minute fantasy story
- 30 clips, 5 batches. Fantasy world block (creatures, magic rules, palette)
  repeated verbatim; chapter structure; magic effects kept consistent.
- Checks 1–10: PASS by design. Limitation noted: fantastical physics are
  generation-dependent; impossible motion is a QC failure, not a feature.

### TEST 4 — 10-minute documentary
- 60 clips, 10 batches, 16:9, episodic chapters, narration script timed to
  chapters, no staged drama (see examples/documentary-example.md).
- Checks 1–10: PASS by design. Limitation noted: factual claims come from
  the prompt only; the skill invents no statistics.

### TEST 5 — 28-minute long-form video
- ~168 clips, 28 batches. Honest message count stated up front; resumable
  state in project files; per-part checkpoints.
- Checks 1–10: PASS by design, with the explicit limitation that Muse AI
  cannot complete this in one run or unattended — it requires 28 user
  messages. Any claim otherwise would be a FAIL.

### TEST 6 — 16:9 horizontal educational video
- Ratio 16:9 throughout; lateral staging; diagrams/objects described as
  visuals, not as on-screen text unless the prompt wants text.
- Checks 1–10: PASS by design.

### TEST 7 — 9:16 short-form animation
- 6 clips, 1 batch, animation style block, no on-screen text if forbidden.
- Checks 1–10: PASS by design (see examples/animation-example.md).

### TEST 8 — Video with multiple recurring characters
- One identity block per character, all repeated verbatim in every shared
  clip; relative sizes tracked; no clothing swaps between characters.
- Checks 1–10: PASS by design. Limitation noted: with 3+ characters, drift
  risk rises; QC per clip is mandatory, not optional.

### TEST 9 — Video with no dialogue
- Sound design carries the story (ambience, music, or silence as planned).
  No dialogue invented to "fill" silence.
- Checks 1–10: PASS by design.

### TEST 10 — Video with complex dialogue and voiceover
- Dialogue lines quoted verbatim, one speaker per clip where possible,
  narration timed to visuals, no mid-sentence clip joins.
- Checks 1–10: PASS by design, with the honest limit that Muse AI has no
  voice-casting control — voice drift between clips is possible and must be
  noted in QC if it occurs, not promised away.

### TEST 11 — Video with multiple locations
- One environment block per location; location changes are storyboard beats
  with transitions; prop tracker follows objects across locations.
- Checks 1–10: PASS by design.

### TEST 12 — Video requiring seamless continuity across multiple clips
- Final-frame reference + 12-field continuity record at every boundary;
  joins inspected; seams reported honestly (see tests/continuity-tests.md).
- Checks 1–10: PASS by design, with the honest limit that each clip is a
  fresh render — "seamless" means one continuous story, not pixel-perfect
  continuation.

## Honest limitations (apply to all scenarios)

- Generation is ~10s per clip, max 6 per user message: long videos need
  multiple messages and cannot run unattended.
- Continuity is best-effort: final-frame references reduce seams but cannot
  eliminate render variation.
- Lip-sync and voice identity are generation-dependent, not guaranteed.
- Aspect ratios are requested and measured, not guaranteed by the generator;
  mismatches are regenerated, never disguised.
- No licensed stock music is bundled; no platform publishing is included.
- No video was generated to validate these scenarios; they are design
  walkthroughs. Re-validate against a real production before claiming
  production-proven status.

## Executed script tests (these DID run)

Run on 2026-10-31 during the build, on this machine:

- `plan_clips.py --duration 60` → 6 clips, 1 message. PASS.
- `plan_clips.py --duration 600` → 60 clips, 10 messages. PASS.
- `plan_clips.py --duration 1680` → 168 clips, 28 messages. PASS.
- `plan_clips.py --duration 0` → error, exit code 2. PASS.
- `assemble.py` on 3 synthetic 720x1280 clips with audio → joined 6.04s,
  720x1280, 30fps, audio present, QC JSON written, verdict PASS. PASS.
- `assemble.py` with wrong expected ratio (16:9 vs actual 9:16) → FAIL
  verdict, exit code 1. PASS (correct rejection).
- `assemble.py` with a missing clip → error, exit code 1. PASS.
- One real bug found and fixed during testing: the concat list initially
  used relative paths, which ffmpeg resolves against the list file's
  directory; fixed to absolute paths and re-tested PASS.
