#include <SDL2/SDL.h>
#include <iostream>

using namespace std;

int main(int argv, char** args)
{
    SDL_Init(SDL_INIT_EVERYTHING);

    SDL_Window *window = SDL_CreateWindow("Hexa engine", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, 1280, 720, 0);
    SDL_Renderer *renderer = SDL_CreateRenderer(window, -1, 0);

    bool isRunning = true;
    SDL_Event event;

    int x = 50, y = 50;
    int xvel = 0, yvel = 0;

    while (isRunning)
    {
        while (SDL_PollEvent(&event))
        {
            switch (event.type)
            {
                case SDL_QUIT:
                    isRunning = false;
                    break;

                case SDL_KEYDOWN:
                    if (event.key.keysym.sym == SDLK_ESCAPE)
                        isRunning = false;

                    if (event.key.keysym.sym == SDLK_LEFT)
                        xvel--;

                    if (event.key.keysym.sym == SDLK_RIGHT)
                        xvel++;

                    if (event.key.keysym.sym == SDLK_UP)
                        yvel--;

                    if (event.key.keysym.sym == SDLK_DOWN)
                        yvel++;

                    break;

                case SDL_KEYUP:
                    if (event.key.keysym.sym == SDLK_LEFT)
                    {
                        if (xvel < 0)
                            xvel = 0;
                    }

                    if (event.key.keysym.sym == SDLK_RIGHT)
                    {
                        if (xvel > 0)
                            xvel = 0;
                    }

                    if (event.key.keysym.sym == SDLK_UP)
                    {
                        if (yvel < 0)
                            yvel = 0;
                    }

                    if (event.key.keysym.sym == SDLK_DOWN)
                    {
                        if (yvel > 0)
                            yvel = 0;
                    }

                    break;
            }
        }

        x += xvel;
        y += yvel;

        SDL_SetRenderDrawColor(renderer, 0, 0, 0, 255);
        SDL_RenderClear(renderer);

        SDL_Rect rect = { x, y, 50, 50 };
        SDL_SetRenderDrawColor(renderer, 255, 255, 255, 255);
        SDL_RenderFillRect(renderer, &rect);

        SDL_RenderPresent(renderer);
    }

    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();

    return 0;
}
