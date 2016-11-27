# coding=UTF-8
import random
from attr import *
from data import *

#========================
# Dice Panel
#========================

class DicePanel:
	def __init__(self, diceId, panelId):
		self.__diceId = diceId
		self.__panelId = panelId

		self.__number = 1
		self.__attr   = DiceAttr.normal
		self.__base   = TowerBase.normal

	def setNumber(self, number):
		self.__number = number

	def setAttr(self, attr):
		self.__attr = attr

	def setBase(self, base):
		self.__base = base

	def getNumber(self):
		return self.__number

	def getAttr(self):
		return self.__attr

	def getBase(self):
		return self.__base

	def getPanelID(self):
		return self.__panelId

	def getAttrImageSrc(self):
		return "{0}Base{1}{2}.png".format(
			TowerBase.intToAttr(self.__base),
			DiceAttr.intToAttr(self.__attr),
			self.__number )

	def getBaseImageSrc(self):
		return "{0}.png".format( TowerBase.intToImageSrc(self.__base) )

	def __str__(self):
		return " {0: <2},{1} :( {2: <10}:{3: <3}:{4} )".format( 
			str(self.__diceId), str(self.__panelId),
			DiceAttr.intToName(self.__attr),
			str(self.__number), TowerBase.intToName(self.__base) )

	def getBaseInfo(self):
		return " {0: <2},{1} : {2} ".format(
			str(self.__diceId), str(self.__panelId),
			TowerBase.intToName(self.__base) )

#========================
# Dice 
#========================

class Dice:
	def __init__(self, diceId):
		self.__diceId = diceId
		self.__size = 6
		self.__panels = list()
		self.__used = False
		self.__num = None
		self.__type = None
		for i in range(self.__size):
			self.__panels.append( DicePanel(diceId, i) )

	def getAllPanels(self):
		return self.__panels

	def getNum(self):
		if self.isIdle():
			self.__num = random.randint(0,5)
			self.__used = True
		return self.__num

	def isIdle(self):
		return not self.__used

	def refresh(self):
		self.__used = False
		self.__num = None

	def __str__(self):
		string = "size:"+str(self.__size)
		for p in self.__panels:
			string += str(p)
		return string

class GameDice(Dice):
	def __init__(self, diceId):
		super().__init__(diceId)

	def getPanel(self):
		return self._Dice__panels[ self.getNum() ]

	def setDice(self, diceType):
		self._Dice__type = diceType
		diceData = DiceData.intToData(diceType)

		for i, panel in zip(range(self._Dice__size), diceData):
			newPanel = DicePanel( self._Dice__diceId, i )
			newPanel.setAttr(   panel[0] )
			newPanel.setNumber( panel[1] )
			newPanel.setBase(   panel[2] )
			self._Dice__panels[i] = newPanel

	def getDiceTypeImageSrc(self):
		return "{0}.png".format( DiceData.intToImageSrc(self._Dice__type) )