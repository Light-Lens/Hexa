#include <SDL2/SDL.h>
#include <iostream>

using namespace std;

int main(int argv, char** args)
{
    SDL_Init(SDL_INIT_EVERYTHING);

    SDL_Window *window = SDL_CreateWindow("Hexa engine", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, 1280, 720, 0);
    SDL_Renderer *renderer = SDL_CreateRenderer(window, -1, 0);

    SDL_Rect square = { 1280/2 - 25, 720/2 - 25, 50, 50 };
    int xvel = 0, yvel = 0;

    bool isRunning = true;
    SDL_Event event;

    Uint32 lastTick = SDL_GetTicks();
    while (isRunning)
    {
        // Calculate the time elapsed since the last frame
        Uint32 currentTick = SDL_GetTicks();
        float deltaTime = (currentTick - lastTick) / 1000.0f;
        lastTick = currentTick;

        while (SDL_PollEvent(&event))
        {
            switch (event.type)
            {
                case SDL_QUIT:
                    isRunning = false;
                    break;

                case SDL_KEYDOWN:
                    switch (event.key.keysym.sym)
                    {
                        case SDLK_UP:
                            yvel = -1000;
                            break;

                        case SDLK_DOWN:
                            yvel = 1000;
                            break;

                        case SDLK_LEFT:
                            xvel = -1000;
                            break;

                        case SDLK_RIGHT:
                            xvel = 1000;
                            break;
                    }
                    break;

                case SDL_KEYUP:
                    switch (event.key.keysym.sym)
                    {
                        case SDLK_UP:
                        case SDLK_DOWN:
                            yvel = 0;
                            break;

                        case SDLK_LEFT:
                        case SDLK_RIGHT:
                            xvel = 0;
                            break;
                    }
                    break;
            }
        }


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

    // Cleanup
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();

    return 0;
}
