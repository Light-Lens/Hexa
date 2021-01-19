# Hexa programming language
# Modules are imported that will be used in Hexa programming language.
import random
import math
import sys
import os

# This import blocks pygame from printing it's startup text.
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from pygame.locals import *

# Initializing Hexa engine
pygame.init()

Loop = True
Logo = pygame.image.load("Logo.png")
clock = pygame.time.Clock()
Display = pygame.display.set_mode((1000, 575), pygame.RESIZABLE)
pygame.display.set_caption("Hexagon editor")
pygame.display.set_icon(Logo)

os.system('title Hexa engine')
def HEXA_ENGINE_LOG(message):
	print(message)

# All engine featues
class GUI:
	class Label:
		def __init__(self, Colors, Posx, Posy, Sizex, Sizey):
			self.Posx = Posx
			self.Posy = Posy
			self.Sizex = Sizex
			self.Sizey = Sizey
			self.Colors = Colors

		def draw(self):
			pygame.draw.rect(Display, self.Colors, (self.Posx, self.Posy, self.Sizex, self.Sizey))

	class Button:
		def __init__(self, Colors, NewColor, Pressed, Posx, Posy, Sizex, Sizey):
			self.Posx = Posx
			self.Posy = Posy
			self.Sizex = Sizex
			self.Sizey = Sizey
			self.Colors = Colors
			self.NewColor = NewColor
			self.Pressed = Pressed

		def draw(self):
			pygame.draw.rect(Display, self.Colors, (self.Posx, self.Posy, self.Sizex, self.Sizey))
			self.mouseX, self.mouseY = pygame.mouse.get_pos()
			if self.Posx + self.Sizex > self.mouseX > self.Posx and self.Posy + self.Sizey > self.mouseY > self.Posy:
				pygame.draw.rect(Display, self.NewColor, (self.Posx, self.Posy, self.Sizex, self.Sizey))
				if pygame.mouse.get_pressed()[0]:
					pygame.draw.rect(Display, self.Pressed, (self.Posx, self.Posy, self.Sizex, self.Sizey))
					return 1

				else: return 0

			else: pygame.draw.rect(Display, self.Colors, (self.Posx, self.Posy, self.Sizex, self.Sizey))

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
		def __init__(self, Posx, Posy, Sizex, Sizey):
			self.Posx = Posx
			self.Posy = Posy
			self.Sizex = Sizex
			self.Sizey = Sizey

		def draw(self, Colors):
			self.Colors = Colors
			pygame.draw.rect(Display, self.Colors, (self.Posx, self.Posy, self.Sizex, self.Sizey))

		def move(self):
			Keys = pygame.key.get_pressed()
			if Keys[K_RIGHT]:
				self.Posx += 7

			if Keys[K_LEFT]:
				self.Posx -= 7

			if Keys[K_UP]:
				self.Posy -= 7

			if Keys[K_DOWN]:
				self.Posy += 7

# Engine loop.
HEXA_ENGINE_LOG("Hexa engine")

# Global variables
Forever = False
IsPressed = 0

# GameObjects
Player = Entity.Quad(530, 320, 50, 50)

# Menubar GUI window
Menubar = GUI.Label((25, 25, 25), 0, 0, 1000, 21)
Menubar_Text = GUI.Text("File", (255, 255, 255), (3, 3), 12)
Menubar_Button = GUI.Button((25, 25, 25), (50, 50, 50), (40, 40, 40), 0, 0, 25, 15)

# Properties GUI window
Properties = GUI.Label((28, 28, 28), 0, 21, 200, 575)
Properties_Border = GUI.Label((20, 20, 20), 198, 42, 2, 575)

Properties_Tab = GUI.Label((25, 25, 25), 0, 21, 200, 21)
Properties_Tab_Border = GUI.Label((20, 20, 20), 0, 42, 200, 2)
Properties_Tab_Title = GUI.Text("Properties", (255, 255, 255), (2, 22), 15)

# Change GUI button
Change = GUI.Button((50, 50, 50), (70, 70, 70), (40, 40, 40), 35, 247, 75, 25)
Change_Text = GUI.Text("Change", (255, 255, 255), (50, 251), 15)
Change_Border = GUI.Label((20, 20, 20), 35, 272, 75, 2)
while Loop:
	clock.tick(60)
	Display.fill((44, 44, 44))

	Keys = pygame.key.get_pressed()
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		if Keys[K_LALT] and Keys[K_F4] or Keys[K_LALT] and Keys[K_SPACE] and Keys[K_c]: sys.exit()
		if event.type == pygame.VIDEORESIZE:
			Display = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
			Menubar = GUI.Label((25, 25, 25), 0, 0, event.w, 21)

			Properties = GUI.Label((28, 28, 28), 0, 0, 200, event.h)
			Properties_Border = GUI.Label((20, 20, 20), 198, 42, 2, event.h)

	if IsPressed == 1 or Forever == True:
		if IsPressed == 1:
			HEXA_ENGINE_LOG("Changed the color of Object \"Player\" to (250, 56, 49)")

		Forever = True
		Player.draw((250, 56, 49))

	elif IsPressed == 0 or Forever == False:
		Player.draw((49, 149, 250))
	Player.move()

	Properties.draw()
	Properties_Tab.draw()
	Properties_Border.draw()
	Properties_Tab_Title.draw()
	Properties_Tab_Border.draw()

	IsPressed = Change.draw()
	Change_Text.draw()
	Change_Border.draw()

	Menubar.draw()
	IsMenuPressed = Menubar_Button.draw()
	Menubar_Text.draw()
	if IsMenuPressed == 1:
		HEXA_ENGINE_LOG("File option has been chosen")

	pygame.display.update()
pygame.quit()
