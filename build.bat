@echo off

if "%1" == "clean" (
    if exist bin (
        rmdir bin /S /Q
    )

    if exist Hexa\src\hxpch.h.gch (
        del Hexa\src\hxpch.h.gch
    )
)

if not exist Hexa\src\hxpch.h.gch (
    g++ Hexa\src\hxpch.h -o Hexa\src\hxpch.h.gch
)

if not exist bin (
    mkdir bin
)

g++ -shared "Hexa/src/Hexa/*.cpp" ^
-o "bin/Hexa.dll" ^
-I"Hexa/src" ^
-I"Hexa/src/Hexa" ^
-I"Hexa/src/Hexa/Events" ^
-I"Hexa/vendor/spdlog/include" ^
-I"Hexa/vendor/SDL2/include" ^
-L"Hexa/vendor/SDL2/lib" ^
-lmingw32 -lSDL2main -lSDL2 ^
-DHX_PLATFORM_WINDOWS -DHX_BUILD_DLL
echo Hexa DLL built successfully!

g++ "Sandbox/src/SandboxApp.cpp" ^
-o "bin/Sandbox.exe" ^
-I"Hexa/src" ^
-I"Hexa/vendor/spdlog/include" ^
-L"bin" ^
-lHexa -Wl,-rpath, ^
-DHX_PLATFORM_WINDOWS -DHX_BUILD_DLL
echo SandboxApp built successfully!

copy Hexa\vendor\SDL2\bin\SDL2.dll bin\SDL2.dll /y
echo SDL2.dll copied successfully!
