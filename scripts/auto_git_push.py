#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
自动Git推送脚本
每天自动提交并推送内容到GitHub
"""

import os
import subprocess
from datetime import datetime
from pathlib import Path

class GitAutoPush:
    def __init__(self, repo_path):
        self.repo_path = Path(repo_path)
        self.date_str = datetime.now().strftime("%Y-%m-%d")
        
    def run_command(self, command, cwd=None):
        """执行命令并返回结果"""
        if cwd is None:
            cwd = self.repo_path
            
        try:
            result = subprocess.run(
                command,
                cwd=cwd,
                shell=True,
                capture_output=True,
                text=True,
                encoding='utf-8'
            )
            return result.returncode == 0, result.stdout, result.stderr
        except Exception as e:
            return False, "", str(e)
    
    def check_git_status(self):
        """检查Git状态"""
        success, stdout, stderr = self.run_command("git status --porcelain")
        
        if not success:
            print(f"[ERROR] Git状态检查失败: {stderr}")
            return False, []
        
        # 解析变更文件
        changed_files = []
        for line in stdout.strip().split('\n'):
            if line:
                changed_files.append(line.strip())
        
        return True, changed_files
    
    def git_add_all(self):
        """添加所有变更文件"""
        success, stdout, stderr = self.run_command("git add .")
        
        if not success:
            print(f"[ERROR] Git add失败: {stderr}")
            return False
        
        print("[OK] 文件已添加到暂存区")
        return True
    
    def git_commit(self, message=None):
        """提交变更"""
        if message is None:
            message = f"Daily content update: {self.date_str}"
        
        # 转义引号
        message = message.replace('"', '\\"')
        
        success, stdout, stderr = self.run_command(f'git commit -m "{message}"')
        
        if not success:
            if "nothing to commit" in stderr or "nothing to commit" in stdout:
                print("[INFO] 没有需要提交的变更")
                return True
            else:
                print(f"[ERROR] Git commit失败: {stderr}")
                return False
        
        print(f"[OK] 提交成功: {message}")
        return True
    
    def git_push(self, remote="origin", branch="main"):
        """推送到远程仓库"""
        success, stdout, stderr = self.run_command(f"git push {remote} {branch}")
        
        if not success:
            print(f"[ERROR] Git push失败: {stderr}")
            
            # 如果是第一次push，提示用户设置upstream
            if "no upstream branch" in stderr or "failed to push" in stderr:
                print("\n[提示] 可能是第一次推送，请手动执行:")
                print(f"    git push -u {remote} {branch}")
                return False
            
            return False
        
        print(f"[OK] 推送成功到 {remote}/{branch}")
        return True
    
    def get_daily_summary(self):
        """生成每日内容摘要"""
        output_dir = self.repo_path / "output"
        date_prefix = datetime.now().strftime("%Y%m%d")
        
        files = [
            f"{date_prefix}_wechat_article_humanized.md",
            f"{date_prefix}_xiaohongshu_post_humanized.md",
            f"{date_prefix}_video_script_humanized.md",
        ]
        
        existing_files = []
        for f in files:
            if (output_dir / f).exists():
                existing_files.append(f)
        
        if existing_files:
            return f"Daily content update: {self.date_str}\n\nFiles:\n" + "\n".join(f"- {f}" for f in existing_files)
        else:
            return f"Daily content update: {self.date_str}"
    
    def auto_push(self):
        """自动提交并推送"""
        print(f"\n{'='*60}")
        print(f"  Git Auto Push - {self.date_str}")
        print(f"{'='*60}\n")
        
        # 1. 检查状态
        print("[1/4] 检查Git状态...")
        success, changed_files = self.check_git_status()
        
        if not success:
            return False
        
        if not changed_files:
            print("[INFO] 没有变更，无需推送")
            return True
        
        print(f"[OK] 发现 {len(changed_files)} 个变更文件:")
        for f in changed_files[:10]:  # 只显示前10个
            print(f"    {f}")
        if len(changed_files) > 10:
            print(f"    ... 还有 {len(changed_files) - 10} 个文件")
        
        # 2. 添加文件
        print("\n[2/4] 添加文件到暂存区...")
        if not self.git_add_all():
            return False
        
        # 3. 提交
        print("\n[3/4] 提交变更...")
        commit_message = self.get_daily_summary()
        if not self.git_commit(commit_message):
            return False
        
        # 4. 推送
        print("\n[4/4] 推送到GitHub...")
        if not self.git_push():
            return False
        
        print(f"\n{'='*60}")
        print("  推送完成！")
        print(f"{'='*60}\n")
        
        return True

def main():
    """主函数"""
    import sys
    
    # 获取脚本所在目录的父目录（项目根目录）
    script_dir = Path(__file__).parent
    repo_path = script_dir.parent
    
    print(f"项目目录: {repo_path}")
    
    # 创建GitAutoPush实例
    pusher = GitAutoPush(repo_path)
    
    # 执行自动推送
    success = pusher.auto_push()
    
    if success:
        print("\n[SUCCESS] 所有操作完成")
        sys.exit(0)
    else:
        print("\n[FAILED] 部分操作失败，请检查错误信息")
        sys.exit(1)

if __name__ == "__main__":
    main()
