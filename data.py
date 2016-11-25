# coding=UTF-8
from attr import *

class DiceData:

	normal  = 0
	attack  = 1
	defense = 2
	move    = 3
	special = 4
	health  = 5

	    #attr, num, base
	NormalDice = [ [ DiceAttr.normal,  3, TowerBase.normal ],
				   [ DiceAttr.attack,  3, TowerBase.normal ],
				   [ DiceAttr.defense, 3, TowerBase.normal ],
				   [ DiceAttr.move,    2, TowerBase.normal ],
				   [ DiceAttr.special, 2, TowerBase.normal ],
				   [ DiceAttr.health,  2, TowerBase.normal ], ]

	AttackDice = [ [ DiceAttr.attack,  3, TowerBase.attack ],
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

	SpecialDice = [ [ DiceAttr.special, 3, TowerBase.special],
				    [ DiceAttr.special, 3, TowerBase.special],
				    [ DiceAttr.special, 3, TowerBase.normal ],
				    [ DiceAttr.move,    2, TowerBase.normal ],
				    [ DiceAttr.move,    2, TowerBase.move   ],
				    [ DiceAttr.health,  2, TowerBase.health ], ]

	@classmethod
	def intToData(cls, n):
		return [ DiceData.NormalDice,
				 DiceData.AttackDice,
				 DiceData.DefenseDice,
				 DiceData.NormalDice,
				 DiceData.SpecialDice,
				 DiceData.NormalDice, ][n]

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
		DiceData.normal, DiceData.normal,
		DiceData.attack, DiceData.attack,
		DiceData.attack, DiceData.attack,
		DiceData.defense, DiceData.defense,
		DiceData.defense, DiceData.defense,
		DiceData.defense, DiceData.defense,
		DiceData.special, DiceData.special,
		DiceData.special, DiceData.special,
	]