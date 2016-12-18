#-*- coding: UTF-8 -*-
import random
from attr import DiceAttr, TowerAttr
from data import DiceData

class DiceFace:
    def __init__(self, diceId, faceId, num=1, attr=DiceAttr.Nor, base=TowerAttr.Nor):
        self.diceId = diceId
        self.faceId = faceId

        self.number = num
        self.attr   = attr
        self.base   = base

    def getAttrImageSrc(self):
        return "{0}Base{1}{2}.png".format(
            self.base.name,
            self.attr.name,
            self.number )

    def getTowerAttrImageSrc(self):
        return "{0}.png".format( TowerAttr.intToImageSrc(self.__base) )

    def clone(self):
        return DiceFace(self.diceId, self.faceId, self.number, self.attr, self.base)

#========================
# Dice 
#========================

class GameDice:
    def __init__(self, diceId, size=6):
        self.diceId = diceId
        self.size   = size
        self.faces  = list()
        self.used   = False
        self.number = None
        self.type   = None
        for i in range(self.size):
            self.faces.append( DiceFace(diceId, i) )

    def getFace(self):
        return self.faces[ self.getNum() ]

    def getNum(self):
        if self.isIdle():
            self.number = random.randint(0,5)
            self.used = True
        return self.number

    def isIdle(self):
        return not self.__used

    def refresh(self):
        self.used = False
        self.number = None

    def clone(self):
        dice = Dice(self.diceId)
        dice.size   = self.size
        dice.used   = self.used
        dice.number = self.number
        dice.type   = self.type
        dice.faces  = [ face.clone() for face in self.faces ]
        return dice

class AttrDice(GameDice):
    def __init__(self, diceId):
        super().__init__(diceId)

    def setDiceType(self, diceType):
        self.type = diceType

        for i, face in zip(range(self.size), self.type.value):
            self.faces[i] = DiceFace( self.diceId, i, face[1], face[0], face[2] )

    def getDiceTypeImageSrc(self):
        return "Dice{0}.png".format( self.type.name )