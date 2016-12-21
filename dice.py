 #-*- coding: UTF-8 -*-
import random
from data import DiceData

class DiceFace:
    def __init__(self, diceId, faceId, faceData ):
        self.diceId = diceId
        self.faceId = faceId

        self.faceData = faceData
        self.number = faceData.value['num']
        self.attr   = faceData.value['attr']
        self.base   = faceData.value['base']
        self.image  = faceData.value['img']

    def getFaceAttrImage(self):
        return self.faceData.value['img'].value

    def getTowerAttrImageSrc(self):
        return 

    def clone(self):
        return DiceFace(self.diceId, self.faceId, self.faceData)

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

    def clone(self, dice=None ):
        if not dice:
            dice = GameDice(self.diceId)
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
        self.size = len(self.type.value['info'])

        for i, faceData in enumerate(self.type.value['info']):
            self.faces.append( DiceFace( self.diceId, i, faceData ) )

    def clone(self):
        dice = super().clone(AttrDice(self.diceId))
        return dice

    def getDiceTypeImage(self):
        return self.type.value['img'].value