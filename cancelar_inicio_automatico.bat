@echo off
title Cancelar Inicio Automatico - Mercado Torrense

echo.
echo  ============================================
echo    MERCADO Torrense
echo    Cancelar Inicio Automatico
echo  ============================================
echo.

set ATALHO=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\MercadoTorrense.lnk

if exist "%ATALHO%" (
    del "%ATALHO%"
    echo  SUCESSO! O sistema nao ira mais iniciar
    echo  automaticamente ao ligar o computador.
) else (
    echo  O inicio automatico ja estava desativado.
)

echo.
pause
