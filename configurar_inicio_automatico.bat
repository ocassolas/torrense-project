@echo off
title Configurar Inicio Automatico - Mercado Torrense

echo.
echo  ============================================
echo    MERCADO TORRENSE
echo    Configurar Inicio Automatico
echo  ============================================
echo.
echo  Configurando para iniciar ao ligar o computador...
echo.

set STARTUP=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup
set VBS=%~dp0iniciar.vbs
set ATALHO=%STARTUP%\MercadoTorrense.lnk

powershell -Command "$sh = New-Object -ComObject WScript.Shell; $s = $sh.CreateShortcut('%ATALHO%'); $s.TargetPath = 'wscript.exe'; $s.Arguments = '\""%VBS%\"\"'; $s.WorkingDirectory = '%~dp0'; $s.Save()"

if exist "%ATALHO%" (
    echo  ============================================
    echo    SUCESSO!
    echo  ============================================
    echo.
    echo  O sistema ira iniciar automaticamente toda
    echo  vez que o computador for ligado.
    echo.
    echo  Para CANCELAR, execute:
    echo    cancelar_inicio_automatico.bat
    echo.
) else (
    echo  ERRO! Nao foi possivel configurar.
    echo  Tente executar como Administrador.
    echo.
)

pause
