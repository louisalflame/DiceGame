#-*- coding: UTF-8 -*-
import pygame
from pygame.locals import *
import sys
 
from scene import MenuScene, battleScene, EquipScene
from util import *
from data import DiceData
from dice import AttrDice
 
class GameManager:
    def __init__(self):
        self.currentScene = None
        self.nextScene = None
        self.cursor = Cursor()
        self.lastCursor = Cursor()
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
        self.lastCursor = self.cursor
        self.cursor = Cursor( pygame.mouse.get_pos(), pygame.mouse.get_pressed() )
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
 
    def startBattle(self):
        teamPlayer = TeamManager( self.equip )
        self.battle = BattleManager( self, teamPlayer, None )
 
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
 
class BattleManager:
    def __init__(self, game, teamPlayer, teamEnemy ):
        self.game = game
        self.teamPlayer = teamPlayer
        self.teamEnemy = teamEnemy
        self.stage = 1

    def updateStage(self):
        if self.stage == 1:
            self.prepare()
            self.game.currentScene.nextMode = 1
        elif self.stage == 2:
            self.popDices()
            self.game.currentScene.nextMode = 2
        self.stage += 1
 
    def prepare(self):
        self.teamPlayer.shuffleDices()

    def popDices(self):
        self.teamPlayer.popDices(5)
 
class TeamManager:
    def __init__(self, equip):
        self.attr = None 
        self.tower = None
        self.player = None
        self.dices = { "box":[], "play":[], "used":[] }
        for i, diceType in enumerate(equip.dices):
            dice = AttrDice(i)
            dice.setDiceType(diceType)
            self.dices["box"].append( dice )
 
    def shuffleDices(self):
        import random
        random.shuffle(self.dices["box"])

    def popDices(self, n):
        for i in range(n):
            self.dices["play"].append( self.dices["box"].pop(0) )