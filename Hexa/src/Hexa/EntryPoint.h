#pragma once

extern Hexa::Application* Hexa::CreateApplication();

int main(int argc, char const *argv[])
{
    std::cout << "test\n";
    std::cout << "Hexa Engine\n";
    auto app = Hexa::CreateApplication();
    app->Run();
    delete app;
    return 0;
}
