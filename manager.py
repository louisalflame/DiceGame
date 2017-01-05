#-*- coding: UTF-8 -*-
import pygame
from pygame.locals import *
from enum import Enum
import sys, time
 
from scene import MenuScene, BattleScene, EquipScene
from util import *
from data import DiceData, DiceAttr
from battle import BattleManager, TeamManager
 
class GameManager:
    def __init__(self):
        self.currentScene = None
        self.nextScene = None
        self.cursor = CursorManager()
        self.equip = EquipmentManager(self)
 
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
        #pygame.time.Clock().tick(1000)

        self.cursor.update()
        self.updateScene()

    def updateScene(self):
        #update scene if nextscene is waiting
        if self.nextScene != None:
            if self.currentScene:
                self.currentScene.remove()
            scene = self.nextScene(self, self.window)
            scene.construct()
            self.currentScene = scene
            self.window.setScene( scene )
            self.nextScene = None

    def setWindow(self, window):
        self.window = window
 
    def setNextScene(self, sceneClass):
        self.nextScene = sceneClass
 
    def startBattle(self, battleScene):
        teamPlayer = TeamManager( self.equip )
        self.battle = BattleManager( self, teamPlayer, None, battleScene )
 
    def endBattle(self):
        self.battle = None
 
#========================
# battle
#========================
class EquipmentManager:
    def __init__(self, game):
        self.game = game
        self.dices = [
            DiceData.Nor, DiceData.Nor, DiceData.Nor,
            DiceData.Atk, DiceData.Atk, DiceData.Atk,
            DiceData.Def, DiceData.Def, DiceData.Def,
            DiceData.Mov, DiceData.Mov, DiceData.Mov,
            DiceData.Spc, DiceData.Spc, DiceData.Spc,
            DiceData.Heal, DiceData.Heal, DiceData.Heal,
        ]
 