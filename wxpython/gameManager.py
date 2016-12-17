# coding=UTF-8
import random
from dice import *
from tower import *
from data import *
from battle import *
from interface import *

class GameManager:
	def __init__(self):
		self.battle = BattleManager()
		self.player = PlayerManager()

		self.STATUS = {
			"INIT" : 0, 
			"PREPARE" : 1,
			"START" : 2,
			"SETTING" : 3,
			"THROW" : 4,
			"COUNT" : 5,
		}
		self.status = self.STATUS["INIT"]

	def setGUI(self, gui):
		self.gui = gui
		self.gui.changeToSettingScene()
		self.gui.showDicesMenu()
		self.gui.showDicePackage( self.getDicePackage() )

	def updateStatus(self):
		if self.status == self.STATUS["INIT"]:
			if self.isInitialComplete():
				self.status = self.STATUS["PREPARE"]
				self.gui.changeToPlayScene()
				self.gui.showText( "Start Game..." )
			else:
				self.gui.showText( "Please Select 20 or more Dices First..." )

		elif self.status == self.STATUS["PREPARE"]:
			self.status = self.STATUS["START"]
			self.prepare()

			self.gui.showDices( self.battle.showDices() )
			self.gui.clearText()
			self.gui.showText( "Press ENTER to Start Game..." )
		elif self.status == self.STATUS["START"] or self.status == self.STATUS["COUNT"]:
			self.status = self.STATUS["SETTING"]
			self.battle.startDiceField(5)

			self.gui.showDices( self.battle.showDices() )
			self.gui.clearText()
			self.gui.showText( "Ready to throw these dices!" )
		elif self.status == self.STATUS["SETTING"]:
			self.status = self.STATUS["THROW"]
			self.battle.throwDices()

			self.gui.showDices( self.battle.showDices() )
			self.gui.clearText()
			self.gui.showText( "Choose a dice as tower base:" )
		elif self.status == self.STATUS["THROW"]:
			self.status = self.STATUS["COUNT"]
			self.gui.clearText()
			self.gui.showText( "Abandon picking dice panel..." )
			self.battle.countPoints()
			self.cleanDices()

	def isInitialComplete(self):
		return len( self.player.getDices() ) >= 5

	def removeDiceOfPackage(self, dice):
		self.player.removeDice(dice)

	def pickDiceToPackage(self, dice):
		self.player.pushDice(dice)

	def getDicePackage(self):
		return self.player.getDices()

	def pickPanel(self, panel):
		self.status = self.STATUS["COUNT"]
		self.battle.buildTowerByPanel(panel)
		self.battle.countPoints()
		self.cleanDices()

	def initGui(self):
		self.gui.showText("press ENTER to prepare game...")

	def prepare(self):
		self.player.diceShuffle()
		self.battle.setDices( self.player.getDices() )

	def cleanDices(self):
		self.battle.cleanDices()
		self.gui.showText(
			self.battle.checkRefreshDices() )
		self.gui.showAttrs(
			self.battle.showAttrs() )
		self.gui.showDices( self.battle.showDices() )
		self.gui.cleanDicePlay()

