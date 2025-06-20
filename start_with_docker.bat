@echo off
echo.
echo ========================================
echo    Hireova AI - Docker Setup
echo ========================================
echo.

REM Check if Docker is running
docker --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Docker is not installed or not running
    echo.
    echo Please install Docker Desktop from:
    echo https://www.docker.com/products/docker-desktop/
    echo.
    pause
    exit /b 1
)

echo [1/4] Starting Docker containers...
docker compose up -d

echo.
echo [2/4] Waiting for services to be ready...
timeout /t 5 /nobreak >nul

echo.
echo [3/4] Checking service status...
docker compose ps

echo.
echo [4/4] Setting up backend...
cd backend
if not exist venv (
    python -m venv venv
)
call venv\Scripts\activate.bat

echo Installing Python dependencies...
pip install -r requirements.txt

echo.
echo ========================================
echo    Docker Services Started!
echo ========================================
echo.
echo PostgreSQL: localhost:5432
echo   Database: hireova_db
echo   User: hireova_user
echo   Password: hireova_pass
echo.
echo Redis: localhost:6379
echo.
echo To start the API server:
echo   cd backend
echo   venv\Scripts\activate
echo   python run.py
echo.
echo To stop Docker services:
echo   docker compose down
echo.
pause