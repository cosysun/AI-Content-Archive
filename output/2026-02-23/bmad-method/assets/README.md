# BMAD-METHOD 配图使用指南

## 📁 配图清单

本目录包含4张专业SVG矢量图，用于BMAD-METHOD技术文章的配图：

### 1. **architecture.svg** - 架构体系图
- **尺寸**: 1200×800px
- **用途**: 展示BMAD-METHOD的整体架构和组件关系
- **包含内容**:
  - AI智能引擎核心层
  - 12+专业Agent展示
  - 34+智能工作流
  - 交付物、过程数据、知识沉淀
  - 项目统计数据
- **建议位置**: 文章开篇或"核心架构"章节

### 2. **comparison.svg** - 对比分析图
- **尺寸**: 1200×700px
- **用途**: 对比传统敏捷与BMAD智能敏捷的差异
- **对比维度**:
  - 需求规划 (2-3天 vs 1-2小时)
  - 开发过程 (单线程 vs 多Agent协作)
  - 质量保证 (60%覆盖率 vs 90%+)
  - 部署发布 (手动 vs 一键智能)
  - 团队规模 (线性扩展 vs 规模自适应)
  - 知识管理 (分散 vs 智能知识库)
  - 效率提升: **300%-500%**
- **建议位置**: "为什么选择BMAD"或"优势分析"章节

### 3. **workflow.svg** - 工作流程全景图
- **尺寸**: 1400×900px
- **用途**: 展示从需求到上线的完整开发流程
- **流程节点**:
  1. 需求分析 (2-3h)
  2. 架构设计 (1-2h)
  3. 代码开发 (3-5h, 并行)
  4. 测试验证 (1-2h)
  5. 部署上线 (30min)
  6. 监控反馈 (持续)
- **特色**: 
  - 展示Party Mode多Agent协作中心
  - 12+Agent能力池展示
  - 完整时间线对比 (2-3周 → 8-12小时)
- **建议位置**: "工作流程"或"实践案例"章节

### 4. **stats.svg** - 数据统计可视化
- **尺寸**: 1200×800px
- **用途**: 展示项目热度和增长趋势
- **数据展示**:
  - GitHub热度指标 (Stars: 37,180 | Forks: 4,618)
  - 技术规模 (12+ Agents | 34+ Workflows | 50K+ 代码)
  - Star增长趋势图 (2024-2025)
  - 年增长率: +285%
  - 主要语言分布
- **建议位置**: "社区反响"或文章开篇引言

---

## 🎨 配图特点

### 设计风格
- **赛博朋克科技风**: 深色背景 + 霓虹渐变
- **配色方案**:
  - 背景: `#0f172a` / `#0a0e1a` (深空蓝)
  - 主色: 紫色 `#8b5cf6`、粉色 `#ec4899`、蓝色 `#3b82f6`、绿色 `#10b981`
  - 渐变效果: 营造科技感
- **矢量格式**: SVG可无损缩放，适配各平台

### 技术优势
- ✅ 无需外部依赖，纯SVG代码
- ✅ 文件体积小 (平均8-12KB)
- ✅ 支持Retina高清屏
- ✅ 可直接嵌入Markdown
- ✅ 可转换为PNG/JPG (用于不支持SVG的平台)

---

## 📝 Markdown引用示例

### 方法1: 相对路径引用 (推荐GitHub/本地)
```markdown
## 核心架构

![BMAD-METHOD架构](./assets/architecture.svg)

## 传统敏捷 vs BMAD对比

![对比分析](./assets/comparison.svg)

## 完整工作流程

![工作流程](./assets/workflow.svg)

## 项目数据

![数据统计](./assets/stats.svg)
```

### 方法2: 绝对路径引用 (适用于在线发布)
```markdown
![BMAD架构](https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/articles/bmad-method/assets/architecture.svg)
```

### 方法3: HTML嵌入 (精细控制尺寸)
```html
<img src="./assets/workflow.svg" width="100%" alt="BMAD工作流程">
```

---

## 🔄 格式转换指南

### SVG → PNG (高质量)
```bash
# 使用 Inkscape (推荐)
inkscape architecture.svg --export-png=architecture.png --export-dpi=300

# 使用 ImageMagick
convert -density 300 architecture.svg architecture.png

# 使用在线工具
# https://cloudconvert.com/svg-to-png
```

### SVG → JPG (微信公众号等)
```bash
convert -density 300 -background white architecture.svg architecture.jpg
```

---

## 🚀 平台发布建议

### 掘金/CSDN/博客园
- ✅ 直接支持SVG
- 建议: 使用相对路径引用

### 微信公众号
- ❌ 不支持SVG
- 建议: 转为PNG/JPG上传 (300dpi, 宽度1200px)

### 知乎/简书
- ⚠️ 部分支持SVG
- 建议: 转为PNG保底 (2x分辨率)

### V2EX/HackerNews
- ✅ 支持外链图片
- 建议: 托管到GitHub Pages或图床

---

## 📐 尺寸优化建议

### 社交媒体分享
- **Twitter/X**: 1200×675px (16:9)
- **LinkedIn**: 1200×627px
- 建议: 使用 `stats.svg` 或 `comparison.svg`

### 文章封面
- 推荐: `architecture.svg` + 标题文字
- 尺寸: 1200×630px (OpenGraph标准)

---

## 🎯 使用小贴士

1. **GitHub直接显示**: GitHub README可直接渲染SVG
2. **移动端优化**: SVG自适应，无需单独适配
3. **深色模式**: 当前配色已针对深色背景优化
4. **打印友好**: 如需打印，建议转PNG/PDF
5. **SEO优化**: 务必添加 `alt` 描述文字

---

## 📄 配图文件信息

| 文件名 | 尺寸 | 大小 | 复杂度 |
|--------|------|------|--------|
| architecture.svg | 1200×800 | ~10KB | 高 |
| comparison.svg | 1200×700 | ~8KB | 中 |
| workflow.svg | 1400×900 | ~12KB | 高 |
| stats.svg | 1200×800 | ~9KB | 中 |

---

## 🔗 资源链接

- **BMAD-METHOD项目**: https://github.com/bmad-code-org/BMAD-METHOD
- **SVG优化工具**: https://jakearchibald.github.io/svgomg/
- **在线预览**: 直接在浏览器打开SVG文件

---

## 📮 反馈建议

如果需要定制配图或有优化建议，请：
- 提交Issue到项目仓库
- 或直接修改SVG源码 (纯文本可编辑)

**最后更新**: 2025-02-23