# coding=UTF-8

class DiceAttr:
	normal  = 0
	attack  = 1
	defense = 2
	special = 3
	health  = 4
	move    = 5

	@classmethod
	def intToName(cls, n):
		return ["normal","attack","defense",
				"special","health","move"][n]

class TowerBase:
	normal  = 0
	attack  = 1
	defense = 2

	@classmethod
	def intToName(cls, n):
		return ["normal Tower","attack Tower","defense Tower",
				"special Tower","health Tower","move Tower"][n]
