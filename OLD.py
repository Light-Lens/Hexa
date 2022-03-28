# Oxygen
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

# Initialize Colorama.
init(autoreset = True)
pygame.init()

# Global variables
PrevFrameTime = time.time()
DeltaTime = 1
Clock = pygame.time.Clock()
Logo = pygame.image.load("Logo.png")

# Setting up window
Display = pygame.display.set_mode((1000, 575))
pygame.display.set_caption("Hexagon editor")
pygame.display.set_icon(Logo)

# Create Log Functions.
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
            with open("Debug.log", "w") as File: File.write("_______ Hexa LOG _______\n")

        if self.SaveFile:
            with open("Debug.log", "a") as File: File.write(f"{CurrentTime} - {Logname}: {message}\n")

# Add GUI elements to the game engine.
class GUI:
    class Label:
        def __init__(self, Colors, Pos, Size):
            self.Pos = Pos
            self.Size = Size
            self.Colors = Colors

        def draw(self):
            pygame.draw.rect(Display, self.Colors, (self.Pos[0], self.Pos[1], self.Size[0], self.Size[1]))

    class Text:
        def __init__(self, Text, Colors, Font_Pos, Font_size):
            self.Colors = Colors
            self.Font_Pos = Font_Pos
            self.Font_size = Font_size
            self.Text = Text

        def draw(self):
            self.font = pygame.font.SysFont("calibri", self.Font_size)
            self.text = self.font.render(self.Text, True, self.Colors)
            Display.blit(self.text, self.Font_Pos)

class Entity:
    class Quad:
        def __init__(self, Colors, Pos, Size):
            self.Pos = Pos
            self.Size = Size
            self.Colors = Colors

        def draw(self):
            pygame.draw.rect(Display, self.Colors, (self.Pos[0], self.Pos[1], self.Size[0], self.Size[1]))

        def move(self):
            Keys = pygame.key.get_pressed()
            if Keys[K_RIGHT]: self.Pos[0] += 700 * DeltaTime
            if Keys[K_LEFT]: self.Pos[0] -= 700 * DeltaTime
            if Keys[K_UP]: self.Pos[1] -= 700 * DeltaTime
            if Keys[K_DOWN]: self.Pos[1] += 700 * DeltaTime

        def gravity(self):
            self.Pos[1] += 500 * DeltaTime
            return self.Pos[1] # Uncomment only if you want to return the position

    class Circle:
        def __init__(self, Colors, Pos, Radius):
            self.Pos = Pos
            self.Colors = Colors
            self.Radius = Radius

        def draw(self):
            pygame.draw.circle(Display, self.Colors, self.Pos, self.Radius)

        def move(self):
            Keys = pygame.key.get_pressed()
            if Keys[K_RIGHT]: self.Pos[0] += 700 * DeltaTime
            if Keys[K_LEFT]: self.Pos[0] -= 700 * DeltaTime
            if Keys[K_UP]: self.Pos[1] -= 700 * DeltaTime
            if Keys[K_DOWN]: self.Pos[1] += 700 * DeltaTime

        def gravity(self):
            self.Pos[1] += 500 * DeltaTime
            return self.Pos[1] # Uncomment only if you want to return the position

    class Texture:
        def __init__(self, Texture, Pos, Size):
            self.Pos = Pos
            self.Size = Size
            self.Texture = Texture

        def draw(self):
            self.texture = pygame.image.load(self.Texture).convert_alpha()
            Load_Texture = pygame.transform.scale(self.texture, (self.Size[0], self.Size[1]))
            Display.blit(Load_Texture, (self.Pos[0], self.Pos[1]))

        def move(self):
            Keys = pygame.key.get_pressed()
            if Keys[K_RIGHT]: self.Pos[0] += 700 * DeltaTime
            if Keys[K_LEFT]: self.Pos[0] -= 700 * DeltaTime
            if Keys[K_UP]: self.Pos[1] -= 700 * DeltaTime
            if Keys[K_DOWN]: self.Pos[1] += 700 * DeltaTime

        def gravity(self):
            self.Pos[1] += 500 * DeltaTime
            return self.Pos[1] # Uncomment only if you want to return the position

if __name__ == "__main__":
    # Setup Terminal
    os.system('title Hexa engine')
    LOG().WARN("Initialized Hexa engine.")

    HexaTextX, HexaTextY = (0, 5)
    HexaTextGoBack = False

    BallJumpX, BallJumpY = (500, 0)
    BallJump = False

    # Using a list insted of tuple because tuples cannot be modified.
    Player = Entity.Quad((49, 149, 250), [450, 250], (50, 50))
    while True:
        # Engine clock.
        Clock.tick(72)
        FPS = str(int(Clock.get_fps())) # Get the current FPS as a string.
        LOG(ShowText=False).INFO(f"FPS: {FPS}")

        # Setup Delta time.
        CurrentFrameTime = time.time()
        DeltaTime = (CurrentFrameTime - PrevFrameTime)
        PrevFrameTime = CurrentFrameTime

        # Setup the canvas.
        Display.fill((44, 44, 44))
        Entity.Texture("Logo.png", (500, 250), (100, 100)).draw()
        Circle = Entity.Circle((0, 255, 115), [BallJumpX, BallJumpY], 15)
        Player.draw()
        Player.move()
        Circle.draw()

        if BallJumpY >= 500: BallJump = True
        elif BallJumpY <= 400: BallJump = False

        if BallJump: BallJumpY -= 500 * DeltaTime
        else: BallJumpY = Circle.gravity()

        # TopBar and FPS counter.
        GUI.Label((25, 25, 25), (0, 0), (1000, 21)).draw()
        GUI.Text("Hexa game engine", (255, 255, 255), (HexaTextX, HexaTextY), 12).draw()
        GUI.Text(FPS, (255, 255, 255), (10, 30), 18).draw()

        if HexaTextX >= 904: HexaTextGoBack = False
        elif HexaTextX <= 0: HexaTextGoBack = True

        if HexaTextX >= 904: HexaTextGoBack = False
        elif HexaTextX <= 0: HexaTextGoBack = True

        if HexaTextGoBack: HexaTextX += 200 * DeltaTime
        else: HexaTextX -= 200 * DeltaTime

        # Setup Event listener.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                LOG().WARN("Exiting Hexa engine.")
                sys.exit()

        pygame.display.update()
    pygame.quit()
    sys.exit()
