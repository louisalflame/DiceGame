# coding=UTF-8
import random
from dice import *
from tower import *
from data import *
from interface import *

class BattleManager:
	def __init__(self):
		self.__diceField = []
		self.__dicePrepare = []
		self.__diceUsed = []

		self.__currentPanels = []
		self.__attrPoints = [ 0,0,0,0,0,0 ]

		self.__towers = []

	def setDices(self, dices):
		self.__dicePrepare += dices

	def startDiceField(self, num=1):
		for i in range(num):
			if not self.__dicePrepare:
				break
			self.__diceField.append( self.__dicePrepare.pop() )

	def throwDices(self):
		for dice in self.__diceField:
			panel = dice.getPanel()
			self.__currentPanels.append(panel)

	def buildTowerByPanel(self, choice):
		panel = self.__currentPanels[choice]
		tower = Tower()
		tower.buildByPanel( panel )
		self.__currentPanels.remove(panel)
		self.__towers.append( tower )
		return "build --->> "+panel.getBaseInfo()

	def countPoints(self):
		for panel in self.__currentPanels:
			self.__attrPoints[ panel.getAttr() ] += panel.getNumber()	

	def cleanDices(self):
		self.__currentPanels = []
		self.__diceUsed += self.__diceField
		self.__diceField = []

	def checkRefreshDices(self):
		if not self.__dicePrepare:
			self.__dicePrepare = self.__diceUsed
			self.__diceUsed = []
			return "End Of Dices, => REFRESH "
		return ""

	def showDicePanels(self):
		return "\n".join([ str(p) for p in self.__currentPanels ])

	def showAttrs(self):
		return self.__attrPoints
		
	def showTower(self): 
		return self.__towers


class PlayerManager:
	def __init__(self):
		self.__diceNum = 20
		self.__dices = []
		for i in range(self.__diceNum):
			dice = GameDice(i)
			dice.setDice( DicePackage.basic[i] )
			self.__dices.append(dice)

	def prepare(self):
		random.shuffle(self.__dices)

	def getDices(self, n=1):
		return self.__dices