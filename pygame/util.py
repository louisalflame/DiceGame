#-*- coding: UTF-8 -*-

import pygame
from pygame.locals import *
import os

def fontMsjhBd(size):
	return pygame.font.Font(os.environ['SYSTEMROOT'] + "\\Fonts\\msjhbd.ttf", size)