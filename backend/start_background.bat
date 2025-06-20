@echo off
echo Starting Hireova API in background...

REM Start minimized in background
start /min cmd /c "venv\Scripts\activate && python run.py"

echo.
echo API server started in background!
echo.
echo To stop the server:
echo 1. Open Task Manager
echo 2. Find "python.exe" 
echo 3. End task
echo.
echo API available at: http://localhost:8000
echo.
pause