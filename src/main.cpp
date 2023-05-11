#include <SDL2/SDL.h>
#include <iostream>

using namespace std;

namespace Hexa
{
    SDL_Renderer *renderer = nullptr;
    namespace Engine
    {
        class Display
        {
        public:
            int SCREEN_WIDTH;
            int SCREEN_HEIGHT;
            string SCREEN_TITLE;

        private:
            SDL_Window *window = nullptr;
            SDL_Event event;

        public:
            Display(string title="Hexa engine", int width=1280, int height=720)
            {
                SCREEN_TITLE = title;
                SCREEN_WIDTH = width;
                SCREEN_HEIGHT = height;

                SDL_Init(SDL_INIT_EVERYTHING);
                window = SDL_CreateWindow(SCREEN_TITLE.c_str(), SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, SCREEN_WIDTH, SCREEN_HEIGHT, 0);
                renderer = SDL_CreateRenderer(window, -1, 0);
            }

            void WindowEvent(bool& isrunning)
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
            void Update(Uint32 DelayTime=10)
            {
                SDL_RenderPresent(renderer);
                SDL_Delay(DelayTime); // Wait for 'x' milliseconds
            }

            // Clear the screen
            void Clear(Uint8 r=255, Uint8 g=255, Uint8 b=255, Uint8 a=1)
            {
                SDL_SetRenderDrawColor(renderer, r, g, b, a);
                SDL_RenderClear(renderer);
            }

            ~Display()
            {
                SDL_DestroyRenderer(renderer);
                SDL_DestroyWindow(window);
                SDL_Quit();
            }
        };

        class Time
        {
        private:
            Uint32 DeltaTimeLastTick;
            Uint32 FPSLastTick;
            int Frames;

        public:
            Time()
            {
                Uint32 DeltaTimeLastTick = SDL_GetTicks();
                Uint32 FPSLastTick = SDL_GetTicks();
            }

            float DeltaTime()
            {
                // Calculate the time elapsed since the last frame
                Uint32 currentTick = SDL_GetTicks();
                float deltaTime = (currentTick - DeltaTimeLastTick) / 1000.0f;
                DeltaTimeLastTick = currentTick;

                return deltaTime;
            }

            int GetFPS()
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
        };

        class Input
        {
        public:
            static Uint8 PlayerInput()
            {
                if (isKeydown(SDL_SCANCODE_UP) || isKeydown(SDL_SCANCODE_W))
                    return 0;

                else if (isKeydown(SDL_SCANCODE_DOWN) || isKeydown(SDL_SCANCODE_S))
                    return 1;

                else if (isKeydown(SDL_SCANCODE_LEFT) || isKeydown(SDL_SCANCODE_A))
                    return 2;

                else if (isKeydown(SDL_SCANCODE_RIGHT) || isKeydown(SDL_SCANCODE_D))
                    return 3;

                else
                    return -1;
            }

            static bool isKeydown(SDL_Scancode scancode)
            {
                const Uint8* state = SDL_GetKeyboardState(NULL);
                return state[scancode];
            }

            static bool isKeyup(SDL_Scancode scancode)
            {
                static bool prevStates[SDL_NUM_SCANCODES] = { false }; // Initial state is released
                const Uint8* state = SDL_GetKeyboardState(NULL);
                bool currState = state[scancode];
                bool prevState = prevStates[scancode];

                prevStates[scancode] = currState;
                return !currState && prevState;
            }

            static bool isKeypressed(SDL_Scancode scancode)
            {
                static bool prevStates[SDL_NUM_SCANCODES] = { false }; // Initial state is released
                const Uint8* state = SDL_GetKeyboardState(NULL);
                bool currState = state[scancode];
                bool prevState = prevStates[scancode];

                prevStates[scancode] = currState;
                return currState && !prevState;
            }
        };
    }

    namespace Entity
    {
        class Square
        {
        private:
            struct DimensionMatrix
            {
                int x, y;
                int w, h;
            };

            struct ColorMatrix
            {
                int r, g, b;
                int a;
            };

        public:
            int x, y;
            int w, h;
            SDL_Color Color;

        public:
            Square(DimensionMatrix dim_matrix, ColorMatrix color_matrix)
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

            void draw()
            {
                SDL_Rect rect = {x, y, w, h};
                SDL_SetRenderDrawColor(renderer, Color.r, Color.g, Color.b, Color.a);
                SDL_RenderFillRect(renderer, &rect);
            }
        };
    }
}

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
        if (key == 0)
            yvel = -1000;

        else if (key == 1)
            yvel = 1000;

        else if (key == 2)
            xvel = -1000;

        else if (key == 3)
            xvel = 1000;

        else
            xvel = 0, yvel = 0;

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
