# 30分钟搭好AI发小红书机器人：OpenClaw + 小红书MCP完整教程

> 通过接入小红书 MCP，OpenClaw 可以直接帮你发布内容到小红书——包括图文、视频、评论、点赞、收藏，全部自动化。本文手把手带你从零完成配置，全程不超过 30 分钟。

---

## 前言：你还在手动发小红书？

每天打开小红书 App，手动写文案、挑图、加话题标签、定时发布……这套流程重复了多少次？

如果你用的是 OpenClaw，那你已经有了一个能帮你写文案的 AI 助手。但你知道吗？通过接入 **小红书 MCP**，OpenClaw 可以直接帮你**一键发布内容到小红书**——包括图文、视频、评论、点赞、收藏，全部自动化。

---

## 一、先搞清楚：MCP 是什么？

MCP（Model Context Protocol，模型上下文协议）是 Anthropic 推出的一套开放标准，让 AI 助手（比如 OpenClaw）能够像调用函数一样调用外部工具和服务。

简单理解：**MCP = AI 的"手"**。

有了 MCP，OpenClaw 就不再只是个聊天机器人，而是能真正操作软件、调用 API、执行任务的智能体。

而 **小红书 MCP**（`xpzouying/xiaohongshu-mcp`）就是专门为小红书定制的 MCP 服务，让 AI 能直接控制小红书的发布、搜索、评论等操作。

