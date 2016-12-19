#-*- coding: UTF-8 -*-
from enum import Enum
from attr import *
from image import DiceImage

class DiceData(Enum):
    #Detail of Dice : ATTR, NUM, BASE
    Nor = { 'info' :
            [ [ DiceAttr.Nor,  3, TowerAttr.Nor ],
            [ DiceAttr.Atk,  3, TowerAttr.Nor ],
            [ DiceAttr.Def, 3, TowerAttr.Nor ],
            [ DiceAttr.Mov,    2, TowerAttr.Nor ],
            [ DiceAttr.Spc, 2, TowerAttr.Nor ],
            [ DiceAttr.Heal,  2, TowerAttr.Nor ], ],
            'img' : DiceImage.DiceNor }

    Atk = { 'info' :
            [ [ DiceAttr.Atk,  3, TowerAttr.Atk ],
            [ DiceAttr.Atk,  3, TowerAttr.Atk ],
            [ DiceAttr.Atk,  3, TowerAttr.Nor ],
            [ DiceAttr.Nor,  2, TowerAttr.Nor ],
            [ DiceAttr.Def, 2, TowerAttr.Def],
            [ DiceAttr.Mov,    2, TowerAttr.Atk ], ],
            'img' : DiceImage.DiceAtk }

    Def = { 'info' :
            [ [ DiceAttr.Def, 3, TowerAttr.Def],
            [ DiceAttr.Def, 3, TowerAttr.Def],
            [ DiceAttr.Def, 3, TowerAttr.Nor ],
            [ DiceAttr.Nor,  2, TowerAttr.Nor ],
            [ DiceAttr.Atk,  2, TowerAttr.Atk ],
            [ DiceAttr.Heal,  2, TowerAttr.Def], ],
            'img' : DiceImage.DiceDef }

    Mov = { 'info' :
            [ [ DiceAttr.Mov,    3, TowerAttr.Mov   ],
            [ DiceAttr.Mov,    2, TowerAttr.Mov   ],
            [ DiceAttr.Mov,    2, TowerAttr.Nor ],
            [ DiceAttr.Nor,  3, TowerAttr.Nor ],
            [ DiceAttr.Atk,  3, TowerAttr.Atk ],
            [ DiceAttr.Spc, 2, TowerAttr.Nor ], ],
            'img' : DiceImage.DiceMov }

    Spc = { 'info' :
            [ [ DiceAttr.Spc, 3, TowerAttr.Spc],
            [ DiceAttr.Spc, 2, TowerAttr.Spc],
            [ DiceAttr.Spc, 2, TowerAttr.Nor ],
            [ DiceAttr.Nor,  3, TowerAttr.Nor ],
            [ DiceAttr.Mov,    2, TowerAttr.Mov   ],
            [ DiceAttr.Heal,  2, TowerAttr.Heal ], ],
            'img' : DiceImage.DiceSpc }

    Heal = { 'info' :
             [ [ DiceAttr.Heal,  2, TowerAttr.Heal ],
             [ DiceAttr.Heal,  2, TowerAttr.Heal ],
             [ DiceAttr.Heal,  2, TowerAttr.Nor ],
             [ DiceAttr.Nor,  3, TowerAttr.Nor ],
             [ DiceAttr.Def, 3, TowerAttr.Def],
             [ DiceAttr.Atk,  3, TowerAttr.Atk ], ],
            'img' : DiceImage.DiceHeal }

    
