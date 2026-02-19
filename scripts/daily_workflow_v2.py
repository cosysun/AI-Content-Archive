#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
每日AI内容自动化工作流 v2.0
优化内容：
1. 明确频道定位（AI知识科普、出海App、AI创业）
2. 多信息源聚合（Brave Search、X、GitHub、Product Hunt、Hacker News）
3. 选题提案机制（提供3-5个选题，用户选择）
4. 日期归档（output/YYYY-MM-DD/所有文件）
"""

import os
import sys
import subprocess
from datetime import datetime
import time

# 项目根目录
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
OUTPUT_DIR = os.path.join(PROJECT_ROOT, 'output')
SCRIPTS_DIR = os.path.join(PROJECT_ROOT, 'scripts')

def log(message, level="INFO"):
    """打印日志"""
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] [{level}] {message}")

def run_command(command, cwd=None):
    """执行命令"""
    try:
        result = subprocess.run(
            command,
            shell=True,
            cwd=cwd or PROJECT_ROOT,
            capture_output=True,
            text=True,
            encoding='utf-8',
            errors='replace'
        )
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def get_today_dir():
    """获取今日输出目录"""
    today = datetime.now().strftime("%Y-%m-%d")
    today_dir = os.path.join(OUTPUT_DIR, today)
    os.makedirs(today_dir, exist_ok=True)
    return today_dir, today

def step_0_generate_topic_proposals():
    """步骤0：生成选题提案"""
    log("=" * 60)
    log("步骤 0/4: 生成选题提案")
    log("=" * 60)
    log("信息源：Brave Search, X/Twitter, GitHub, Product Hunt, Hacker News")
    log("频道定位：AI知识科普 | 出海App | AI创业")
    
    topic_script = os.path.join(SCRIPTS_DIR, 'topic_selector.py')
    
    if not os.path.exists(topic_script):
        log("⚠️  未找到选题生成脚本，跳过此步骤", "WARNING")
        return True
    
    log("生成选题提案...")
    success, stdout, stderr = run_command(f'python "{topic_script}"')
    
    if success:
        log("✓ 选题提案生成完成")
        if stdout:
            print(stdout)
        
        today_dir, today = get_today_dir()
        proposal_file = os.path.join(today_dir, 'topic_proposals.md')
        
        if os.path.exists(proposal_file):
            log(f"✓ 选题文件: {proposal_file}")
            log("⏸  请查看选题提案，选择后继续...")
            return True
        else:
            log("⚠️  选题文件未生成", "WARNING")
            return False
    else:
        log("✗ 选题提案生成失败", "ERROR")
        if stderr:
            print(stderr)
        return False

def step_1_collect_hot_topics():
    """步骤1：收集热点话题"""
    log("\n" + "=" * 60)
    log("步骤 1/4: 收集AI热点")
    log("=" * 60)
    
    log("⚠️  此步骤需要调用Claude进行信息聚合")
    log("    信息源:")
    log("    - Brave Search (Google News)")
    log("    - X/Twitter 热点")
    log("    - GitHub Trending")
    log("    - Product Hunt")
    log("    - Hacker News")
    
    today_dir, today = get_today_dir()
    
    # 检查是否已有内容
    files = [f for f in os.listdir(today_dir) if f.endswith('.md')]
    if len(files) >= 3:  # 至少3篇文章
        log(f"✓ 发现今日内容: {len(files)} 个文件")
        return True
    else:
        log("⚠️  内容生成需要通过Claude对话完成", "WARNING")
        return False

def step_2_generate_content():
    """步骤2：生成内容"""
    log("\n" + "=" * 60)
    log("步骤 2/4: 生成内容（微信+小红书+视频）")
    log("=" * 60)
    
    today_dir, today = get_today_dir()
    
    # 检查必需的文件
    required_files = [
        "wechat_article.md",
        "xiaohongshu_post.md",
        "video_script.md"
    ]
    
    existing_files = []
    for filename in required_files:
        filepath = os.path.join(today_dir, filename)
        if os.path.exists(filepath):
            existing_files.append(filename)
    
    if len(existing_files) >= 3:
        log(f"✓ 内容已生成: {len(existing_files)}/3 个文件")
        return True
    else:
        log(f"⚠️  内容文件不完整: {len(existing_files)}/3", "WARNING")
        log("    需要生成的文件:")
        for filename in required_files:
            if filename not in existing_files:
                log(f"    - {filename}")
        return False

def step_3_humanize_content():
    """步骤3：去AI味处理"""
    log("\n" + "=" * 60)
    log("步骤 3/4: 去AI味处理")
    log("=" * 60)
    
    humanizer_script = os.path.join(SCRIPTS_DIR, 'humanizer_integration.py')
    
    if not os.path.exists(humanizer_script):
        log("✗ 未找到humanizer脚本", "ERROR")
        return False
    
    log("执行去AI味处理...")
    success, stdout, stderr = run_command(f'python "{humanizer_script}"')
    
    if success:
        log("✓ 去AI味处理完成")
        if stdout:
            print(stdout)
        return True
    else:
        log("⚠️  去AI味处理失败（可能没有新文件）", "WARNING")
        return True  # 不阻断流程

def step_4_push_to_github():
    """步骤4：推送到GitHub"""
    log("\n" + "=" * 60)
    log("步骤 4/4: 推送到GitHub")
    log("=" * 60)
    
    git_push_script = os.path.join(SCRIPTS_DIR, 'auto_git_push.py')
    
    if not os.path.exists(git_push_script):
        log("✗ 未找到Git推送脚本", "ERROR")
        return False
    
    log("执行Git推送...")
    success, stdout, stderr = run_command(f'python "{git_push_script}"')
    
    if success:
        log("✓ GitHub推送完成")
        if stdout:
            print(stdout)
        return True
    else:
        log("✗ GitHub推送失败", "ERROR")
        if stderr:
            print(stderr)
        return False

def main():
    """主流程"""
    print("\n")
    print("=" * 60)
    print("  AI内容自动化工作流 v2.0")
    print("  " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("=" * 60)
    print()
    
    # 检查项目目录
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        log(f"✓ 创建输出目录: {OUTPUT_DIR}")
    
    # 获取今日目录
    today_dir, today = get_today_dir()
    log(f"✓ 今日工作目录: {today_dir}")
    print()
    
    # 执行工作流
    results = []
    
    # 步骤0：生成选题提案
    results.append(("生成选题提案", step_0_generate_topic_proposals()))
    
    # 步骤1：收集热点
    results.append(("收集AI热点", step_1_collect_hot_topics()))
    
    # 步骤2：生成内容
    results.append(("生成内容", step_2_generate_content()))
    
    # 步骤3：去AI味
    results.append(("去AI味处理", step_3_humanize_content()))
    
    # 步骤4：推送GitHub
    results.append(("推送GitHub", step_4_push_to_github()))
    
    # 输出总结
    print("\n")
    log("=" * 60)
    log("执行总结")
    log("=" * 60)
    
    for step_name, success in results:
        status = "✓ 成功" if success else "✗ 失败"
        log(f"{step_name}: {status}")
    
    all_success = all(result[1] for result in results)
    
    if all_success:
        log("\n🎉 所有步骤执行成功！", "SUCCESS")
        log(f"今日目录: {today_dir}")
        log(f"GitHub仓库: https://github.com/cosysun/AI-Content-Archive")
    else:
        log("\n⚠️  部分步骤失败，请检查日志", "WARNING")
        log("提示: 内容生成步骤需要通过Claude对话完成")
    
    print()
    return all_success

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        log("\n用户中断执行", "WARNING")
        sys.exit(1)
    except Exception as e:
        log(f"\n执行出错: {e}", "ERROR")
        import traceback
        traceback.print_exc()
        sys.exit(1)