**项目地址**：[https://github.com/xpzouying/xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp)

目前项目已有 **26 位贡献者**，Docker Hub 拉取次数持续增长，社区活跃度很高。作者还把所有赞赏款项全部捐给了慈善（截至目前已捐 CNY 1300+），开源精神值得尊重。

---

## 二、小红书 MCP 能做什么？

在动手之前，先看看这个工具的能力边界：

| 功能 | 说明 |
|------|------|
| 🔐 登录管理 | 扫码登录，保存 Cookie，后续免登录 |
| 📸 发布图文 | 支持本地图片路径 / HTTP 图片链接 |
| 🎬 发布视频 | 支持本地视频文件，自动等待处理完成 |
| 🔍 搜索内容 | 关键词搜索，支持按点赞/时间/评论数排序 |
| 📋 获取推荐 | 拉取首页推荐 Feed 列表 |
| 💬 发表评论 | 自动评论指定帖子，支持回复二级评论 |
| ❤️ 点赞收藏 | 自动点赞/取消点赞，收藏/取消收藏 |
| 👤 用户主页 | 获取任意用户的主页信息和笔记列表 |
| ⏰ 定时发布 | 支持 1 小时至 14 天内的定时发布 |
| 🔒 可见范围 | 公开/仅自己/仅互关好友 |

**一句话总结**：只要是你在小红书 App 里能手动做的事，这个 MCP 基本都能让 AI 替你做。

---

## 三、环境准备

### 3.1 你需要准备的东西

- **OpenClaw**（已安装并可正常使用）
- **小红书账号**（建议已实名认证，未实名的新号容易触发验证）
- **一台 Mac / Windows / Linux 电脑**（服务器也可以）

### 3.2 安装方式选择

小红书 MCP 提供三种安装方式，根据你的技术背景选择：

**方式一：下载预编译二进制文件（推荐新手）**

直接从 GitHub Releases 下载对应平台的可执行文件，无需任何开发环境：

```bash
# macOS Apple Silicon（M1/M2/M3/M4）
xiaohongshu-mcp-darwin-arm64
xiaohongshu-login-darwin-arm64

# macOS Intel
xiaohongshu-mcp-darwin-amd64
xiaohongshu-login-darwin-amd64

# Windows x64
xiaohongshu-mcp-windows-amd64.exe
xiaohongshu-login-windows-amd64.exe

# Linux x64
xiaohongshu-mcp-linux-amd64
xiaohongshu-login-linux-amd64
```

下载地址：[https://github.com/xpzouying/xiaohongshu-mcp/releases](https://github.com/xpzouying/xiaohongshu-mcp/releases)

**方式二：Docker 部署（推荐服务器 / 懒人）**

```bash
# 拉取镜像
docker pull xpzouying/xiaohongshu-mcp

# 下载 docker-compose.yml
wget https://raw.githubusercontent.com/xpzouying/xiaohongshu-mcp/main/docker/docker-compose.yml

# 启动服务
docker compose up -d
```

Docker 版本会自动配置 Chrome 浏览器和中文字体，挂载 `./data` 存储 Cookie，暴露 **18060 端口**供 MCP 连接。

> ⚠️ **Docker 登录说明**：Docker 版本的登录流程与二进制版本不同，需要通过 VNC 或官方提供的登录接口完成扫码。具体步骤请参考项目文档：[docker/README.md](https://github.com/xpzouying/xiaohongshu-mcp/tree/main/docker)

**方式三：源码编译（适合开发者）**

```bash
# 需要先安装 Go 环境
# 配置国内代理（加速下载）
go env -w GOPROXY=https://goproxy.cn,direct

# 克隆并编译
git clone https://github.com/xpzouying/xiaohongshu-mcp.git
cd xiaohongshu-mcp
go build -o xiaohongshu-mcp .
go build -o xiaohongshu-login ./cmd/login/
```

> ⚠️ **首次运行注意**：程序会自动下载无头浏览器（约 150MB），请确保网络畅通，或提前开好代理。

---

## 四、登录小红书（关键步骤，仅限二进制方式）

> Docker 部署的登录方式请参考上一节的官方文档链接。

安装完成后，**第一步必须先完成登录**，否则所有操作都无法进行。

### 4.1 运行登录工具

```bash
# 给文件添加执行权限（macOS / Linux）
chmod +x xiaohongshu-login-darwin-arm64

# 运行登录工具
./xiaohongshu-login-darwin-arm64
```

运行后会弹出一个浏览器窗口，显示小红书登录页面。

> ⚠️ **注意**：此步骤需要有桌面环境（GUI）才能弹出浏览器窗口。如果你在无桌面的 Linux 服务器上操作，请改用 Docker 部署方式。

### 4.2 扫码登录

用手机小红书 App 扫描二维码完成登录。登录成功后，程序会自动保存 Cookie 到本地（`data/cookies.json`），后续运行 MCP 服务时会自动加载，无需重复登录。

### 4.3 启动 MCP 服务

```bash
# 默认无头模式（推荐，后台运行）
./xiaohongshu-mcp-darwin-arm64

# 非无头模式（调试时使用，能看到浏览器界面）
./xiaohongshu-mcp-darwin-arm64 -headless=false

# 如需代理（可选）
XHS_PROXY=http://127.0.0.1:7890 ./xiaohongshu-mcp-darwin-arm64
```

服务启动后，默认监听 `http://localhost:18060`，MCP 端点为 `http://localhost:18060/mcp`。

### 4.4 验证服务是否正常

```bash
# 使用官方 Inspector 工具验证
npx @modelcontextprotocol/inspector
```

打开输出的链接，在 URL 栏输入 `http://localhost:18060/mcp`，点击 Connect，再点击 List Tools，能看到所有工具列表说明服务正常。

---

## 五、在 OpenClaw 中接入小红书 MCP

这是最关键的一步：把小红书 MCP 服务接入 OpenClaw。

### 5.1 通过 OpenClaw 的 MCP 管理界面添加

在 OpenClaw 设置中找到 **MCP Servers** 配置项，添加一个新的 HTTP 类型 MCP 服务器：

- **名称**：`xiaohongshu-mcp`
- **类型**：Remote / HTTP
- **URL**：`http://localhost:18060/mcp`

### 5.2 通过配置文件添加（适合高级用户）

如果你使用的是 Claude Code CLI 模式，可以直接用命令添加：

```bash
claude mcp add --transport http xiaohongshu-mcp http://localhost:18060/mcp
```

验证是否添加成功：

```bash
claude mcp list
```

> 💡 **Docker 环境特别注意**：如果 MCP 服务运行在 Docker 容器内，连接地址应改为 `http://host.docker.internal:18060/mcp`，而不是 `localhost`。

### 5.3 验证 OpenClaw 能调用 MCP

配置完成后，在 OpenClaw 中输入：

```
检查一下小红书的登录状态
```

OpenClaw 会自动调用登录状态检查工具，返回当前登录状态。如果显示已登录，说明一切就绪！

---

## 六、实战演练：让 OpenClaw 帮你发小红书

现在进入最有意思的部分——实际操作。

### 场景一：AI 写文案 + 自动发布图文

**对 OpenClaw 说**：

```
帮我写一篇关于"春日咖啡探店"的小红书笔记，
配图使用这张：https://images.unsplash.com/photo-1495474472287-4d71bcdd2085

发布到小红书，加上话题标签：咖啡、探店、春日氛围感
```

OpenClaw 会：
1. 根据你的描述生成小红书风格的文案（带 emoji、口语化、有情绪）
2. 调用图文发布工具，传入标题、正文、图片链接、话题标签等参数
3. 完成发布，返回发布结果（含笔记链接）

### 场景二：竞品分析 + 批量搜索

**对 OpenClaw 说**：

```
帮我搜索小红书上关于"AI工具"的热门笔记，
按点赞数排序，给我分析一下爆款内容的规律
```

OpenClaw 会调用内容搜索工具，返回按点赞数排序的笔记列表，然后自动分析爆款标题规律、常用话题标签、内容结构特点等。

### 场景三：定时发布（错峰运营）

```
帮我写一篇关于"周末读书分享"的笔记，
明天上午10点发布，仅互关好友可见
```

OpenClaw 会在发布时设置定时时间和可见范围，无需你守着手机操作。

### 场景四：自动化互动（谨慎使用）

```
帮我搜索关键词"Python教程"的笔记，
找到点赞数最高的那篇，给它点个赞并收藏
```

> ⚠️ **风控提示**：自动化互动行为存在被平台检测的风险，建议：
> - 控制操作频率，不要批量操作
> - 互动内容要真实有价值
> - 新账号谨慎使用，建议先用老号测试

---

## 七、进阶玩法：OpenClaw + 小红书 MCP 自动化运营

掌握基础操作后，可以搭建更完整的自动化运营流程：

### 7.1 内容日历自动化

让 OpenClaw 维护一个内容日历，按计划自动生成内容草稿，配合系统 cron 定时触发发布：

```bash
# 示例：每天早上9点触发 OpenClaw 生成并发布内容
0 9 * * * /path/to/your/publish_script.sh
```

> 💡 OpenClaw 本身不内置定时任务功能，需要结合系统 cron 或外部调度工具实现定时触发。

### 7.2 竞品监控 + 快速跟进

```
帮我搜索"AI绘画"相关的最新内容，
分析其中点赞数最高的几篇的内容结构，
生成一篇类似但差异化的内容草稿给我看
```

> 💡 "监控"功能需要定期手动触发或配合 cron 脚本，OpenClaw 不会主动轮询。

### 7.3 评论区运营（推荐方式）

```
获取我最近发布的帖子的评论，
对每条评论生成个性化回复，
但先给我看一遍再发
```

这里体现了 **Human-in-the-Loop** 的最佳实践：让 AI 生成回复草稿，人工审核后再发布，避免翻车。**强烈推荐所有互动操作都采用这种模式。**

### 7.4 数据分析报告

```
获取我的个人主页数据，
分析最近30天发布的笔记，
哪些话题获赞最多？什么时间发布效果最好？
生成一份运营分析报告
```

---

## 八、避坑指南：这些问题你一定会遇到

根据社区的高频问题，整理了以下排查清单：

### ❓ 发布成功但小红书上看不到？

按顺序排查：

1. **用非无头模式重新发布一次**（`-headless=false`），观察浏览器实际操作
2. **更换不同的文案内容**重新尝试（可能触发内容审核）
3. **登录网页版小红书**，检查账号是否有风控提示
4. **检查图片大小**，过大的图片可能上传失败
5. **确认图片路径无中文字符**（会导致路径解析失败）
6. **网络图片链接**需确保可以正常访问

### ❓ MCP 服务连接失败？

- 确认服务已启动（`./xiaohongshu-mcp-darwin-arm64`）
- Docker 环境中使用 `http://host.docker.internal:18060/mcp`
- 如果 `localhost` 连不上，改用 `http://127.0.0.1:18060/mcp`
- 检查防火墙是否放行 18060 端口

### ❓ 程序闪退怎么办？

- 优先尝试**从源码编译**安装
- 或者改用 **Docker 部署**，稳定性更好
- Windows 用户参考官方 [Windows 安装指南](https://github.com/xpzouying/xiaohongshu-mcp/blob/main/docs/windows_guide.md)

### ❓ 账号触发实名认证？

这不是封号，是正常流程。完成实名认证后账号恢复正常。建议**使用前先完成实名认证**，特别是新注册的账号。

### ❓ 不想自己部署？

项目作者还提供了另一个工具 [xpzouying/x-mcp](https://github.com/xpzouying/x-mcp)，通过浏览器插件驱动 MCP，**无需部署服务**，对非技术用户更友好。

---

## 九、OpenClaw 接入 MCP 的最佳实践

用了一段时间后，总结几条经验：

**1. 先测试再自动化**

新功能先用 MCP Inspector 手动测试，确认正常后再让 OpenClaw 自动调用。

**2. 保持 Human-in-the-Loop**

特别是发布和互动操作，建议让 AI 生成内容后，人工确认再执行。OpenClaw 的对话式界面天然支持这种工作流。

**3. 控制自动化频率**

小红书有风控机制，建议：
- 发布频率：每天不超过 3-5 篇
- 互动操作：加入随机延时，模拟人工节奏
- 避免批量重复操作

**4. 内容质量优先**

MCP 帮你解决了"发布"的效率问题，但内容质量还是核心。让 OpenClaw 写出真正有价值的内容，而不是批量生产垃圾内容。

**5. 定期检查 Cookie 状态**

小红书的登录状态会过期，建议每隔一段时间检查一次登录状态，及时重新登录。

---

## 十、总结

| 对比项 | 手动运营 | OpenClaw + 小红书MCP |
|--------|---------|---------------------|
| 内容创作 | 30-60分钟/篇 | 3-5分钟/篇 |
| 发布操作 | 手动操作 | 一句话自动完成 |
| 数据分析 | 人工整理 | AI实时分析 |
| 竞品监控 | 定期手动查看 | 按需搜索汇报 |
| 定时发布 | 需要守着手机 | 配合 cron 自动执行 |

小红书 MCP 项目本身的完成度很高，文档详细，社区活跃，是目前最成熟的小红书自动化方案之一。结合 OpenClaw 的 AI 能力，可以实现从**内容生产**到**发布运营**的完整闭环。

当然，工具只是工具。真正让账号增长的，还是内容本身的价值。用 AI 提升效率，但不要用 AI 代替思考。

---

## 参考资源

- 项目主页：[github.com/xpzouying/xiaohongshu-mcp](https://github.com/xpzouying/xiaohongshu-mcp)
- 疑难杂症合集：[Issues #56](https://github.com/xpzouying/xiaohongshu-mcp/issues/56)
- Docker Hub：[hub.docker.com/r/xpzouying/xiaohongshu-mcp](https://hub.docker.com/r/xpzouying/xiaohongshu-mcp)
- 无部署版本：[github.com/xpzouying/x-mcp](https://github.com/xpzouying/x-mcp)
- n8n 集成教程：[examples/n8n/README.md](https://github.com/xpzouying/xiaohongshu-mcp/blob/main/examples/n8n/README.md)
- Cherry Studio 教程：[examples/cherrystudio/README.md](https://github.com/xpzouying/xiaohongshu-mcp/blob/main/examples/cherrystudio/README.md)

---

*如果这篇文章对你有帮助，欢迎点赞收藏～有问题欢迎在评论区交流。*
