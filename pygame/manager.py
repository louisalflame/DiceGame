#-*- coding: UTF-8 -*-
import pygame
from pygame.locals import *
import sys

from scene import *
from util import *

class GameManager:
    def __init__(self):
        self.sceneStack = []
        self.cursor = Cursor()
        self.lastCursor = Cursor()

    def loopGame(self):        
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.exit()

            self.update()
            self.window.draw()
            self.window.update()

    def exit(self):
        sys.exit()

    def update(self):
        self.lastCursor = self.cursor
        self.cursor = Cursor( pygame.mouse.get_pos(), pygame.mouse.get_pressed() )

    def setWindow(self, window):
        self.window = window

    def startScene(self, scene):
        self.sceneStack.append( scene )
        self.window.setScene( scene )

    def startSceneClass(self, sceneClass):
        self.startScene( sceneClass(self, self.window) )

    def backScene(self):
        if len(self.sceneStack) < 2:
            return None

        self.sceneStack.pop().remove()
        self.window.setScene( self.sceneStack[-1] )


class BattleManager:
    def __init__(self):
        self.teamA = None
        self.teamB = None

class TeamManager:
    def __init__(self):
        self.attr = None
        self.tower = None
        self.player = None
        self.dices = None

