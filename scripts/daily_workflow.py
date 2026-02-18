#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
每日AI内容自动化工作流
功能：搜索热点 → 生成内容 → 去AI味 → 推送GitHub
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

def step_1_generate_content():
    """步骤1：生成AI内容"""
    log("=" * 60)
    log("步骤 1/3: 生成AI内容")
    log("=" * 60)
    
    # 这里应该调用内容生成逻辑
    # 由于原始内容生成是通过对话完成的，这里只做说明
    log("⚠️  内容生成需要手动触发或通过定时任务调用Claude")
    log("    预期生成文件:")
    log("    - 微信公众号文章")
    log("    - 小红书文章")
    log("    - 视频脚本")
    
    today = datetime.now().strftime("%Y-%m-%d")
    today_dir = os.path.join(OUTPUT_DIR, today)
    
    if os.path.exists(today_dir):
        files = os.listdir(today_dir)
        log(f"✓ 发现今日内容目录: {len(files)} 个文件")
        return True
    else:
        log("✗ 未找到今日内容目录", "WARNING")
        log(f"  期望路径: {today_dir}", "WARNING")
        return False

def step_2_humanize_content():
    """步骤2：去AI味处理"""
    log("\n" + "=" * 60)
    log("步骤 2/3: 去AI味处理")
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
        log("✗ 去AI味处理失败", "ERROR")
        if stderr:
            print(stderr)
        return False

def step_3_push_to_github():
    """步骤3：推送到GitHub"""
    log("\n" + "=" * 60)
    log("步骤 3/3: 推送到GitHub")
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
    print("  AI内容自动化工作流 v1.0")
    print("  " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("=" * 60)
    print()
    
    # 检查项目目录
    if not os.path.exists(OUTPUT_DIR):
        log("✗ output目录不存在", "ERROR")
        return False
    
    # 执行三个步骤
    results = []
    
    # 步骤1：生成内容
    results.append(("生成AI内容", step_1_generate_content()))
    
    # 步骤2：去AI味
    if results[-1][1]:  # 如果上一步成功
        results.append(("去AI味处理", step_2_humanize_content()))
    else:
        log("⊘ 跳过去AI味处理（前置步骤失败）", "WARNING")
        results.append(("去AI味处理", False))
    
    # 步骤3：推送GitHub
    if results[-1][1]:  # 如果上一步成功
        results.append(("推送GitHub", step_3_push_to_github()))
    else:
        log("⊘ 跳过GitHub推送（前置步骤失败）", "WARNING")
        results.append(("推送GitHub", False))
    
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
        log(f"查看GitHub: https://github.com/cosysun/AI-Content-Archive")
    else:
        log("\n⚠️  部分步骤失败，请检查日志", "WARNING")
    
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
