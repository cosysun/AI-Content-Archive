#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI 内容创作工作流 - 快速启动脚本
作者：AI Content Creator
日期：2026-02-17
"""

import os
import sys
import json
from datetime import datetime
from pathlib import Path

def setup_project():
    """初始化项目结构"""
    print("🚀 正在初始化项目...")
    
    base_dir = Path(__file__).parent
    
    # 创建必要的目录
    directories = [
        "config",
        "scripts",
        "data/raw",
        "data/processed",
        "output",
        "templates",
        "logs"
    ]
    
    for dir_path in directories:
        full_path = base_dir / dir_path
        full_path.mkdir(parents=True, exist_ok=True)
        print(f"✅ 创建目录：{dir_path}")
    
    print("\n✨ 项目结构初始化完成！")

def check_dependencies():
    """检查依赖库"""
    print("\n🔍 检查Python依赖...")
    
    required_packages = [
        "requests",
        "anthropic",
        "openai"
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} (未安装)")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n⚠️ 缺少依赖库，请运行：")
        print(f"pip install {' '.join(missing_packages)}")
        return False
    
    print("\n✅ 所有依赖库已安装！")
    return True

def create_sample_config():
    """创建示例配置文件"""
    config_dir = Path(__file__).parent / "config"
    
    # API密钥配置模板
    api_config = {
        "anthropic": {
            "api_key": "YOUR_CLAUDE_API_KEY",
            "model": "claude-3-opus-20240229"
        },
        "openai": {
            "api_key": "YOUR_OPENAI_API_KEY",
            "model": "gpt-4-turbo-preview"
        },
        "wechat_bot": {
            "webhook_url": "YOUR_WECHAT_BOT_WEBHOOK"
        }
    }
    
    config_file = config_dir / "api_keys.json"
    if not config_file.exists():
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(api_config, f, indent=2, ensure_ascii=False)
        print(f"✅ 创建配置文件：{config_file}")
        print("⚠️ 请编辑 config/api_keys.json 填入你的API密钥")
    else:
        print(f"ℹ️ 配置文件已存在：{config_file}")

def show_menu():
    """显示主菜单"""
    print("\n" + "="*50)
    print("    AI 内容创作工作流 - 控制面板")
    print("="*50)
    print("\n📋 可用命令：\n")
    print("  1. setup     - 初始化项目结构")
    print("  2. collect   - 执行每日数据收集")
    print("  3. generate  - 生成内容（需先收集数据）")
    print("  4. check     - 检查系统状态")
    print("  5. help      - 显示帮助信息")
    print("  6. exit      - 退出程序")
    print("\n" + "="*50)

def show_help():
    """显示帮助信息"""
    help_text = """
📖 使用指南

【首次使用】
1. 运行 `python quick_start.py setup` 初始化项目
2. 编辑 config/api_keys.json 填入API密钥
3. 运行 `python quick_start.py collect` 测试数据收集

【日常使用】
- 每天早上7点自动执行数据收集（需设置定时任务）
- 查看推送到微信的摘要，选择感兴趣的话题
- 运行 `python quick_start.py generate` 生成完整内容

【设置定时任务】
Windows:
1. 打开"任务计划程序"
2. 创建基本任务
3. 触发器：每天 07:00
4. 操作：启动程序
   - 程序：python.exe
   - 参数：quick_start.py collect
   - 起始于：C:\\Users\\andygzsun\\AI_Content_Creation

【获取帮助】
- 查看 WORKFLOW_CONFIG.md 了解完整配置
- 查看 logs/ 目录下的日志文件排查问题
    """
    print(help_text)

def main():
    """主函数"""
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "setup":
            setup_project()
            create_sample_config()
            print("\n🎉 项目初始化完成！")
            print("下一步：编辑 config/api_keys.json 填入你的API密钥")
            
        elif command == "collect":
            print("🔍 开始收集数据...")
            print("⚠️ 此功能需要完整脚本支持，请查看 WORKFLOW_CONFIG.md")
            # TODO: 调用实际的数据收集脚本
            
        elif command == "generate":
            print("🎨 开始生成内容...")
            print("⚠️ 此功能需要完整脚本支持，请查看 WORKFLOW_CONFIG.md")
            # TODO: 调用实际的内容生成脚本
            
        elif command == "check":
            print("🔍 检查系统状态...\n")
            setup_project()
            check_dependencies()
            
        elif command == "help":
            show_help()
            
        else:
            print(f"❌ 未知命令：{command}")
            print("运行 `python quick_start.py help` 查看帮助")
    
    else:
        show_menu()
        print("\n💡 提示：运行 `python quick_start.py help` 查看详细使用指南")

if __name__ == "__main__":
    main()
