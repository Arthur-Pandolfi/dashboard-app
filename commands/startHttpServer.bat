@echo off
:: Verifica se o script já está rodando como administrador
net session >nul 2>&1
if %errorLevel% neq 0 (
    echo Solicitando permissao de administrador...
    powershell -Command "Start-Process '%~0' -Verb RunAs"
    exit
)

:: Inicia o XAMPP Control
echo Iniciando Xampp...
start "" "C:\xampp\xampp-control.exe"
echo Xampp iniciado

:: Inicia o Apache
echo Iniciando Apache...
start "" /b "C:\xampp\apache_start.bat"
echo Apache iniciado

:: Inicia o MySQL
echo Iniciando MySQL...
start "" /b "C:\xampp\mysql_start.bat"
echo MySQL iniciado

cls
echo Servidor iniciado com sucesso!

pause