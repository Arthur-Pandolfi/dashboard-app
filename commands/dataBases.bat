@echo off

:: Variáveis
set "mode=%1"
set "dataBase1=%2"
set "dataBase2=%3"

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
    echo Erro: Modo inválido! Use "open" ou "stop".
    exit /b 1
)

:: Verifica quais bancos devem ser abertos
if "%mode%"=="open" (
    if "%dataBase1%"=="mySql" (
        echo Iniciando Apache...
        start "" /b "C:\xampp\apache_start.bat"
        echo Apache iniciado.
        
        echo Iniciando MySQL...
        start "" /b "C:\xampp\mysql_start.bat"
        echo MySQL iniciado.
    )
    if "%dataBase2%"=="keyDB" (
        echo Iniciando KeyDB...
        start "" powershell -Command "ubuntu run keydb-server"
        echo KeyDB iniciado.
    )
)

:: Verifica quais bancos devem ser fechados
if "%mode%"=="close" (
    
    if "%dataBase1%"=="mySql" (
        echo Encerrando Apache...
        taskkill /F /IM httpd.exe
        echo Apache encerrado.
        
        echo Encerrando MySQL...
        taskkill /F /IM mysqld.exe
        echo MySQL encerrado.
    )
    if "%dataBase2%"=="keyDB" (     
        taskkill /F /IM wsl.exe
        taskkill /F /IM vmmem.exe
        taskkill /F /IM wslrelay.exe
        taskkill /F /IM wslService.exe

        echo keyDB encerrado
    )
)

