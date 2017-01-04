#-*- coding: UTF-8 -*-
from enum import Enum
from image import DiceImage, AttrImage, TowerImage

class DiceAttr(Enum):
    Nor  = 1
    Atk  = 2
    Def  = 3
    Mov  = 4
    Spc  = 5
    Heal = 6

class TowerAttr(Enum):
    Nor  = { 'id': 1,
             'img' : TowerImage.NorTower }
    Atk  = { 'id': 2,
             'img' : TowerImage.AtkTower }
    Def  = { 'id': 3,
             'img' : TowerImage.DefTower }
    Mov  = { 'id': 4,
             'img' : TowerImage.MovTower }
    Spc  = { 'id': 5,
             'img' : TowerImage.SpcTower }
    Heal = { 'id': 6,
             'img' : TowerImage.HealTower }

class FaceData(Enum):
    NorNor1 = { 'attr' : DiceAttr.Nor,
                'base' : TowerAttr.Nor,
                'num' : 1,
                'img' : AttrImage.NorNor1,}
    NorNor2 = { 'attr' : DiceAttr.Nor,
                'base' : TowerAttr.Nor, 
                'num' : 2,
                'img' : AttrImage.NorNor2, }
    NorNor3 = { 'attr' : DiceAttr.Nor,
                'base' : TowerAttr.Nor,
                'num' : 3,
                'img' : AttrImage.NorNor3, }
    NorAtk1 = { 'attr' : DiceAttr.Atk,
                'base' : TowerAttr.Nor,
                'num' : 1,
                'img' : AttrImage.NorAtk1, }
    NorAtk2 = { 'attr' : DiceAttr.Atk,
                'base' : TowerAttr.Nor,
                'num' : 2,
                'img' : AttrImage.NorAtk2, }
    NorAtk3 = { 'attr' : DiceAttr.Atk,
                'base' : TowerAttr.Nor,
                'num' : 3,
                'img' : AttrImage.NorAtk3, }
    NorDef1 = { 'attr' : DiceAttr.Def,
                'base' : TowerAttr.Nor,
                'num' : 1,
                'img' : AttrImage.NorDef1, }
    NorDef2 = { 'attr' : DiceAttr.Def,
                'base' : TowerAttr.Nor,
                'num' : 2,
                'img' : AttrImage.NorDef2, }
    NorDef3 = { 'attr' : DiceAttr.Def,
                'base' : TowerAttr.Nor,
                'num' : 3,
                'img' : AttrImage.NorDef3, }
    NorMov1 = { 'attr' : DiceAttr.Mov,
                'base' : TowerAttr.Nor,
                'num' : 1,
                'img' : AttrImage.NorMov1, }
    NorMov2 = { 'attr' : DiceAttr.Mov,
                'base' : TowerAttr.Nor,
                'num' : 2,
                'img' : AttrImage.NorMov2, }
    NorMov3 = { 'attr' : DiceAttr.Mov,
                'base' : TowerAttr.Nor,
                'num' : 3,
                'img' : AttrImage.NorMov3, }
    NorSpc1 = { 'attr' : DiceAttr.Spc,
                'base' : TowerAttr.Nor,
                'num' : 1,
                'img' : AttrImage.NorSpc1, }
    NorSpc2 = { 'attr' : DiceAttr.Spc,
                'base' : TowerAttr.Nor,
                'num' : 2,
                'img' : AttrImage.NorSpc2, }
    NorSpc3 = { 'attr' : DiceAttr.Spc,
                'base' : TowerAttr.Nor,
                'num' : 3,
                'img' : AttrImage.NorSpc3, }
    NorHeal1 = { 'attr' : DiceAttr.Heal,
                'base' : TowerAttr.Nor,
                'num' : 1,
                'img' : AttrImage.NorHeal1, }
    NorHeal2 = { 'attr' : DiceAttr.Heal,
                'base' : TowerAttr.Nor,
                'num' : 2,
                'img' : AttrImage.NorHeal2, }
    NorHeal3 = { 'attr' : DiceAttr.Heal,
                'base' : TowerAttr.Nor,
                'num' : 3,
                'img' : AttrImage.NorHeal3, }
    AtkNor1 = { 'attr' : DiceAttr.Nor,
                'base' : TowerAttr.Atk,
                'num' : 1,
                'img' : AttrImage.AtkNor1,}
    AtkNor2 = { 'attr' : DiceAttr.Nor,
                'base' : TowerAttr.Atk, 
                'num' : 2,
                'img' : AttrImage.AtkNor2, }
    AtkNor3 = { 'attr' : DiceAttr.Nor,
                'base' : TowerAttr.Atk,
                'num' : 3,
                'img' : AttrImage.AtkNor3, }
    AtkAtk1 = { 'attr' : DiceAttr.Atk,
                'base' : TowerAttr.Atk,
                'num' : 1,
                'img' : AttrImage.AtkAtk1, }
    AtkAtk2 = { 'attr' : DiceAttr.Atk,
                'base' : TowerAttr.Atk,
                'num' : 2,
                'img' : AttrImage.AtkAtk2, }
    AtkAtk3 = { 'attr' : DiceAttr.Atk,
                'base' : TowerAttr.Atk,
                'num' : 3,
                'img' : AttrImage.AtkAtk3, }
    AtkDef1 = { 'attr' : DiceAttr.Def,
                'base' : TowerAttr.Atk,
                'num' : 1,
                'img' : AttrImage.AtkDef1, }
    AtkDef2 = { 'attr' : DiceAttr.Def,
                'base' : TowerAttr.Atk,
                'num' : 2,
                'img' : AttrImage.AtkDef2, }
    AtkDef3 = { 'attr' : DiceAttr.Def,
                'base' : TowerAttr.Atk,
                'num' : 3,
                'img' : AttrImage.AtkDef3, }
    AtkMov1 = { 'attr' : DiceAttr.Mov,
                'base' : TowerAttr.Atk,
                'num' : 1,
                'img' : AttrImage.AtkMov1, }
    AtkMov2 = { 'attr' : DiceAttr.Mov,
                'base' : TowerAttr.Atk,
                'num' : 2,
                'img' : AttrImage.AtkMov2, }
    AtkMov3 = { 'attr' : DiceAttr.Mov,
                'base' : TowerAttr.Atk,
                'num' : 3,
                'img' : AttrImage.AtkMov3, }
    AtkSpc1 = { 'attr' : DiceAttr.Spc,
                'base' : TowerAttr.Atk,
                'num' : 1,
                'img' : AttrImage.AtkSpc1, }
    AtkSpc2 = { 'attr' : DiceAttr.Spc,
                'base' : TowerAttr.Atk,
                'num' : 2,
                'img' : AttrImage.AtkSpc2, }
    AtkSpc3 = { 'attr' : DiceAttr.Spc,
                'base' : TowerAttr.Atk,
                'num' : 3,
                'img' : AttrImage.AtkSpc3, }
    AtkHeal1 = { 'attr' : DiceAttr.Heal,
                'base' : TowerAttr.Atk,
                'num' : 1,
                'img' : AttrImage.AtkHeal1, }
    AtkHeal2 = { 'attr' : DiceAttr.Heal,
                'base' : TowerAttr.Atk,
                'num' : 2,
                'img' : AttrImage.AtkHeal2, }
    AtkHeal3 = { 'attr' : DiceAttr.Heal,
                'base' : TowerAttr.Atk,
                'num' : 3,
                'img' : AttrImage.AtkHeal3, }
    DefNor1 = { 'attr' : DiceAttr.Nor,
                'base' : TowerAttr.Def,
                'num' : 1,
                'img' : AttrImage.DefNor1,}
    DefNor2 = { 'attr' : DiceAttr.Nor,
                'base' : TowerAttr.Def,
                'num' : 2,
                'img' : AttrImage.DefNor2, }
    DefNor3 = { 'attr' : DiceAttr.Nor,
                'base' : TowerAttr.Def,
                'num' : 3,
                'img' : AttrImage.DefNor3, }
    DefAtk1 = { 'attr' : DiceAttr.Atk,
                'base' : TowerAttr.Def,
                'num' : 1,
                'img' : AttrImage.DefAtk1, }
    DefAtk2 = { 'attr' : DiceAttr.Atk,
                'base' : TowerAttr.Def,
                'num' : 2,
                'img' : AttrImage.DefAtk2, }
    DefAtk3 = { 'attr' : DiceAttr.Atk,
                'base' : TowerAttr.Def,
                'num' : 3,
                'img' : AttrImage.DefAtk3, }
    DefDef1 = { 'attr' : DiceAttr.Def,
                'base' : TowerAttr.Def,
                'num' : 1,
                'img' : AttrImage.DefDef1, }
    DefDef2 = { 'attr' : DiceAttr.Def,
                'base' : TowerAttr.Def,
                'num' : 2,
                'img' : AttrImage.DefDef2, }
    DefDef3 = { 'attr' : DiceAttr.Def,
                'base' : TowerAttr.Def,
                'num' : 3,
                'img' : AttrImage.DefDef3, }
    DefMov1 = { 'attr' : DiceAttr.Mov,
                'base' : TowerAttr.Def,
                'num' : 1,
                'img' : AttrImage.DefMov1, }
    DefMov2 = { 'attr' : DiceAttr.Mov,
                'base' : TowerAttr.Def,
                'num' : 2,
                'img' : AttrImage.DefMov2, }
    DefMov3 = { 'attr' : DiceAttr.Mov,
                'base' : TowerAttr.Def,
                'num' : 3,
                'img' : AttrImage.DefMov3, }
    DefSpc1 = { 'attr' : DiceAttr.Spc,
                'base' : TowerAttr.Def,
                'num' : 1,
                'img' : AttrImage.DefSpc1, }
    DefSpc2 = { 'attr' : DiceAttr.Spc,
                'base' : TowerAttr.Def,
                'num' : 2,
                'img' : AttrImage.DefSpc2, }
    DefSpc3 = { 'attr' : DiceAttr.Spc,
                'base' : TowerAttr.Def,
                'num' : 3,
                'img' : AttrImage.DefSpc3, }
    DefHeal1 = { 'attr' : DiceAttr.Heal,
                'base' : TowerAttr.Def,
                'num' : 1,
                'img' : AttrImage.DefHeal1, }
    DefHeal2 = { 'attr' : DiceAttr.Heal,
                'base' : TowerAttr.Def,
                'num' : 2,
                'img' : AttrImage.DefHeal2, }
    DefHeal3 = { 'attr' : DiceAttr.Heal,
                'base' : TowerAttr.Def,
                'num' : 3,
                'img' : AttrImage.DefHeal3, }
    MovNor1 = { 'attr' : DiceAttr.Nor,
                'base' : TowerAttr.Mov,
                'num' : 1,
                'img' : AttrImage.MovNor1,}
    MovNor2 = { 'attr' : DiceAttr.Nor,
                'base' : TowerAttr.Mov,
                'num' : 2,
                'img' : AttrImage.MovNor2, }
    MovNor3 = { 'attr' : DiceAttr.Nor,
                'base' : TowerAttr.Mov,
                'num' : 3,
                'img' : AttrImage.MovNor3, }
    MovAtk1 = { 'attr' : DiceAttr.Atk,
                'base' : TowerAttr.Mov,
                'num' : 1,
                'img' : AttrImage.MovAtk1, }
    MovAtk2 = { 'attr' : DiceAttr.Atk,
                'base' : TowerAttr.Mov,
                'num' : 2,
                'img' : AttrImage.MovAtk2, }
    MovAtk3 = { 'attr' : DiceAttr.Atk,
                'base' : TowerAttr.Mov,
                'num' : 3,
                'img' : AttrImage.MovAtk3, }
    MovDef1 = { 'attr' : DiceAttr.Def,
                'base' : TowerAttr.Mov,
                'num' : 1,
                'img' : AttrImage.MovDef1, }
    MovDef2 = { 'attr' : DiceAttr.Def,
                'base' : TowerAttr.Mov,
                'num' : 2,
                'img' : AttrImage.MovDef2, }
    MovDef3 = { 'attr' : DiceAttr.Def,
                'base' : TowerAttr.Mov,
                'num' : 3,
                'img' : AttrImage.MovDef3, }
    MovMov1 = { 'attr' : DiceAttr.Mov,
                'base' : TowerAttr.Mov,
                'num' : 1,
                'img' : AttrImage.MovMov1, }
    MovMov2 = { 'attr' : DiceAttr.Mov,
                'base' : TowerAttr.Mov,
                'num' : 2,
                'img' : AttrImage.MovMov2, }
    MovMov3 = { 'attr' : DiceAttr.Mov,
                'base' : TowerAttr.Mov,
                'num' : 3,
                'img' : AttrImage.MovMov3, }
    MovSpc1 = { 'attr' : DiceAttr.Spc,
                'base' : TowerAttr.Mov,
                'num' : 1,
                'img' : AttrImage.MovSpc1, }
    MovSpc2 = { 'attr' : DiceAttr.Spc,
                'base' : TowerAttr.Mov,
                'num' : 2,
                'img' : AttrImage.MovSpc2, }
    MovSpc3 = { 'attr' : DiceAttr.Spc,
                'base' : TowerAttr.Mov,
                'num' : 3,
                'img' : AttrImage.MovSpc3, }
    MovHeal1 = { 'attr' : DiceAttr.Heal,
                'base' : TowerAttr.Mov,
                'num' : 1,
                'img' : AttrImage.MovHeal1, }
    MovHeal2 = { 'attr' : DiceAttr.Heal,
                'base' : TowerAttr.Mov,
                'num' : 2,
                'img' : AttrImage.MovHeal2, }
    MovHeal3 = { 'attr' : DiceAttr.Heal,
                'base' : TowerAttr.Mov,
                'num' : 3,
                'img' : AttrImage.MovHeal3, }
    SpcNor1 = { 'attr' : DiceAttr.Nor,
                'base' : TowerAttr.Spc,
                'num' : 1,
                'img' : AttrImage.SpcNor1,}
    SpcNor2 = { 'attr' : DiceAttr.Nor,
                'base' : TowerAttr.Spc,
                'num' : 2,
                'img' : AttrImage.SpcNor2, }
    SpcNor3 = { 'attr' : DiceAttr.Nor,
                'base' : TowerAttr.Spc,
                'num' : 3,
                'img' : AttrImage.SpcNor3, }
    SpcAtk1 = { 'attr' : DiceAttr.Atk,
                'base' : TowerAttr.Spc,
                'num' : 1,
                'img' : AttrImage.SpcAtk1, }
    SpcAtk2 = { 'attr' : DiceAttr.Atk,
                'base' : TowerAttr.Spc,
                'num' : 2,
                'img' : AttrImage.SpcAtk2, }
    SpcAtk3 = { 'attr' : DiceAttr.Atk,
                'base' : TowerAttr.Spc,
                'num' : 3,
                'img' : AttrImage.SpcAtk3, }
    SpcDef1 = { 'attr' : DiceAttr.Def,
                'base' : TowerAttr.Spc,
                'num' : 1,
                'img' : AttrImage.SpcDef1, }
    SpcDef2 = { 'attr' : DiceAttr.Def,
                'base' : TowerAttr.Spc,
                'num' : 2,
                'img' : AttrImage.SpcDef2, }
    SpcDef3 = { 'attr' : DiceAttr.Def,
                'base' : TowerAttr.Spc,
                'num' : 3,
                'img' : AttrImage.SpcDef3, }
    SpcMov1 = { 'attr' : DiceAttr.Mov,
                'base' : TowerAttr.Spc,
                'num' : 1,
                'img' : AttrImage.SpcMov1, }
    SpcMov2 = { 'attr' : DiceAttr.Mov,
                'base' : TowerAttr.Spc,
                'num' : 2,
                'img' : AttrImage.SpcMov2, }
    SpcMov3 = { 'attr' : DiceAttr.Mov,
                'base' : TowerAttr.Spc,
                'num' : 3,
                'img' : AttrImage.SpcMov3, }
    SpcSpc1 = { 'attr' : DiceAttr.Spc,
                'base' : TowerAttr.Spc,
                'num' : 1,
                'img' : AttrImage.SpcSpc1, }
    SpcSpc2 = { 'attr' : DiceAttr.Spc,
                'base' : TowerAttr.Spc,
                'num' : 2,
                'img' : AttrImage.SpcSpc2, }
    SpcSpc3 = { 'attr' : DiceAttr.Spc,
                'base' : TowerAttr.Spc,
                'num' : 3,
                'img' : AttrImage.SpcSpc3, }
    SpcHeal1 = { 'attr' : DiceAttr.Heal,
                'base' : TowerAttr.Spc,
                'num' : 1,
                'img' : AttrImage.SpcHeal1, }
    SpcHeal2 = { 'attr' : DiceAttr.Heal,
                'base' : TowerAttr.Spc,
                'num' : 2,
                'img' : AttrImage.SpcHeal2, }
    SpcHeal3 = { 'attr' : DiceAttr.Heal,
                'base' : TowerAttr.Spc,
                'num' : 3,
                'img' : AttrImage.SpcHeal3, }
    HealNor1 = { 'attr' : DiceAttr.Nor,
                'base' : TowerAttr.Heal,
                'num' : 1,
                'img' : AttrImage.HealNor1,}
    HealNor2 = { 'attr' : DiceAttr.Nor,
                'base' : TowerAttr.Heal,
                'num' : 2,
                'img' : AttrImage.HealNor2, }
    HealNor3 = { 'attr' : DiceAttr.Nor,
                'base' : TowerAttr.Heal,
                'num' : 3,
                'img' : AttrImage.HealNor3, }
    HealAtk1 = { 'attr' : DiceAttr.Atk,
                'base' : TowerAttr.Heal,
                'num' : 1,
                'img' : AttrImage.HealAtk1, }
    HealAtk2 = { 'attr' : DiceAttr.Atk,
                'base' : TowerAttr.Heal,
                'num' : 2,
                'img' : AttrImage.HealAtk2, }
    HealAtk3 = { 'attr' : DiceAttr.Atk,
                'base' : TowerAttr.Heal,
                'num' : 3,
                'img' : AttrImage.HealAtk3, }
    HealDef1 = { 'attr' : DiceAttr.Def,
                'base' : TowerAttr.Heal,
                'num' : 1,
                'img' : AttrImage.HealDef1, }
    HealDef2 = { 'attr' : DiceAttr.Def,
                'base' : TowerAttr.Heal,
                'num' : 2,
                'img' : AttrImage.HealDef2, }
    HealDef3 = { 'attr' : DiceAttr.Def,
                'base' : TowerAttr.Heal,
                'num' : 3,
                'img' : AttrImage.HealDef3, }
    HealMov1 = { 'attr' : DiceAttr.Mov,
                'base' : TowerAttr.Heal,
                'num' : 1,
                'img' : AttrImage.HealMov1, }
    HealMov2 = { 'attr' : DiceAttr.Mov,
                'base' : TowerAttr.Heal,
                'num' : 2,
                'img' : AttrImage.HealMov2, }
    HealMov3 = { 'attr' : DiceAttr.Mov,
                'base' : TowerAttr.Heal,
                'num' : 3,
                'img' : AttrImage.HealMov3, }
    HealSpc1 = { 'attr' : DiceAttr.Spc,
                'base' : TowerAttr.Heal,
                'num' : 1,
                'img' : AttrImage.HealSpc1, }
    HealSpc2 = { 'attr' : DiceAttr.Spc,
                'base' : TowerAttr.Heal,
                'num' : 2,
                'img' : AttrImage.HealSpc2, }
    HealSpc3 = { 'attr' : DiceAttr.Spc,
                'base' : TowerAttr.Heal,
                'num' : 3,
                'img' : AttrImage.HealSpc3, }
    HealHeal1 = { 'attr' : DiceAttr.Heal,
                'base' : TowerAttr.Heal,
                'num' : 1,
                'img' : AttrImage.HealHeal1, }
    HealHeal2 = { 'attr' : DiceAttr.Heal,
                'base' : TowerAttr.Heal,
                'num' : 2,
                'img' : AttrImage.HealHeal2, }
    HealHeal3 = { 'attr' : DiceAttr.Heal,
                'base' : TowerAttr.Heal,
                'num' : 3,
                'img' : AttrImage.HealHeal3, }
    
