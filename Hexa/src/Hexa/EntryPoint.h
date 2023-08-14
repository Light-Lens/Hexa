#pragma once

#ifdef HX_PLATFORM_WINDOWS

extern Hexa::Application* Hexa::CreateApplication();

int main(int argc, char** argv)
{
	std::cout << "Hello world!\n";
	auto app = Hexa::CreateApplication();
	app->Run();
	delete app;
}

#endif
