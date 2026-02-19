#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AI内容选题生成器
功能：从多个信息源收集热点，生成选题提案供用户选择
"""

import os
import json
from datetime import datetime

# 频道定位
CHANNEL_FOCUS = {
    "ai_knowledge": "AI知识科普",
    "outbound_app": "出海App",
    "ai_startup": "AI创业"
}

# 信息源配置
INFO_SOURCES = {
    "brave_search": {
        "name": "Brave Search (Google News)",
        "keywords": [
            "AI breakthrough",
            "AI startup funding",
            "AI app international",
            "machine learning tutorial",
            "generative AI news"
        ]
    },
    "x_twitter": {
        "name": "X (Twitter) Trending",
        "accounts": [
            "@sama",  # Sam Altman
            "@karpathy",  # Andrej Karpathy
            "@goodside",  # Riley Goodside
            "@pengcheng_ai",  # AI researcher
            "@weights_biases"  # ML tools
        ]
    },
    "github": {
        "name": "GitHub Trending",
        "categories": ["ai", "machine-learning", "deep-learning"]
    },
    "product_hunt": {
        "name": "Product Hunt",
        "tags": ["ai", "machine-learning", "productivity"]
    },
    "hacker_news": {
        "name": "Hacker News",
        "keywords": ["AI", "ML", "GPT", "LLM"]
    }
}

def generate_topic_template(topic_id, title, category, heat_score, sources):
    """生成选题模板"""
    return {
        "id": topic_id,
        "title": title,
        "category": category,  # ai_knowledge, outbound_app, ai_startup
        "heat_score": heat_score,  # 1-10
        "sources": sources,  # 信息来源列表
        "keywords": [],
        "target_platforms": ["微信公众号", "小红书", "抖音"],
        "estimated_reading_time": "5-8分钟",
        "seo_potential": "high",  # high, medium, low
        "monetization_potential": "medium",  # high, medium, low
        "timestamp": datetime.now().isoformat()
    }

def save_topic_proposals(date_str, topics):
    """保存选题提案"""
    output_dir = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "output",
        date_str
    )
    os.makedirs(output_dir, exist_ok=True)
    
    proposal_file = os.path.join(output_dir, "topic_proposals.json")
    
    with open(proposal_file, 'w', encoding='utf-8') as f:
        json.dump({
            "date": date_str,
            "channel_focus": CHANNEL_FOCUS,
            "info_sources": INFO_SOURCES,
            "proposals": topics,
            "generated_at": datetime.now().isoformat()
        }, f, ensure_ascii=False, indent=2)
    
    return proposal_file

def generate_markdown_proposal(date_str, topics):
    """生成Markdown格式的选题提案"""
    output_dir = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "output",
        date_str
    )
    
    md_content = f"""# AI内容选题提案
**日期**: {date_str}
**频道定位**: AI知识科普 | 出海App | AI创业

---

## 📊 今日热点分析

"""
    
    for i, topic in enumerate(topics, 1):
        category_cn = CHANNEL_FOCUS.get(topic['category'], topic['category'])
        
        md_content += f"""
### 选题 {i}: {topic['title']}

**分类**: {category_cn}  
**热度**: {'🔥' * topic['heat_score']} ({topic['heat_score']}/10)  
**信息源**: {', '.join(topic['sources'])}  
**关键词**: {', '.join(topic['keywords'])}

**内容价值**:
- 📖 阅读时长: {topic['estimated_reading_time']}
- 🔍 SEO潜力: {topic['seo_potential']}
- 💰 变现潜力: {topic['monetization_potential']}

**适用平台**: {' | '.join(topic['target_platforms'])}

---
"""
    
    md_content += """
## 🎯 选择指引

请回复选题编号（1-5），我将为你生成该选题的完整内容包。

**示例回复**: 
- "选择选题3"
- "我要第1个"
- "用2号选题"
"""
    
    md_file = os.path.join(output_dir, "topic_proposals.md")
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(md_content)
    
    return md_file

def main():
    """主流程"""
    import sys
    import io
    
    # 修复Windows控制台编码问题
    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
    
    today = datetime.now().strftime("%Y-%m-%d")
    
    print(f"\n{'=' * 60}")
    print(f"  AI内容选题生成器")
    print(f"  日期: {today}")
    print(f"{'=' * 60}\n")
    
    # 这里应该调用实际的信息源API
    # 当前只生成模板示例
    print("⚠️  选题生成需要配合Claude对话或API调用")
    print("   当前脚本提供结构模板，实际内容需要动态生成\n")
    
    # 示例选题
    sample_topics = [
        generate_topic_template(
            "topic_001",
            "DeepSeek-V3开源震撼：中国AI大模型首次超越GPT-4",
            "ai_knowledge",
            9,
            ["GitHub Trending", "X/Twitter", "Hacker News"]
        ),
        generate_topic_template(
            "topic_002",
            "Cursor编辑器出海爆红：AI编程工具月收入破千万美元",
            "outbound_app",
            8,
            ["Product Hunt", "X/Twitter"]
        ),
        generate_topic_template(
            "topic_003",
            "AI创业者必看：YC 2024冬季营Demo Day十大AI项目解析",
            "ai_startup",
            7,
            ["Hacker News", "X/Twitter"]
        )
    ]
    
    # 保存选题
    json_file = save_topic_proposals(today, sample_topics)
    md_file = generate_markdown_proposal(today, sample_topics)
    
    print(f"✓ 选题提案已生成:")
    print(f"  JSON: {json_file}")
    print(f"  Markdown: {md_file}\n")
    
    return True

if __name__ == "__main__":
    main()
