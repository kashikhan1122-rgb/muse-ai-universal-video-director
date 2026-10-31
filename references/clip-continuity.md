# Clip Continuity

## Goal

The final video must feel like one coherent production, not a set of
disconnected generated clips. Continuity is a system, not a hope.

## The continuity record (per boundary)

For every boundary between clip N and clip N+1, record:

1. Previous clip's final visual state
2. Previous clip's final character positions
3. Character facial expressions
4. Character body positions
5. Character movement direction
6. Prop positions
7. Environmental conditions
8. Lighting conditions
9. Camera position and framing
10. Ongoing actions
11. Dialogue or audio state
12. The exact action that must continue

Template: templates/continuity-template.md. The log lives in the project folder
and survives across batches and sessions.

## The final-frame reference (the main tool)

When supported, extract the previous clip's final frame and pass it as the next
clip's starting reference:

```
ffmpeg -sseof -0.15 -i clip_N.mp4 -frames:v 1 clip_N_final.png
```

Then write the next clip's prompt as a continuation: "Continue from this frame:
[same characters, same positions, same light]. The next action is [X]." The
reference image plus the written continuation together are far stronger than
either alone.

## Rules

1. **Continue, don't restart.** Do not restart an action the previous clip
   already started. Do not teleport characters. Do not reset the environment.
2. **No unexplained jumps.** A time or location jump must be a storyboard
   decision with a transition (a cut, a door, a morning title in the plan —
   never unlabelled on screen unless the prompt wants it).
3. **One handover action per boundary.** Each clip ends mid-action or on a
   clear beat that the next clip picks up. A clip that ends on a completed
   action with nothing pending makes the next clip feel like a restart.
4. **Inspect every join.** After assembly, watch the joins specifically: the
   10s, 20s, 30s marks and every batch boundary. A visible cut, a character
   jump, or an audio break at a join is a defect to fix (re-prompt with a
   stronger continuation) or report.
5. **Audio continuity.** Clip audio must not cut mid-word or mid-note at a
   join. If the generator's clip audio ends abruptly, prefer a clean audio
   boundary (end of a line, end of a phrase) in the storyboard split.

## Honest limit

Each clip is a fresh render. Even with a final-frame reference and a full
continuity note, small changes (a shifted background, a slightly different
face angle) can occur. The skill's standard is: the viewer experiences one
continuous story; minor render variation is acceptable and is not hidden, but
a character teleport, identity change, or location reset is a defect — retried
within budget, otherwise reported in the QC report and the final message.