class DiceData(Enum):
    #Detail of Dice : ATTR, NUM, BASE
    Nor = { 'info' : [ 
                FaceData.NorNor3,
                FaceData.NorAtk3,
                FaceData.NorDef3,
                FaceData.NorMov2,
                FaceData.NorSpc2,
                FaceData.NorHeal2, ],
            'img' : DiceImage.DiceNor }

    Atk = { 'info' : [ 
                FaceData.AtkAtk3,
                FaceData.AtkAtk3,
                FaceData.NorAtk3,
                FaceData.NorNor2,
                FaceData.DefDef2,
                FaceData.AtkMov2, ],
            'img' : DiceImage.DiceAtk }

    Def = { 'info' : [
                FaceData.DefDef3,
                FaceData.DefDef3,
                FaceData.NorDef3,
                FaceData.NorNor2,
                FaceData.AtkAtk2,
                FaceData.DefHeal2, ],
            'img' : DiceImage.DiceDef }

    Mov = { 'info' : [
                FaceData.MovMov3,
                FaceData.MovMov2,
                FaceData.NorMov2,
                FaceData.NorNor3,
                FaceData.MovAtk2,
                FaceData.NorSpc2, ],
            'img' : DiceImage.DiceMov }

    Spc = { 'info' : [ 
                FaceData.SpcSpc3,
                FaceData.SpcSpc2,
                FaceData.NorSpc2,
                FaceData.NorNor3,
                FaceData.MovMov2,
                FaceData.HealHeal2, ],
            'img' : DiceImage.DiceSpc }

    Heal = { 'info' : [ 
                FaceData.HealHeal2,
                FaceData.DefHeal2,
                FaceData.NorHeal2,
                FaceData.HealNor3,
                FaceData.DefDef3,
                FaceData.AtkAtk3 ],
            'img' : DiceImage.DiceHeal }


