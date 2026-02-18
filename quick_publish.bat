@echo off
chcp 65001 >nul
echo ========================================
echo   AI内容自动化工作流
echo   执行: 去AI味 + 推送GitHub
echo ========================================
echo.

cd /d "%~dp0.."

echo [1/2] 去AI味处理...
python scripts\humanizer_integration.py
if errorlevel 1 (
    echo [ERROR] 去AI味处理失败
    pause
    exit /b 1
)

echo.
echo [2/2] 推送到GitHub...
python scripts\auto_git_push.py
if errorlevel 1 (
    echo [ERROR] GitHub推送失败
    pause
    exit /b 1
)

echo.
echo ========================================
echo   执行完成！
echo   查看: https://github.com/cosysun/AI-Content-Archive
echo ========================================
pause
