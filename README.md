# Muse AI — Universal Video Director

A universal, long-form-capable, fully automated video production skill for **Muse AI only**.

Give it **one complete video prompt** — concept, story, characters, location, duration,
aspect ratio, visual style, dialogue, narration, camera notes, anything you have — and it
runs the whole production end to end:

```
PROMPT → ANALYSIS → STORY → STORYBOARD → REFERENCES → SCENE PLANNING
→ CLIP GENERATION → CONTINUITY CONTROL → AUDIO → ASSEMBLY
→ QUALITY CHECK → FINAL VIDEO + PRODUCTION PACKAGE
```

## What it is not

- **Not a stickman skill.** It works with any niche: animal rescue, wildlife documentary,
  emotional storytelling, comedy, fantasy, history, education, food, animation, realistic
  smartphone footage, cinematic drama, mystery, children's content, long-form YouTube,
  short-form social video — anything the prompt describes. The prompt decides the content
  and the visual identity. There is no fixed category list.
- **Not a prompt-only skill.** The default is **FULL AUTOPILOT**: it does not stop at a
  storyboard and does not deliver only text prompts when a finished video is expected.
  It generates clips, assembles them, checks them, and delivers the finished video plus
  a production package.
- **Not a multi-platform skill.** It is built for Muse AI's workflow only. It creates no
  workflows for Seedance, Kling, Veo, Runway, Sora, or any other video platform.

## How to use it

1. Send one complete video prompt. Include whatever you know: story, characters,
   setting, duration, aspect ratio, style, dialogue, narration, camera, platform.
2. If an essential detail is genuinely missing and cannot reasonably be inferred, you
   will be asked one minimum clarification — nothing more. Routine production decisions
   are made independently; there are no approval gates between stages.
3. Receive the finished video plus the production package (see
   [references/output-organization.md](references/output-organization.md)).

## Muse AI capability honesty — read this first

This skill is written for what Muse AI can actually do, not for an idealised pipeline.
Where the original master instruction assumes more, this skill adapts honestly:

| Assumed capability | Muse AI reality | What this skill does instead |
|---|---|---|
| One continuous generation of any length | Video is generated in ~10-second clips | Plans the video as N × ~10s clips and assembles them with ffmpeg |
| Unlimited generation in one run | Max 6 successful video generations per user message | Batches clips 6 per message; long videos continue across messages on the user's "continue" — never silently truncated, never faked |
| True frame-exact clip continuation | Each generation renders anew; a previous clip's final frame can be used as a reference image, but the next clip is still a fresh render | Final-frame reference + continuity notes + join inspection; visible seams are reported, not hidden |
| Guaranteed lip-sync / voice casting | Clip audio comes from generation; no voice cloning or casting controls | Dialogue is written into prompts; lip-sync is QC-checked, failures retried (max 3), then reported honestly |
| Any aspect ratio on demand | Generators do not always honour a requested ratio | Requested ratio is specified in every prompt and every clip is measured; a mismatch is regenerated, never disguised with blur fill, black bars, or a side-cropping pass-off |
| Licensed stock music | No licensed stock library is bundled | Uses generation audio, or audio the user supplies; never claims a licence it does not have |
| Single-run 28-minute films | 28 min ≈ 168 clips ≈ 28+ messages at 6 clips each | Plans the full film honestly, delivers it in verified parts, and never labels a partial join as the complete film |

If a required capability is unavailable for a given project, the skill says so plainly
and offers the best achievable alternative. It never claims a failed clip was generated,
never presents an incomplete join as the full video, and never fabricates a file that
was not created.

## Failure policy

Max **3 generation attempts per failed section**. After 3 unsuccessful attempts the
section is marked failed, the reason is recorded, production continues with the
remaining sections, and the final report lists every unresolved problem. One failed
clip never abandons the whole project. See [references/failure-recovery.md](references/failure-recovery.md).

## Repository structure

```
muse-ai-universal-video-director/
├── README.md
├── LICENSE
├── SKILL.md                      # Central operating instruction — start here
├── CONTRIBUTING.md
├── CHANGELOG.md
├── agents/
│   └── openai.yaml               # Agent metadata for the skill
├── references/                   # Deep technical guides (linked from SKILL.md)
│   ├── workflow-architecture.md
│   ├── prompt-analysis.md
│   ├── storyboard-system.md
│   ├── character-consistency.md
│   ├── environment-consistency.md
│   ├── camera-and-cinematography.md
│   ├── clip-continuity.md
│   ├── audio-and-voice.md
│   ├── quality-control.md
│   ├── long-form-production.md
│   ├── failure-recovery.md
│   └── output-organization.md
├── templates/                    # Copy-ready production documents
│   ├── production-brief.md
│   ├── storyboard-template.md
│   ├── character-reference-template.md
│   ├── environment-reference-template.md
│   ├── continuity-template.md
│   └── quality-control-template.md
├── examples/                     # Worked production plans
│   ├── short-video-example.md
│   ├── long-form-video-example.md
│   ├── documentary-example.md
│   ├── animation-example.md
│   └── realistic-video-example.md
├── scripts/                      # Small, tested helpers (ffmpeg-based)
│   ├── plan_clips.py             # Duration → clip plan + per-message batching
│   └── assemble.py               # Join clips, verify duration/ratio, write QC note
└── tests/                        # Design validation against the 12 scenarios
    ├── prompt-analysis-tests.md
    ├── continuity-tests.md
    ├── duration-tests.md
    ├── aspect-ratio-tests.md
    └── workflow-validation.md
```

## Attribution

The architecture of this skill was informed by studying the
[stickman-video-director](https://github.com/kaomei/stickman-video-director) repository
(MIT licence) — its dual Director/Autopilot modes, style catalogue idea, voice-continuity
discipline, storyboard template, local rendering approach, caption alignment, and tests
were useful conceptual references. **No code or documentation was copied from it.**
All instructions, templates, scripts, and examples here are original, and this skill is
independent: it is not a rename, fork, or port of that project, and it deliberately
removes that project's stickman-only scope and approval-gated Director flow.

## Licence

MIT — see [LICENSE](LICENSE).
