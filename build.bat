@echo off

if "%1" == "clean" (
    if exist bin (
        rmdir bin /S /Q
    )

    if exist Hexa/src/hxpch.h.gch (
        del Hexa/src/hxpch.h.gch
    )
)

if not exist Hexa/src/hxpch.h.gch (
    g++ Hexa/src/hxpch.h -o Hexa/src/hxpch.h.gch
)

@REM if not exist bin/ (
@REM     mkdir bin
@REM )

@REM g++ -shared "Hexa/src/Hexa/*.cpp" ^
@REM -o "bin/Hexa.dll" ^
@REM -I"Hexa/src" ^
@REM -I"Hexa/src/Hexa" ^
@REM -I"Hexa/src/Hexa/Events" ^
@REM -I"Hexa/vendor/spdlog/include" ^
@REM -I"Hexa/vendor/SDL2/include" ^
@REM -L"Hexa/vendor/SDL2/lib" ^
@REM -lmingw32 -lSDL2main -lSDL2 ^
@REM -DHX_PLATFORM_WINDOWS -DHX_BUILD_DLL

@REM echo Hexa DLL built successfully!

@REM g++ "Sandbox/src/SandboxApp.cpp" ^
@REM -I"Hexa/src" ^
@REM -L"bin" ^
@REM -lHexa -Wl,-rpath, ^
@REM -DHX_PLATFORM_WINDOWS -DHX_BUILD_DLL

@REM echo SandboxApp built successfully!
