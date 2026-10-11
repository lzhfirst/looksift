# Looksift MCP 1.6.1

**English** · [简体中文](README.zh-CN.md)

Connect your Agent to Looksift's live visual references and prompt-writing tools. This repository distributes the remote MCP connector.

[Connection guide](mcp/1.6.1/README.md) · [Latest release](https://github.com/lzhfirst/looksift/releases/latest) · [Download connector ZIP](https://github.com/lzhfirst/looksift/releases/download/mcp-v1.6.1/looksift-1.6.1.zip) · [Website](https://looksift.com/gallery/mcp.html)

## Connect

1. Add a remote **Streamable HTTP** MCP server in your Agent client.
2. Set its URL to **`https://looksift.com/api/mcp`**. Public reads need no login or API key.
3. Enable the tools and ask the Agent to use Looksift.

Or send your Agent: “Install Looksift MCP using https://github.com/lzhfirst/looksift/tree/main/mcp/1.6.1 and verify the remote connection.” If the client supports Agent Plugin packages, the ZIP supplies the same MCP connection with its display metadata and icons. Other clients can use the endpoint directly.

## What you can do

- Choose a style, palette, outfit or layout number, then describe your own image.
- Describe a facial expression and adjust its intensity.
- Create and edit a pose scene, inspect its actual reference image and continue adjustments in the website editor.
- Give the Agent a picture or describe a video to receive a complete H3 video prompt, including timing, media roles and dialogue.

Your Agent uses its actual image-reading and generation capabilities. Looksift supplies reference data, scene references and complete writing guidance over MCP; final image or video generation requires a capable host tool.

The connector contains only connection metadata, setup documentation and brand icons. No standalone Skill, local catalogue or Skill installation is distributed. All writing guidance is obtained through MCP tools.

## Package verification

The website, GitHub and [Hugging Face](https://huggingface.co/datasets/larryqq/looksift-mcp) provide the same connector ZIP. Verify it against the adjacent SHA-256 file. Read [source notices](mcp/1.6.1/THIRD_PARTY_NOTICES.md) for the materials returned by remote tools.
