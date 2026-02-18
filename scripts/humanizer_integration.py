#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI 内容创作工作流 - 自动化脚本
整合humanizer去AI味功能
作者：AI Content Creator
日期：2026-02-19
版本：2.0 (集成humanizer)
"""

import os
import re
from datetime import datetime
from pathlib import Path

# humanizer规则（基于SKILL.md）
class HumanizerRules:
    """AI写作模式检测和修复规则"""
    
    # 需要替换的AI词汇
    AI_VOCABULARY = {
        '此外': '另外',
        '另外': '',  # 直接删除
        '关键是': '重要的是',
        '至关重要': '重要',
        '深入探讨': '研究',
        '深入了解': '了解',
        '令人印象深刻': '很好',
        '值得注意的是': '',
        '显著提升': '提升',
        '显著改善': '改善',
        '极大地': '大幅',
        '持续不断': '持续',
        '日益增长': '增长',
    }
    
    # promotional语言模式
    PROMOTIONAL_PATTERNS = [
        (r'震惊[了！]', ''),
        (r'全球首个', ''),
        (r'希望之光', '希望'),
        (r'突破性的', ''),
        (r'革命性的', ''),
        (r'里程碑式', ''),
        (r'划时代', ''),
        (r'前所未有', ''),
        (r'史无前例', ''),
        (r'令人瞩目', ''),
    ]
    
    # 表情符号（需要移除）
    EMOJI_PATTERN = r'[🔥💡✅❌⚠️📊🎯🚀💰🏥📚🧬📄🌍👨‍⚕️💬❓🎁📱📝💡🛠️⚡📈⭐🎬]+'
    
    # 过度强调模式
    EMPHASIS_PATTERNS = [
        (r'【([^】]+)】', r'\1'),  # 移除【】
        (r'《([^》]+)》', r'\1'),  # 保留书名但去掉书名号
        (r'\*\*([^*]+)\*\*', r'\1'),  # 移除粗体**
    ]

def humanize_text(text):
    """对文本进行去AI味处理"""
    
    # 1. 移除表情符号
    text = re.sub(HumanizerRules.EMOJI_PATTERN, '', text)
    
    # 2. 替换AI词汇
    for ai_word, replacement in HumanizerRules.AI_VOCABULARY.items():
        if replacement:
            text = text.replace(ai_word, replacement)
        else:
            text = text.replace(ai_word + '，', '')
            text = text.replace(ai_word + ',', '')
    
    # 3. 移除promotional语言
    for pattern, replacement in HumanizerRules.PROMOTIONAL_PATTERNS:
        text = re.sub(pattern, replacement, text)
    
    # 4. 简化过度强调
    for pattern, replacement in HumanizerRules.EMPHASIS_PATTERNS:
        text = re.sub(pattern, replacement, text)
    
    # 5. 移除多余的空行（超过2个连续换行）
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    # 6. 移除行首行尾空格
    lines = text.split('\n')
    lines = [line.strip() for line in lines]
    text = '\n'.join(lines)
    
    return text

def humanize_file(input_path, output_path):
    """处理单个文件"""
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 应用humanizer规则
        humanized_content = humanize_text(content)
        
        # 保存
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(humanized_content)
        
        return True
    except Exception as e:
        print(f"处理文件失败: {e}")
        return False

def process_daily_content(date_str=None):
    """处理每日生成的内容"""
    if date_str is None:
        date_str = datetime.now().strftime("%Y%m%d")
    
    base_dir = Path(__file__).parent
    output_dir = base_dir / "output"
    
    files_to_process = [
        (f"{date_str}_wechat_article.md", f"{date_str}_wechat_article_humanized.md"),
        (f"{date_str}_xiaohongshu_post.md", f"{date_str}_xiaohongshu_post_humanized.md"),
        (f"{date_str}_video_script.md", f"{date_str}_video_script_humanized.md"),
    ]
    
    processed_count = 0
    
    print(f"\n>>> 开始处理 {date_str} 的内容...\n")
    
    for input_name, output_name in files_to_process:
        input_path = output_dir / input_name
        output_path = output_dir / output_name
        
        if not input_path.exists():
            print(f"[!] 文件不存在: {input_name}")
            continue
        
        print(f"[>] 处理: {input_name}")
        if humanize_file(input_path, output_path):
            print(f"[OK] 完成: {output_name}")
            processed_count += 1
        else:
            print(f"[FAIL] 失败: {input_name}")
    
    print(f"\n>>> 处理完成！成功处理 {processed_count}/{len(files_to_process)} 个文件")
    
    return processed_count

def show_usage():
    """显示使用说明"""
    usage = """
============================================================
   AI内容创作工作流 - Humanizer集成版 v2.0
============================================================

[使用方法]

1. 处理今天的内容:
   python humanizer_integration.py

2. 处理指定日期的内容:
   python humanizer_integration.py 20260219

3. 测试单个文件:
   python humanizer_integration.py test input.md output.md

[功能说明]

- 自动移除表情符号
- 替换AI词汇 ("此外"、"关键是"等)
- 移除promotional语言 ("震惊"、"全球首个"等)
- 简化过度强调 (**粗体**、【】等)
- 清理多余空行和空格

[文件命名规则]

原始文件: YYYYMMDD_wechat_article.md
处理后: YYYYMMDD_wechat_article_humanized.md

[集成到定时任务]

在定时任务中添加这一步:
AI生成内容 -> humanizer处理 -> 保存文件 -> 发送通知

============================================================
"""
    print(usage)

def test_mode(input_path, output_path):
    """测试模式：处理单个文件"""
    print(f"\n[TEST] 测试模式\n")
    print(f"输入文件: {input_path}")
    print(f"输出文件: {output_path}")
    
    if humanize_file(input_path, output_path):
        print(f"\n[OK] 测试成功！")
        print(f"请检查输出文件: {output_path}")
    else:
        print(f"\n[FAIL] 测试失败")

def main():
    """主函数"""
    import sys
    
    if len(sys.argv) == 1:
        # 无参数：处理今天的内容
        process_daily_content()
        
    elif len(sys.argv) == 2:
        arg = sys.argv[1]
        
        if arg in ['help', '--help', '-h']:
            show_usage()
        elif arg == 'test':
            print("[ERROR] test模式需要指定输入输出文件")
            print("用法: python humanizer_integration.py test input.md output.md")
        else:
            # 假设是日期
            process_daily_content(arg)
    
    elif len(sys.argv) == 4 and sys.argv[1] == 'test':
        # test模式
        input_path = sys.argv[2]
        output_path = sys.argv[3]
        test_mode(input_path, output_path)
    
    else:
        print("[ERROR] 参数错误")
        show_usage()

if __name__ == "__main__":
    main()
