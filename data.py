# coding=UTF-8
from attr import *

class DiceData:
	#Index of dice
	normal  = 0
	attack  = 1
	defense = 2
	move    = 3
	special = 4
	health  = 5

	#Detail of Dice : ATTR, NUM, BASE
	NormalDice =  [ [ DiceAttr.normal,  3, TowerBase.normal ],
				    [ DiceAttr.attack,  3, TowerBase.normal ],
				    [ DiceAttr.defense, 3, TowerBase.normal ],
				    [ DiceAttr.move,    2, TowerBase.normal ],
				    [ DiceAttr.special, 2, TowerBase.normal ],
				    [ DiceAttr.health,  2, TowerBase.normal ], ]

	AttackDice =  [ [ DiceAttr.attack,  3, TowerBase.attack ],
				    [ DiceAttr.attack,  3, TowerBase.attack ],
				    [ DiceAttr.attack,  3, TowerBase.normal ],
				    [ DiceAttr.normal,  2, TowerBase.normal ],
				    [ DiceAttr.defense, 2, TowerBase.defense],
				    [ DiceAttr.move,    2, TowerBase.attack ], ]

	DefenseDice = [ [ DiceAttr.defense, 3, TowerBase.defense],
				    [ DiceAttr.defense, 3, TowerBase.defense],
				    [ DiceAttr.defense, 3, TowerBase.normal ],
				    [ DiceAttr.normal,  2, TowerBase.normal ],
				    [ DiceAttr.attack,  2, TowerBase.attack ],
				    [ DiceAttr.health,  2, TowerBase.defense], ]

	MoveDice =    [ [ DiceAttr.move,    3, TowerBase.move   ],
				    [ DiceAttr.move,    2, TowerBase.move   ],
				    [ DiceAttr.move,    2, TowerBase.normal ],
				    [ DiceAttr.normal,  3, TowerBase.normal ],
				    [ DiceAttr.attack,  3, TowerBase.attack ],
				    [ DiceAttr.special, 2, TowerBase.normal ], ]

	SpecialDice = [ [ DiceAttr.special, 3, TowerBase.special],
				    [ DiceAttr.special, 2, TowerBase.special],
				    [ DiceAttr.special, 2, TowerBase.normal ],
				    [ DiceAttr.normal,  3, TowerBase.normal ],
				    [ DiceAttr.move,    2, TowerBase.move   ],
				    [ DiceAttr.health,  2, TowerBase.health ], ]

	HealthDice =  [ [ DiceAttr.health,  2, TowerBase.health ],
				    [ DiceAttr.health,  2, TowerBase.health ],
				    [ DiceAttr.health,  2, TowerBase.normal ],
				    [ DiceAttr.normal,  3, TowerBase.normal ],
				    [ DiceAttr.defense, 3, TowerBase.defense],
				    [ DiceAttr.attack,  3, TowerBase.attack ], ]

	@classmethod
	def getAllDataType(cls):
		return [ DiceData.normal,
				 DiceData.attack,
				 DiceData.defense,
				 DiceData.move,
				 DiceData.special,
				 DiceData.health, ]

	@classmethod
	def intToData(cls, n):
		return [ DiceData.NormalDice,
				 DiceData.AttackDice,
				 DiceData.DefenseDice,
				 DiceData.MoveDice,
				 DiceData.SpecialDice,
				 DiceData.HealthDice, ][n]

	@classmethod
	def intToImageSrc(cls, n):
		return [ "DiceNor",
				 "DiceAtk",
				 "DiceDef",
				 "DiceMov",
				 "DiceSpc",
				 "DiceHeal", ][n]

class DicePackage:
	basic = [ 
		DiceData.normal, DiceData.normal,
		DiceData.normal, DiceData.normal,
		DiceData.attack, DiceData.attack,
		DiceData.attack, DiceData.attack,
		DiceData.defense, DiceData.defense,
		DiceData.defense, DiceData.defense,
		DiceData.move, DiceData.move,
		DiceData.special, DiceData.special,
		DiceData.special, DiceData.special,
		DiceData.health, DiceData.health,
	]