@echo off
title Mercado Torrense - Servidor
cd /d "%~dp0"

echo.
echo  ============================================
echo    MERCADO TORRENSE - Sistema de Catalogo
echo  ============================================
echo.
echo  ATENCAO: Nao feche esta janela!
echo  O servidor precisa ficar aberto para
echo  o catalogo funcionar nas telas.
echo.
echo  Acesse no navegador:
echo    Gerenciamento: http://localhost:5000/gerenciar
echo    Catalogo TV:   http://localhost:5000/catalogo
echo.
echo  ============================================
echo.

set PYTHONPATH=C:\Users\joaop\AppData\Local\Programs\Python\Python314\Lib\site-packages
C:\Python314\python.exe app.py
pause
