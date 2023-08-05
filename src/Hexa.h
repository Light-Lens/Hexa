#pragma once
#include <iostream>

namespace Hexa
{
    namespace Engine
    {
        class Display
        {
        private:
            SDL_Window *window = nullptr;
            SDL_Event event;

        public:
            int SCREEN_WIDTH;
            int SCREEN_HEIGHT;
            std::string SCREEN_TITLE;

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
            static bool isKeydown(SDL_Scancode scancode);
            static bool isKeyup(SDL_Scancode scancode);
            static bool isKeypressed(SDL_Scancode scancode);
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

        class Circle
        {
        private:
            struct DimensionMatrix
            {
                int x, y;
                int radius;
            };

            struct ColorMatrix
            {
                int r, g, b;
                int a;
            };

        public:
            int x, y;
            int radius;
            SDL_Color Color;

        public:
            Circle(DimensionMatrix dim_matrix, ColorMatrix color_matrix);
            void draw();
        };
    }
}
