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
Display = pygame.display.set_mode((1000, 500), pygame.RESIZABLE)
pygame.display.set_caption("Hexa Engine")
pygame.display.set_icon(Logo)

print("Hexa game engine")

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

			else: pygame.draw.rect(Display, self.Colors, (self.Posx, self.Posy, self.Sizex, self.Sizey))

	class Text:
		def __init__(self, Text, Colors, Font_Pos, Font_size):
			self.Colors = Colors
			self.Font_Pos = Font_Pos
			self.Font_size = Font_size
			self.Text = Text

		def draw(self):
			self.font = pygame.font.SysFont("arial", self.Font_size)
			self.text = self.font.render(self.Text, True, self.Colors)
			Graphics.blit(self.text, self.Font_Pos)

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
# Global variables
Forever = False

# GameObjects
Player = Entity.Quad(530, 320, 50, 50)

# Properties GUI window
Properties = GUI.Label((28, 28, 28), 0, 0, 200, 500)
Properties_Tab = GUI.Label((17, 17, 17), 0, 0, 200, 19)
Properties_Tab_Title = GUI.Text("Properties", (255, 255, 255), (2, 0), 15)

Title = GUI.Text("Change", (255, 255, 255), (50, 250), 15)
Change = GUI.Button((50, 50, 50), (70, 70, 70), (40, 40, 40), 35, 247, 75, 25)
while Loop:
	clock.tick(60)
	Display.fill((44, 44, 44))

	Keys = pygame.key.get_pressed()

	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		if Keys[K_LALT] and Keys[K_F4] or Keys[K_LALT] and Keys[K_SPACE] and Keys[K_c]: sys.exit()
		if event.type == pygame.VIDEORESIZE:
			Graphics = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
			Properties = GUI.Label((28, 28, 28), 0, 0, 200, event.h)

	Player.draw((49, 149, 250))
	Player.move()

	Properties.draw()
	Properties_Tab.draw()
	Properties_Tab_Title.draw()

	IsPressed = Change.draw()
	Title.draw()
	if IsPressed == 1 or Forever == True:
		Forever = True
		Player.draw((250, 56, 49))

	pygame.display.update()
pygame.quit()
