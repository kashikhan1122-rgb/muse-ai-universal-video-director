# Output Organization

## Project folder

One folder per video, named for the project (not for the date):

```
<project-name>/
├── final/
│   └── <Project_Name>_<duration>.mp4
├── clips/
│   ├── clip-01.mp4 ... clip-NN.mp4
├── frames/
│   └── clip-NN-final.png          (final-frame references, when used)
├── production-brief.md
├── story-outline.md
├── storyboard.md
├── character-reference.md         (if created)
├── environment-reference.md       (if created)
├── camera-reference.md            (if created)
├── scene-plan.md
├── clip-manifest.md
├── continuity-log.md
├── dialogue-script.md
├── sound-design-notes.md
├── music-instructions.md
├── captions.srt                   (only if captions were actually produced)
├── editing-timeline.md
├── export-info.md
├── failed-generation-report.md    (only if failures occurred)
└── qc-report.md
```

## Naming rules

- Clip files: `clip-01.mp4`, zero-padded, in story order. Never reuse a clip
  number for a different shot.
- Final file: project name + duration + INCOMPLETE marker when applicable,
  e.g. `Project_60s.mp4` or `Project_160s_INCOMPLETE_16clips.mp4`.
- Document files: lowercase with hyphens, matching the template names.

## The delivery message

Every delivery states, in plain language:

1. What was delivered (title, duration verified by ffprobe, ratio, frame rate).
2. Whether it is complete or incomplete — with missing clip numbers if
   incomplete.
3. The download link (in a copy box) and its expiry, when a link is used.
4. Failures, if any, in one line each.
5. What the user can do next (post, request a fix, supply a missing clip).

## Only files actually created

The production package lists only files that exist in the project folder. If
captions were not produced, there is no `captions.srt` and the delivery says
so. If no storyboard images were generated, there is no images folder. A
package index that lists a file nobody made is fabrication, and this skill
does not do it.

## Export information (recorded per delivery)

- Container and codec (e.g. MP4, H.264, AAC)
- Resolution, frame rate, duration (ffprobe values, not rounded claims)
- Assembly method (ffmpeg concat, re-encode or stream copy)
- Link expiry, when applicable
