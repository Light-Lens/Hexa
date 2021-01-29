# Hexa game engine
# Modules are imported that will be used in Hexa game engine.
from colorama import Fore, Back, Style
from colorama import init
import platform
import random
import time
import math
import sys
import os

# This import blocks pygame from printing it's startup text.
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
from pygame.locals import *

# Initializing Hexa engine
init(autoreset = True)
pygame.init()

# Global variables
Zoom = 0
Loop = True
clock = pygame.time.Clock()
System_details = platform.uname()
Logo = pygame.image.load("Logo.png")

# Setting up window
Display = pygame.display.set_mode((1000, 575), pygame.RESIZABLE)
pygame.display.set_caption("Hexagon editor")
pygame.display.set_icon(Logo)

# Setting up Terminal
os.system('title Hexa engine')
def HEXA_ENGINE_LOG(message):
	print(message)

def HEXA_ENGINE_ERROR_LOG(message):
	print(Fore.RED + message)

def HEXA_ENGINE_LOG_CLEAR():
	os.system('cls')
	HEXA_ENGINE_LOG(Fore.GREEN + "Hexa engine")
	HEXA_ENGINE_LOG(Fore.GREEN + f"Host Name: {System_details.node}")
	HEXA_ENGINE_LOG(Fore.GREEN + f"System: {System_details.system} {System_details.release}")
	HEXA_ENGINE_LOG(Fore.GREEN + f"Processor: {System_details.processor}")

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
					pygame.time.delay(100)
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
			pygame.draw.rect(Display, self.Colors, (self.Posx + Zoom, self.Posy  + Zoom, self.Sizex  + Zoom, self.Sizey  + Zoom))

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

class Components:
	class Physics:
		def __init__(self):
			pass

# Engine loop.
HEXA_ENGINE_LOG(Fore.GREEN + "Hexa engine")
HEXA_ENGINE_LOG(Fore.GREEN + f"Host Name: {System_details.node}")
HEXA_ENGINE_LOG(Fore.GREEN + f"System: {System_details.system} {System_details.release}")
HEXA_ENGINE_LOG(Fore.GREEN + f"Processor: {System_details.processor}")

# Global variables
Forever = {
'Change' : False,
'File' : False,
'Help' : False,
'Help_ABOUT' : False,
}

IsPressed = {
'Change' : 0,
'File' : 0,
'Help' : 0,
'Help_ABOUT' : 0,
'Help_ABOUT_Button' : 0
}

# GameObjects
Player = Entity.Quad(530, 320, 50, 50)

# Menubar GUI window
Menubar = GUI.Label((25, 25, 25), 0, 0, 1000, 21)
Filemenu_Text = GUI.Text("File", (255, 255, 255), (3, 3), 12)
Filemenu_Button = GUI.Button((25, 25, 25), (50, 50, 50), (40, 40, 40), 0, 0, 25, 15)
File_Submenu = GUI.Label((50, 50, 50), 0, 15, 100, 72)
File_Submenu_Button_NEW = GUI.Button((50, 50, 50), (70, 70, 70), (40, 40, 40), 2, 17, 96, 17)
File_Submenu_Text_NEW = GUI.Text("New", (255, 255, 255), (37, 19), 11)
File_Submenu_Button_OPEN = GUI.Button((50, 50, 50), (70, 70, 70), (40, 40, 40), 2, 34, 96, 17)
File_Submenu_Text_OPEN = GUI.Text("Open", (255, 255, 255), (36, 36), 11)
File_Submenu_Button_SAVE = GUI.Button((50, 50, 50), (70, 70, 70), (40, 40, 40), 2, 51, 96, 17)
File_Submenu_Text_SAVE = GUI.Text("Save", (255, 255, 255), (37, 53), 11)
File_Submenu_Button_EXIT = GUI.Button((50, 50, 50), (70, 70, 70), (40, 40, 40), 2, 68, 96, 17)
File_Submenu_Text_EXIT = GUI.Text("Exit", (255, 255, 255), (37, 70), 11)

