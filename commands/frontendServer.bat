@echo off

:: Vari�veis
set "mode=%1%"

:: Solicita permiss�o de administrador
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo Solicitando permissao de administrador...
    powershell -Command "Start-Process cmd -ArgumentList '/c %~f0 %mode% %dataBase1% %dataBase2%' -Verb RunAs"
    exit
)

:: Verifica se o modo � v�lido
if not "%mode%"=="open" if not "%mode%"=="close" (
    cd /d %~dp0
    cd ".\errorMessage"
    python close_or_open_error.py
    echo Erro: Modo inv�lido! Use "open" ou "close".
    exit /b 1
)

:: Abre o servidor
if "%mode%"=="open" (
   cd /d %~dp0
   echo %cd%
   cd ..\frontend
   npm run dev
) 
:: Fecha o servidor
if "%mode%"=="close" (
   taskkill /F /IM node.exe
   echo Servidor Backend Python Finalizado.
)

