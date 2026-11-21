@echo off
cd /d "%~dp0"
title Uvicorn Launcher

:menu
cls
echo ==========================================
echo      Select how to start the server
echo ==========================================
echo   1 - python -m uvicorn main:app
echo   2 - py -m uvicorn main:app
echo   3 - uvicorn main:app
echo   4 - Exit
echo ==========================================

choice /c 1234 /n /m "Chose (1-4): "

if errorlevel 4 exit /b
if errorlevel 3 goto opt3
if errorlevel 2 goto opt2
if errorlevel 1 goto opt1

:opt1
echo.
echo Starting with python...
python -m uvicorn main:app --reload
goto end

:opt2
echo.
echo Starting with py...
py -m uvicorn main:app --reload
goto end

:opt3
echo.
echo Starting with uvicorn...
uvicorn main:app --reload
goto end

:end
echo.
echo Server stopped.
pause
