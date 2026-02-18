# GitHub仓库设置指南

## 📌 重要提示

你的项目已经在本地初始化完成，并且完成了第一次提交。现在需要你手动在GitHub上创建仓库并关联。

---

## 🚀 步骤1：在GitHub上创建仓库

### 1.1 访问GitHub

打开浏览器，访问：https://github.com/new

### 1.2 填写仓库信息

- **Repository name**: `AI-Content-Archive`（或你喜欢的名字）
- **Description**: `🤖 AI内容创作自动归档 - 每日生成的微信公众号、小红书、视频脚本内容`
- **Public/Private**: 
  - ✅ **Private**（推荐）- 如果内容包含草稿或私密信息
  - ⚪ **Public** - 如果你想分享你的内容创作流程
- **Initialize this repository with**: 
  - ❌ 不要勾选 "Add a README file"
  - ❌ 不要勾选 "Add .gitignore"
  - ❌ 不要勾选 "Choose a license"

### 1.3 点击 "Create repository"

---

## 🔗 步骤2：关联本地仓库到GitHub

### 2.1 复制GitHub仓库URL

创建仓库后，GitHub会显示一个页面，上面有仓库的URL。

**HTTPS方式**（推荐新手）：
```
https://github.com/YOUR_USERNAME/AI-Content-Archive.git
```

**SSH方式**（如果你已配置SSH key）：
```
git@github.com:YOUR_USERNAME/AI-Content-Archive.git
```

### 2.2 在本地关联远程仓库

**打开PowerShell，执行以下命令**：

```powershell
# 进入项目目录
cd C:\Users\andygzsun\AI_Content_Creation

# 添加远程仓库（替换YOUR_USERNAME为你的GitHub用户名）
git remote add origin https://github.com/YOUR_USERNAME/AI-Content-Archive.git

# 如果你用SSH方式（需要先配置SSH key）
# git remote add origin git@github.com:YOUR_USERNAME/AI-Content-Archive.git

# 验证是否添加成功
git remote -v
```

**预期输出**：
```
origin  https://github.com/YOUR_USERNAME/AI-Content-Archive.git (fetch)
origin  https://github.com/YOUR_USERNAME/AI-Content-Archive.git (push)
```

### 2.3 推送到GitHub

```powershell
# 推送master分支到GitHub（并设置upstream）
git push -u origin master
```

**如果使用HTTPS方式，会提示输入GitHub用户名和密码**：
- 用户名：你的GitHub用户名
- 密码：**Personal Access Token**（不是GitHub登录密码）

---

## 🔑 步骤3：配置GitHub Personal Access Token（HTTPS方式）

### 3.1 为什么需要Token？

GitHub从2021年8月开始，不再支持用密码push代码，必须使用Personal Access Token。

### 3.2 创建Token

1. 登录GitHub
2. 访问：https://github.com/settings/tokens
3. 点击 "Generate new token" → "Generate new token (classic)"
4. 设置：
   - **Note**: `AI Content Archive`
   - **Expiration**: `90 days`（或选择更长时间）
   - **Select scopes**: 勾选 `repo`（包含所有repo权限）
5. 点击 "Generate token"
6. **立即复制Token！**（只显示一次，关闭页面后无法再查看）

### 3.3 使用Token

当执行 `git push` 时：
- 用户名：你的GitHub用户名
- 密码：粘贴刚才复制的Token

### 3.4 保存凭据（避免每次输入）

**Windows Git Credential Manager**（推荐）：
```powershell
# Git会自动提示保存凭据，选择"是"即可
# 下次push时不需要再输入
```

---

## 🔐 步骤4：配置SSH方式（可选，推荐）

### 4.1 为什么用SSH？

- ✅ 不需要每次输入密码或Token
- ✅ 更安全
- ✅ 配置一次，永久使用

### 4.2 生成SSH Key

```powershell
# 生成SSH key（替换你的邮箱）
ssh-keygen -t ed25519 -C "your_email@example.com"

# 按Enter使用默认路径（C:\Users\andygzsun\.ssh\id_ed25519）
# 设置密码（可以留空直接按Enter）
```

### 4.3 添加SSH Key到GitHub

```powershell
# 复制公钥内容
Get-Content C:\Users\andygzsun\.ssh\id_ed25519.pub | clip
```

然后：
1. 访问：https://github.com/settings/keys
2. 点击 "New SSH key"
3. Title: `AI Content Creation - Windows PC`
4. Key: 粘贴刚才复制的内容
5. 点击 "Add SSH key"

