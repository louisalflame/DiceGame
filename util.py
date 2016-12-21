#-*- coding: UTF-8 -*-

import pygame
from pygame.locals import *
import os

class Cursor:
    def __init__(self, pos=(0,0), pressed=(0,0,0)):
        self.x = pos[0]
        self.y = pos[1]
        self.leftClick = pressed[0]
        self.middleClick = pressed[1]
        self.rightClick = pressed[2]

    def isOverRect(self, pos, size):
        return self.x >= pos[0] and self.x <= pos[0]+size[0] and self.y >= pos[1] and self.y <= pos[1]+size[1]

    def isLeftClick(self):
        return self.leftClick

def font_MsjhBd(size):
    return pygame.font.Font(os.environ['SYSTEMROOT'] + "\\Fonts\\msjhbd.ttf", size)

def imageTransparent(image, percent):
    image = image.convert()
    image.set_alpha( int( 256 * percent ) )
    return image