# AI Content Creation Workflow

## 工作流程说明

### 自动化工作流（每天7:00）

```
┌─────────────────────────────────────┐
│  1. 热点收集 (5分钟)                │
│  - 搜索最新AI新闻                   │
│  - 查询GitHub热门项目               │
│  - 分析趋势和热度                   │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│  2. 话题选择 (2分钟)                │
│  - 评估话题价值                     │
│  - 考虑目标受众                     │
│  - 确定创作角度                     │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│  3. 内容生成 (10分钟)               │
│  - 微信公众号文章 (8000-15000字)   │
│  - 小红书文章 (3000-6000字)        │
│  - 视频脚本 (60秒详细分镜)         │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│  4. Humanizer处理 (1分钟)           │
│  - 移除表情符号                     │
│  - 替换AI词汇                       │
│  - 删除promotional语言              │
│  - 简化过度强调                     │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│  5. Git归档 (1分钟)                 │
│  - 保存到output目录                 │
│  - 提交到本地仓库                   │
│  - 推送到GitHub                     │
└─────────────────────────────────────┘
              ↓
┌─────────────────────────────────────┐
│  6. 通知 (即时)                     │
│  - 发送企业微信通知                 │
│  - 包含文件链接                     │
│  - 质量对比说明                     │
└─────────────────────────────────────┘

总耗时: 约20分钟
```

---

## 文件命名规范

### 命名格式

```
YYYYMMDD_<platform>_<type>[_humanized].md
```

### 示例

- `20260219_wechat_article.md` - 微信公众号文章（原始）
- `20260219_wechat_article_humanized.md` - 微信文章（去AI味）
- `20260219_xiaohongshu_post.md` - 小红书文章（原始）
- `20260219_xiaohongshu_post_humanized.md` - 小红书（去AI味）
- `20260219_video_script.md` - 视频脚本（原始）
- `20260219_video_script_humanized.md` - 视频脚本（去AI味）
- `20260219_report.md` - 每日报告

---

## 目录结构

```
AI_Content_Creation/
├── output/                    # 生成的内容
│   ├── 2026/                 # 按年份归档
│   │   ├── 02/              # 按月份归档
│   │   │   ├── 20260219_*.md
│   │   │   ├── 20260220_*.md
│   │   │   └── ...
│   │   └── ...
│   └── latest/              # 最新内容（符号链接或副本）
├── scripts/                  # 自动化脚本
│   ├── humanizer_integration.py
│   ├── auto_git_push.py
│   └── ...
├── docs/                     # 文档
│   ├── HUMANIZER_INTEGRATION_GUIDE.md
│   └── WORKFLOW.md
├── templates/               # 模板（可选）
│   ├── wechat_template.md
│   ├── xiaohongshu_template.md
│   └── video_template.md
└── README.md
```

---

## 内容质量标准

### 微信公众号文章

**原始版本**：
- 字数：8000-15000字
- 结构：标题 + 引言 + 3-5个章节 + 结论
- 风格：专业、深入、数据驱动
- 适用：追求内容深度的读者

**Humanized版本**：
- 字数：4000-8000字（精简）
- 结构：更简洁，去除冗余
- 风格：平实、客观、可信
- 适用：专业读者、理性决策者

### 小红书文章

**原始版本**：
- 字数：3000-6000字
- 结构：吸睛标题 + 案例故事 + 实用攻略 + 互动引导
- 风格：热情、互动、种草
- 适用：小红书平台，追求高互动

**Humanized版本**：
- 字数：2000-4000字
- 结构：简化但保留实用性
- 风格：真实、接地气
- 适用：需要建立信任的场景

### 视频脚本

**原始版本**：
- 时长：60秒
- 结构：详细分镜 + 配音文案 + 拍摄要求 + 发布策略
- 风格：完整、可执行
- 适用：专业视频制作团队

**Humanized版本**：
- 时长：60秒
- 结构：核心脚本内容
- 风格：精简、实用
- 适用：个人创作者

---

## Git提交规范

### Commit Message格式

```
Daily content update: YYYY-MM-DD

Files:
- 20260219_wechat_article_humanized.md
- 20260219_xiaohongshu_post_humanized.md
- 20260219_video_script_humanized.md

Topic: [话题名称]
Status: Published/Draft
```

### 示例

```
Daily content update: 2026-02-19

Files:
- 20260219_wechat_article_humanized.md
- 20260219_xiaohongshu_post_humanized.md
- 20260219_video_script_humanized.md

Topic: DeepRare AI罕见病诊断系统
Status: Published
```

---

## 自动化脚本说明

### 1. humanizer_integration.py

**功能**：
- 去除AI写作痕迹
- 批量处理每日内容
- 生成_humanized.md文件

**使用**：
```bash
# 处理今天的内容
python scripts/humanizer_integration.py

# 处理指定日期
python scripts/humanizer_integration.py 20260219
```

### 2. auto_git_push.py

**功能**：
- 自动检查变更
- 提交到本地仓库
- 推送到GitHub

**使用**：
```bash
python scripts/auto_git_push.py
```

---

## 定时任务设置

### Windows任务计划

```powershell
# 每天7:00执行内容生成
schtasks /create /tn "AI Content Creation" /tr "python C:\Users\andygzsun\AI_Content_Creation\scripts\daily_workflow.py" /sc daily /st 07:00

# 每天7:30执行Git推送
schtasks /create /tn "AI Content Git Push" /tr "python C:\Users\andygzsun\AI_Content_Creation\scripts\auto_git_push.py" /sc daily /st 07:30
```

### Linux/Mac Cron

```bash
# 编辑crontab
crontab -e

# 添加任务
0 7 * * * python ~/AI_Content_Creation/scripts/daily_workflow.py
30 7 * * * python ~/AI_Content_Creation/scripts/auto_git_push.py
```

---

## 常见问题

### Q1: Git push失败怎么办？

**可能原因**：
1. 没有配置remote origin
2. 没有权限（需要SSH key或Personal Access Token）
3. 网络问题

**解决方法**：
```bash
# 1. 检查remote
git remote -v

# 2. 添加remote（如果没有）
git remote add origin https://github.com/YOUR_USERNAME/AI-Content-Archive.git

# 3. 第一次推送
git push -u origin main
```

### Q2: 如何修改Humanizer规则？

编辑 `scripts/humanizer_integration.py`：

```python
class HumanizerRules:
    # 修改这里的规则
    AI_VOCABULARY = {
        '此外': '另外',
        # 添加你自己的规则
    }
```

### Q3: 如何查看历史内容？

```bash
# 查看提交历史
git log --oneline

# 查看某个日期的内容
git show <commit_id>:output/20260219_wechat_article_humanized.md
```

---

## 更新日志

### 2026-02-19
- ✅ 初始化项目
- ✅ 创建自动化脚本
- ✅ 集成Humanizer
- ✅ 配置Git自动推送
- ✅ 完善文档

---

生成时间：2026-02-19  
维护者：AI Content Creator  
版本：1.0
