# coding=UTF-8
from attr import *
from data import *

class Tower:
	def __init__(self):
		self.__attr = TowerBase.normal
		self.__level = 0

	def buildByPanel(self, panel):
		self.__attr = panel.getBase()

	def __str__(self):
		return " {0:-<15}Level:{1} ".format( 
			TowerBase.intToName(self.__attr), str(self.__level) )