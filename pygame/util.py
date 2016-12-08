#-*- coding: UTF-8 -*-

import pygame
from pygame.locals import *
import os

def font_MsjhBd(size):
	return pygame.font.Font(os.environ['SYSTEMROOT'] + "\\Fonts\\msjhbd.ttf", size)