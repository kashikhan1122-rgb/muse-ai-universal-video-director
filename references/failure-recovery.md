# Failure Recovery

## Policy (hard rule)

**Maximum 3 generation attempts per failed section.** No exceptions, no silent
fourth attempt through another route for the same clip. (A genuinely different
creative approach — a replacement scene the user approves — is a new section,
not a retry, and is labelled as such.)

## Failure taxonomy

| Failure | Likely cause | First fix |
|---|---|---|
| Generation refused / blocked | Prompt trips a safety or content filter | Reword the sensitive element; keep the story beat; never re-submit the identical refused prompt |
| Wrong aspect ratio | Generator ignored the ratio | Restate ratio first in the prompt ("Tall vertical 9:16, 720x1280"), regenerate |
| Character drift | Identity block omitted or paraphrased | Restore the verbatim block + reference image |
| Continuity break | Weak handover | Add final-frame reference + explicit continuation sentence |
| Garbled on-screen text | Generator text rendering | Remove on-screen text from the prompt; add it in editing if needed, or drop it |
| Lip-sync mismatch | Dialogue not matched to speaker | Shorten the line, name the speaker explicitly, single speaker per clip |
| Missing / broken audio | Generation audio fault | Regenerate; if persistent, mark failed and note the audio gap |
| Visual defect (extra limbs, distortion) | Render fault | Reword the action more simply; split the action across two clips |

## Retry procedure

1. Identify the failure precisely (what is wrong, in which clip, at what second).
2. Diagnose the likely cause from the table above.
3. Improve the generation instructions (one change at a time where possible,
   so the fix is learnable).
4. Retry. Inspect the new result against the same checklist.
5. Record every attempt in the clip manifest: attempt number, prompt change,
   result.

## After 3 unsuccessful attempts

1. Mark the section FAILED in the manifest and the failed-generation report,
   with the reason and the attempts made.
2. Choose, in this order: (a) the best acceptable alternative already
   generated (an earlier attempt that passed QC except for a minor note);
   (b) a planned bridge — a simpler shot covering the same story beat;
   (c) skip the section and bridge the story in the neighbouring clips'
   prompts, noting the skip.
3. Continue producing the remaining sections. Never abandon the project.
4. Report the failure plainly at delivery: which section, why, what replaced
   it (or what is missing), and what the user can supply to complete it
   (e.g. a clip they generate themselves from a provided prompt).

## What never happens

- A failed clip is never claimed as generated.
- An incomplete join is never presented as the full video.
- A failure is never hidden by reordering clips to disguise a gap.
- The same refused prompt is never resubmitted unchanged.
