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
        self.sceneStack = []
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

    def startBattle(self):
        teamPlayer = TeamManager( self.equip )
        self.battle = BattleManager( self, teamPlayer, None )

    def endBattle(self):
        self.battle = None

    def test(self):
        print ( [ dice.getDiceTypeImageSrc() for dice in self.battle.teamPlayer.dices ] )


#========================
# battle
#========================
class EquipmentManager:
    def __init__(self, game):
        self.game = game
        self.dices = [
            DiceData.NormalDice,
            DiceData.NormalDice,
            DiceData.NormalDice,
            DiceData.AttackDice,
        ]

class BattleManager:
    def __init__(self, game, teamPlayer, teamEnemy ):
        self.game = game
        self.teamPlayer = teamPlayer
        self.teamEnemy = teamEnemy

class TeamManager:
    def __init__(self, equip):
        self.attr = None  
        self.tower = None
        self.player = None
        self.dices = []
        for i, diceType in enumerate(equip.dices):
            dice = AttrDice(i)
            dice.setDiceType(diceType)
            self.dices.append( dice )