### 4.4 测试SSH连接

```powershell
ssh -T git@github.com
```

**预期输出**：
```
Hi YOUR_USERNAME! You've successfully authenticated, but GitHub does not provide shell access.
```

### 4.5 切换到SSH方式

```powershell
# 如果之前添加了HTTPS的remote，先删除
git remote remove origin

# 添加SSH方式的remote
git remote add origin git@github.com:YOUR_USERNAME/AI-Content-Archive.git

# 推送
git push -u origin master
```

---

## ✅ 步骤5：验证设置成功

### 5.1 检查GitHub仓库

访问：`https://github.com/YOUR_USERNAME/AI-Content-Archive`

应该能看到：
- ✅ README.md
- ✅ output/ 目录（包含今天的内容）
- ✅ scripts/ 目录
- ✅ docs/ 目录

### 5.2 测试自动推送脚本

```powershell
# 运行自动推送脚本
python scripts\auto_git_push.py
```

**预期输出**：
```
============================================================
  Git Auto Push - 2026-02-19
============================================================

[1/4] 检查Git状态...
[INFO] 没有变更，无需推送

============================================================
  推送完成！
============================================================
```

---

## 🤖 步骤6：集成到自动化工作流

### 6.1 修改定时任务（如果已创建）

如果你之前创建了定时任务，现在需要更新它，添加Git推送步骤：

**查看现有任务**：
```powershell
schtasks /query /tn "AI Content Creation" /fo list /v
```

**创建新的定时任务（包含Git推送）**：
```powershell
# 创建一个批处理脚本
$batchContent = @"
@echo off
cd C:\Users\andygzsun\AI_Content_Creation
python scripts\humanizer_integration.py
python scripts\auto_git_push.py
pause
"@

$batchContent | Out-File -FilePath "C:\Users\andygzsun\AI_Content_Creation\daily_workflow.bat" -Encoding ASCII

# 创建定时任务
schtasks /create /tn "AI Content Creation with Git" /tr "C:\Users\andygzsun\AI_Content_Creation\daily_workflow.bat" /sc daily /st 07:00 /f
```

### 6.2 测试完整流程

```powershell
# 手动运行批处理脚本
C:\Users\andygzsun\AI_Content_Creation\daily_workflow.bat
```

---

## 📊 步骤7：查看归档内容

### 7.1 在GitHub上查看

访问你的仓库：`https://github.com/YOUR_USERNAME/AI-Content-Archive`

点击 "Commits" 可以看到每天的提交历史。

### 7.2 克隆到其他设备

```bash
# 在其他电脑上克隆仓库
git clone https://github.com/YOUR_USERNAME/AI-Content-Archive.git
```

---

## ❓ 常见问题

### Q1: push时提示 "Permission denied"

**原因**：没有权限

**解决**：
1. 检查Token权限是否包含 `repo`
2. 检查仓库名是否正确
3. 检查用户名是否正确

### Q2: push时提示 "Authentication failed"

**原因**：
- HTTPS方式：Token过期或错误
- SSH方式：SSH key未添加或配置错误

**解决**：
- HTTPS：重新生成Token
- SSH：检查 `ssh -T git@github.com`

### Q3: 如何修改仓库可见性（Public ↔ Private）

1. 访问仓库页面
2. 点击 "Settings"
3. 滚动到 "Danger Zone"
4. 点击 "Change repository visibility"

### Q4: 如何删除敏感信息？

如果不小心提交了敏感信息（如API key）：

```powershell
# 1. 从历史中删除文件
git filter-branch --force --index-filter "git rm --cached --ignore-unmatch path/to/sensitive/file" --prune-empty --tag-name-filter cat -- --all

# 2. 强制推送
git push origin --force --all

# 3. 通知GitHub清理缓存
# 访问：https://github.com/YOUR_USERNAME/AI-Content-Archive/settings
```

**更好的做法**：重新生成敏感信息（如更换API key）

---

## 📝 总结

完成以上步骤后，你将拥有：

✅ GitHub仓库（在线备份）  
✅ 自动化Git推送（每天自动归档）  
✅ 历史版本管理（可以查看任何历史版本）  
✅ 多设备访问（在任何地方都能查看内容）  

---

**下一步**：

1. 在GitHub上创建仓库
2. 在本地执行关联命令
3. 推送代码
4. 测试自动化脚本

如果遇到问题，随时告诉我！

---

生成时间：2026-02-19  
文档版本：1.0