Editmenu_Text = GUI.Text("Edit", (255, 255, 255), (28, 3), 12)
Editmenu_Button = GUI.Button((25, 25, 25), (50, 50, 50), (40, 40, 40), 25, 0, 25, 15)

Viewmenu_Text = GUI.Text("View", (255, 255, 255), (53, 3), 12)
Viewmenu_Button = GUI.Button((25, 25, 25), (50, 50, 50), (40, 40, 40), 50, 0, 30, 15)

Projectmenu_Text = GUI.Text("Project", (255, 255, 255), (83, 3), 12)
Projectmenu_Button = GUI.Button((25, 25, 25), (50, 50, 50), (40, 40, 40), 80, 0, 40, 15)

Helpmenu_Text = GUI.Text("Help", (255, 255, 255), (123, 3), 12)
Helpmenu_Button = GUI.Button((25, 25, 25), (50, 50, 50), (40, 40, 40), 120, 0, 28, 15)
Help_Submenu = GUI.Label((50, 50, 50), 120, 15, 100, 21)
Help_Submenu_Button_ABOUT = GUI.Button((50, 50, 50), (70, 70, 70), (40, 40, 40), 122, 17, 96, 17)
Help_Submenu_Text_ABOUT = GUI.Text("About Hexa", (255, 255, 255), (141, 19), 11)
Help_ABOUT_Label = GUI.Label((40, 40, 40), 400, 200, 310, 200)
Help_ABOUT_Title = GUI.Text("About Hexa", (255, 255, 255), (512, 210), 17)
Help_ABOUT_Info = GUI.Text("Hexa is Powerful, Open-source 2D Game Engine.", (255, 255, 255), (412, 240), 15)
Help_ABOUT_Button = GUI.Button((25, 25, 25), (50, 50, 50), (10, 10, 10), 530, 372, 40, 25)
Help_ABOUT_Button_Text = GUI.Text("Ok", (255, 255, 255), (540, 377), 17)

# Properties GUI window
Properties = GUI.Label((28, 28, 28), 0, 21, 200, 575)
Properties_Border = GUI.Label((18, 18, 18), 198, 42, 2, 575)

Properties_Tab = GUI.Label((25, 25, 25), 0, 21, 200, 21)
Properties_Tab_Border = GUI.Label((18, 18, 18), 0, 42, 200, 2)
Properties_Tab_Hilighter = GUI.Label((20, 20, 20), 0, 21, 175, 21)
Properties_Tab_Title = GUI.Text("Properties", (255, 255, 255), (2, 24), 15)
Properties_Tab_ObjectName = GUI.Text("(Player)", (255, 255, 255), (125, 24), 15)

Add_Feature_Button = GUI.Button((28, 28, 28), (50, 50, 50), (40, 40, 40), 52, 47, 85, 25)
Add_Feature_Title = GUI.Text("Add Feature", (255, 255, 255), (57, 51), 15)
Add_Feature_Border = GUI.Label((18, 18, 18), 20, 75, 160, 2)

