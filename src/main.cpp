#include "Hexa.hpp"

using namespace std;

int main(int argv, char** args)
{
    Hexa::Engine::Display screen = Hexa::Engine::Display();
    Hexa::Engine::Time time = Hexa::Engine::Time();

    Hexa::Entity::Square square = Hexa::Entity::Square({1280/2 - 25, 720/2 - 25, 50, 50}, {43, 153, 255, 1});
    int xvel = 0, yvel = 0;

    bool isRunning = true;
    SDL_Event event;

    while (isRunning)
    {
        float deltaTime = time.DeltaTime();
        screen.WindowEvent(isRunning);

        Uint8 key = Hexa::Engine::Input::PlayerInput();

        const Uint8* state = SDL_GetKeyboardState(NULL);
        if (state[SDL_SCANCODE_UP])
            yvel = -1000;

        else if (state[SDL_SCANCODE_DOWN])
            yvel = 1000;

        else
            yvel = 0;

        if (state[SDL_SCANCODE_LEFT])
            xvel = -1000;

        else if (state[SDL_SCANCODE_RIGHT])
            xvel = 1000;

        else
            xvel = 0;

        // Update the square's position based on its velocity
        square.x += xvel * deltaTime;
        square.y += yvel * deltaTime;

        // Clamp the square's position to the screen bounds
        square.x = max(min(square.x, 1280 - 50), 0);
        square.y = max(min(square.y, 720 - 50), 0);

        // Clear the screen
        screen.Clear();

        // Draw the square
        square.draw();

        // Update the screen
        screen.Update();
    }

    return 0;
}