class TowerData(Enum):
    Null = { 'max': 1,
             'img' : [ TowerImage.TowerBase ] }
             
    Nor = { 'max' : 5,
            'img': [ 
                TowerImage.TowerBase,
                TowerImage.TowerNor1,
                TowerImage.TowerNor2,
                TowerImage.TowerNor3,
                TowerImage.TowerNor4, ] }

    Atk = { 'max' : 5,
            'img': [ 
                TowerImage.TowerBase,
                TowerImage.TowerAtk1,
                TowerImage.TowerAtk2,
                TowerImage.TowerAtk3,
                TowerImage.TowerAtk4, ] }

    Def = { 'max' : 5,
            'img': [ 
                TowerImage.TowerBase,
                TowerImage.TowerDef1,
                TowerImage.TowerDef2,
                TowerImage.TowerDef3,
                TowerImage.TowerDef4, ] }

    Mov = { 'max' : 5,
            'img': [ 
                TowerImage.TowerBase,
                TowerImage.TowerMov1,
                TowerImage.TowerMov2,
                TowerImage.TowerMov3,
                TowerImage.TowerMov4, ] }

    Spc = { 'max' : 5,
            'img': [ 
                TowerImage.TowerBase,
                TowerImage.TowerSpc1,
                TowerImage.TowerSpc2,
                TowerImage.TowerSpc3,
                TowerImage.TowerSpc4, ] }

    Heal = { 'max' : 5,
             'img': [ 
                TowerImage.TowerBase,
                TowerImage.TowerHeal1,
                TowerImage.TowerHeal2,
                TowerImage.TowerHeal3,
                TowerImage.TowerHeal4, ] }