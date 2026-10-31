# Workflow Architecture

## Pipeline

```
PROMPT
  → PROMPT ANALYSIS        (references/prompt-analysis.md)
  → STORY & STRUCTURE      (references/long-form-production.md)
  → STORYBOARD             (references/storyboard-system.md)
  → REFERENCE SHEETS       (character + environment consistency)
  → SCENE PLAN             (clip boundaries, per-message batches)
  → CLIP GENERATION        (max 6 successful generations per user message)
  → CONTINUITY CONTROL     (final-frame reference + continuity note per clip)
  → AUDIO                  (references/audio-and-voice.md)
  → ASSEMBLY               (ffmpeg join, scripts/assemble.py)
  → QUALITY CONTROL        (references/quality-control.md)
  → DELIVERY               (video + production package)
```

## Stage contracts

Each stage produces a named artefact that the next stage consumes. No stage is
skipped silently: if a stage produces nothing (e.g. no reference images because a
text storyboard was clearer), the production brief records why.

| Stage | Produces | Consumed by |
|---|---|---|
| Prompt analysis | Production brief | Story, storyboard |
| Story & structure | Story outline, scene list | Storyboard, scene plan |
| Storyboard | Scene-by-scene storyboard | Clip prompts |
| Reference sheets | Character + environment blocks | Every clip prompt |
| Scene plan | Clip list with batch numbers | Generation |
| Generation | Verified clips (duration, ratio, fps, audio) | Assembly |
| Continuity control | Continuity note + final frame per boundary | Next clip prompt |
| Audio | Dialogue/VO script, sound notes | Clip prompts, assembly |
| Assembly | Joined video | QC |
| QC | QC report, fail list | Delivery report |
| Delivery | Video + package | User |

## Batching rule (the hard constraint that shapes everything)

Muse AI generates ~10-second clips, max 6 successful generations per user
message. The scene plan therefore assigns every clip a **batch number**:

- Batch 1 = clips 1–6, batch 2 = clips 7–12, and so on.
- A batch is generated, verified, and only then does the next batch start.
- Long videos span messages: the user says "continue" and the next batch runs.
  The plan states the total message count up front (e.g. "60 clips = 10
  messages") so the user is never surprised.
- A batch is never half-delivered as a finished video. Partial joins are
  labelled INCOMPLETE with the missing clip numbers, every time.

## State that must survive across batches

Keep in the project folder, not in memory alone:

- `production-brief.md` — the parsed prompt and all inferred choices
- `storyboard.md` — the full storyboard
- `character-reference.md` / `environment-reference.md` — verbatim identity blocks
- `continuity-log.md` — one entry per clip boundary (see continuity template)
- `clip-manifest.md` — clip number, prompt, file, verification result, attempts
- `qc-report.md` — defects found, fixed, or accepted with reason

If a session ends mid-project, these files are what lets the next session resume
without re-asking the user anything.

## What this architecture deliberately does not include

- No approval gates between stages (FULL AUTOPILOT default).
- No fixed scene count, duration, ratio, or niche.
- No platform-specific export paths (no Seedance/Kling/Veo/Runway/Sora).
- No render farm, no background worker, no unattended multi-message execution:
  Muse AI cannot continue generating while the user is away, so the plan must
  be resumable, not continuous.
