#pragma once

#ifdef HX_PLATFORM_WINDOWS

extern Hexa::Application* Hexa::CreateApplication();

int main(int argc, char** argv)
{
	Hexa::Log::Init();
	HX_CORE_WARN("Initialized Log!");
	int a = 5;
	HX_INFO("Hello! Var={0}", a);

	auto app = Hexa::CreateApplication();
	app->Run();
	delete app;
}

#endif
