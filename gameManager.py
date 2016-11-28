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
			"THROW" : 3,
			"COUNT" : 4,
		}
		self.status = self.STATUS["INIT"]

	def setGUI(self, gui):
		self.gui = gui
		self.gui.changeToSettingScene()
		self.gui.showDicesMenu()

	def updateStatus(self):
		if self.status == self.STATUS["INIT"]:
			if self.isInitialComplete():
				self.status = self.STATUS["PREPARE"]
				self.gui.changeToPlayScene()
				self.gui.showText( "Start Game..." )
			else:
				self.gui.showText( "Please Select Dices First..." )

		elif self.status == self.STATUS["PREPARE"]:
			self.status = self.STATUS["START"]			
			self.prepare()

			self.gui.showDices( self.battle.showDices() )
			self.gui.clearText()
			self.gui.showText( "Press ENTER to throw dices..." )
		elif self.status == self.STATUS["START"] or self.status == self.STATUS["COUNT"]:
			self.status = self.STATUS["THROW"]
			self.battle.startDiceField(5)
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
		return len( self.player.getDices() ) % 5 is 0

	def pickDiceToPackage(self, dice):
		self.player.pushDice(dice)

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

