# Looksift MCP 1.10.0

[English](README.md) · **简体中文**

让你的 Agent 使用 Looksift 的视觉参考、可编辑姿势场景和动作时间轴。

[连接说明](mcp/1.10.0/README.md) · [最新版本](https://github.com/lzhfirst/looksift/releases/latest) · [下载安装包](https://github.com/lzhfirst/looksift/releases/download/mcp-v1.10.0/looksift-1.10.0.zip) · [官网](https://looksift.com/gallery/mcp.html)

## 连接

1. 添加远程 **Streamable HTTP** MCP 服务：`https://looksift.com/api/mcp`。
2. 按客户端提示，在浏览器中登录 Looksift Pro 账号并授权。不支持浏览器授权的客户端可使用私有 MCP 令牌，配置方法见连接说明。
3. 启用工具，直接让你的 Agent 调用 Looksift。

不需要本地服务器、下载图库或单独配置模型 API 密钥。支持 Agent Plugin 的客户端可以导入安装包；其他 MCP 客户端直接添加同一个远程地址。

## 使用自己的 Agent 创作

- 获取风格、配色、服装、排版、表情及其真实参考图。
- 检索 2,446 个原生动作及测量帧，创建和修改 XBot 姿势场景。
- 从结构化姿势场景创建动作时间轴，打开同一份动作编辑器文档，自行播放和调整。
- 获取导演编号对应的视觉方法、电影参考和一份完整通用提示词。
- 根据文字或参考图编写 H3 视频提示词。

语义理解与参考选择由用户自己的 Agent 完成；MCP 不调用 Looksift DP。最终出图或视频生成需要客户端具备相应工具。动作时间轴不等于生成或导出视频，也不会同步浏览器本机作品。

安装包仅包含远程连接配置、说明和品牌图标。导入前可使用同目录 SHA-256 文件核对安装包。
