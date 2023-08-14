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

Hexa::Application* Hexa::CreateApplication()
{
	return new Sandbox();
}
