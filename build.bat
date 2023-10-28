@echo off

if "%1" == "clean" (
    if exist bin (
        rmdir bin /S /Q
    )
)

if not exist bin (
    mkdir bin
)

g++ -shared "Hexa/src/*.cpp" ^
-o "bin/Hexa.dll" ^
-I"Hexa/src" ^
-I"Hexa/vendor/SDL2/include" ^
-L"Hexa/vendor/SDL2/lib" ^
-lmingw32 -lSDL2main -lSDL2 ^
-DHX_PLATFORM_WINDOWS -DHX_BUILD_DLL
echo Hexa DLL built successfully!

@REM g++ "Sandbox/src/SandboxApp.cpp" ^
@REM -o "bin/Sandbox.exe" ^
@REM -I"Hexa/src" ^
@REM -I"Hexa/vendor/spdlog/include" ^
@REM -L"bin" ^
@REM -lHexa -Wl,-rpath, ^
@REM -DHX_PLATFORM_WINDOWS -DHX_BUILD_DLL
@REM echo SandboxApp built successfully!

copy Hexa\vendor\SDL2\bin\SDL2.dll bin\SDL2.dll /y
echo SDL2.dll copied successfully!
