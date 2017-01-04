 #-*- coding: UTF-8 -*-
import random
from data import DiceData, TowerData
from image import TowerImage

class DiceFace:
    def __init__(self, diceId, faceId, faceData ):
        self.diceId = diceId
        self.faceId = faceId
        self.faceData = faceData

    def getFaceAttrImage(self):
        return self.faceData.value['img'].value

    def getTowerAttrImageSrc(self):
        return self.faceData.value['base'].value

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
        return self.faces[ self.number ] if not self.isIdle() else None

    def getNum(self):
        return self.number if not self.isIdle() else None

    def isIdle(self):
        return not self.used

    def throw(self):
        self.number = random.randint(0, self.size-1)
        self.used = True

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



#========================
# Tower
#========================
class Tower:
    def __init__(self, towerId, towerData=TowerData.Null):
        self.towerId = towerId
        self.level = 0
        self.towerData = towerData

    def getTowerImage(self):
        return self.towerData.value['img'][ self.level ].value

    def levelUp(self):
        self.level = (self.level + 1) % self.towerData.value['max']