# Hexa
# Block pygame from printing on startup.
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

# Important modules.
from colorama import Fore, Style, init
from pygame.locals import *
import datetime
import pygame
import time
import sys
import os

# Initialize colorama and pygame.
init(autoreset = True)
pygame.init()

# Global variables
PrevFrameTime = 0
DeltaTime = 0
Clock = pygame.time.Clock()

# Create Log class.
class LOG:
    def __init__(self, SaveFile=True, ShowText=True):
        self.SaveFile = SaveFile
        self.ShowText = ShowText

    def INFO(self, message):
        CurrentTime = self.GetCurrentTime()
        if self.ShowText: print(f"{CurrentTime} - INFO: {message}")
        self.DebugLog(CurrentTime, "INFO", message)

    def STATUS(self, message):
        CurrentTime = self.GetCurrentTime()
        if self.ShowText: print(f"{Fore.BLUE}{Style.BRIGHT}{CurrentTime} - STATUS: {message}")
        self.DebugLog(CurrentTime, "STATUS", message)

    def ERROR(self, message):
        CurrentTime = self.GetCurrentTime()
        if self.ShowText: print(f"{Fore.RED}{Style.BRIGHT}{CurrentTime} - ERROR: {message}")
        self.DebugLog(CurrentTime, "ERROR", message)

    def WARN(self, message):
        CurrentTime = self.GetCurrentTime()
        if self.ShowText: print(f"{Fore.YELLOW}{Style.BRIGHT}{CurrentTime} - WARNING: {message}")
        self.DebugLog(CurrentTime, "WARNING", message)

    def GetCurrentTime(self):
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def DebugLog(self, CurrentTime, Logname, message):
        if os.path.isfile("Debug.log") == False:
            with open("Debug.log", "w") as File: File.write("_______ LOG _______\n")

        if self.SaveFile:
            with open("Debug.log", "a") as File: File.write(f"{CurrentTime} - {Logname}: {message}\n")

# Create GUI class.
class GUI:
    class Label:
        def __init__(self, Display, Colors, Pos, Size):
            self.Pos = Pos
            self.Size = Size
            self.Colors = Colors
            self.Display = Display

        def draw(self):
            pygame.draw.rect(self.Display, self.Colors, (self.Pos[0], self.Pos[1], self.Size[0], self.Size[1]))

        def update(self, Colors, Pos, Size):
            self.Pos = Pos
            self.Size = Size
            self.Colors = Colors

        def kill(self):
            self.Pos = (-1, -1)
            self.Size = (0, 0)
            self.Colors = (0, 0, 0)

    class Text:
        def __init__(self, Display, Text, Colors, FontPos, FontSize):
            self.Text = Text
            self.Colors = Colors
            self.FontPos = FontPos
            self.FontSize = FontSize
            self.Display = Display

        def draw(self):
            self.font = pygame.font.SysFont("calibri", self.FontSize)
            self.text = self.font.render(self.Text, True, self.Colors)
            self.Display.blit(self.text, self.FontPos)

        def update(self, Text, Colors, FontPos, FontSize):
            self.Text = Text
            self.Colors = Colors
            self.FontPos = FontPos
            self.FontSize = FontSize

        def kill(self):
            self.Text = ""
            self.Colors = (0, 0, 0)
            self.FontPos = (-1, -1)
            self.FontSize = (0, 0)

    class Button:
        def __init__(self, Display, Colors, Pos, Size):
            self.Pos = Pos
            self.Size = Size
            self.Colors = Colors
            self.Display = Display

        def draw(self):
            pygame.draw.rect(self.Display, self.Colors, (self.Pos[0], self.Pos[1], self.Size[0], self.Size[1]))

        def IsHover(self):
            Hitbox = pygame.Rect(self.Pos[0], self.Pos[1], self.Size[0], self.Size[1])
            MousePos = pygame.mouse.get_pos()
            IsHover = Hitbox.collidepoint(MousePos)
            return IsHover

        def IsClicked(self):
            Hitbox = pygame.Rect(self.Pos[0], self.Pos[1], self.Size[0], self.Size[1])
            MousePos = pygame.mouse.get_pos()
            IsHover = Hitbox.collidepoint(MousePos)
            IsClicked = False
            if IsHover:
                if pygame.mouse.get_pressed()[0] == 1 and IsClicked == False: IsClicked = True
                if pygame.mouse.get_pressed()[0] == 0: IsClicked = False

            return IsClicked

        def update(self, Colors, Pos, Size):
            self.Pos = Pos
            self.Size = Size
            self.Colors = Colors

        def kill(self):
            self.Pos = (-1, -1)
            self.Size = (0, 0)
            self.Colors = (0, 0, 0)

