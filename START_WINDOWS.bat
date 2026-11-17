@echo off
setlocal
cd /d "%~dp0"
title PAC-MIND - Python AI Search Lab
where py >nul 2>nul
if errorlevel 1 goto use_python
py -3 launcher.py
goto finished
:use_python
where python >nul 2>nul
if errorlevel 1 (
  echo Install Python 3.12 from https://www.python.org/downloads/
  echo Then extract this folder and run START_WINDOWS.bat again.
  pause
  exit /b 1
)
python launcher.py
:finished
if errorlevel 1 pause
