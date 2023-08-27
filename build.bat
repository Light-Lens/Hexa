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

if not exist bin/ (
    mkdir bin
)

g++ -shared "src\Hexa\*.cpp" ^
-o "bin\Hexa.dll" ^
-I"Hexa\src" ^
-I"Hexa\src\Hexa" ^
-I"Hexa\src\Hexa\Events" ^
-I"Hexa\vendor\spdlog\include" ^
-I"Hexa\vendor\spdlog\include" ^
-DHX_PLATFORM_WINDOWS -DHX_BUILD_DLL

echo Hexa DLL built successfully!

g++ "Sandbox\src\SandboxApp.cpp" ^
-L"bin" ^
-lHexa -Wl,-rpath,
-DHX_PLATFORM_WINDOWS -DHX_BUILD_DLL

echo SandboxApp built successfully!
