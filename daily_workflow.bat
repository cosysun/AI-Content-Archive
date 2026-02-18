@echo off
REM AI Content Creation - Daily Workflow with Git Push
REM This script runs daily at 7:00 AM

echo.
echo ============================================================
echo   AI Content Creation - Daily Workflow
echo   Date: %DATE% %TIME%
echo ============================================================
echo.

cd /d C:\Users\andygzsun\AI_Content_Creation

echo [Step 1/2] Processing content with Humanizer...
python scripts\humanizer_integration.py
IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Humanizer processing failed!
    pause
    exit /b 1
)

echo.
echo [Step 2/2] Pushing to GitHub...
python scripts\auto_git_push.py
IF %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Git push failed!
    pause
    exit /b 1
)

echo.
echo ============================================================
echo   All tasks completed successfully!
echo ============================================================
echo.

REM Uncomment the line below if you want to keep the window open
REM pause
