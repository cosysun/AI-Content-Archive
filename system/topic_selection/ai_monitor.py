#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI热点监控系统
每日自动抓取AI行业动态，生成候选主题报告

运行方式：
    python ai_monitor.py              # 运行一次
    python ai_monitor.py --daemon     # 后台运行（每4小时）
    python ai_monitor.py --test       # 测试模式（仅HackerNews）
"""

import requests
import feedparser
import json
from datetime import datetime, timedelta
from collections import Counter
from typing import List, Dict
import time
import sys

# ============================================
# 配置
# ============================================

# Brave Search API配置（可选）
BRAVE_API_KEY = ""  # 从 https://brave.com/search/api/ 获取

# 关键词配置
AI_KEYWORDS = [
    "AI", "artificial intelligence", "machine learning", "deep learning",
    "GPT", "Gemini", "Claude", "LLM", "large language model",
    "generative AI", "AI tools", "AI coding", "AI startup",
    "OpenAI", "Anthropic", "Google AI", "neural network"
]

# 热度阈值
TRENDING_THRESHOLD = {
    "high": 5000,    # 24小时内讨论量 > 5000
    "medium": 1000,  # 1000-5000
    "low": 100       # 100-1000
}

# ============================================
# 数据采集模块
# ============================================

def fetch_hackernews():
    """抓取HackerNews热门话题"""
    print("📰 正在抓取 HackerNews...")
    
    try:
        url = "https://hacker-news.firebaseio.com/v0/topstories.json"
        story_ids = requests.get(url, timeout=10).json()[:30]
        
        stories = []
        for story_id in story_ids:
            story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
            story = requests.get(story_url, timeout=10).json()
            
            if story and 'title' in story:
                title = story['title'].lower()
                if any(kw.lower() in title for kw in AI_KEYWORDS):
                    stories.append({
                        "source": "HackerNews",
                        "title": story['title'],
                        "url": story.get('url', f"https://news.ycombinator.com/item?id={story_id}"),
                        "score": story.get('score', 0),
                        "comments": story.get('descendants', 0),
                        "timestamp": datetime.now().isoformat()
                    })
        
        print(f"  ✅ 找到 {len(stories)} 条AI相关话题")
        return stories
    
    except Exception as e:
        print(f"  ❌ 抓取失败：{e}")
        return []

def fetch_brave_search():
    """使用Brave Search API搜索AI热点"""
    print("🔍 正在使用 Brave Search...")
    
    if not BRAVE_API_KEY or BRAVE_API_KEY == "":
        print("  ⚠️  未配置Brave API Key，跳过")
        return []
    
    try:
        headers = {
            "Accept": "application/json",
            "X-Subscription-Token": BRAVE_API_KEY
        }
        
        results = []
        queries = ["AI news today", "new AI tools 2026", "AI startup"]
        
        for query in queries:
            url = f"https://api.search.brave.com/res/v1/web/search?q={query}&count=10"
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                for item in data.get('web', {}).get('results', []):
                    results.append({
                        "source": "Brave Search",
                        "title": item.get('title'),
                        "url": item.get('url'),
                        "description": item.get('description'),
                        "timestamp": datetime.now().isoformat()
                    })
        
        print(f"  ✅ 找到 {len(results)} 条搜索结果")
        return results
    
    except Exception as e:
        print(f"  ❌ 搜索失败：{e}")
        return []

def fetch_producthunt():
    """抓取ProductHunt AI工具"""
    print("🚀 正在抓取 ProductHunt...")
    
    try:
        feed = feedparser.parse("https://www.producthunt.com/topics/artificial-intelligence.rss")
        
        tools = []
        for entry in feed.entries[:10]:
            tools.append({
                "source": "ProductHunt",
                "title": entry.title,
                "url": entry.link,
                "description": entry.get('summary', ''),
                "timestamp": entry.get('published', datetime.now().isoformat())
            })
        
        print(f"  ✅ 找到 {len(tools)} 个AI工具")
        return tools
    
    except Exception as e:
        print(f"  ❌ 抓取失败：{e}")
        return []

def fetch_arxiv():
    """抓取arXiv AI论文"""
    print("📚 正在抓取 arXiv...")
    
    try:
        feeds = [
            "http://export.arxiv.org/rss/cs.AI",
            "http://export.arxiv.org/rss/cs.CL",
            "http://export.arxiv.org/rss/cs.LG"
        ]
        
        papers = []
        for feed_url in feeds:
            feed = feedparser.parse(feed_url)
            for entry in feed.entries[:5]:
                papers.append({
                    "source": "arXiv",
                    "title": entry.title,
                    "url": entry.link,
                    "description": entry.get('summary', ''),
                    "timestamp": entry.get('published', datetime.now().isoformat())
                })
        
        print(f"  ✅ 找到 {len(papers)} 篇论文")
        return papers
    
    except Exception as e:
        print(f"  ❌ 抓取失败：{e}")
        return []

def fetch_techcrunch():
    """抓取TechCrunch AI新闻"""
    print("📰 正在抓取 TechCrunch...")
    
    try:
        feed = feedparser.parse("https://techcrunch.com/category/artificial-intelligence/feed/")
        
        news = []
        for entry in feed.entries[:10]:
            news.append({
                "source": "TechCrunch",
                "title": entry.title,
                "url": entry.link,
                "description": entry.get('summary', ''),
                "timestamp": entry.get('published', datetime.now().isoformat())
            })
        
        print(f"  ✅ 找到 {len(news)} 条新闻")
        return news
    
    except Exception as e:
        print(f"  ❌ 抓取失败：{e}")
        return []

# ============================================
# 数据处理模块
# ============================================

def calculate_heat(item: Dict) -> int:
    """计算热度分数"""
    heat = 0
    
    # HackerNews热度
    if item['source'] == 'HackerNews':
        heat = item.get('score', 0) + item.get('comments', 0) * 2
    
    # 其他来源基础分
    else:
        heat = 100
    
    # 时效性加成
    try:
        timestamp = datetime.fromisoformat(item['timestamp'].replace('Z', '+00:00'))
        hours_ago = (datetime.now() - timestamp.replace(tzinfo=None)).total_seconds() / 3600
        if hours_ago < 24:
            heat *= 2
        elif hours_ago < 72:
            heat *= 1.5
    except:
        pass
    
    return int(heat)

def classify_topic(title: str, description: str = "") -> List[str]:
    """分类到内容线"""
    text = (title + " " + description).lower()
    
    categories = []
    
    # AI科普关键词
    if any(kw in text for kw in ['explain', 'understand', 'what is', 'how does', 'introduction', 'guide']):
        categories.append("AI科普")
    
    # AI工具关键词
    if any(kw in text for kw in ['tool', 'app', 'software', 'platform', 'api', 'product', 'launch']):
        categories.append("AI工具")
    
    # AI编程关键词
    if any(kw in text for kw in ['code', 'coding', 'programming', 'developer', 'github', 'open source', 'library']):
        categories.append("AI编程")
    
    # AI出海创业关键词
    if any(kw in text for kw in ['startup', 'funding', 'market', 'business', 'revenue', 'valuation', 'raises']):
        categories.append("AI出海创业")
    
    # 默认分类
    if not categories:
        categories.append("AI科普")
    
    return categories

def deduplicate(items: List[Dict]) -> List[Dict]:
    """去重"""
    seen_titles = set()
    unique_items = []
    
    for item in items:
        # 简单去重：比较标题前50个字符
        title_key = item['title'][:50].lower()
        if title_key not in seen_titles:
            seen_titles.add(title_key)
            unique_items.append(item)
    
    return unique_items

# ============================================
# 报告生成模块
# ============================================

def generate_report(items: List[Dict]) -> str:
    """生成Markdown报告"""
    
    # 按热度排序
    items_with_heat = []
    for item in items:
        item['heat'] = calculate_heat(item)
        item['categories'] = classify_topic(item['title'], item.get('description', ''))
        items_with_heat.append(item)
    
    items_sorted = sorted(items_with_heat, key=lambda x: x['heat'], reverse=True)
    
    # 分级
    high_heat = [x for x in items_sorted if x['heat'] >= TRENDING_THRESHOLD['high']]
    medium_heat = [x for x in items_sorted if TRENDING_THRESHOLD['medium'] <= x['heat'] < TRENDING_THRESHOLD['high']]
    low_heat = [x for x in items_sorted if TRENDING_THRESHOLD['low'] <= x['heat'] < TRENDING_THRESHOLD['medium']]
    
    # 生成报告
    report = []
    report.append(f"# AI热点日报")
    report.append(f"")
    report.append(f"> 生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append(f"> 数据源：HackerNews, ProductHunt, arXiv, TechCrunch, Brave Search")
    report.append(f"> 总计：{len(items_sorted)} 条热点")
    report.append(f"")
    report.append(f"---")
    report.append(f"")
    
    # 高热度
    if high_heat:
        report.append(f"## 🔥🔥🔥 高热度（{len(high_heat)}条）")
        report.append(f"")
        for i, item in enumerate(high_heat, 1):
            report.append(f"### {i}. {item['title']}")
            report.append(f"")
            report.append(f"- **来源**：{item['source']}")
            report.append(f"- **热度**：{item['heat']}")
            report.append(f"- **推荐内容线**：{', '.join(item['categories'])}")
            report.append(f"- **链接**：{item['url']}")
            if item.get('description'):
                desc = item['description'][:200].strip()
                if desc:
                    report.append(f"- **简介**：{desc}...")
            report.append(f"")
    else:
        report.append(f"## 🔥🔥🔥 高热度（0条）")
        report.append(f"")
        report.append(f"*今日暂无高热度话题*")
        report.append(f"")
    
    # 中热度
    if medium_heat:
        report.append(f"## 🔥 中热度（{len(medium_heat)}条）")
        report.append(f"")
        for i, item in enumerate(medium_heat, 1):
            report.append(f"{i}. **{item['title']}** ({item['source']}, 热度{item['heat']})")
            report.append(f"   - 推荐：{', '.join(item['categories'])}")
            report.append(f"   - {item['url']}")
            report.append(f"")
    
    # 低热度（仅列标题）
    if low_heat:
        report.append(f"## 💤 低热度（{len(low_heat)}条）")
        report.append(f"")
        for item in low_heat[:10]:
            report.append(f"- {item['title']} ({item['source']})")
        if len(low_heat) > 10:
            report.append(f"- ... 还有 {len(low_heat)-10} 条")
        report.append(f"")
    
    # 统计
    report.append(f"---")
    report.append(f"")
    report.append(f"## 📊 统计")
    report.append(f"")
    
    category_counter = Counter()
    for item in items_sorted:
        for cat in item['categories']:
            category_counter[cat] += 1
    
    report.append(f"**内容线分布**：")
    for cat, count in category_counter.most_common():
        report.append(f"- {cat}: {count}条")
    report.append(f"")
    
    source_counter = Counter([x['source'] for x in items_sorted])
    report.append(f"**数据源分布**：")
    for source, count in source_counter.most_common():
        report.append(f"- {source}: {count}条")
    report.append(f"")
    
    # 下一步建议
    report.append(f"---")
    report.append(f"")
    report.append(f"## 💡 下一步建议")
    report.append(f"")
    
    if high_heat:
        report.append(f"✅ 建议立即对以下高热度话题进行深度调研：")
        for item in high_heat[:3]:
            report.append(f"- {item['title']}")
        report.append(f"")
        report.append(f"可使用 `python topic_scorer.py \"主题名称\"` 进行评分")
    else:
        report.append(f"⚠️  今日无高热度话题，建议：")
        report.append(f"- 观察中热度话题的发展")
        report.append(f"- 或从选题库中选择常青选题")
    
    return "\n".join(report)

# ============================================
# 主程序
# ============================================

def run_monitor(test_mode=False):
    """运行监控"""
    print(f"\n{'='*60}")
    print(f"🤖 AI热点监控系统")
    print(f"{'='*60}\n")
    
    all_items = []
    
    # 采集数据
    if test_mode:
        print("⚠️  测试模式：仅抓取HackerNews\n")
        all_items.extend(fetch_hackernews())
    else:
        all_items.extend(fetch_hackernews())
        all_items.extend(fetch_brave_search())
        all_items.extend(fetch_producthunt())
        all_items.extend(fetch_arxiv())
        all_items.extend(fetch_techcrunch())
    
    # 去重
    all_items = deduplicate(all_items)
    
    print(f"\n{'='*60}")
    print(f"📊 数据采集完成：共 {len(all_items)} 条（去重后）")
    print(f"{'='*60}\n")
    
    if len(all_items) == 0:
        print("⚠️  未找到任何热点，请检查网络连接或关键词配置")
        return None, None
    
    # 生成报告
    report = generate_report(all_items)
    
    # 保存
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    report_file = f"ai_trending_{timestamp}.md"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"✅ 报告已生成：{report_file}\n")
    
    # 保存JSON
    json_file = f"ai_trending_{timestamp}.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(all_items, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 数据已保存：{json_file}\n")
    
    return report_file, json_file

def main():
    """主函数"""
    test_mode = "--test" in sys.argv
    daemon_mode = "--daemon" in sys.argv
    
    if daemon_mode:
        print("🔄 后台运行模式（每4小时执行一次）")
        print("按 Ctrl+C 停止\n")
        
        while True:
            try:
                run_monitor(test_mode)
                next_run = datetime.now() + timedelta(hours=4)
                print(f"\n⏰ 下次运行时间：{next_run.strftime('%Y-%m-%d %H:%M:%S')}")
                print(f"⏳ 等待中...\n")
                time.sleep(4 * 3600)
            except KeyboardInterrupt:
                print("\n\n👋 监控已停止")
                break
            except Exception as e:
                print(f"\n❌ 运行出错：{e}")
                print(f"⏰ 5分钟后重试...\n")
                time.sleep(300)
    else:
        run_monitor(test_mode)

if __name__ == "__main__":
    main()
