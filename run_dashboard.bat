@echo off
echo ===================================
echo  Starting Cafe Sales Dashboard     
echo ===================================
echo.

:: Check if Python is installed
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ❌ Python is not installed or not in PATH.
    echo Please install Python from https://www.python.org/downloads/
    pause
    exit /b 1
)

echo Installing required Python packages...
pip install streamlit plotly pandas --quiet

echo.
echo 🚀 Starting Cafe Sales Dashboard...
echo.
echo Please wait while the dashboard loads in your default web browser...
echo.

:: Run the Streamlit dashboard
streamlit run dashboard.py

:: Keep the console open
pause
