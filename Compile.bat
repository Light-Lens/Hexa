@ECHO OFF

title Compile Hexa engine
echo Compiling Hexa engine.

pyinstaller.exe --icon=Logo.ico --onefile Quantum.py
cls

echo Done.
move dist\Hexa.exe ..\Hexa.exe

cd src
del dist
del build
del __pycache__
del Quantum.spec

rmdir dist
rmdir build
rmdir __pycache__

echo|set /p="Continue."
pause >nul
exit
