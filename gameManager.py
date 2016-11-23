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
			"THROW" : 2,
			"COUNT" : 3,
		}
		self.status = self.STATUS["INIT"]

	def setGUI(self, gui):
		self.gui = gui

	def updateStatus(self, string):
		if self.status == self.STATUS["INIT"]:
			self.prepare()
			self.status = self.STATUS["PREPARE"]
			self.gui.clearText()

			self.gui.showDices( self.battle.showDices() )
			self.gui.showText( "start Game...\npress ENTER to throw dices..." )
		elif self.status == self.STATUS["PREPARE"] or self.status == self.STATUS["COUNT"]:
			self.battle.startDiceField(5)
			self.battle.throwDices()

			self.gui.showDices( self.battle.showDices() )	
			self.gui.showText( "Choose a dice as tower base:" )
			self.status = self.STATUS["THROW"]
		elif self.status == self.STATUS["THROW"]:				
			self.gui.showText( "Abandon picking dice panel..." )
			self.battle.countPoints()
			self.cleanDices()
			self.status = self.STATUS["COUNT"]

	def pickPanel(self, panel):
		self.battle.buildTowerByPanel(panel)
		self.battle.countPoints()
		self.cleanDices()
		self.status = self.STATUS["COUNT"]

	def initGui(self):
		self.gui.showText("press ENTER to prepare game...")

	def prepare(self):
		self.player.prepare()
		self.battle.setDices( self.player.getDices() )

	def cleanDices(self):
		self.battle.cleanDices()
		self.gui.showText(
			self.battle.checkRefreshDices() )
		self.gui.showAttrs(
			self.battle.showAttrs() )
		self.gui.showDices( self.battle.showDices() )
		self.gui.cleanDicePlay()

