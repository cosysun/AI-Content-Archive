# 📦 GitHub归档使用指南

## 🎯 目录结构说明

本项目按**日期目录**组织文章归档，便于版本管理和内容追溯。

```
articles/
└── YYYY/                    # 年份目录
    └── MM/                  # 月份目录（01-12）
        └── DD/              # 日期目录（01-31）
            ├── README.md                    # 📋 文章索引（必读！）
            ├── article.md                   # 📝 正式发布版
            ├── research_report.md           # 🔍 调研报告
            ├── review_report.md             # ✏️ 审校报告
            ├── title_proposals.md           # 🏷️ 标题方案
            ├── final_review.md              # ✅ 最终审阅
            ├── publish_checklist.md         # 🚀 发布清单
            ├── metadata.json                # 📊 结构化数据
            └── assets/                      # 🎨 资源文件夹
                ├── cover.jpg                # 封面图
                └── diagrams/                # 图表素材
```

---

## 🚀 快速开始

### 1️⃣ 初始化Git仓库（首次使用）

```bash
cd /data/workspace
git init
git add articles/
git commit -m "初始化文章归档系统"
```

### 2️⃣ 关联远程仓库

```bash
# 方式A：创建新仓库后关联
git remote add origin https://github.com/你的用户名/你的仓库名.git
git branch -M main
git push -u origin main

# 方式B：克隆现有仓库后添加内容
# git clone https://github.com/你的用户名/你的仓库名.git
# cp -r /data/workspace/articles/* ./仓库名/articles/
```

### 3️⃣ 每次新增文章后提交

```bash
cd /data/workspace
git add articles/2026/02/21/    # 添加今天的文章
git commit -m "新增文章：AI进入象牙塔（2026-02-21）"
git push origin main
```

---

## 📝 标准工作流

### 阶段1：创建新文章目录

```bash
# 自动获取今天日期并创建目录
TODAY=$(date +%Y/%m/%d)
mkdir -p articles/$TODAY/{assets/diagrams,}
echo "已创建目录：articles/$TODAY"
```

### 阶段2：生成文章内容

使用八段式工作流生成内容后，自动归档到日期目录：

```bash
# 复制文件到归档目录
cp article_draft_*.md articles/$TODAY/article.md
cp *_research_*.md articles/$TODAY/research_report.md
cp stage4_*.md articles/$TODAY/review_report.md
cp stage5_*.md articles/$TODAY/title_proposals.md
cp stage6_*.md articles/$TODAY/final_review.md
cp stage8_*.md articles/$TODAY/publish_checklist.md
```

### 阶段3：创建索引和元数据

```bash
# README.md 和 metadata.json 会自动生成
# 手动补充：封面图、发布链接等
```

### 阶段4：提交到GitHub

```bash
git add articles/$TODAY/
git commit -m "新增文章：$(cat articles/$TODAY/README.md | grep '^#' | head -1 | sed 's/# //')（$(date +%Y-%m-%d)）"
git push origin main
```

---

## 📊 文件说明

### 核心文件（必需）

| 文件名 | 用途 | 重要性 |
|--------|------|--------|
| `README.md` | 文章索引，包含摘要、链接、数据 | ⭐⭐⭐⭐⭐ |
| `article.md` | 正式发布版文章 | ⭐⭐⭐⭐⭐ |
| `metadata.json` | 结构化元数据（标签、数据点、分析） | ⭐⭐⭐⭐⭐ |

### 工作流文件（推荐保留）

| 文件名 | 用途 | 重要性 |
|--------|------|--------|
| `research_report.md` | 调研报告（15+信息源） | ⭐⭐⭐⭐ |
| `review_report.md` | 三遍审校记录 | ⭐⭐⭐ |
| `title_proposals.md` | 20个标题方案 | ⭐⭐⭐ |
| `final_review.md` | 质量评估报告 | ⭐⭐⭐ |
| `publish_checklist.md` | 发布执行清单 | ⭐⭐⭐⭐ |

### 资源文件（可选）

| 文件夹 | 用途 | 重要性 |
|--------|------|--------|
| `assets/` | 封面图、配图、流程图 | ⭐⭐⭐⭐ |

---

## 🔍 查找和检索

### 按日期查找

```bash
# 查看2026年2月的所有文章
ls -la articles/2026/02/

# 查看今天的文章
ls -la articles/$(date +%Y/%m/%d)/
```

### 按标题搜索

```bash
# 搜索标题包含"AI"的文章
find articles/ -name "README.md" -exec grep -l "AI" {} \;
```

### 按标签搜索

```bash
# 搜索标签包含"学术科研"的文章
find articles/ -name "metadata.json" -exec grep -l "学术科研" {} \;
```

### 统计文章数量

```bash
# 统计总文章数
find articles/ -name "article.md" | wc -l

# 统计本月文章数
find articles/$(date +%Y/%m)/ -name "article.md" | wc -l
```

---

## 📈 数据更新规范

### 发布后更新README.md

在文章发布后，及时更新以下内容：

1. **发布链接**（🔗 发布链接部分）
   ```markdown
   - **微信公众号**: https://mp.weixin.qq.com/s/xxxxx
   - **知乎**: https://zhuanlan.zhihu.com/p/xxxxx
   ```

