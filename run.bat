@echo off
REM Quick Start Script for Windows
REM Run this to start the application: run.bat

cls
echo.
echo ==================================================
echo   AI-Enhanced Employee Onboarding with Backboard
echo ==================================================
echo.

REM Check Python
echo Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [X] Python not found. Please install Python 3.7+
    echo Visit: https://www.python.org/downloads/
    pause
    exit /b 1
)

for /f "tokens=2" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
echo [OK] Python %PYTHON_VERSION% found

REM Check if venv exists
if not exist "venv" (
    echo.
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate venv
echo [OK] Virtual environment ready

REM Install requirements
echo.
echo Installing Flask and dependencies...
python -m pip install -r requirements.txt -q
if %errorlevel% neq 0 (
    echo [X] Failed to install dependencies
    pause
    exit /b 1
)

REM Start the app
echo.
echo ==================================================
echo [OK] Starting Onboarding Application...
echo ==================================================
echo.
echo   URL: http://localhost:5000
echo   
echo   Tips:
echo   - Click "AI Insights" on any card for learning enhancements
echo   - Click "Related" to see connected topics
echo   - Press ESC to close insights
echo   - Responsive design works on mobile
echo.
echo   Press Ctrl+C to stop the server
echo ==================================================
echo.

python OnBoard.py

pause
