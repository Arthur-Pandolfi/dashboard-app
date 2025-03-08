@echo off

net session >nul 2>&1
if %errorLevel% neq 0 (
    echo Solicitando permissao de administrador...
    powershell -Command "Start-Process '%~0' -Verb RunAs"
    exit
)

taskkill /F /IM powershell.exe
taskkill /F /IM cmd.exe

echo Powershell e Cmd Finalizados.
pause
exit