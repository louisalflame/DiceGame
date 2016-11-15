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
		return ["normal","attack","defense",
				"move","special","health"][n]

class TowerBase:
	normal  = 0
	attack  = 1
	defense = 2

	@classmethod
	def intToName(cls, n):
		return ["normal Tower","attack Tower","defense Tower",
				"move Tower","special Tower","health Tower"][n]
