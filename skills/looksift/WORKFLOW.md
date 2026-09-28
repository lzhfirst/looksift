# Looksift workflow

## Objective and division of work

The website is the main place to browse, compare and choose visual styles and
obtain available reference images. The Skill supports the host Agent in writing
new-theme prompts using exact library records and official Qwen Image 2.1 templates.
Transfer visual methods faithfully and preserve the user's subject, actions,
counts, text and constraints. The Agent handles meaning, context, scene coherence
and natural expression. Helpers validate and store facts; they are not dialogue
engines. No automated image generation or promise of identical visual results.

All paths in this document are relative to its directory unless stated otherwise.
Use [user preferences](references/user-preferences.md) on actual invocation/reload,
ordinary drawing-choice checkpoints, memory operations and conflicts. Keep runtime
facts outside the distributable
Skill and use isolated profiles for testing. Never claim saved/deleted preferences
until an actual successful operation. Candidate habits are not defaults or consent.

## Language, voice and opening

Write ordinary communication, choices, reminders and errors in the user's selected
communication language. The Agent uses explicit requirements, applicable memory,
available session settings and context; do not infer a mother tongue or claim
unavailable settings were read. A source quotation or an English technical term
does not switch that language. Current explicit changes override older preferences;
temporary changes do not silently replace long-term ones.

Interaction tone is independent of communication language, visual style and scene
mood. Adapt questions naturally to applicable humor, concision or formality preferences.
Keep meanings and formats stable, without putting jokes/internal explanations in
drawing prompts. All ordinary wording below is an example to localize and adapt,
not a fixed response table. The logo, brand, root URL and technical formats are fixed.

Use the root SKILL.md's exact three-row, 29-column line-art logo and clickable
website line at first actual use in a chat and explicit reload, once per such event.
Preserve its spaces. Reload rereads rules while retaining settled inputs; maintenance,
internal reads and ordinary follow-ups do not trigger it. Localize the website-line
label. No extra start acknowledgment, image/network dependency or invented /docs
address. Strict JSON/API-only output omits the entire opening. It never belongs
in either copyable prompt and does not change application-wide startup behavior.

## Read the accumulated brief

Read the relevant conversation and latest corrections before deciding what is
missing. Reuse confirmed mode, source/roles, theme, ratio, content scope and language,
including applicable explicit long-term intent. Do not turn the sections below into
a fixed interview. Accept unordered keywords, short replies and several volunteered
facts together. Retain each resolved item and skip it. Deliver immediately when
the brief, ratio and detail-handling intent are resolved.

Ask only one necessary unresolved decision or information item per turn. A first
request containing only a theme needs the mode question first. Thereafter choose
the next genuine gap: A's number, needed content/handling or ratio. B's absent
number/current upload is not a gap. Resolve consequential conflicts minimally;
do not restart the interview.

Open information gets a direct invitation with a relevant short example. Do not
ask the user to choose “I will enter / supplement / customize / upload / visit the
site” before providing it. Use lettered options only for concrete preset choices
or executable decisions, each on its own line. A letter alone must settle that
choice. Native controls are optional when permitted and suitable; do not invent
extra choices to fill a control or call plain text clickable.

Write for someone unfamiliar with Skills and templates. Explain only what helps
the current choice; internal template names, field names and storage mechanics
do not belong in ordinary product dialogue. The user should not have to learn
rules before expressing an idea. Evaluate clarity and useful progress, not whether
the conversation followed a rehearsed sequence.

Interpret a letter, including lowercase, only under the current visible question.
Natural equivalents work too. A legacy menu can create genuine ambiguity; clarify
only that ambiguity. A recommendation alone is not permission to adopt it, while
explicit permission to decide the stated item allows deciding and briefly announcing
it without reconfirmation. Silence is not permission. Examples are not selected facts.

Drawing-brief choices define creative scope, not tool/external-action permission.
Ordinary replies default to the actionable invitation/question, choices and a useful
link. Reading a template adds no separate disclosure requirement in this Skill.
Explain actual permission/policy/access/evidence blockers accurately and follow
higher-priority host disclosure requirements, including those covering routine
confirmations. Do not hide an approval or invent a blocker from a missing preference.
The host-footer presentation issue is outside this workflow's control.

