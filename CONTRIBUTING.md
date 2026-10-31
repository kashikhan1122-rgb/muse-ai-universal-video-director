# Contributing to Muse AI — Universal Video Director

## Ground rules

1. **Muse AI only.** Never add workflows for Seedance, Kling, Veo, Runway, Sora, or
   any other video platform.
2. **Original work only.** Do not copy documentation, prompts, or code from the
   reference repository or any other project. Architectural ideas may be credited in
   the README; text must be your own.
3. **Capability honesty is non-negotiable.** Any new workflow step must state what
   Muse AI can actually do, what it cannot, and the fallback. A contribution that
   claims an unavailable feature works will be rejected.
4. **No empty files.** Every file must have a clear purpose. Do not add a file just
   to fill a folder.
5. **No fabricated outputs.** Templates and examples must be labelled as templates
   and examples. Never present a sample as a produced deliverable.

## How to propose a change

- Open an issue describing the problem, the Muse AI capability it touches, and the
  proposed change.
- Keep SKILL.md operational and concise; put deep technical detail in `references/`
  and link to it.
- If you add a script, it must be genuinely useful and tested: include the test
  command and its result in your proposal, and keep runtime dependencies minimal
  (Python 3 standard library + ffmpeg).
- Update CHANGELOG.md under an "Unreleased" heading.

## Style

- Write instructions as direct, checkable steps, not marketing prose.
- Prefer tables for capability mappings and checklists for QC steps.
- Use the user's prompt as the single source of truth; never invent a fixed niche,
  duration, aspect ratio, or style.
