@echo off

:: Variáveis
set "mode=%1%"

:: Solicita permissão de administrador
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo Solicitando permissao de administrador...
    powershell -Command "Start-Process cmd -ArgumentList '/c %~f0 %mode% %dataBase1% %dataBase2%' -Verb RunAs"
    exit
)

:: Verifica se o modo é válido
if not "%mode%"=="open" if not "%mode%"=="close" (
    cd /d %~dp0
    cd ".\errorMessage"
    python close_or_open_error.py
    echo Erro: Modo inválido! Use "open" ou "close".
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