# Change GUI button
Change = GUI.Button((50, 50, 50), (70, 70, 70), (40, 40, 40), 57, 100, 75, 25)
Change_Text = GUI.Text("Change", (255, 255, 255), (70, 104), 15)
Change_Border = GUI.Label((18, 18, 18), 57, 125, 75, 2)
Change_Left_Border = GUI.Label((18, 18, 18), 57, 100, 2, 25)
while Loop:
	clock.tick(120)
	Display.fill((44, 44, 44))

	Keys = pygame.key.get_pressed()
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
		if Keys[K_LALT] and Keys[K_F4] or Keys[K_LALT] and Keys[K_SPACE] and Keys[K_c]: sys.exit()
		if pygame.mouse.get_pressed()[1]:
			mouseX, mouseY = pygame.mouse.get_pos()
			Player = Entity.Quad(mouseX + 53, mouseY + 32, 50, 50)

		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 4: Zoom += 2.01
			if event.button == 5: Zoom += -1.99

		if event.type == pygame.VIDEORESIZE:
			Display = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
			Menubar = GUI.Label((25, 25, 25), 0, 0, event.w, 21)

			Properties = GUI.Label((28, 28, 28), 0, 0, 200, event.h)
			Properties_Border = GUI.Label((20, 20, 20), 198, 42, 2, event.h)

			Console_Tab = GUI.Label((25, 25, 25), 0, (event.h - 25), event.w, 25)

	if IsPressed['Change'] == 1 and Forever['Change'] == True:
		if IsPressed['Change'] == 1:
			HEXA_ENGINE_LOG("Changed the color of Object \"Player\" to (49, 149, 250)")

		Forever['Change'] = False
		Player.draw((49, 149, 250))

	elif IsPressed['Change'] == 1 or Forever['Change'] == True:
		if IsPressed == 1:
			HEXA_ENGINE_LOG("Changed the color of Object \"Player\" to (250, 56, 49)")

		Forever['Change'] = True
		Player.draw((250, 56, 49))

	elif IsPressed['Change'] == 0 or Forever['Change'] == False:
		Player.draw((49, 149, 250))
	Player.move()

	Properties.draw()
	Properties_Tab.draw()
	Properties_Border.draw()
	Properties_Tab_Hilighter.draw()
	Properties_Tab_Title.draw()
	Properties_Tab_Border.draw()
	Properties_Tab_ObjectName.draw()

	Add_Feature_Button.draw()
	Add_Feature_Title.draw()
	Add_Feature_Border.draw()

	IsPressed['Change'] = Change.draw()
	Change_Text.draw()
	Change_Border.draw()
	Change_Left_Border.draw()

	Menubar.draw()
	IsPressed['File'] = Filemenu_Button.draw()
	Filemenu_Text.draw()

	if IsPressed['File'] == 1 and Forever['File'] == True:
		Forever['File'] = False

	elif IsPressed['File'] == 1 or Forever['File'] == True:
		Forever['File'] = True
		File_Submenu.draw()
		File_Submenu_Button_NEW.draw()
		File_Submenu_Text_NEW.draw()
		File_Submenu_Button_OPEN.draw()
		File_Submenu_Text_OPEN.draw()
		File_Submenu_Button_SAVE.draw()
		File_Submenu_Text_SAVE.draw()
		File_Submenu_Button_EXIT.draw()
		File_Submenu_Text_EXIT.draw()

	Editmenu_Button.draw()
	Editmenu_Text.draw()

	Viewmenu_Button.draw()
	Viewmenu_Text.draw()

	Projectmenu_Button.draw()
	Projectmenu_Text.draw()

	IsPressed['Help'] = Helpmenu_Button.draw()
	Helpmenu_Text.draw()
	if IsPressed['Help'] == 1 and Forever['Help'] == True:
		Forever['Help'] = False

	elif IsPressed['Help'] == 1 or Forever['Help'] == True:
		Forever['Help'] = True
		Help_Submenu.draw()
		IsPressed['Help_ABOUT'] = Help_Submenu_Button_ABOUT.draw()
		Help_Submenu_Text_ABOUT.draw()

	if IsPressed['Help_ABOUT'] == 1 or Forever['Help_ABOUT'] == True:
		Forever['Help_ABOUT'] = True
		Help_ABOUT_Label.draw()
		IsPressed['Help_ABOUT_Button'] = Help_ABOUT_Button.draw()
		Help_ABOUT_Button_Text.draw()
		Help_ABOUT_Title.draw()
		Help_ABOUT_Info.draw()
		if IsPressed['Help_ABOUT_Button'] == 1:
			Forever['Help_ABOUT'] = False
			Forever['Help'] = False

	pygame.display.update()
pygame.quit()