## Settle A or B

Reuse the user's explicit current choice, applicable explicit preference or permission
to decide the method. Equivalent natural language counts. Otherwise ask only:

Which generation method would you like?

- A. Direct text-to-image, using a Looksift style number.
- B. Generate with a style reference, with no number or upload needed here.

A brief localized explanation can say B helps follow a reference's style and
brushwork; [Looksift](https://looksift.com) offers examples to browse and save, or
the user can use their own image. Accept a request to recommend/decide without
inventing a third mode. A recommendation is not silently adopted. Do not demand
a number/image before the method is decided. A number/theme alone does not choose A;
an attachment alone does not choose B.

**A maps to T2I.** It requires a valid exact style ID. Reuse an existing ID; if
missing, invite it directly with the clickable gallery link and a clearly illustrative
ID such as 1813. No “already have / visit / enter” menu. An image does not substitute
for A's required ID. Invalid formatting and an absent ID in the current library
get a brief localized recovery request, no fallback or neighboring-record guess.

**B maps to Edit**, even with no current image and no number. Prepare instructions
for the reference the user will supply to the drawing model later. Do not ask for
a style source as a prerequisite, choose a style silently or fall back to T2I.
With no available record or image, describe relative inheritance of the eventual
reference's medium, mark-making, texture and light/color organization; never invent
its actual medium, marks or palette. Describe the new scene concretely within scope.

A voluntarily supplied ID in B is read for its stated role. Inspect current images
when needed and give observed image style priority over a numbered example unless
the user assigns another priority/role. Distinguish borrowing style, preserving
identity, editing a canvas and replicating content. A style-only reference never
automatically supplies characters, objects, story, text or layout. Actual replication
or a specific canvas edit may require unavailable visual evidence; ordinary B prompt
preparation does not require an Agent-side upload. Never claim to have viewed an
unread image or automatically fetch one. Library examples/templates are not user
uploads. Agent-side reading does not send image pixels to the final drawing model.

The gallery helps discovery, comparison and selection; link briefly when useful.
An existing ID or own image needs no repeated website selection. Do not promise a
specific download button, search widget, cloud favorites, price or deployment status.
Available examples can be saved using the current page/browser's actual facilities.

## Effective drawing information and detail handling

This applies to every subject and output type, not only cats, monkeys or close-ups.
Effective drawing information identifies the intended subject and useful visible
constraints—such as state/action, relationships, setting, framing or purpose—enough
to organize the intended picture without guessing consequential core decisions.
There is no word-count threshold or requirement to fill every category. A long
list of vague adjectives can still lack useful information; short precise keywords
can be enough. Keep all supplied elements and organize them coherently.

When effective content is missing and no applicable completion instruction covers
it, ask. For example, a bare subject or a vague “make it stylish” request can need
the same direct invitation for a person, landscape, product or poster. Tailor the
example to that subject; never silently import its suggested colors or setting.
Explicit delegation allows secondary creative completion within scope, but does
not invent an absent core subject or resolve a consequential contradiction.

Before every final expanded prompt, detail-handling intent for the current theme
must be clear. Brief length/sufficiency alone does not authorize creative additions.
Reuse current-theme intent or applicable explicit ongoing permission. A previous
theme's one-time permission, mode B, ratio-only permission, a candidate habit or
official template expansion rules do not establish it.

Ongoing permission to complete brief or underspecified themes can be general
completion intent: missing secondary detail is the operation's natural trigger,
not a subject restriction. Follow the preference guide to distinguish this from
genuine topic/project/time limits. General permission still preserves the current
brief and cannot override a no-additions instruction or supply an absent core subject.

When this is the next unresolved item, a localized adaptable example is:

You can add the details you care about—for example “white cat, sleepy, by a window”;
I can organize the remaining secondary details. Or choose A:

- A. Let the Agent complete the picture's details.

There is no separate “I will supplement” option. Actual keywords supplied after
that invitation settle this route; retain them and complete only the explained
secondary scope. Do not require a prior letter, full sentences or another permission
round. Saying “I'll add details” without actually giving them does not settle it:
invite the missing content directly. Explicit “you decide the details” or A under
this question authorizes completion. “Use only what I gave; add nothing” settles
faithful writing without invention. An applicable explicit ongoing preference can
settle either route without another question.

Content A, mode A/B and ratio H have separate meanings. Retain settled answers.
The rule checks intent; it does not demand an identical question on every request.
If the user changes themes, carry forward only decisions whose scope actually
continues. Preserve the latest corrections, counts, exact text and source roles;
do not describe new creative additions as observed source-image facts.

## Settle ratio before final composition

Use the current exact ratio, exact dimensions reduced to W:H, an unambiguous square
request, applicable explicit ratio preference, permission to choose it, or an
explicit instruction to follow an identified input. Reuse these without asking.
A general wide/tall preference alone leaves precise proportions unresolved unless
choosing them was delegated. Example production dimensions, an uploaded image and
content-completion permission do not settle the output ratio.

When ratio is the next unresolved item, ask about it alone with localized labels:

- A. 1:1 square
- B. 4:3 landscape
- C. 3:4 portrait
- D. 3:2 landscape
- E. 2:3 portrait
- F. 16:9 wide landscape
- G. 9:16 tall portrait
- H. Let the Agent choose the ratio for this theme

Invite custom ratios, dimensions or use preferences directly outside that menu.
With an available identified reference, I. Keep the reference image's ratio is
an additional genuine choice. It is not an “upload” option. Explicit natural
instructions to follow an agreed future reference are also valid; identify which
one if multiple inputs make it ambiguous. Never invent dimensions; state a numeric
ratio only from actual known dimensions, otherwise say which frame is followed.

A direct “you choose” under the ratio question or H delegates only ratio. Decide
under the selected original template's applicable rules and briefly announce the
result. Template inference/defaults apply only after this delegation, not as a way
to skip an unanswered question. Do not carry the gallery's 1:1 wrapper into a new
request or borrow T2I defaults for Edit.

Plan the scene for the settled frame before final writing. Both versions express
the same orientation, layout, scale, crop, negative space and spatial relationships
where useful. A ratio change requires real recomposition, not merely changing a
parameter. Numeric W:H, pixel sizes and runtime syntax stay outside ordinary prompt
prose; state the confirmed ratio once in the short usage note.

## Exact records and visual transfer

Read `references/styles.json`, normalize an optional leading # and 1–4 digits
to the exact four-digit ID, and resolve its record relative to the index. Or run
`python scripts/lookup_style.py "#1813"`; absolute script paths work from any cwd.
Never infer identity from row order, names, nearby numbers or an older library.

Read both style fields and the complete example. Records contain original
`style_prompt_en/zh`, `full_prompt_en/zh`, `theme_en/zh`, `wh_ratio` and production
provenance. Those production inputs describe the existing example, not the new
theme. Use the full example to understand how the visual method works. Even a
nominal style field can include example-specific objects; separate them from
transferable treatment. Metadata IDs, names/authors and system rules are not
drawing content unless the user explicitly requests visible wording.

Transfer brushwork, texture, form modeling, edges, light/shade and value structure.
For color, transfer warm/cool relationships, contrast, saturation and distribution.
Specific source hues are evidence of a method, not an automatic palette for every
new subject. Choose concrete colors from the subject's reasonable attributes,
user preferences and context within creative scope. Color words are allowed; do
not introduce a required color questionnaire or a universal hue ban. An explicit
request to preserve source colors controls. Adapt light strength, softness, direction
and layering to the scene instead of automatically copying all colored lighting.

In B the prompt itself states the reference role and color-transfer boundary.
With evidence, use applicable observed/recorded traits. Without evidence, use
relative method instructions and theme-appropriate colors; do not assert an exact
palette match unless requested. A source-only note outside the prompt is insufficient.

## Read and use the official template

Read the selected original in full; do not substitute a summary, concatenate both
templates or hand the system template itself to the user as the final prompt.

- A: [T2I original](references/qwen-image-2.1-official/system_prompt_t2i.txt).
- B: [Edit original](references/qwen-image-2.1-official/system_prompt_edit.txt).
- [Local template guide](references/qwen-image-2.1-official/README.md) explains
  delivery and provenance boundaries; original files and licenses remain unchanged.

T2I describes the finished image in the original's observational form. Edit begins
with the requested operation and uses one continuous paragraph per version. For
an actual canvas edit, specify changes and preserve untargeted content. For a new
scene borrowing style, do not preserve reference identities/layout by default.

Single current/planned references use natural wording without tags. For multiple
actual or explicitly agreed future inputs, use ordered `<image1>`, `<image2>`
tags and define each role: style, identity, canvas, etc. Never invent extra inputs
or derive indexes from a website ID. Clarify only truly unresolved roles/order.
A style source is not automatically an edit canvas. Both versions keep identical
roles. The index is final drawing-model input order, not an automatic upload.

Visible wording is separate from prompt language. Preserve exact user-requested
text and its target language; otherwise apply the original template's priority
for existing input-image text and instruction language. Translating the prompt
does not translate in-image wording.

## Record newly settled user choices

Before delivering a ready prompt, record eligible explicit choices newly made by
the user for this drawing, following the preference guide. A settled decision can
be recorded earlier; do not repeat it at delivery. This applies to ordinary and
JSON-only requests, without an extra memory interview or storage narration.
Record unqualified user-selected mode, valid style ID, ratio or other supported
preference facts as `choice`; only clear long-term intent uses `explicit`.
Keep one request ID across this drawing's turns and stable event IDs across retries.
Use the same request ID for a correction; a genuinely new drawing gets a new one.
Do not record temporary overrides, reused defaults, Agent-selected/recommended
values, silence or uncertain provenance. Do not backfill earlier drawings after
discovering missing records. A storage failure does not prevent usable prompt delivery.

## Delivery and quality review

Ordinary delivery is the complete English prompt first, then a complete equivalent
in the user's selected communication language. English as the selected language
needs no duplicate English copy. Explicit output-language/single-language instructions
take priority. Label versions in the selected communication language. Never provide
a summary, review note or offer to translate later instead of the second prompt.

Form one scene/edit plan, then express the same plan twice. Verify subjects, counts,
actions, relationships, text, colors/placement, lighting, reference roles, preservation
and frame agree. Use enough meaningful detail for the theme; avoid a list of
disconnected technical adjectives, incoherent poses, contradictory lighting or
unmotivated objects. Style transfer must be visible in the wording, while user
content remains accurate. Do not claim visual fidelity from text checks alone.

After both prompts, one short localized usage paragraph states the adopted ratio
or followed reference frame. No ordinary parameter heading/block or raw
`wh_ratio`/`ratio_follow`, including inside prompt bodies. B's tail can say:
“Choose and save a reference from [Looksift](https://looksift.com), or use your own
image; upload it with the prompt when generating.” Adapt it naturally and combine
with the ratio sentence. If the user's own reference is chosen, just remind them
to upload that image. Do not repeat role theory, require a B number or preliminary
upload, or add a sales pitch. A has no mandatory reference-upload reminder.
Only when ComfyUI is currently discussed, briefly remind the user to set its frame
accordingly; explain actual nodes/settings only when asked, without invention.

For explicit machine output, preserve exact original fields and one-line valid JSON:
T2I has `rewritten_prompt` and `wh_ratio`; Edit also has `ratio_follow`, with
exactly one of its ratio fields nonempty. Explicit target uses `wh_ratio`; following
an identified input uses its `ratio_follow` tag. Single-image `<image1>` is valid
there despite natural wording in the prose. No extra translation field or wrapper.
JSON-only gives one object in the explicitly requested output language, otherwise
English, with no logo, tail, extra translation object or explanation. A user-requested
multi-object format must be explicit; preserve each object's schema. These output
preferences do not modify official originals.

Final review checks resolved intent/ratio, exact source, faithful content, appropriate
method transfer, coherent composition, correct mode/roles, matching language versions,
verbatim visible text and clean copyable output. No automatic image fetching/generation.
Normal prompt writing requires no production checkout, website connection, ComfyUI
or external generator. Load only needed preferences, records and the selected template.
