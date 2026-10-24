# Looksift MCP 1.8.0

**English** · [简体中文](README.zh-CN.md)

Connect your Agent to Looksift's live visual references and prompt-writing tools. This repository distributes the remote MCP connector.

[Connection guide](mcp/1.8.0/README.md) · [Latest release](https://github.com/lzhfirst/looksift/releases/latest) · [Download connector ZIP](https://github.com/lzhfirst/looksift/releases/download/mcp-v1.8.0/looksift-1.8.0.zip) · [Website](https://looksift.com/gallery/mcp.html)

## Connect

1. Add a remote **Streamable HTTP** MCP server in your Agent client.
2. Set its URL to **`https://looksift.com/api/mcp`**. Public reads need no login or API key.
3. Enable the tools and ask the Agent to use Looksift.

Or send your Agent: “Install Looksift MCP using https://github.com/lzhfirst/looksift/tree/main/mcp/1.8.0 and verify the remote connection.” If the client supports Agent Plugin packages, the ZIP supplies the same MCP connection with its display metadata and icons. Other clients can use the endpoint directly.

## What you can do

- Choose a style, palette, outfit or layout number, then describe your own image.
- Describe a facial expression and adjust its intensity.
- Create and edit a pose scene, inspect its actual reference image and continue adjustments in the website editor.
- Give the Agent a picture or describe a video to receive a complete H3 video prompt, including timing, media roles and dialogue.

Your Agent uses its actual image-reading and generation capabilities. Looksift supplies reference data, scene references and complete writing guidance over MCP; final image or video generation requires a capable host tool.

The connector contains only connection metadata, setup documentation and brand icons. No standalone Skill, local catalogue or Skill installation is distributed. All writing guidance is obtained through MCP tools.

## Women and men

Choose the Women or Men category and its displayed palette or outfit number.
Keep their independent identities even when colors match. For a two-image men
reference, Image 1 is clothing and Image 2 is the palette. Its portrait preview
is an output example, never an identity input. Follow the image roles returned
by each MCP record; all previous tools remain available.

## Package verification

The website, GitHub and [Hugging Face](https://huggingface.co/datasets/larryqq/looksift-mcp) provide the same connector ZIP. Verify it against the adjacent SHA-256 file. Read [source notices](mcp/1.8.0/THIRD_PARTY_NOTICES.md) for the materials returned by remote tools.

## Native pose motions / 原生动作

MCP 1.8.0 adds three motion lookup tools and native scene version 2. Your Agent understands words or images, searches 2,446 measured motions, selects a source-pinned frame, and creates or edits the website XBot scene. MCP returns an actual PNG and an editor link. No Looksift DP/DeepSeek request is made. Legacy version 1 scenes remain supported.

新版由用户自己的 Agent 理解语义、检索和选择真实动作帧，MCP 提供动作索引、场景编辑、实际参考图与同一场景的网页编辑入口，不调用 Looksift 的 DP。
