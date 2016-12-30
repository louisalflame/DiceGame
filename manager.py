#-*- coding: UTF-8 -*-
import pygame
from pygame.locals import *
from enum import Enum
import sys, time
 
from scene import MenuScene, BattleScene, EquipScene
from util import *
from data import DiceData, DiceAttr
from dice import AttrDice
 
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
        pygame.time.Clock().tick(100)

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
 
class BattleManager:
    class BattleMode(Enum):
        Prepare  = 1
        Move     = 2
        MovThrow = 21
        MovBuild = 22
        Attack   = 3
        Deffense = 4

    def __init__(self, game, teamPlayer, teamEnemy, battleScene ):
        self.game = game
        self.teamPlayer = teamPlayer
        self.teamEnemy = teamEnemy
        self.scene = battleScene
        self.stage = self.BattleMode.Prepare

    def updateStage(self):
        if self.stage == self.BattleMode.Prepare:
            self.prepare()
            self.stage = self.BattleMode.Move
        elif self.stage == self.BattleMode.Move:
            self.popDices()
            self.stage = self.BattleMode.MovThrow
        elif self.stage == self.BattleMode.MovThrow:
            self.throw()
            self.stage = self.BattleMode.MovBuild
        elif self.stage == self.BattleMode.MovBuild:
            self.collect()
            self.stage = self.BattleMode.Attack
        elif self.stage == self.BattleMode.Attack:
            self.stage = self.BattleMode.Deffense
        elif self.stage == self.BattleMode.Deffense:
            self.stage = self.BattleMode.Move
        print( " -->> "+str(self.stage.name) )
 
    def prepare(self):
        self.teamPlayer.shuffleDices()

    def popDices(self):
        self.teamPlayer.popDices()

    def throw(self):
        self.teamPlayer.throw()

    def collect(self):
        self.teamPlayer.collect()
 
class TeamManager:
    def __init__(self, equip):
        self.attr = {
            DiceAttr.Nor: 0, DiceAttr.Atk: 0, DiceAttr.Def: 0,
            DiceAttr.Mov: 0, DiceAttr.Spc: 0, DiceAttr.Heal: 0
        }
        self.tower = {
            DiceAttr.Nor: 0, DiceAttr.Atk: 0, DiceAttr.Def: 0,
            DiceAttr.Mov: 0, DiceAttr.Spc: 0, DiceAttr.Heal: 0
        }
        self.player = None
        self.dices = { "box":[], "play":[], "base":[], "used":[] }
        for i, diceType in enumerate(equip.dices):
            dice = AttrDice(i)
            dice.setDiceType(diceType)
            self.dices["box"].append( dice )
 
    def shuffleDices(self):
        import random
        random.shuffle(self.dices["box"])

    def popDices(self):
        for i in range( min(5, len(self.dices["box"])) ):
            self.dices["play"].append( self.dices["box"].pop(0) )

    def throw(self):
        for dice in self.dices["play"]:
            dice.throw()

    def dicePlayTurnBase(self, i):
        self.dices["base"].append( self.dices["play"].pop(i) )

    def diceBaseTurnPlay(self, i):
        self.dices["play"].append( self.dices["base"].pop(i) )

    def collect(self):
        for dice in self.dices["play"]:
            face = dice.getFace().faceData.value
            self.attr[ face['attr'] ] += face['num']
            dice.refresh()
            self.dices['used'].append( dice )
        for dice in self.dices["base"]:
            self.dices['used'].append( dice )
        self.dices["play"] = []
        self.dices["base"] = []
        if not self.dices["box"]:
            while self.dices["used"]:
                self.dices["box"].append( self.dices["used"].pop() )