2. **传播数据**（📊 传播数据部分）
   - 发布后第1天、第3天、第7天更新
   - 记录阅读量、点赞、评论、转发数据

3. **更新时间**
   ```markdown
   **更新时间**: 2026-02-25 21:00（D+1）
   ```

### 发布后更新metadata.json

```json
{
  "publishing": {
    "platforms": [
      {
        "name": "微信公众号",
        "status": "已发布",  // 从"待发布"改为"已发布"
        "url": "https://mp.weixin.qq.com/s/xxxxx"  // 添加实际链接
      }
    ]
  },
  "analytics": {
    "actual_performance": {
      "day_1": {
        "views": 12580,
        "likes": 436,
        "shares": 89,
        "comments": 67
      }
    }
  }
}
```

---

## 🎨 最佳实践

### ✅ 推荐做法

1. **每篇文章独立目录**：方便管理和追溯
2. **保留完整工作流文件**：便于后续复盘和学习
3. **及时更新数据**：发布后24小时内更新链接和初始数据
4. **统一命名规范**：所有文件名使用英文和下划线
5. **Git提交规范**：使用清晰的commit message

### ❌ 避免的做法

1. ❌ 不要直接修改已发布的`article.md`（可创建v1.1版本）
2. ❌ 不要删除工作流文件（除非确定不再需要）
3. ❌ 不要混淆日期目录（严格按YYYY/MM/DD格式）
4. ❌ 不要在`assets/`外存放图片（统一管理）

---

## 🔧 自动化脚本

### 快速创建新文章目录

```bash
#!/bin/bash
# 文件名：create_article_dir.sh

TODAY=$(date +%Y/%m/%d)
ARTICLE_DIR="articles/$TODAY"

# 创建目录结构
mkdir -p $ARTICLE_DIR/{assets/diagrams,}

# 创建空白README.md
cat > $ARTICLE_DIR/README.md << 'EOF'
# [文章标题]

## 📋 文章信息
- **发布日期**: $(date +%Y年%m月%d日)
- **主题分类**: [待补充]
- **字数**: [待补充]

## 📝 内容摘要
[待补充]

## 🔗 发布链接
- **微信公众号**: [待添加]

## 📂 文件清单
[待补充]
EOF

echo "✅ 已创建文章目录：$ARTICLE_DIR"
```

使用方法：
```bash
chmod +x create_article_dir.sh
./create_article_dir.sh
```

### 批量提交到GitHub

```bash
#!/bin/bash
# 文件名：commit_articles.sh

# 获取今天日期
TODAY=$(date +%Y/%m/%d)

# 添加文件
git add articles/$TODAY/

# 获取文章标题
TITLE=$(cat articles/$TODAY/README.md | grep '^#' | head -1 | sed 's/# //')

# 提交
git commit -m "新增文章：$TITLE（$(date +%Y-%m-%d)）"

# 推送
git push origin main

echo "✅ 已提交到GitHub"
```

---

## 📚 进阶技巧

### 1. 创建文章索引页

在`articles/`根目录创建`INDEX.md`，自动汇总所有文章：

```bash
# 生成索引
echo "# 文章归档总索引" > articles/INDEX.md
echo "" >> articles/INDEX.md
find articles/ -name "README.md" | sort -r | while read file; do
    title=$(grep '^#' $file | head -1 | sed 's/# //')
    date=$(echo $file | grep -oP '\d{4}/\d{2}/\d{2}')
    echo "- [$title]($file) - $date" >> articles/INDEX.md
done
```

### 2. 按标签分类

创建`articles/TAGS.md`，按标签分类文章：

```bash
# 提取所有标签
find articles/ -name "metadata.json" -exec jq -r '.tags[]' {} \; | sort | uniq
```

### 3. 数据可视化

使用`jq`提取所有文章的数据指标：

```bash
# 统计文章字数分布
find articles/ -name "metadata.json" -exec jq -r '.article.word_count' {} \; | sort -n

# 统计AI味评分
find articles/ -name "metadata.json" -exec jq -r '.article.ai_detection_score' {} \; | sort -n
```

---

## 🆘 常见问题

### Q1: 如何处理同一天的多篇文章？

A: 在日期目录下创建子目录：
```
articles/2026/02/21/
├── article-1/
│   ├── README.md
│   └── article.md
└── article-2/
    ├── README.md
    └── article.md
```

### Q2: 如何迁移旧文章？

A: 按发布日期创建目录，手动整理：
```bash
mkdir -p articles/2025/12/15
# 将旧文章内容复制到对应目录
```

### Q3: 如何备份归档？

A: 定期推送到GitHub即可实现自动备份：
```bash
# 每天自动提交（可配合crontab）
git add articles/
git commit -m "每日备份 $(date +%Y-%m-%d)"
git push origin main
```

---

## 📞 技术支持

如有问题，请通过以下方式联系：
- GitHub Issues: [仓库地址]
- 邮箱: [待补充]

---

*本指南由八段式专业写作工作流团队维护 | 最后更新: 2026-02-21*
