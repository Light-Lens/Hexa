# Import all modules
import platform
import time
import sys
import os

# Custom modules.
from Renderer import *
from Entity import *
from Pygame import *
from LOG import *

# Initialize Hexa engine
os.system('title Hexa engine')
init(autoreset = True)
pygame.init()

clock = pygame.time.Clock()
SystemDetails = platform.uname()
Logo = pygame.image.load("./Logo.png")

# Get, Display and Log the information of the current system.
def UserSystemInfo(GetSystemInfo=[]):
    for message in GetSystemInfo:
        LOG.INFO(Fore.GREEN + Style.BRIGHT + message, save_log=False)

        CurrentTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        open("Debug.log", "a", encoding = "utf-8").write(f"{CurrentTime} - INFO: {message}\n")

# Setting up Terminal
LOG.WARN("Initialized Hexa engine!")
Display = Renderer("Hexagon editor", (1000, 575), Logo).SetupDisplay(resize=True)

UserSystemInfo([
f"Host [{SystemDetails.node}]",
f"System [{SystemDetails.system} {SystemDetails.release} (OS Build {SystemDetails.version})]",
f"Machine [{SystemDetails.machine}]",
f"Processor [{SystemDetails.processor}]"
])

# Engine loop.
DeltaTime = 0
PrevFrameTime = time.time()

Player = Entity.Quad(Display, (61, 145, 255), [100, 100], (50, 50))
while 1:
    # Engine clock.
    clock.tick(72)
    FPS = str(int(clock.get_fps())) # Get the current FPS as a string.

    # Setup Delta time.
    CurrentFrameTime = time.time()
    DeltaTime = (CurrentFrameTime - PrevFrameTime)
    PrevFrameTime = CurrentFrameTime

    # Setup the canvas.
    Display.fill((44, 44, 44))

    # Window event.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # If the Cross button is pressed then Exit the engine.
            LOG.WARN("Exiting Hexa engine!")
            LOG.STATUS("Stoping all the processes.")
            pygame.quit()
            sys.exit()

        elif event.type == pygame.VIDEORESIZE:
            Display = Renderer("Hexagon editor", event.dict['size'], Logo).SetupDisplay(resize=True)
            LOG.INFO(f"Window resized to {event.dict['size']}")

    # Render Player.
    Player.Draw()
    Player.Transform(DeltaTime)
    pygame.display.update()
pygame.quit()
sys.exit()
