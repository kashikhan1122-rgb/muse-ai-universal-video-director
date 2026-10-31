# Changelog

All notable changes to this skill will be documented in this file.

## [Unreleased]

- Initial release: full skill built from the Muse AI — Universal Video Director master
  instruction (25 sections), Phases 2–7.
- One-prompt input, FULL AUTOPILOT default, no fixed duration / aspect ratio / niche.
- Intelligent long-form and hybrid scene planning with honest per-message batching
  (max 6 video generations per user message, ~10s clips, ffmpeg assembly).
- Ultra-detailed storyboard engine, character identity system, environment/prop
  consistency, seamless clip continuity with final-frame references.
- Camera/cinematography engine, storytelling/retention rules, audio and voice design
  with language-from-prompt rule, caption rules.
- QC engine, max-3-retry failure policy, automatic assembly, full production package
  (only files actually created).
- Tested helper scripts: `scripts/plan_clips.py` and `scripts/assemble.py`.
- Design validation documented against all 12 master-instruction scenarios in `tests/`.

## [1.0.0] — Initial public structure

- Repository layout per master instruction section 21 (README, LICENSE, SKILL.md,
  CONTRIBUTING, CHANGELOG, agents, references, templates, examples, scripts, tests).
