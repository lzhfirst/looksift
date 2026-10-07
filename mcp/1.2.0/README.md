# Looksift MCP 1.2.0

Use real numbered style, palette and outfit references from [Looksift](https://looksift.com)
with your Agent. Responses and prompts follow your language. Reference data stays
on Looksift; no catalogue download or local MCP server is needed.

## Connect

1. In an MCP-compatible client, add a remote **Streamable HTTP** server.
2. Set the URL to **`https://looksift.com/api/mcp`**. No login, API key or extra
   authorization header is required for these public reads.
3. Enable its tools, choose a number on the website and send your request.

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
data only; pose, action, expression, monster and private collections are outside
this version.

## Try it

- “用 Looksift 47 号画风画一只戴黄帽的猫，16:9。”
- “用 A032 给我上传的人物换装，保持身份、姿势和其他构图不变。”
- “Use Looksift style 47 for a seaside bookshop. Prompt-only, with both reference
  images and the input order. Do not generate images.”

## Tools

`looksift_get_style`, `looksift_get_palette`, `looksift_get_clothing`,
`looksift_get_reference_image`, and `looksift_get_prompt_guide` are read-only.
The guide returns the full pinned original edit or text-to-image template,
workflow, source, SHA-256 and license. See [the contract](skills/looksift/references/mcp-contract.md).

## Version history

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
