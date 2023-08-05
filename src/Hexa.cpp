#include <SDL2/SDL.h>
#include <iostream>
#include <cmath>

#include "Hexa.h"

using namespace std;

namespace Hexa
{
    SDL_Renderer *renderer = nullptr;
    namespace Engine
    {
        Display::Display(string title = "Hexa engine", int width = 1280, int height = 720)
        {
            SCREEN_TITLE = title;
            SCREEN_WIDTH = width;
            SCREEN_HEIGHT = height;

            SDL_Init(SDL_INIT_EVERYTHING);
            window = SDL_CreateWindow(SCREEN_TITLE.c_str(), SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, SCREEN_WIDTH, SCREEN_HEIGHT, 0);
            if (window == NULL)
                cout << "Could not create window: " << SDL_GetError() << endl;

            renderer = SDL_CreateRenderer(window, -1, 0);
        }

        void Display::WindowEvent(bool &isrunning)
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

        // Update the screen
        void Display::Update(Uint32 DelayTime = 10)
        {
            SDL_RenderPresent(renderer);
            SDL_Delay(DelayTime); // Wait for 'x' milliseconds
        }

        // Clear the screen
        void Display::Clear(Uint8 r = 255, Uint8 g = 255, Uint8 b = 255, Uint8 a = 1)
        {
            SDL_SetRenderDrawColor(renderer, r, g, b, a);
            SDL_RenderClear(renderer);
        }

        Display::~Display()
        {
            SDL_DestroyRenderer(renderer);
            SDL_DestroyWindow(window);
            SDL_Quit();
        }

        Time::Time()
        {
            Uint32 DeltaTimeLastTick = SDL_GetTicks();
            Uint32 FPSLastTick = SDL_GetTicks();
        }

        float Time::DeltaTime()
        {
            // Calculate the time elapsed since the last frame
            Uint32 currentTick = SDL_GetTicks();
            float deltaTime = (currentTick - DeltaTimeLastTick) / 1000.0f;
            DeltaTimeLastTick = currentTick;

            return deltaTime;
        }

        int Time::GetFPS()
        {
            Uint32 currentTick = SDL_GetTicks();
            Uint32 elapsedTimeMs = currentTick - FPSLastTick;
            int FPS = 0;

            Frames++;
            if (elapsedTimeMs >= 10)
            {
                FPS = static_cast<int>(Frames) / (elapsedTimeMs / 1000.0f);

                Frames = 0;
                FPSLastTick = currentTick;
            }

            return FPS;
        }

        Uint8 Input::PlayerInput()
        {
            if (isKeydown(SDL_SCANCODE_UP) || isKeydown(SDL_SCANCODE_W))
                return 0;

            if (isKeydown(SDL_SCANCODE_DOWN) || isKeydown(SDL_SCANCODE_S))
                return 1;

            if (isKeydown(SDL_SCANCODE_LEFT) || isKeydown(SDL_SCANCODE_A))
                return 2;

            if (isKeydown(SDL_SCANCODE_RIGHT) || isKeydown(SDL_SCANCODE_D))
                return 3;

            return -1;
        }

        bool Input::isKeydown(SDL_Scancode scancode)
        {
            const Uint8 *state = SDL_GetKeyboardState(NULL);
            return state[scancode];
        }

        bool Input::isKeyup(SDL_Scancode scancode)
        {
            static bool prevStates[SDL_NUM_SCANCODES] = {false}; // Initial state is released
            const Uint8 *state = SDL_GetKeyboardState(NULL);
            bool currState = state[scancode];
            bool prevState = prevStates[scancode];

            prevStates[scancode] = currState;
            return !currState && prevState;
        }

        bool Input::isKeypressed(SDL_Scancode scancode)
        {
            static bool prevStates[SDL_NUM_SCANCODES] = {false}; // Initial state is released
            const Uint8 *state = SDL_GetKeyboardState(NULL);
            bool currState = state[scancode];
            bool prevState = prevStates[scancode];

            prevStates[scancode] = currState;
            return currState && !prevState;
        }
    }

    namespace Entity
    {
        Square::Square(DimensionMatrix dim_matrix, ColorMatrix color_matrix)
        {
            x = dim_matrix.x;
            y = dim_matrix.y;
            w = dim_matrix.w;
            h = dim_matrix.h;

            Color.r = color_matrix.r;
            Color.g = color_matrix.g;
            Color.b = color_matrix.b;
            Color.a = color_matrix.a;
        }

        void Square::draw()
        {
            SDL_Rect rect = {x, y, w, h};
            SDL_SetRenderDrawColor(renderer, Color.r, Color.g, Color.b, Color.a);
            SDL_RenderFillRect(renderer, &rect);
        }

        Circle::Circle(DimensionMatrix dim_matrix, ColorMatrix color_matrix)
        {
            x = dim_matrix.x;
            y = dim_matrix.y;
            radius = dim_matrix.radius;

            Color.r = color_matrix.r;
            Color.g = color_matrix.g;
            Color.b = color_matrix.b;
            Color.a = color_matrix.a;
        }

        void Circle::draw()
        {
            SDL_SetRenderDrawColor(renderer, Color.r, Color.g, Color.b, Color.a);
            for (int yloop = -radius; yloop <= radius; yloop++)
            {
                for (int xloop = -radius; xloop <= radius; xloop++)
                {
                    if (xloop * xloop + yloop * yloop <= radius * radius)
                        SDL_RenderDrawPoint(renderer, x + xloop, y + yloop);
                }
            }
        }
    }
}