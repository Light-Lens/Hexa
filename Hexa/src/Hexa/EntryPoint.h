#pragma once

extern Hexa::Application* Hexa::CreateApplication();

int main(int argc, char const *argv[])
{
    Hexa::Log::Init();
    HX_CORE_WARN("Initialized Log!");
    HX_INFO("Hello!");

    auto app = Hexa::CreateApplication();
    app->Run();
    delete app;
    return 0;
}
