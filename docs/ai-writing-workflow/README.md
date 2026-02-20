# AI-Content-Workflow
#ai-content-workflow

AI 内容创作自动化工作流 - 从选题到发布的完整流程

## 命名

**八段式写作工作流** (8-Step Writing Workflow)

---

## 核心理念

让 AI 成为你的写作搭档，而不是替代品。

- ✅ 完整流程：从需求到发布
- ✅ 透明思考：每个决策都能看到
- ✅ 用户确认：选题、标题必须确认
- ✅ 质量保障：三遍审校 + Humanizer

---

## 流程概览

```
选题 → 调研 → 写作 → 审校 → 标题 → 审阅 → 保存 → 发布
```

---

## 完整流程

### 第一阶段：选题确认

| 步骤 | 操作 | 说明 |
|------|------|------|
| 8:00 | 推送 5 个选题 | 多来源验证，热门程度排序 |
| 你选 | 选一个话题 | 手动回复 |

### 第二阶段：调研准备

| 步骤 | 操作 | 说明 |
|------|------|------|
| 2.1 | Brave Search 搜索 | 至少 3 个来源验证 |
| 2.2 | 数据验证 | 确保信息准确，不过时 |
| 2.3 | 保存素材 | 记录来源和关键信息 |

### 第三阶段：写作创作

| 步骤 | 操作 | 说明 |
|------|------|------|
| 3.1 | 确定文章类型 | 热点事件 / 深度分析 / 工具教程 / 创业话题 |
| 3.2 | 选择结构 | 根据类型选 |
| 3.3 | 写初稿 v1 | 1500-3000 字 |

**结构选择：**

| 类型 | 结构 | 字数 |
|------|------|------|
| 热点事件 | 场景开头 → 核心亮点 → 观点 → 互动 | 800-1500 |
| 深度分析 | 背景 → 原因分析 → 趋势预测 → 建议 | 3000-10000 |
| 工具教程 | 痛点 → 解决步骤 → 案例 → 总结 | 1000-2000 |
| 创业话题 | 故事 → 洞察 → 建议 → 互动 | 1500-3000 |

### 第四阶段：三遍审校

| 遍数 | 检查内容 | 输出 |
|------|----------|------|
| 第一遍 | 事实准确性、逻辑清晰、结构合理、无编造数据 | v2 |
| 第二遍 | 降 AI 味：删套话、口语化、加真实细节 | v3 |
| 第三遍 | 标点、排版、节奏、段落长度 | final |

**降 AI 味具体操作：**
- 删除套话："归根结底"、"不可忽视"、"在这个时代"
- 拆解复杂句式："不仅...而且..." → 简单句
- 替换书面词："某种程度上" → "算是"
- 加入真实细节：时间，地点，数字、感受

### 第五阶段：标题拟定

| 轮次 | 数量 | 说明 |
|------|------|------|
| 第一轮 | 3 个 | 爆款标题（数字、悬念、情绪）|
| 第二轮 | 2 个 | 自然风格（符合作者风格）|
| 你选 | 1 个 | 最终标题 |

### 第六阶段：最终处理

| 步骤 | 操作 | 说明 |
|------|------|------|
| 6.1 | Humanizer 检查 | 24 种模式检测 |
| 6.2 | 你审阅 | 调整确认 |
| 6.3 | 封面 Prompt | 生成 3 个方案，你选 1 个 |
| 6.4 | 保存 | GitHub 每日目录 |
| 6.5 | 可选 | baoyu-post-to-wechat 发布 |

### 封面图生成

**方式一：Claude Code 本地**
- 使用 baoyu-cover-image skill
- 需要本地安装 Claude Code

**方式二：AI 生图工具（当前使用）**
- 生成 3 个风格方案 Prompt
- 你选好后，复制到 Midjourney / DALL-E / Google Imagen 等工具生图

---

## 核心原则

| 原则 | 说明 |
|------|------|
| 绝不编造数据 | 所有数据必须可验证 |
| 绝不过时信息 | 标注时间来源 |
| 绝不跳过确认 | 选题、标题必须你确认 |
| Think Aloud | 关键决策说明为什么 |

---

## 信息来源

| 来源 | 说明 |
|------|------|
| GitHub Trending | 热门 AI 项目 |
| Google AI 博客 | 官方动态 |
| TechCrunch / The Verge | 科技媒体 |
| Product Hunt | 热门产品 |
| AI 创业/融资 | 行业新闻 |

---

## 工具集成

| 工具 | 用途 |
|------|------|
| Brave Search | 信息搜索 |
| Humanizer | 去 AI 味 |
| baoyu-cover-image | 封面图生成 |
| baoyu-post-to-wechat | 公众号发布 |
| baoyu-xhs-images | 小红书图文 |
| baoyu-infographic | 信息图生成 |

---

## 封面 Prompt 生成

基于 baoyu-cover-image 技能，生成 3 个不同风格的封面 Prompt：

| 维度 | 选项 |
|------|------|
| --type | hero, conceptual, typography, metaphor, scene, minimal |
| --palette | warm, elegant, cool, dark, earth, vivid, pastel, mono, retro |
| --rendering | flat-vector, hand-drawn, painterly, digital, pixel, chalk |
| --mood | subtle, balanced, bold |
| --aspect | 16:9, 2.35:1, 4:3, 1:1 |

---

## 账号定位

- AI
- AI 工具
- AI 编程
- AI 创业
- 出海

---

## 版本

- v1.0 - 初始版本

---

## 参考

- [blader/humanizer](https://github.com/blader/humanizer) - AI 味检测
- [JimLiu/baoyu-skills](https://github.com/JimLiu/baoyu-skills) - 内容发布工具
- [cosysun/auto-claude-writing-agent-pub](https://github.com/cosysun/auto-claude-writing-agent-pub) - 写作流程参考
