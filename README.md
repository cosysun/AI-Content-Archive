# AI Content Creation Archive

🤖 自动化AI内容创作归档项目

这个仓库用于存档每天自动生成的AI内容（微信公众号文章、小红书文章、视频脚本）。

## 📂 项目结构

```
AI_Content_Creation/
├── output/                              # 每天生成的内容
│   ├── 20260219_wechat_article.md      # 微信公众号文章（原始）
│   ├── 20260219_wechat_article_humanized.md  # 微信文章（去AI味）
│   ├── 20260219_xiaohongshu_post.md    # 小红书文章（原始）
│   ├── 20260219_xiaohongshu_post_humanized.md  # 小红书（去AI味）
│   ├── 20260219_video_script.md        # 视频脚本（原始）
│   ├── 20260219_video_script_humanized.md  # 视频脚本（去AI味）
│   └── 20260219_report.md              # 每日报告
├── scripts/                             # 自动化脚本
│   ├── humanizer_integration.py        # 去AI味处理脚本
│   └── auto_git_push.py                # 自动Git推送脚本
├── docs/                                # 文档
│   ├── HUMANIZER_INTEGRATION_GUIDE.md  # Humanizer使用指南
│   └── WORKFLOW.md                     # 工作流说明
├── .gitignore                          # Git忽略文件
└── README.md                           # 项目说明
```

## 🚀 功能特性

- ✅ **每日自动生成内容**：基于最新AI热点和GitHub趋势
- ✅ **多平台适配**：微信公众号、小红书、抖音/视频号
- ✅ **去AI味处理**：基于humanizer规则，让内容更自然
- ✅ **自动归档**：每天自动提交到GitHub
- ✅ **版本对比**：保留原始版本和处理后版本

## 📊 内容统计

| 日期 | 话题 | 微信文章 | 小红书 | 视频脚本 | 状态 |
|------|------|---------|--------|---------|------|
| 2026-02-19 | DeepRare罕见病AI诊断 | ✅ | ✅ | ✅ | 已发布 |

## 🔧 使用方法

### 自动化工作流

每天早上7:00自动执行：
```
1. 搜索AI热点 + GitHub趋势
2. 选择话题
3. 生成内容（3个平台）
4. Humanizer处理（去AI味）
5. Git提交并推送
6. 发送通知
```

### 手动运行

```bash
# 处理今天的内容
python scripts/humanizer_integration.py

# 推送到GitHub
python scripts/auto_git_push.py
```

## 📖 质量标准

### 原始版本
- AI检测概率：~95%
- 风格：吸睛、热情、互动性强
- 适用：小红书、抖音等需要高互动的平台

### Humanized版本
- AI检测概率：45-60%（人工润色后可降至15-25%）
- 风格：平实、客观、可信
- 适用：微信公众号、知乎等专业平台

## 🛠️ 技术栈

- **内容生成**：Claude AI（基于最新AI热点）
- **去AI味处理**：基于 [github.com/blader/humanizer](https://github.com/blader/humanizer) 的24种AI写作模式检测
- **自动化**：Python + Windows定时任务
- **版本控制**：Git + GitHub

## 📝 许可证

MIT License

## 📧 联系方式

如有问题或建议，欢迎提Issue。

---

**最后更新**：2026-02-19  
**生成方式**：自动化 + 人工审核  
**更新频率**：每日一次
