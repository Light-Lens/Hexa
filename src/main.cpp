#include <SDL2/SDL.h>
#include <iostream>

using namespace std;

class Window
{
public:
    int SCREEN_WIDTH = 1280;
    int SCREEN_HEIGHT = 720;
    string SCREEN_TITLE = "Hexa engine";

    SDL_Window *window;
    SDL_Renderer *renderer;

private:
    SDL_Event event;
    Uint32 lastTick = SDL_GetTicks();

public:
    Window()
    {
        SDL_Init(SDL_INIT_EVERYTHING);
        window = SDL_CreateWindow(SCREEN_TITLE.c_str(), SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, SCREEN_WIDTH, SCREEN_HEIGHT, 0);
        renderer = SDL_CreateRenderer(window, -1, 0);
    }

    float DeltaTime()
    {
        // Calculate the time elapsed since the last frame
        Uint32 currentTick = SDL_GetTicks();
        float deltaTime = (currentTick - lastTick) / 1000.0f;
        lastTick = currentTick;

        return deltaTime;
    }

    void Event(bool& isrunning)
    {
        while (SDL_PollEvent(&event))
        {
            switch (event.type)
            {
                case SDL_QUIT:
                    isrunning = false;
                    break;
            }
        }
    }

    ~Window()
    {
        SDL_DestroyRenderer(renderer);
        SDL_DestroyWindow(window);
        SDL_Quit();
    }
};

int main(int argv, char** args)
{
    Window screen = Window();
    auto renderer = screen.renderer;
    auto window = screen.window;

    SDL_Rect square = { 1280/2 - 25, 720/2 - 25, 50, 50 };
    int xvel = 0, yvel = 0;

    bool isRunning = true;
    SDL_Event event;

    while (isRunning)
    {
        float deltaTime = screen.DeltaTime();
        screen.Event(isRunning);

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
        SDL_SetRenderDrawColor(renderer, 255, 255, 255, 1);
        SDL_RenderClear(renderer);

        // Draw the square
        SDL_SetRenderDrawColor(renderer, 43, 153, 255, 1);
        SDL_RenderFillRect(renderer, &square);

        // Update the screen
        SDL_RenderPresent(renderer);
        SDL_Delay(10); // Wait for 10 milliseconds
    }

    return 0;
}
