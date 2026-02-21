#!/bin/bash

# ========================================
# 文章归档自动化脚本
# ========================================
# 用途：自动将工作流输出文件归档到日期目录
# 作者：八段式专业写作工作流
# 版本：v1.0
# 日期：2026-02-21
# ========================================

# 颜色定义
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# 获取当前日期
TODAY=$(date +%Y/%m/%d)
ARTICLE_DIR="articles/$TODAY"

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}📦 文章归档自动化脚本${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# 步骤1：创建目录结构
echo -e "${YELLOW}[1/5] 创建目录结构...${NC}"
mkdir -p "$ARTICLE_DIR"/{assets/diagrams,}
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ 目录创建成功：$ARTICLE_DIR${NC}"
else
    echo -e "${RED}❌ 目录创建失败${NC}"
    exit 1
fi
echo ""

# 步骤2：复制文章文件
echo -e "${YELLOW}[2/5] 复制文章文件...${NC}"

# 定义文件映射
declare -A file_map=(
    ["article_draft_*.md"]="article.md"
    ["*research*.md"]="research_report.md"
    ["stage4*.md"]="review_report.md"
    ["stage5*.md"]="title_proposals.md"
    ["stage6*.md"]="final_review.md"
    ["stage8*.md"]="publish_checklist.md"
)

copied_count=0
for pattern in "${!file_map[@]}"; do
    target="${file_map[$pattern]}"
    # 查找匹配的文件
    files=($(ls $pattern 2>/dev/null))
    if [ ${#files[@]} -gt 0 ]; then
        # 取第一个匹配的文件
        source_file="${files[0]}"
        cp "$source_file" "$ARTICLE_DIR/$target"
        if [ $? -eq 0 ]; then
            echo -e "${GREEN}  ✓ $source_file → $target${NC}"
            ((copied_count++))
        else
            echo -e "${RED}  ✗ 复制失败：$source_file${NC}"
        fi
    else
        echo -e "${YELLOW}  ⊘ 未找到：$pattern${NC}"
    fi
done

echo -e "${GREEN}✅ 已复制 $copied_count 个文件${NC}"
echo ""

# 步骤3：生成README.md
echo -e "${YELLOW}[3/5] 生成README.md...${NC}"

# 提取文章标题（从article.md的第一行）
if [ -f "$ARTICLE_DIR/article.md" ]; then
    TITLE=$(head -1 "$ARTICLE_DIR/article.md" | sed 's/^# //')
    WORD_COUNT=$(wc -w "$ARTICLE_DIR/article.md" | awk '{print $1}')
else
    TITLE="[待补充]"
    WORD_COUNT="0"
fi

cat > "$ARTICLE_DIR/README.md" << EOF
# $TITLE

## 📋 文章信息

- **发布日期**: $(date +%Y年%m月%d日)
- **主题分类**: [待补充]
- **字数**: $WORD_COUNT字
- **阅读时长**: 约$((WORD_COUNT/500))分钟
- **质量评分**: [待补充]/10

---

## 📝 内容摘要

[待补充 - 请手动添加100-200字的内容摘要]

---

## 🔗 发布链接

- **微信公众号**: [待添加]
- **知乎**: [待添加]
- **小红书**: [待添加]
- **LinkedIn**: [待添加]

---

## 📊 传播数据（实时更新）

| 平台 | 阅读量 | 点赞 | 评论 | 转发 |
|------|--------|------|------|------|
| 公众号 | - | - | - | - |
| 知乎 | - | - | - | - |
| 小红书 | - | - | - | - |

**更新时间**: 待发布

---

## 📂 文件清单

### 核心文件
- \`article.md\` - 正式发布版文章
- \`research_report.md\` - 深度调研报告
- \`metadata.json\` - 结构化元数据

### 工作流文件
- \`review_report.md\` - 三遍审校报告
- \`title_proposals.md\` - 标题方案
- \`final_review.md\` - 最终审阅报告
- \`publish_checklist.md\` - 发布执行清单

---

## 🏷️ 标签

\`#待补充\`

---

*本文档由八段式专业写作工作流生成 | 创建时间: $(date +%Y-%m-%d\ %H:%M)*
EOF

echo -e "${GREEN}✅ README.md 生成成功${NC}"
echo ""

# 步骤4：生成metadata.json
echo -e "${YELLOW}[4/5] 生成metadata.json...${NC}"

cat > "$ARTICLE_DIR/metadata.json" << EOF
{
  "article": {
    "title": "$TITLE",
    "author": "待补充",
    "publish_date": "$(date +%Y-%m-%d)",
    "word_count": $WORD_COUNT,
    "reading_time": "$((WORD_COUNT/500))分钟",
    "quality_score": 0,
    "ai_detection_score": 0
  },
  "classification": {
    "primary_category": "待补充",
    "secondary_categories": [],
    "content_type": "待补充"
  },
  "keywords": {
    "primary": [],
    "secondary": []
  },
  "tags": [],
  "data_sources": {
    "total_count": 0,
    "primary_sources": []
  },
  "publishing": {
    "platforms": []
  },
  "workflow_metadata": {
    "creation_date": "$(date +%Y-%m-%d)",
    "workflow_version": "八段式专业写作工作流 v1.0"
  }
}
EOF

echo -e "${GREEN}✅ metadata.json 生成成功${NC}"
echo ""

# 步骤5：显示归档结果
echo -e "${YELLOW}[5/5] 归档完成！${NC}"
echo ""
echo -e "${BLUE}========================================${NC}"
echo -e "${GREEN}✅ 归档成功！${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""
echo -e "📁 归档位置: ${GREEN}$ARTICLE_DIR${NC}"
echo ""
echo -e "📂 目录结构:"
ls -lh "$ARTICLE_DIR" | awk 'NR>1 {printf "  %s  %s\n", $5, $9}'
echo ""
echo -e "${BLUE}========================================${NC}"
echo -e "${YELLOW}📝 下一步操作：${NC}"
echo ""
echo -e "1. 编辑 ${GREEN}$ARTICLE_DIR/README.md${NC}"
echo -e "   - 补充内容摘要"
echo -e "   - 添加标签和分类"
echo ""
echo -e "2. 编辑 ${GREEN}$ARTICLE_DIR/metadata.json${NC}"
echo -e "   - 补充质量评分"
echo -e "   - 完善元数据"
echo ""
echo -e "3. 提交到GitHub："
echo -e "   ${BLUE}git add articles/$TODAY/${NC}"
echo -e "   ${BLUE}git commit -m \"新增文章：$TITLE（$(date +%Y-%m-%d)）\"${NC}"
echo -e "   ${BLUE}git push origin main${NC}"
echo ""
echo -e "${BLUE}========================================${NC}"
