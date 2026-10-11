# Looksift MCP 1.5.0

Use real style, palette, outfit, layout, facial-expression and editable pose-scene references from [Looksift](https://looksift.com)
with your Agent. Responses and prompts follow your language. Reference data stays
on Looksift; no catalogue download or local MCP server is needed.

## Ask your Agent to install

Choose one of the three equivalent entries below and copy its request to your Agent. It can configure a remote MCP
connection when its client grants configuration permission; otherwise it should
provide the three short manual steps below. Copying a request does not install
anything by itself. No local server, paid API key or catalogue download is needed.

GitHub:

```text
请帮我安装 Looksift MCP，并按这个页面的说明配置远程连接：https://github.com/lzhfirst/looksift/tree/main/mcp/1.5.0；如果你没有配置权限，请给我最短的手动添加步骤。
```

Hugging Face:

```text
请帮我安装 Looksift MCP，并按这个页面的说明配置远程连接：https://huggingface.co/datasets/larryqq/looksift-mcp；如果你没有配置权限，请给我最短的手动添加步骤。
```

English GitHub request: “Please help me install Looksift MCP and configure its
remote connection using this guide: https://github.com/lzhfirst/looksift/tree/main/mcp/1.5.0;
if you lack configuration permission, give me the shortest manual steps.”

English Hugging Face request: “Please help me install Looksift MCP and configure
its remote connection using this guide: https://huggingface.co/datasets/larryqq/looksift-mcp;
if you lack configuration permission, give me the shortest manual steps.”

Direct website ZIP: [download looksift-1.5.0.zip](https://looksift.com/gallery/downloads/looksift-1.5.0.zip)
and [SHA-256 checksum](https://looksift.com/gallery/downloads/looksift-1.5.0.zip.sha256).
This is the same ZIP provided by GitHub and Hugging Face. Attach it to your Agent,
then paste this request:

```text
请根据我附上的 looksift-1.5.0.zip 安装并连接 Looksift MCP，使用压缩包中的远程连接配置；如果无法直接配置，请给我最短的手动添加步骤。
```

English: “Please install and connect Looksift MCP using the remote configuration
in my attached looksift-1.5.0.zip; if you cannot configure it directly, give me the
shortest manual steps.” The ZIP supplies client configuration, the guide and
reference rules/templates. It does not run an MCP server on your computer.

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
2. Set the URL to **`https://looksift.com/api/mcp`**. No login, API key or extra
   authorization header is required for these public reads.
3. Enable its tools, choose a numbered website reference or describe a facial
   expression or pose/scene, and send your request.

Clients with Agent Plugin support can import this package using their supported
plugin workflow. It contains `plugin.json`, `mcp.json`, `skills/` and the unchanged
Looksift icons. There is no universal install button; client capabilities and UI
vary. The remote endpoint also serves the workflow and full prompt templates to
clients that do not install the plugin. This package is not an OpenAI directory
listing or approval, and it does not require a paid OpenAI API account.

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
parameters and references and accepts bounded structured scenes. Action, monster
and private collection catalogues are outside this version. The server renders
neutral expression heads and scene references; your Agent creates final artwork.
Original images, private long prompts and chat history are not sent to MCP.
Scene geometry is sent via remote HTTPS and is not publicly cached.

## Editable pose scenes

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
workflow, source, SHA-256 and license. See [the contract](skills/looksift/references/mcp-contract.md).

## Version history

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

The bundled Qwen Image 2.1 original templates, source manifest and license remain
unchanged. They use the upstream **Qwen RESEARCH LICENSE AGREEMENT**, including its
non-commercial condition and separate commercial-license requirement; they are
not Apache-licensed. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) and the
[full upstream license](skills/looksift/references/qwen-image-2.1-official/LICENSE).
Those terms do not grant rights to the Looksift brand or other package files.
