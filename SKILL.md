---
name: looksift
description: Write Qwen Image 2.1 prompts from a new theme using a Looksift style number (A, T2I) or a style reference supplied at generation time (B, Edit). Reuse applicable user preferences and deliver complete English and selected-language versions without generating images.
---

# Looksift

[Looksift](https://looksift.com) is the main gallery for browsing, comparing and
choosing styles and obtaining available reference images. This Skill helps the
host Agent turn the user's new theme into usable drawing prompts with the bundled
style records and the selected official template.

Transfer the source's visual methods—marks, texture, form, edges, lighting and
color organization—while faithfully expressing the new subject and constraints.
The Agent understands context, user intent, applicable memory and scene coherence.
The Skill supplies methods and resources; its helper stores facts, not dialogue
or fixed responses. Prompt quality is the objective, not completion of a questionnaire.
Do not promise that prompt text alone guarantees an identical visual result.

## Read the relevant resources

Read [the workflow](skills/looksift/WORKFLOW.md) for the actual drawing request.
Read [the preference guide](skills/looksift/references/user-preferences.md) and
load the relevant local profile on actual invocation/reload. Combine it with
genuinely available applicable host memory; never invent access or synchronization.
Current explicit requirements and confirmed current-request choices take priority
over applicable explicit long-term preferences. Candidate habits are not defaults.
An explicit preference mutation must actually succeed before reporting it saved
or forgotten. Maintenance and tests must not access or seed real user profiles.
Ordinary drawing requests also use the preference guide: record newly settled,
eligible user choices at the decision/delivery checkpoint as candidate observations.
Do not wait for a “remember” request, replay old drawings or promote observations
to defaults. Agent-made choices and temporary overrides are not user habits.

Every ordinary question, option label, reminder and recovery message uses the
user's selected communication language. Infer that selection from explicit intent,
applicable memory, available session settings and context, not nationality or
quoted source text. Ordinary wording may adapt to the user's communication style.
Examples show meaning and format, not mandatory phrases. Humor in conversation
does not change the picture or belong in the copyable drawing prompt.

## Show the opening once

On first actual Looksift use in a new chat, or an explicit reload, start the
ordinary reply with this fixed three-row, 29-column line-art logo in a monospaced
block. Preserve spaces, including the final space on rows 2 and 3.

```text
╦   ╔═╗ ╔═╗ ╦╔═ ╔═╗ ╦ ╔═╗ ╔╦╗
║   ║ ║ ║ ║ ╠╩╗ ╚═╗ ║ ╠╣   ║ 
╩═╝ ╚═╝ ╚═╝ ╩ ╩ ╚═╝ ╩ ╩    ╩ 
```

Style browsing and usage: [Looksift](https://looksift.com)

Localize that short website line; keep the logo, brand and root URL unchanged.
Do not repeat the opening for follow-ups, internal reads or maintenance, or put it
inside a drawing prompt. Reload rereads current rules but retains agreed inputs.
Strict JSON/API-only output omits the entire opening. Continue with the next
necessary action; no “start/next” acknowledgment or invented documentation URL.

## Understand before asking

Read the relevant conversation and latest corrections. Retain volunteered facts
even when supplied out of order or together. Reuse settled mode, source roles,
theme, ratio, creative scope and language. Ask only one necessary unresolved item
at a time, wait for its answer, then proceed. For a first request containing only
a theme, ask mode first. Complete authorized briefs proceed immediately.

Open input gets a direct invitation and a relevant short example, not a fake
“enter/supplement/customize/upload” choice. Genuine choices appear on separate
lettered lines. A letter, including lowercase, answers only the current question;
equivalent natural language is valid. Clarify real ambiguity without resetting
settled answers or requiring compound reply syntax.

Across all subjects, ask when the user's material lacks effective drawing
information needed to express the intended picture. Judge the missing content
and its consequences, not a subject list, word count or a close-up trigger.
The workflow explains both this criterion and the detail-handling intent needed
before final expansion. Reuse applicable current or explicit ongoing delegation;
mode B and ratio-only delegation do not authorize content expansion. Silence
does not establish a missing decision.

These are drawing-brief choices, not operational tool permission. Ordinary replies
contain the actionable question and useful choices/link. Follow higher-priority
host disclosure rules and accurately explain genuine blockers; Skill examples
cannot waive host requirements.

## Respect the two methods

- **A — direct text-to-image:** requires an exact valid Looksift style number.
  If missing, link the gallery and invite the number directly. Read its exact
  bundled style fields and full example, then the original T2I template.
- **B — style-reference generation:** requires the new theme, not a number or a
  preliminary upload to the Agent. Read the original Edit template even if the
  user will select and supply the reference only at generation time. A short
  gallery link can help find a reference; the user's own image also works.

Neither a number nor an attachment selects the mode. Reuse an explicit choice or
applicable delegation/default; otherwise ask A/B alone. Explain briefly that B
helps follow a reference's visual style. Do not create a third method.

Use [the exact bundled index](skills/looksift/references/styles.json) or the
portable lookup helper, never list position, neighboring IDs or an old mapping.
An optional numbered source in B is read for its stated purpose. Inspect current
images when the task needs them; never claim to have viewed a future reference.
Actual edit/replication tasks may require missing visual evidence.

A style reference supplies visual treatment, not its characters, story or layout.
Transfer color organization rather than automatically copying a hue list; choose
colors fitting the new subject/user intent within authorized scope. Honor an
explicit request to retain source colors. Without source evidence in B, describe
relative inheritance from the eventual reference, without inventing medium,
brushwork or palette. State image roles inside the copyable prompt. Use natural
single-image wording; ordered tags only for multiple actual/agreed inputs.

Resolve the output ratio or explicit permission to choose/follow it before final
composition. Uploaded dimensions, example ratios and content delegation alone do
not settle it. Recompose both language versions when the frame changes.

## Deliver the finished prompts

Use the full selected [official template](skills/looksift/references/qwen-image-2.1-official/README.md).
Ordinary delivery gives complete English and selected-communication-language
versions of the same scene, preserving exact requested in-image text. If the
selected language is English, one complete English version serves both roles.
Explicit output-language/single-language/JSON requests take priority.

Express actual composition in both prompt bodies; keep numeric sizes and machine
fields outside ordinary prose. After the prompts, one brief localized usage note
states the confirmed ratio and, for B, reminds the user to upload the chosen
reference with the prompt at generation time. A gallery link is useful when no
image is chosen; an existing own image needs no repeated gallery selection.
Do not promise a specific website download button. ComfyUI size reminders apply
only when that tool is currently discussed.

For explicit JSON, preserve the exact official schema: T2I has
`rewritten_prompt` and `wh_ratio`; Edit adds `ratio_follow`, with exactly one
ratio field nonempty. No extra translation field, wrapper, opening or tail in
JSON-only output. Follow the workflow for image tags and visible-text handling.

Deliver prompts without automatically fetching images or generating them.
Preserve the upstream originals, licenses and exact numbered source records.
