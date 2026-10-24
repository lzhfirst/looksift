# Looksift MCP 1.8.0

[English](README.md) · **简体中文**

让 Agent 连接 Looksift，读取实时视觉参考和提示词规范。这个仓库只发布远程 MCP 连接器。

[连接说明](mcp/1.8.0/README.md) · [最新发布](https://github.com/lzhfirst/looksift/releases/latest) · [下载连接包](https://github.com/lzhfirst/looksift/releases/download/mcp-v1.8.0/looksift-1.8.0.zip) · [官网入口](https://looksift.com/gallery/mcp.html)

## 连接方法

1. 在 Agent 客户端添加远程 **Streamable HTTP** MCP 服务。
2. 地址填写 **`https://looksift.com/api/mcp`**，公开数据读取不需要登录或 API Key。
3. 启用工具，然后告诉 Agent 使用 Looksift。

也可以直接说：“请按照 https://github.com/lzhfirst/looksift/tree/main/mcp/1.8.0 的说明安装 Looksift MCP，并验证远程连接。”支持 Agent Plugin 包的客户端可以使用 ZIP 中的连接配置、名称和图标；其他 MCP 客户端直接配置上面的地址即可。

## 能做什么

- 选择画风、配色、服装或排版编号，再描述自己要画的内容。
- 用自然语言描述表情，并继续调整强弱。
- 创建、修改姿势场景，读取真实场景参考图，也能打开网站编辑器继续调整。
- 提供图片或描述视频，让 Agent 写出包含时长、素材用途和对白的完整 H3 视频提示词。

Agent 按它实际具备的看图和生成能力工作。Looksift 通过 MCP 提供参考资料、场景参考和完整提示词规范；实际生成图片或视频需要宿主有对应工具。

连接包只有远程连接配置、说明和品牌图标，不再分发独立 Skill、本地素材库或 Skill 安装入口。所有提示词规范都由 MCP 工具提供。

## 女装和男装

先选女装或男装，再使用页面显示的配色或服装编号。颜色相同也不能混用两个类目的独立编号。男装两图参考按图 1 服装、图 2 色板使用，人物预览只是效果示例，不能作为身份输入。始终遵守各条 MCP 记录返回的图片用途，原有 16 个工具全部保留。

## 核对安装包

官网、GitHub 和 [Hugging Face](https://huggingface.co/datasets/larryqq/looksift-mcp) 提供同一份连接包，可用附带的 SHA-256 文件核对。远程工具返回资料的来源说明见[来源声明](mcp/1.8.0/THIRD_PARTY_NOTICES.md)。

## Native pose motions / 原生动作

MCP 1.8.0 adds three motion lookup tools and native scene version 2. Your Agent understands words or images, searches 2,446 measured motions, selects a source-pinned frame, and creates or edits the website XBot scene. MCP returns an actual PNG and an editor link. No Looksift DP/DeepSeek request is made. Legacy version 1 scenes remain supported.

新版由用户自己的 Agent 理解语义、检索和选择真实动作帧，MCP 提供动作索引、场景编辑、实际参考图与同一场景的网页编辑入口，不调用 Looksift 的 DP。
