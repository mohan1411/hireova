@echo off
echo.
echo ========================================
echo    Hireova AI - Windows Setup
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.11+ from https://www.python.org/
    pause
    exit /b 1
)

echo [1/5] Creating virtual environment...
if not exist venv (
    python -m venv venv
    echo Virtual environment created!
) else (
    echo Virtual environment already exists.
)

echo.
echo [2/5] Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo [3/5] Installing dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt

echo.
echo [4/5] Setting up environment file...
if not exist .env (
    echo.
    echo Choose your database setup:
    echo 1. SQLite - Easiest, no setup required
    echo 2. PostgreSQL - Requires Docker or local installation
    echo.
    set /p choice="Enter your choice (1 or 2): "
    
    if "%choice%"=="1" (
        copy .env.sqlite .env
        echo Using SQLite for database
    ) else (
        copy .env.example .env
        echo Using PostgreSQL - Remember to start Docker containers!
    )
) else (
    echo .env file already exists
)

echo.
echo [5/5] Testing setup...
python test_setup.py

echo.
echo ========================================
echo    Setup Complete!
echo ========================================
echo.
echo To start the application:
echo   python run.py
echo.
echo Then visit:
echo   - API: http://localhost:8000
echo   - API Docs: http://localhost:8000/api/docs
echo.
pause