@ECHO OFF

title Compile Hexa engine
echo Compiling Hexa engine.

pyinstaller.exe --icon=Logo.ico --onefile Hexa.py
cls

echo Done.
move dist\Hexa.exe Hexa.exe

del dist
del build
del __pycache__
del Hexa.spec

echo|set /p="Continue."
pause >nul
exit
