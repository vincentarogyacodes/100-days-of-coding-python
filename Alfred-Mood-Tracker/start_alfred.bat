@echo off
echo ========================================
echo    Alfred Mood Tracker - Starting...
echo ========================================
echo.
echo Please wait while Alfred starts up...
echo.
echo Starting Flask application...
echo.
start "Alfred Mood Tracker" python app.py
echo.
echo Alfred is starting in a new window...
echo.
echo Once you see "Debugger is active!" in the new window:
echo 1. Open your web browser
echo 2. Go to: http://localhost:5000
echo.
echo To stop Alfred, close the command window that opened.
echo.
pause
