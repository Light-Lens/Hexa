# Custom modules.
from Pygame import *
from LOG import *

# Create Renderer Class
class Renderer:
    def __init__(self, Title="Hexa engine", DisplaySize=(500, 500), Logo=None):
        LOG.STATUS("Using Hexa Renderer!")

        # Initialize arguments
        self.Logo = Logo
        self.Title = Title
        self.DisplaySize = DisplaySize

    # Setup Window
    def SetupDisplay(self, resize=False):
        Display = (resize == True) and pygame.display.set_mode(self.DisplaySize, pygame.RESIZABLE) or pygame.display.set_mode(self.DisplaySize)
        pygame.display.set_caption(self.Title)
        if self.Logo != None: pygame.display.set_icon(self.Logo)
        return Display
