@echo off
echo 'cleaning up!'
del *.log /s >nul
echo 'done!'
timeout /t 1 >nul
cls
nb run
pause