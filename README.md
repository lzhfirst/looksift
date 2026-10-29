# Looksift MCP 1.10.0

**English** · [简体中文](README.zh-CN.md)

Connect your Agent to Looksift's visual references, editable Pose scenes and Actions timelines.

[Connection guide](mcp/1.10.0/README.md) · [Latest release](https://github.com/lzhfirst/looksift/releases/latest) · [Download connector](https://github.com/lzhfirst/looksift/releases/download/mcp-v1.10.0/looksift-1.10.0.zip) · [Website](https://looksift.com/gallery/mcp.html)

## Connect

1. Add a remote **Streamable HTTP** MCP server at `https://looksift.com/api/mcp`.
2. Complete the client's browser authorization with your Looksift Pro account. Clients without browser authorization can use a private MCP token in protected headers; see the connection guide.
3. Enable the tools and ask your Agent to use Looksift.

No local server, catalogue download or separate model API key is needed. Agent Plugin clients can import the optional connector ZIP; other MCP clients use the same endpoint directly.

## Create with your own Agent

- Read styles, palettes, outfits, layouts and expressions with their actual references.
- Search 2,446 native motions and measured frames; create or edit native XBot Pose scenes.
- Build Actions timelines from structured Pose scenes; open the same timeline paused in the Actions editor and play or adjust it there.
- Read numbered director references, film stills and one detailed model-neutral prompt.
- Prepare H3 video prompts from text or image references.

Your Agent interprets the request and selects the references. MCP does not call Looksift DP. Final image or video generation requires a capable host tool. Actions timeline creation is not video generation or export, and does not synchronize local saved works.

The ZIP contains only remote connection metadata, instructions and brand icons. Check the adjacent SHA-256 checksum before importing it.
