@ECHO OFF

title Compile Hexa engine
echo Compiling Hexa engine.

pyinstaller.exe --icon=Logo.ico --onefile main.py

mkdir Hexa\res
copy res\* Hexa\res\*
move dist\main.exe Hexa\Hexa.exe

rmdir /s /q dist
rmdir /s /q build
rmdir /s /q __pycache__

del Hexa.spec

cls
if EXIST Hexa\Hexa.exe goto Compiled
if NOT EXIST Hexa\Hexa.exe goto NotCompiled

:Compiled
echo Hexa Compiled Successfully!
echo|set /p="Continue."
pause >nul
exit

:NotCompiled
echo Can't Compile Hexa!
echo|set /p="Continue."
pause >nul
exit
