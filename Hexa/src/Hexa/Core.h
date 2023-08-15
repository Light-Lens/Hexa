#pragma once

#ifdef HX_PLATFORM_WINDOWS
	#ifdef HX_BUILD_DLL
		#define Hexa_API __declspec(dllexport)

	#else
		#define Hexa_API __declspec(dllimport)

	#endif

#else
	#error Hexa only supports Windows!

#endif

#define BIT(x) (1 << x)
