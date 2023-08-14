#include <Hexa.h>

class Sandbox : public Hexa::Application
{
public:
    Sandbox()
    {
    }

    ~Sandbox()
    {
    }
};

int main(int argc, char const *argv[])
{
    Sandbox* sandbox = new Sandbox();
    sandbox->Run();
    delete sandbox;
    return 0;
}
