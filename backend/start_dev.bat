@echo off
echo Starting Hireova Development Server...
echo.
echo Press Ctrl+C to stop the server
echo The server will auto-reload when you change code
echo.

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Start the development server
python run.py