@echo off

net session >nul 2>&1
if %errorLevel% neq 0 (
    echo Solicitando permissao de administrador...
    powershell -Command "Start-Process '%~0' -Verb RunAs"
    exit
)

start "" /b "C:\Users\arthu\dashboard-app\commands\startHttpServer.bat"
cd "C:\users\arthu\dashboard-app\frontend\"
npm run dev