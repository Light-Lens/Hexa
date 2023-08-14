@echo off

if not exist ..\..\bin\ (
  mkdir ..\..\bin\
)

REM Compile SandboxApp and link with Hexa DLL
g++ ..\src\main.cpp -o ..\..\bin\SandboxApp.exe -I..\..\Hexa\src -L..\..\bin -lHexa -Wl,-rpath,. -DHX_PLATFORM_WINDOWS -DHX_BUILD_DLL

echo SandboxApp built successfully!
