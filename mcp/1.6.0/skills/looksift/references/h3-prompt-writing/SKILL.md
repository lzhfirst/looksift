---
name: h3-prompt-writing
description: Write MiniMax H3 video generation prompts for T2VA, I2VA, FL2VA, L2VA, and Ref2VA. Use when rewriting multimodal requests into H3 prompt structures, composing integrated_multimodal_description, overall_soundscape, and non_diegetic_music, aligning keyframes, or defining reference labels for images, videos, and audio.
---

# H3 Prompt Writing

Portable to any agent that can read local files. It requires no external API calls, MiniMax Hub tools,
or proprietary runtime; `agents/openai.yaml` only adds optional ChatGPT/Codex UI metadata.

## Workflow

1. Identify the input mode: T2VA, I2VA, FL2VA, L2VA, or full-reference Ref2VA.
2. For base text/keyframe modes, read `references/base-en.txt` and follow its final prompt structure.
3. For full-reference mode, read `references/ref-en.txt` and follow its six-section rewrite format.
4. Preserve the exact field names, section order, labels, and timing notation from the selected guide.

## Base Modes

- T2VA: build the full audiovisual timeline from text.
- I2VA: start from the first frame and develop forward from it.
- FL2VA: describe the continuous path between the first and last frames.
- L2VA: infer a plausible opening and converge to the supplied last frame.

For FL2VA, do not schedule a meaningful last-frame event only at the final instant. When the
last frame contains a reveal, lightning flash, completed gesture, landing, or other endpoint that
must be readable, reach that endpoint early enough to leave an explicit stable hold afterward.
Default to about two seconds of locked final composition when the duration permits, while allowing
rain, light decay, cloth, smoke, or sound to finish naturally. Omit or shorten the hold only when the
user or edit contract explicitly calls for an immediate cut, impact cut, or unresolved interruption.
State the arrival time, hold interval, camera lock, and exact end time in the prompt.

Use `integrated_multimodal_description`, `overall_soundscape`, and `non_diegetic_music` in the order shown in `references/base-en.txt`.

## Full-Reference Mode

Ref2VA rewrites use `subject_definitions`, `summary`, `retention_analysis`, `detailed_description`, `overall_soundscape`, and `non_diegetic_music` in that order. Reference labels stay consistent across all sections.

Read `references/ref-en.txt` for label rules, retention analysis, and complete examples.

## Output Rules

- Follow the selected official guide's language default unless the user explicitly requests another prose language. Preserve official field names, labels and syntax, and keep dialogue, lyrics and visible scene text in their requested original language.
- Describe each shot by composition, subjects, environment, actions, camera, sound, and the exact point where referenced content appears.
- Use current creative intent and actual selected media. This prompt-format skill has no prerequisite planner, acting/physical contract, project schema or compulsory planning image. It can be used within the same ongoing director session.
- Preserve the director's intended shot boundaries and timing. Do not add cuts or merge shots merely to fit a template; use the official guide to express the actual audiovisual design.
- Ground visual subject labels in observable appearance, position, posture and contact relationships. Keep internal asset IDs and bookkeeping out of the prompt. Distinguish visible dialogue from off-screen or system voices using official speaker notation; do not assign an unseen narrator's speech to an unrelated visible person.
- Avoid plot summaries, unresolved reference labels, and timing that does not match the requested duration.
## Tips for Better Results
- Always match the total duration of the description to the requested video length (4–15 seconds).
- Keep reference labels consistent (e.g. `<Picture 1>`, `<Video 1>`, `<Audio 1>`) across every section.
- Prefer concrete visual and audio details over abstract words like "cinematic" or "beautiful".
- When using keyframes (I2VA / FL2VA / L2VA), clearly state how the first and/or last frame connects to the timeline.
