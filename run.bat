net session >nul 2>&1
if %errorLevel% neq 0 (
    echo Solicitando permissao de administrador...
    powershell -Command "Start-Process '%~0' -Verb RunAs"
    exit
)

start "" /b "C:\Users\arthu\OneDrive\Documentos\repositories\dashboard-app\commands\startHttpServer"
start "" /b "C:\Users\arthu\OneDrive\Documentos\repositories\dashboard-app\commands\startPythonHttpServer.bat"
start "" /b "C:\Users\arthu\OneDrive\Documentos\repositories\dashboard-app\commands\startReactServer.bat"
start "" powershell -NoExit -Command "ubuntu run keydb-server"
