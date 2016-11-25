# coding=UTF-8
class DiceAttr:
	normal  = 0
	attack  = 1
	defense = 2
	move    = 3
	special = 4
	health  = 5

	@classmethod
	def intToName(cls, n):
		return [ "normal",
				 "attack",
				 "defense",
				 "move",
				 "special",
				 "health" ][n]

	@classmethod
	def intToAttr(cls, n):
		return [ "Nor",
				 "Atk",
				 "Def",
				 "Mov",
				 "Spc",
				 "Heal" ][n]

class TowerBase:
	normal  = 0
	attack  = 1
	defense = 2
	move    = 3
	special = 4
	health  = 5

	@classmethod
	def intToName(cls, n):
		return [ "normal Tower",
				 "attack Tower",
				 "defense Tower",
				 "move Tower",
				 "special Tower",
				 "health Tower" ][n]

	@classmethod
	def intToImageSrc(cls, n):
		return [ "NorTower",
				 "AtkTower",
				 "DefTower",
				 "MovTower",
				 "SpcTower",
				 "HealTower" ][n]
				 
	@classmethod
	def intToAttr(cls, n):
		return [ "Nor",
				 "Atk",
				 "Def",
				 "Mov",
				 "Spc",
				 "Heal" ][n]

