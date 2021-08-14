# This import blocks pygame from printing it's startup text.
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
from pygame.locals import *
from pygame.math import Vector2
