@echo off
echo ===================================
echo  Cafe Sales Analysis for Power BI  
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

:: Install required packages if needed
echo Checking for required Python packages...
pip install pandas matplotlib seaborn --quiet

:: Run the analysis script
echo.
echo 🚀 Running cafe sales analysis...
python run_analysis.py

:: Pause to see any error messages
echo.
pause
