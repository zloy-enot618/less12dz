@echo off
chcp 65001 > nul
cd /d "%~dp0"

:menu
cls
echo ==========================================
echo      Выберите способ запуска сервера:
echo ==========================================
echo   1 - python -m uvicorn main:app
echo   2 - py -m uvicorn main:app
echo   3 - uvicorn main:app (напрямую)
echo   4 - Выход
echo ==========================================

choice /c 1234 /n /m "Нажмите клавишу (1-4): "

if errorlevel 4 exit /b
if errorlevel 3 goto opt3
if errorlevel 2 goto opt2
if errorlevel 1 goto opt1

:opt1
echo.
echo Запуск через python...
python -m uvicorn main:app --reload
goto end

:opt2
echo.
echo Запуск через py...
py -m uvicorn main:app --reload
goto end

:opt3
echo.
echo Запуск напрямую через uvicorn...
uvicorn main:app --reload
goto end

:end
echo.
pause
