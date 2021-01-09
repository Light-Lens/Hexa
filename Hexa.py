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
clock = pygame.time.Clock()
Display = pygame.display.set_mode((1000, 500), pygame.RESIZABLE)
pygame.display.set_caption("Hexa Engine")

# All engine featues
class Entity:
	class Quad:
		def __init__(self, Colors, Posx, Posy, Sizex, Sizey):
			self.Posx = Posx
			self.Posy = Posy
			self.Sizex = Sizex
			self.Sizey = Sizey
			self.Colors = Colors

		def draw(self):
			pygame.draw.rect(Graphics, self.Colors, (self.Posx, self.Posy, self.Sizex, self.Sizey))

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
Player = Entity.Quad((49, 149, 250), 530, 320, 50, 50)
while Loop:
	clock.tick(60)
	Display.fill((44, 44, 44))

	Keys = pygame.key.get_pressed()

	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		if Keys[K_LALT] and Keys[K_F4] or Keys[K_LALT] and Keys[K_SPACE] and Keys[K_c]: sys.exit()
		if event.type == pygame.VIDEORESIZE: Graphics = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

	Player.draw()
	Player.move()

	pygame.display.update()
pygame.quit()
