# Cron 任务配置

## 每日选题

```json
{
  "name": "每日5个选题",
  "schedule": "0 8 * * *",
  "timezone": "Asia/Shanghai",
  "prompt": "见 prompts.md - 每日选题 Prompt"
}
```

## 写作任务

手动触发（用户选择话题后）：
- 使用 "写作 Prompt"
- 三遍审校
- 标题拟定

---

## 执行流程

1. 8:00 定时推送 5 个选题
2. 用户选择话题
3. 执行写作 Prompt
4. 用户审阅确认
5. 保存到 GitHub
