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
        return self.x >= pos[0] and \
               self.x <= pos[0]+size[0] and \
               self.y >= pos[1] and \
               self.y <= pos[1]+size[1]

    def isLeftClick(self):
        return self.leftClick

class CursorManager:
    def __init__(self):
        self.cursor = Cursor()
        self.lastCursor = Cursor()
        self.lastPressDown = Cursor()

    def update(self):
        #update cursor position
        self.lastCursor = self.cursor
        self.cursor = Cursor( pygame.mouse.get_pos(), pygame.mouse.get_pressed() )

        if self.cursor.isLeftClick() and not self.lastCursor.isLeftClick():
            self.lastPressDown = self.cursor
        if not self.cursor.isLeftClick() and self.lastCursor.isLeftClick():
            self.lastPressUp = self.cursor

    def isOverRect(self, pos, size):
        return self.cursor.isOverRect(pos, size)

    def isPressDown(self, pos, size):
        return self.cursor.isOverRect(pos, size) and \
               self.cursor.isLeftClick()

    def isClick(self, pos, size):
        return self.lastPressDown.isOverRect(pos, size) and \
               self.cursor.isOverRect(pos, size) and \
               self.lastCursor.isLeftClick() and \
               not self.cursor.isLeftClick()

    def isNewMoveIn(self, pos, size):
        return not self.lastCursor.isOverRect(pos, size)

def font_MsjhBd(size):
    return pygame.font.Font(os.environ['SYSTEMROOT'] + "\\Fonts\\msjhbd.ttf", size)

def imageTransparent(image, percent):
    image = image.convert()
    image.set_alpha( int( 256 * percent ) )
    return image

def imageScaleFromCenter(image, pos, size, scale):
    image = pygame.transform.scale( 
            image, (int(size[0]*scale), int(size[1]*scale)) )
    pos = ( pos[0]-int(size[0]*(scale-1)/2), pos[1]-int(size[1]*(scale-1)/2) )
    return image, pos