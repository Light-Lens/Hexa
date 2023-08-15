#pragma once

#include <memory>

#include "Core.h"
#include "spdlog/spdlog.h"
#include "spdlog/fmt/ostr.h"

namespace Hexa
{
    class Hexa_API Log
    {
    public:
        static void Init();

		inline static std::shared_ptr<spdlog::logger>& GetCoreLogger() { return s_CoreLogger; }
		inline static std::shared_ptr<spdlog::logger>& GetClientLogger() { return s_ClientLogger; }

	private:
		static std::shared_ptr<spdlog::logger> s_CoreLogger;
		static std::shared_ptr<spdlog::logger> s_ClientLogger;
    };
}

// Core log macros
#define HX_CORE_TRACE(...)    ::Hexa::Log::GetCoreLogger()->trace(__VA_ARGS__)
#define HX_CORE_INFO(...)     ::Hexa::Log::GetCoreLogger()->info(__VA_ARGS__)
#define HX_CORE_WARN(...)     ::Hexa::Log::GetCoreLogger()->warn(__VA_ARGS__)
#define HX_CORE_ERROR(...)    ::Hexa::Log::GetCoreLogger()->error(__VA_ARGS__)
#define HX_CORE_FATAL(...)    ::Hexa::Log::GetCoreLogger()->fatal(__VA_ARGS__)

// Client log macros
#define HX_TRACE(...)	      ::Hexa::Log::GetClientLogger()->trace(__VA_ARGS__)
#define HX_INFO(...)	      ::Hexa::Log::GetClientLogger()->info(__VA_ARGS__)
#define HX_WARN(...)	      ::Hexa::Log::GetClientLogger()->warn(__VA_ARGS__)
#define HX_ERROR(...)	      ::Hexa::Log::GetClientLogger()->error(__VA_ARGS__)
#define HX_FATAL(...)	      ::Hexa::Log::GetClientLogger()->fatal(__VA_ARGS__)
