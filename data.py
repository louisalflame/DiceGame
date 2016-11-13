# coding=UTF-8
from attr import *

class DiceData:
	    #attr, num, base
	AttackDice = [
		[ DiceAttr.normal,  1, TowerBase.normal ],
		[ DiceAttr.normal,  2, TowerBase.normal ],
		[ DiceAttr.defense, 1, TowerBase.normal ],
		[ DiceAttr.attack,  1, TowerBase.normal ],
		[ DiceAttr.attack,  2, TowerBase.normal ],
		[ DiceAttr.attack,  3, TowerBase.attack ],
	]

	DefenseDice = [
		[ DiceAttr.normal,  1, TowerBase.normal ],
		[ DiceAttr.normal,  2, TowerBase.normal ],
		[ DiceAttr.health,  1, TowerBase.normal ],
		[ DiceAttr.defense, 1, TowerBase.normal ],
		[ DiceAttr.defense, 2, TowerBase.normal ],
		[ DiceAttr.defense, 3, TowerBase.attack ],
	]

	SpecialDice = [
		[ DiceAttr.normal,  2, TowerBase.normal ],
		[ DiceAttr.normal,  3, TowerBase.normal ],
		[ DiceAttr.move,    1, TowerBase.normal ],
		[ DiceAttr.special, 1, TowerBase.normal ],
		[ DiceAttr.special, 1, TowerBase.normal ],
		[ DiceAttr.special, 2, TowerBase.attack ],
	]


class DicePackage:
	basic = [ 
		DiceData.AttackDice, DiceData.AttackDice,
		DiceData.AttackDice, DiceData.AttackDice,
		DiceData.AttackDice, DiceData.AttackDice,
		DiceData.AttackDice, DiceData.AttackDice,
		DiceData.DefenseDice, DiceData.DefenseDice,
		DiceData.DefenseDice, DiceData.DefenseDice,
		DiceData.DefenseDice, DiceData.DefenseDice,
		DiceData.DefenseDice, DiceData.DefenseDice,
		DiceData.SpecialDice, DiceData.SpecialDice,
		DiceData.SpecialDice, DiceData.SpecialDice,
	]