# Continuity Tests

> Status: DESIGN VALIDATION, not an executed test run. Each case checks the
> continuity system (references/clip-continuity.md) against a scenario. No
> video was generated for these cases.

## Case C1 — Simple two-clip handover

Clip 1 ends with a character mid-step toward a door. Clip 2 must start with
the same character, same position, same direction, same room, same light.

- PASS: clip 2 prompt contains the final-frame reference + a continuation
  sentence naming the action. FAIL: clip 2 restarts the walk from the room's
  centre.

## Case C2 — Prop state across a boundary

A letter is sealed in clip 3, opened in clip 4, read in clip 5.

- PASS: prop tracker records sealed → opened → read; no clip shows the letter
  sealed again. FAIL: any clip contradicts the tracker's state.

## Case C3 — Location change

Story moves from kitchen to street between clips 6 and 7.

- PASS: the change is a storyboard beat with a transition (door, cut) and the
  street block is introduced in clip 7's prompt. FAIL: the location changes
  mid-clip with no storyboard reason.

## Case C4 — Batch boundary (clips 6 → 7, separate messages)

A long video's batch 1 ends at clip 6; batch 2 starts later, possibly in a
new session.

- PASS: the continuity log + final frame + recap paragraph restore the exact
  state, and clip 7 continues it. FAIL: clip 7 restarts the scene or changes
  the character's look because the session forgot.

## Case C5 — Audio across a join

A narration sentence spans the 20s boundary.

- PASS: the storyboard split the narration at a phrase boundary so no word is
  clipped. FAIL: a word is cut mid-syllable at the join and shipped anyway.

## Case C6 — Visible seam reported, not hidden

A join shows a small background shift despite a final-frame reference.

- PASS: QC records it as ACCEPT WITH NOTE (minor, story-safe) or RETRY if
  major; the delivery mentions it if major. FAIL: the seam is silently
  shipped as "seamless".
