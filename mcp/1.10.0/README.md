# Looksift MCP 1.10.0

Use real style, palette, outfit, layout, facial-expression, editable pose-scene and Actions timeline references from [Looksift](https://looksift.com)
with your Agent. Responses and prompts follow your language. Reference data stays
on Looksift; no catalogue download or local MCP server is needed.

## Ask your Agent to install

Choose one of the three equivalent entries below and copy its request to your Agent. It can configure a remote MCP
connection when its client grants configuration permission; otherwise it should
provide the three short manual steps below. Copying a request does not install
anything by itself. No local server, paid API key or catalogue download is needed.

GitHub:

```text
请帮我安装 Looksift MCP，并按这个页面的说明配置远程连接：https://github.com/lzhfirst/looksift/tree/main/mcp/1.10.0；如果你没有配置权限，请给我最短的手动添加步骤。
```

Hugging Face:

```text
请帮我安装 Looksift MCP，并按这个页面的说明配置远程连接：https://huggingface.co/datasets/larryqq/looksift-mcp；如果你没有配置权限，请给我最短的手动添加步骤。
```

English GitHub request: “Please help me install Looksift MCP and configure its
remote connection using this guide: https://github.com/lzhfirst/looksift/tree/main/mcp/1.10.0;
if you lack configuration permission, give me the shortest manual steps.”

English Hugging Face request: “Please help me install Looksift MCP and configure
its remote connection using this guide: https://huggingface.co/datasets/larryqq/looksift-mcp;
if you lack configuration permission, give me the shortest manual steps.”

Direct website ZIP: [download looksift-1.10.0.zip](https://looksift.com/gallery/downloads/looksift-1.10.0.zip)
and [SHA-256 checksum](https://looksift.com/gallery/downloads/looksift-1.10.0.zip.sha256).
This MCP-only connector is the same ZIP provided by GitHub and Hugging Face. Attach it to your Agent,
then paste this request:

```text
请根据我附上的 looksift-1.10.0.zip 安装并连接 Looksift MCP，使用压缩包中的远程连接配置；如果无法直接配置，请给我最短的手动添加步骤。
```

English: “Please install and connect Looksift MCP using the remote configuration
in my attached looksift-1.10.0.zip; if you cannot configure it directly, give me the
shortest manual steps.” The ZIP supplies only remote client configuration, connection instructions and brand icons. Prompt-writing rules/templates are returned by MCP tools. It does not run an MCP server on your computer.

For the receiving Agent: use the client's supported remote MCP configuration
mechanism and the real endpoint below. Do not download or run a local server.
Do not assume that every MCP client can install a Codex/Agent Plugin ZIP. Use that
optional package only when the client actually supports it. If configuration
access is unavailable, explain where to add a remote server using the client's
known controls, or give the generic three steps below when its UI is unknown.
Confirm installation only after the connection works; do not claim a copy action
or a prepared configuration already installed the service.

## Then send a test request

If the client supports an @ selector, select **Looksift** there first. In Codex
that selection creates the actual plugin mention; pasting ordinary `@Looksift`
text does not. In other MCP clients, simply send the request to use the already
connected Looksift tools.

```text
@Looksift 请调用已连接的 Looksift 工具，按 47 号画风画一个女人，3:4。
```

English: “@Looksift Use the connected Looksift tools to draw a woman with style
47, in 3:4.” Style 47 has been verified through the live MCP. The Agent uses both
actual reference variants independently. Without the required drawing/reference
input capability, it returns complete prompts, actual references and brief steps.

## Manual connection

1. In an MCP-compatible client, add a remote **Streamable HTTP** server.
2. Set the URL to **`https://looksift.com/api/mcp`**. In clients supporting MCP
   browser authorization, connect and complete the Looksift sign-in/consent page
   with an active Pro account. If the client only supports protected headers,
   create a private token on the MCP page and set
   `Authorization: Bearer <your token>`. Never publish or commit this token.
3. Enable its tools, choose a numbered website reference or describe a facial
   expression, pose/scene or video idea, and send your request.

Clients with Agent Plugin support can import this package using their supported
plugin workflow. It contains `plugin.json`, `mcp.json`, connection instructions, notices and the unchanged
Looksift icons. There is no installable Skill or bundled local catalogue. There is no universal install button; client capabilities and UI
vary. The remote endpoint also serves the workflow and full prompt templates to
clients that do not install the plugin. This package is not an OpenAI directory
listing or approval, and it does not require a paid OpenAI API account.

## Women and men references

Choose the **Women** or **Men** category and use the displayed palette number or
outfit A-number. Matching colors do not make the two outfits interchangeable.
Existing requests that omit a series continue to select women.

For MCP clients, pass `series: "men"` to `looksift_get_palette`,
`looksift_get_clothing` and `looksift_get_reference_image`. Preserve the returned
`appearance_id`, public `number` and `appearance_release`. Male palette image
reads also retain the returned palette `release`; male outfit reads use
`appearance_release` instead of a women clothing release. A missing male result
must never be replaced with the same-color women entry or its source number.

Use each record's returned `reference_order` and `reference_images`:

- `clothing-palette-v1`: exactly two generation inputs, **Image 1 clothing,
  Image 2 palette**. Create a new fictional adult model. The separately returned
  portrait `preview_image` is an output example, never an identity input.
- Existing `portrait-palette-clothing-v1` records retain their authored input
  roles. Do not force a two-input record into that older three-input pattern.

女装和男装以页面显示的独立编号为准。男装两图记录按“图 1 服装、图 2 色板”使用，
人物预览图只是效果示例，不能作为人物身份参考。始终遵守该条记录返回的图片用途。

## Choose a reference

- [Styles](https://looksift.com/gallery/styles.html): a selected style provides
  two independent versions using its actual **Qwen reference** and **GPT reference**
  images on the same release. These labels identify examples, not the renderer.
- [Palettes and outfits](https://looksift.com/gallery/colors.html): choose an exact
  palette number or an independent outfit A-number from a palette detail. A palette
  applies its real HEX colors. An outfit applies its actual clothing-and-shoes
  reference; it does not silently select the palette or the catalogue person's face.
- [Layouts](https://looksift.com/gallery/layouts.html): choose a stable L-number,
  such as L0001, then describe your own subject and exact title. The Agent adapts
  composition and typography, with English, Chinese, German and French prompts.
  Your requested canvas ratio takes precedence over the reference dimensions.
- [Expressions](https://looksift.com/gallery/expression.html): describe the
  expression naturally; no number is required. Choose natural, Pixar or anime
  facial movement and adjust the intensity (0–150%, default 100%). For example,
  ask for laughing at natural 65%, then make it stronger or softer in conversation.
  These modes change facial movement, not your person or overall art style. The
  real reference PNG is rendered from the chosen state on a neutral 3D head.
  Supply your person as Image 1 and the expression reference as Image 2; the Agent
  preserves identity, clothing, pose and composition. Fine controls are on the
  expression page.
- Any one kind is enough. Clear natural numbers such as style 47 / 047 / 四十七
  or outfit 三十二号 / A032 are accepted in their own context. Missing or ambiguous
  choices are clarified; invalid entries are never silently replaced.

## What you receive

A client with an image tool supporting all needed reference inputs can generate
the requested image. A numbered style produces two separate images, with the same
subject and aspect ratio. An outfit-only edit uses one image and preserves the
user original's identity, pose and unrequested composition. Supply that original
for a person edit.

Without drawing capability, or when the drawing tool cannot accept the required
references, the Agent delivers **complete prompts plus actual reference images or
download links**. Each kit maps Image 1, Image 2, etc. to the prompt. Download the
listed references, upload them in that order to a reference-capable drawing tool,
paste the matching prompt and set the requested aspect ratio. Run the Qwen and GPT
style kits separately. This fallback does not claim images were generated.

`prompt-only` never generates; `image+prompt` includes the actual prompt as well
as generated images when the client is capable. The user's output format wins.
Image generation availability and limits depend on the client. MCP reads public
parameters and references and accepts bounded structured scenes. Monster
and private collection catalogues are outside this version. The server renders
neutral expression heads and scene references; your Agent creates final artwork.
Original images, private long prompts and chat history are not sent to MCP.
Scene geometry is sent via remote HTTPS and is not publicly cached.

## Editable pose scenes

Version 1.9.0 connects the website's 2,446 native motions and measured frame index.
Your Agent interprets the request and selects a real motion; Looksift does not
call DeepSeek or another model. Browse with `looksift_list_pose_motions`, search
with `looksift_search_pose_motions`, and inspect an exact frame with
`looksift_get_pose_motion`. Compare both action meaning and measured body
relationships. Copy the returned `library` and `poseFrame` into a version 2 scene,
then use the existing create, edit and reference tools. Never invent motion IDs.
New scenes use the native XBot skeleton. Old version 1 scenes remain readable;
their preset/joint/gaze parameters must not be applied to version 2 scenes.


Describe a scene, or attach an image for a vision-capable Agent to interpret.
A single-image scene is an editable approximation, not an exact 3D reconstruction.
The Agent keeps stable people/object IDs across follow-ups such as “a little
left”, “closer again”, “look at the cat” or “move the camera back”. Screen-left
is separate from the person’s left; eye gaze is separate from head/body direction.
Unrequested entities and camera settings stay unchanged. Animals represented by
proxy geometry are labelled as approximations, never real anatomical controls.

For an edit, **Image 1 is your original** (identity, appearance, clothing, animals
and art style); **Image 2 is the modified scene** (requested pose, position, gaze
and camera). The neutral models and helpers are guides, not final artwork.
For a new scene, the scene PNG is Image 1. Other selected references follow in
clearly stated order. A numbered style still produces two independent versions.

Every scene delivery includes a link that opens **that same scene** in the pose
editor, plus a short reminder that you can fine-tune it with the mouse. Geometry
is stored in the link’s fragment: it is not a private access-controlled link, so
share it only as intended. The scene PNG is returned directly as image bytes and
saved/attached by your Agent; there is no public scene download URL.

If the Agent has no vision, describe the important scene details or export a scene
from the [pose editor](https://looksift.com/gallery/pose.html). If it cannot draw
or cannot receive all the reference images, it supplies the actual PNG, complete
prompt, image order and brief manual steps instead of claiming it generated an
image. If it cannot save the PNG, use the same-scene editor link to export it;
the Agent must disclose that remaining manual step.

## Editable Actions timelines

Version 1.10.0 connects Actions to the same native XBot model and motion library
as Pose. Your own Agent understands the request, selects real motion IDs using
the pose-motion discovery tools, and supplies a structured timeline. No DeepSeek
or other Looksift model is called by these MCP tools.

- `looksift_create_action_scene`: supply a complete native Pose version 2 `scene`,
  a `duration` from 1 to 15 seconds and `motion`. Actor tracks are identified by
  `id` and contain `keys` and `nativeClips`; each clip supplies `motionId`, `start`
  and `end`, with optional `offset`, `speed`, `loop` and `blend`. Optional prop and
  camera tracks follow the tool's advertised schema. `locale` and `release` are
  optional. Keep the returned source release and use real library motion IDs.
- `looksift_edit_action_scene`: pass the previous complete returned `action` and
  a `motion` patch. Supplied tracks replace their corresponding tracks; omitted
  tracks remain unchanged. Optional `locale` and `release` use the same contract.

Each call returns `action`, `editor_url` and `release`. Retain the complete action
document for follow-up edits. The editor link opens that same timeline paused;
the user chooses when to play it and can adjust it in the Actions editor. This
does not upload local saved works, generate final artwork or export a video.
Do not invent missing scene data or claim access to a browser's local saves.

Example: “Use this native Pose scene to animate the first person kicking a ball
for 5 seconds. Keep the other people, props and camera unchanged, and give me the
editable Actions link.”

## Try it

- “根据这张女人和猫的图片建一个可修改的姿势场景，让女人往画面左边移一点，猫和镜头不动。”
  Then: “再靠近猫一点，只让眼睛看向它，头和身体别转。”
- “先做一个 3:4 的坐姿场景，再拉远镜头，给我参考图和完整提示词。”
- “让这张人物图大笑，真人自然 65%，保留人物身份和原来的画风。”
  Then: “再夸张一些。” Or: “保持真人自然，只调到 80%。”

- “用排版 L0001 做咖啡新品海报，标题写‘晨光’，使用我指定的画幅。”

- “用 Looksift 47 号画风画一只戴黄帽的猫，16:9。”
- “用 A032 给我上传的人物换装，保持身份、姿势和其他构图不变。”
- “Use Looksift style 47 for a seaside bookshop. Prompt-only, with both reference
  images and the input order. Do not generate images.”

## Tools

`looksift_get_style`, `looksift_get_palette`, `looksift_get_clothing`,
`looksift_get_layout`, `looksift_get_reference_image`, `looksift_list_expressions`,
`looksift_get_expression`, `looksift_get_expression_reference` and
`looksift_get_prompt_guide` expose public references.
`looksift_create_pose_scene`, `looksift_edit_pose_scene` and
`looksift_get_pose_scene_reference` validate, edit and render the supplied bounded
scene without publicly storing its content.
The guide returns the full pinned original edit or text-to-image template,
workflow, source, SHA-256 and license directly over MCP.
`looksift_get_video_prompt_guide` returns the full selected H3 guides and host
writing workflow for all five video modes, with pinned source hashes. It accepts
only mode, optional locale and duration; it does not inspect media or make videos.

## Version history

- **1.10.0** — Create and edit model-independent native XBot Actions timelines from structured Pose scenes, with same-document paused editor links. The host Agent interprets requests; MCP does not call DP. Browser authorization is documented alongside the private-token fallback.

- **1.9.0** — Native XBot motion discovery, measured frame search, source-pinned scene creation and PNG rendering. 16 MCP tools. The host Agent interprets and selects; no Looksift DP call.
- **1.7.0** — Women and men palette/outfit selections with independent public IDs, immutable appearance snapshots and exact reference-image roles. The same 13 MCP tools remain available.
- **1.6.1** — MCP-only distribution: no Skill entry, standalone Skill installer or bundled catalogue. Complete writing guidance is served remotely.
- **1.6.0** — H3 video prompt writing from text, keyframes and mixed references;
  complete portable guides, language-aware workflow, exact media and speech roles,
  and useful prompt kits without requiring a video generator or catalogue number.
- **1.5.1** — Original-image analysis, cumulative edit anchors and final artwork
  checks for pose-based edits, with targeted correction or honest limits.
- **1.5.0** — Editable structured pose scenes, state-preserving follow-ups,
  actual rendered scene PNGs, same-scene editor links, original/reference priority
  and complete capability-aware fallback instructions.
- **1.4.0** — Real expression presets, mode-specific parameters and exact-state
  PNG references; continuous conversational adjustment and complete fallback kits.
  All previous style, palette, outfit and layout capabilities remain available.
- **1.3.0** — Three equivalent installation entries: GitHub, Hugging Face and
  direct website ZIP; copyable Agent requests and one shared test request, with
  permission-aware remote setup and a short manual fallback.
- **1.2.0** — General remote Agent capability routing; complete prompt/reference
  fallback kits; original templates readable over MCP; public connection package.
- **1.1.1** — Reference-selection guidance and context-aware number handling.
- **1.1.0** — Independent outfit records and exact pinned reference lookup.

The same complete version is distributed on GitHub and Hugging Face. Check the
ZIP SHA-256 against its adjacent checksum before installation.

## Sources and licenses

Qwen Image 2.1 templates are provided by the remote prompt-guide tool together with their pinned sources, hashes and upstream license. The connector ZIP does not bundle these templates. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). Source terms remain applicable to material returned by the service.

## Write a video prompt from your picture

Give your Agent a picture and say, for example: “Use this as the opening frame.
Write an 8-second video prompt: she turns and walks away. Keep her appearance.
Do not generate a video.” No website number is needed.

Your Agent reads the picture and the H3 guide, then writes the prompt in your
language with the media order and a few usage steps. It supports text-only,
opening-frame, first/last-frame, ending-frame and mixed-reference requests. Say
whether a picture should be a video frame or only a character/style reference.
For a single generation, choose 4–15 seconds; longer ideas can be split into
agreed segments. Without a compatible video tool, you still receive the full
prompt and instructions. Looksift MCP provides writing rules, not video rendering.

The remote H3 guide returns the byte-preserved source documents and provenance hashes. An original public publisher URL has not been verified. These are tool response data; no Skill installation is needed or distributed.

## Director references · 1.9.0

An active Looksift Pro account is required. Create the private MCP access token on [Connect MCP](https://looksift.com/gallery/mcp.html) and supply it through your client's protected Authorization header configuration. The portable ZIP contains no credentials.

Use `looksift_list_directors` or `looksift_search_directors` for catalogue discovery, then `looksift_get_director` with the actual ID (001–200), `locale` (`zh-CN` or `en`) and returned `catalog_release`. It returns the complete structured visual reference, reviewed representative films and frames, and one detailed `universal_prompt`. Director numbers are independent of styles and other catalogues. The host Agent interprets the user request and adapts the subject locally. MCP does not call DP or any other model. Film titles and credits retain their actual identities; proposed palettes are creative guidance, not measured claims for every film.
