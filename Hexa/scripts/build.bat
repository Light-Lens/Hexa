@echo off

if not exist ..\..\bin\ (
  mkdir ..\..\bin\
)

REM Compile Hexa as a DLL
g++ -shared "..\src\Hexa\*.cpp" -o "..\..\bin\Hexa.dll" -I"..\src\Hexa" -I"..\src\Hexa\Hexa" -DHX_PLATFORM_WINDOWS -DHX_BUILD_DLL

echo Hexa DLL built successfully!
