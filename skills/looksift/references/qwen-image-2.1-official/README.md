# Official Qwen Image 2.1 templates: local execution guide

This English guide is local Skill instruction, not upstream template text. All
ordinary responses use the user's selected communication language, independent
of the instruction-file language. Follow the [workflow](../../WORKFLOW.md) and
[user preference guide](../user-preferences.md) for context, scope, language and
natural interaction. Examples are localizable demonstrations, not fixed wording.

## Choose the established method and read its full original

- **A, direct text-to-image:** requires the exact Looksift style number. Read its
  reusable style fields and complete example, then [the T2I original](system_prompt_t2i.txt).
- **B, style-reference generation:** use [the Edit original](system_prompt_edit.txt)
  even if the user has no number or current upload. The user can select a reference
  and supply it to the drawing model later. Do not fall back to T2I.

Reuse established or applicable explicitly delegated/default method choices;
otherwise ask A/B alone. A number does not choose A; an attachment does not choose
B. B's missing number/upload is not a prerequisite. Actual edits/replication may
require unavailable visual evidence. Inspect images when needed; never claim
to have seen an unread image. Follow explicit image roles and source priorities.

Read the chosen template in full; do not combine the two, substitute this guide
for the original, or output the system template as the user's drawing prompt.
First resolve effective drawing content/detail-handling intent and the ratio under
the workflow; do not use a template default to bypass missing user intent.

## Apply visual treatment to the new theme

Read the full numbered example when supplied. Extract medium, marks, texture,
form/edge treatment, light/shade and color organization. Source subject matter,
story, identity, text and layout are not automatically inherited. Concrete colors
fit the new subject or explicit preferences; transferring style alone does not
require copying a fixed palette. Honor an explicit palette-preservation request.
Adapt lighting methods to the new scene.

For B without a current source, use relative inheritance from the eventual image
without inventing style values. In the copyable prompt itself, state each reference's
role and the new content. A style-only image supplies visual treatment; a real
canvas edit supplies the canvas and requires preserving untargeted content.
Single-image prose uses natural reference wording. Use ordered image tags only
for multiple actual/agreed inputs with established roles and order.

## Template form and output

T2I uses observational finished-image description. Edit begins with the operation
and uses one continuous paragraph per version. Plan actual composition for the
settled frame before writing; changing ratio requires recomposition.

Ordinary delivery gives complete English and selected-communication-language
versions of the same scene. If that selected language is English, one complete
version serves both roles. Explicit single-language/output-language requests take
priority. Preserve exact in-image text and its target language in every version;
otherwise follow the original's visible-text priority. Prompt translation never
authorizes changing text rendered in the image.

Keep numeric sizes/runtime fields out of ordinary copyable prose. One short localized
usage note states the adopted ratio/followed image and, for B, uploading the chosen
reference with the prompt at generation time. The gallery can help choose/save a
reference; do not promise a specific download button or require a preliminary upload.
Only discuss ComfyUI setup when currently relevant or requested.

For explicit JSON/API delivery, preserve the original schema and one-line valid JSON:

| Method | Exact fields | Ratio rule |
| --- | --- | --- |
| T2I | `rewritten_prompt`, `wh_ratio` | settled target W:H |
| Edit | `rewritten_prompt`, `wh_ratio`, `ratio_follow` | exactly one ratio field nonempty |

An explicitly followed actual/agreed input can use `<image1>` in `ratio_follow`
even when single-image prose has no tag. Do not derive image indexes from style
numbers. Delegated ratio choice follows the selected original's rules; do not
import T2I defaults into Edit or use a library example's production ratio.

JSON-only returns one official object in the requested output language, otherwise
English. No opening, tail, translation field, custom wrapper or unrequested second
object. Explicit multi-object requests retain each object's schema.

## Quality and provenance

Check faithful subjects/counts/actions/text, justified style traits or relative
future-reference instructions, coherent scene relationships and light, matching
language versions, image roles and actual frame composition. Source metadata and
system rules must not leak into the drawing prompt. No fixed test subject/palette.

The Skill delivers prompts, without automatically generating images. Using official
templates is not running an official prompt-enhancement checkpoint. Structural
validation is not visual validation; only actual generated images and comparison
can support a visual result claim. Existing production jobs have separate protocols.

780×780 and 50 steps belong to a project test configuration, not general Skill
defaults. The optional project helper `scripts/qwen_prompt_enhancement.py` is not
required by the independently installed Skill. It must not be confused with this
prompt-only B route or used to impose its generation-time image requirement here.

Pinned source revision, URLs and SHA-256 hashes are in [manifest.json](manifest.json).
Preserve the original [LICENSE](LICENSE). Upstream texts are not relicensed under
the project's MIT license.
