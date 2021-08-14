# Custom modules.
from Pygame import *
from LOG import *

# Create Entity Class
class Entity:
    class Quad:
        def __init__(self, Display, Colors, Pos, Size):
            LOG.INFO(f"Game Object is Initialized [Color: {Colors}, Size: {Size}, Position: {Pos}]")

            # Initialize arguments
            self.Display = Display
            self.Colors = Colors
            self.Size = Size
            self.Pos = Pos

        def Draw(self):
            pygame.draw.rect(self.Display, self.Colors, (self.Pos, self.Size))

        def Transform(self, DeltaTime, TransformType="Position"):
            if TransformType == "Position":
                Keys = pygame.key.get_pressed()
                if Keys[K_UP]: self.Pos[1] -= 500 * DeltaTime
                if Keys[K_DOWN]: self.Pos[1] += 500 * DeltaTime
                if Keys[K_LEFT]: self.Pos[0] -= 500 * DeltaTime
                if Keys[K_RIGHT]: self.Pos[0] += 500 * DeltaTime
