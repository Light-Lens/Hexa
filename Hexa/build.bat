@echo off

if not exist ..\bin\ (
  mkdir ..\bin\
)

REM Create the precompiled header (PCH)
@REM g++ "src\hxpch.h" -o "src\hxpch.h.gch"

REM Compile Hexa as a DLL
g++ -shared "src\Hexa\*.cpp" ^
-o "..\bin\Hexa.dll" ^
-I"src" ^
-I"src\Hexa" ^
-I"src\Hexa\Events" ^
-I"vendor\spdlog\include" ^
-DHX_PLATFORM_WINDOWS -DHX_BUILD_DLL

echo Hexa DLL built successfully!
