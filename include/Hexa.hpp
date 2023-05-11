#pragma once

#include <SDL2/SDL.h>
#include <iostream>

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
            std::string SCREEN_TITLE;

        private:
            SDL_Window *window = nullptr;
            SDL_Event event;

        public:
            Display(std::string title="Hexa engine", int width=1280, int height=720);

            void WindowEvent(bool& isrunning);
            void Update(Uint32 DelayTime=10);
            void Clear(Uint8 r=255, Uint8 g=255, Uint8 b=255, Uint8 a=1);

            ~Display();
        };

        class Time
        {
        private:
            Uint32 DeltaTimeLastTick;
            Uint32 FPSLastTick;
            int Frames;

        public:
            Time();

            float DeltaTime();
            int GetFPS();
        };

        class Input
        {
        public:
            static Uint8 PlayerInput();
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
            Square(DimensionMatrix dim_matrix, ColorMatrix color_matrix);
            void draw();
        };
    }
}
