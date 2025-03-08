@echo off

net session >nul 2>&1
if %errorLevel% neq 0 (
    echo Solicitando permissao de administrador...
    powershell -Command "Start-Process '%~0' -Verb RunAs"
    exit
)

cd /d %~dp0
start "" /b ".\commands\dataBases.bat" close mySql keyDB
start "" /b ".\commands\backendServer.bat" close
start "" /b ".\commands\frontendServer.bat" close
start "" /b  ".\commands\closeTerminals.bat"