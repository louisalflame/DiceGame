#-*- coding: UTF-8 -*-
import random
from enum import Enum

from data import DiceAttr
from dice import AttrDice, Tower

class AttrManager:
    def __init__(self):
        self.attrs = DiceAttr.getNewAttrsDict()

    def collect(self, countAttrs):
        for attr, num in countAttrs.items():
            if attr in DiceAttr.getAttrs():
                self.attrs[ attr ] += num

    def getAttrs(self):
        return dict( self.attrs )

class TowerManager:
    def __init__(self):
        self.towers = [
            Tower(0), Tower(1), Tower(2),
            Tower(3), Tower(4), Tower(5)
        ]

    def getTowersImage(self):
        return [ Tower(0).getTowerImage(),
        Tower(0).getTowerImage() ,
        Tower(0).getTowerImage() ,
        Tower(0).getTowerImage() ,
        Tower(0).getTowerImage() ,
        Tower(0).getTowerImage()  ]

class DiceManager:
    def __init__(self):
        self.box  = []
        self.play = []
        self.base = []
        self.used = []
    
    def setDices(self, equip):
        for i, diceType in enumerate(equip.dices):
            dice = AttrDice(i)
            dice.setDiceType(diceType)
            self.box.append( dice )

    def shuffleDices(self):
        random.shuffle(self.box)

    def pop(self, num):
        for i in range( min(num, len(self.box)) ):
            self.play.append( self.box.pop(0) )

    def throw(self):
        for dice in self.play:
            dice.throw()

    def dicePlayTurnBase(self, i):
        self.base.append( self.play.pop(i) )

    def diceBaseTurnPlay(self, i):
        self.play.append( self.base.pop(i) )

    def countAttr(self):
        count = DiceAttr.getNewAttrsDict()
        for dice in self.play:
            face = dice.getFace().faceData.value
            count[ face['attr'] ] += face['num']
        return count

    def cleanPlayBase(self):
        for dice in (self.play+self.base):
            dice.refresh()
            self.used.append( dice )
        self.play = []
        self.base = []

    def checkResetBox(self):
        if not self.box:
            while self.used:
                self.box.append( self.used.pop() )
    
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
        self.attr = AttrManager()
        self.tower = TowerManager()
        self.player = None
        self.dices = DiceManager()
        self.dices.setDices(equip)
 
    def shuffleDices(self):
        self.dices.shuffleDices()

    def popDices(self):
        self.dices.pop(5)

    def throw(self):
        self.dices.throw()

    def dicePlayTurnBase(self, i):
        self.dices.dicePlayTurnBase(i)

    def diceBaseTurnPlay(self, i):
        self.dices.diceBaseTurnPlay(i)

    def collect(self):
        self.attr.collect( self.dices.countAttr() )
        self.dices.cleanPlayBase()
        self.dices.checkResetBox()