# Create Entity class.
class Entity:
    class Quad:
        def __init__(self, Display, Colors, Pos, Size):
            self.Pos = Pos
            self.Size = Size
            self.Colors = Colors
            self.Display = Display
            LOG().INFO(f"Created a Quad at {self.Pos}")

        def draw(self):
            return pygame.draw.rect(self.Display, self.Colors, (self.Pos[0], self.Pos[1], self.Size[0], self.Size[1]))

        def update(self, Colors, Pos, Size):
            self.Pos = Pos
            self.Size = Size
            self.Colors = Colors

        def kill(self):
            self.Pos = (-1, -1)
            self.Size = (0, 0)
            self.Colors = (0, 0, 0)
            LOG().INFO(f"Destroyed Quad")

    class Circle:
        def __init__(self, Display, Colors, Pos, Radius):
            self.Pos = Pos
            self.Colors = Colors
            self.Radius = Radius
            self.Display = Display
            LOG().INFO(f"Created a Circle at {self.Pos}")

        def draw(self):
            return pygame.draw.circle(self.Display, self.Colors, self.Pos, self.Radius)

        def update(self, Colors, Pos, Radius):
            self.Pos = Pos
            self.Colors = Colors
            self.Radius = Radius

        def kill(self):
            self.Pos = (-1, -1)
            self.Colors = (0, 0, 0)
            self.Radius = 0
            LOG().INFO(f"Destroyed Circle")

    class Polygons:
        def __init__(self, Display, Colors, X, Y):
            self.X = X
            self.Y = Y
            self.Colors = Colors
            self.Display = Display
            LOG().INFO(f"Created a Polygon at {self.X} and {self.Y}")

        def draw(self):
            return pygame.draw.polygon(self.Display, self.Colors, [[self.X[0], self.Y[0]], [self.X[1], self.Y[1]], [self.X[2], self.Y[2]]])

        def update(self, Colors, X, Y):
            if Colors != self.Colors or X != self.X or Y != self.Y:
                LOG().INFO(f"Updated the Polygon at {self.X} and {self.Y}")

            self.X = X
            self.Y = Y
            self.Colors = Colors

        def kill(self):
            self.X = (-1, -1, -1)
            self.Y = (-1, -1, -1)
            self.Colors = (0, 0, 0)
            LOG().INFO(f"Destroyed Triangle")

    class Texture:
        def __init__(self, Display, Texture, Pos, Size):
            self.Pos = Pos
            self.Size = Size
            self.Texture = Texture
            self.Display = Display
            LOG().INFO(f"Created a {(Texture)} at {self.Pos}")

        def draw(self):
            Texture = pygame.image.load(self.Texture).convert_alpha()
            LoadTexture = pygame.transform.scale(Texture, (self.Size[0], self.Size[1]))
            return self.Display.blit(LoadTexture, (self.Pos[0], self.Pos[1]))

        def update(self, Texture, Pos, Size):
            self.Pos = Pos
            self.Size = Size
            self.Texture = Texture

        def kill(self):
            self.Pos = (-1, -1)
            self.Size = (0, 0)
            LOG().INFO(f"Destroyed Texture")

# Create Entity class.
class Physics:
    def Gravity(YPos):
        if YPos >= 9: YPos = 9
        else: YPos += 1
        return YPos

    def AddForce(ObjectCordinates, Force): return ObjectCordinates + Force
    def IsColliding(Object1, Object2):
        if Object1.colliderect(Object2): return True
        else: return False

# Create Engine class.
class Engine:
    class Display:
        def Create(Title="Hexagon editor", Size=(500, 500), Logo="Logo.png"):
            global PrevFrameTime
            global DeltaTime
            LOG().WARN("Initialized Hexa engine.")
            Display = pygame.display.set_mode(Size)
            PrevFrameTime = time.time()
            DeltaTime = 1

            pygame.display.set_caption(Title)
            if Logo:
                GetLogo = pygame.image.load(Logo)
                pygame.display.set_icon(GetLogo)

            return Display

        def Events():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    LOG().WARN("Exiting Hexa engine")
                    sys.exit()

        def Update(): pygame.display.update()
        def Canvas(Display, Color=(0, 0, 0), Image=""):
            Display.fill(Color)
            if Image:
                Texture = pygame.image.load(Image).convert_alpha()
                LoadTexture = pygame.transform.scale(Texture, pygame.display.get_window_size())
                Display.blit(LoadTexture, (0, 0))

    class Input:
        def GetKey(KeyCode: str):
            KeyPressed = pygame.key.key_code(KeyCode)
            return pygame.key.get_pressed()[KeyPressed]

        def MouseKey(KeyCode: int): return pygame.mouse.get_pressed()[KeyCode]

    class Time:
        # Setup Delta time.
        def DeltaTime():
            global PrevFrameTime
            global DeltaTime

            CurrentFrameTime = time.time()
            DeltaTime = (CurrentFrameTime - PrevFrameTime)
            PrevFrameTime = CurrentFrameTime

            return DeltaTime

        # Engine clock.
        def GetFPS(MaxFPS=72):
            Clock.tick(MaxFPS)
            return str(int(Clock.get_fps())) # Get the current FPS as a string.
