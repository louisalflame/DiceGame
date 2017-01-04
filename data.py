#-*- coding: UTF-8 -*-
from enum import Enum
from image import DiceImage, AttrImage, TowerImage

class DiceAttr(Enum):
    Nor  = AttrImage.Nor
    Atk  = AttrImage.Atk
    Def  = AttrImage.Def
    Mov  = AttrImage.Mov
    Spc  = AttrImage.Spc
    Heal = AttrImage.Heal

    def getAttrs():
        return [
            DiceAttr.Nor,
            DiceAttr.Atk,
            DiceAttr.Def,
            DiceAttr.Mov,
            DiceAttr.Spc,
            DiceAttr.Heal,
        ]
    def getNewAttrsDict():
        return {
            DiceAttr.Nor : 0,
            DiceAttr.Atk : 0,
            DiceAttr.Def : 0,
            DiceAttr.Mov : 0,
            DiceAttr.Spc : 0,
            DiceAttr.Heal : 0,
        }

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
                'tower' : DiceAttr.Nor,
                'num' : 1,
                'img' : AttrImage.NorNor1,
                'base' : TowerImage.NorTower, }
    NorNor2 = { 'attr' : DiceAttr.Nor,
                'tower' : DiceAttr.Nor, 
                'num' : 2,
                'img' : AttrImage.NorNor2,
                'base' : TowerImage.NorTower, }
    NorNor3 = { 'attr' : DiceAttr.Nor,
                'tower' : DiceAttr.Nor,
                'num' : 3,
                'img' : AttrImage.NorNor3,
                'base' : TowerImage.NorTower, }
    NorAtk1 = { 'attr' : DiceAttr.Atk,
                'tower' : DiceAttr.Nor,
                'num' : 1,
                'img' : AttrImage.NorAtk1,
                'base' : TowerImage.NorTowerBase, }
    NorAtk2 = { 'attr' : DiceAttr.Atk,
                'tower' : DiceAttr.Nor,
                'num' : 2,
                'img' : AttrImage.NorAtk2,
                'base' : TowerImage.NorTowerBase, }
    NorAtk3 = { 'attr' : DiceAttr.Atk,
                'tower' : DiceAttr.Nor,
                'num' : 3,
                'img' : AttrImage.NorAtk3,
                'base' : TowerImage.NorTowerBase, }
    NorDef1 = { 'attr' : DiceAttr.Def,
                'tower' : DiceAttr.Nor,
                'num' : 1,
                'img' : AttrImage.NorDef1,
                'base' : TowerImage.NorTowerBase, }
    NorDef2 = { 'attr' : DiceAttr.Def,
                'tower' : DiceAttr.Nor,
                'num' : 2,
                'img' : AttrImage.NorDef2,
                'base' : TowerImage.NorTowerBase, }
    NorDef3 = { 'attr' : DiceAttr.Def,
                'tower' : DiceAttr.Nor,
                'num' : 3,
                'img' : AttrImage.NorDef3,
                'base' : TowerImage.NorTowerBase, }
    NorMov1 = { 'attr' : DiceAttr.Mov,
                'tower' : DiceAttr.Nor,
                'num' : 1,
                'img' : AttrImage.NorMov1,
                'base' : TowerImage.NorTowerBase, }
    NorMov2 = { 'attr' : DiceAttr.Mov,
                'tower' : DiceAttr.Nor,
                'num' : 2,
                'img' : AttrImage.NorMov2,
                'base' : TowerImage.NorTowerBase, }
    NorMov3 = { 'attr' : DiceAttr.Mov,
                'tower' : DiceAttr.Nor,
                'num' : 3,
                'img' : AttrImage.NorMov3,
                'base' : TowerImage.NorTowerBase, }
    NorSpc1 = { 'attr' : DiceAttr.Spc,
                'tower' : DiceAttr.Nor,
                'num' : 1,
                'img' : AttrImage.NorSpc1,
                'base' : TowerImage.NorTowerBase, }
    NorSpc2 = { 'attr' : DiceAttr.Spc,
                'tower' : DiceAttr.Nor,
                'num' : 2,
                'img' : AttrImage.NorSpc2,
                'base' : TowerImage.NorTowerBase, }
    NorSpc3 = { 'attr' : DiceAttr.Spc,
                'tower' : DiceAttr.Nor,
                'num' : 3,
                'img' : AttrImage.NorSpc3,
                'base' : TowerImage.NorTowerBase, }
    NorHeal1 = { 'attr' : DiceAttr.Heal,
                'tower' : DiceAttr.Nor,
                'num' : 1,
                'img' : AttrImage.NorHeal1,
                'base' : TowerImage.NorTowerBase, }
    NorHeal2 = { 'attr' : DiceAttr.Heal,
                'tower' : DiceAttr.Nor,
                'num' : 2,
                'img' : AttrImage.NorHeal2,
                'base' : TowerImage.NorTowerBase, }
    NorHeal3 = { 'attr' : DiceAttr.Heal,
                'tower' : DiceAttr.Nor,
                'num' : 3,
                'img' : AttrImage.NorHeal3,
                'base' : TowerImage.NorTowerBase, }
    AtkNor1 = { 'attr' : DiceAttr.Nor,
                'tower' : DiceAttr.Atk,
                'num' : 1,
                'img' : AttrImage.AtkNor1,
                'base' : TowerImage.AtkTowerBase, }
    AtkNor2 = { 'attr' : DiceAttr.Nor,
                'tower' : DiceAttr.Atk, 
                'num' : 2,
                'img' : AttrImage.AtkNor2,
                'base' : TowerImage.AtkTowerBase, }
    AtkNor3 = { 'attr' : DiceAttr.Nor,
                'tower' : DiceAttr.Atk,
                'num' : 3,
                'img' : AttrImage.AtkNor3,
                'base' : TowerImage.AtkTowerBase, }
    AtkAtk1 = { 'attr' : DiceAttr.Atk,
                'tower' : DiceAttr.Atk,
                'num' : 1,
                'img' : AttrImage.AtkAtk1,
                'base' : TowerImage.AtkTower, }
    AtkAtk2 = { 'attr' : DiceAttr.Atk,
                'tower' : DiceAttr.Atk,
                'num' : 2,
                'img' : AttrImage.AtkAtk2,
                'base' : TowerImage.AtkTower, }
    AtkAtk3 = { 'attr' : DiceAttr.Atk,
                'tower' : DiceAttr.Atk,
                'num' : 3,
                'img' : AttrImage.AtkAtk3,
                'base' : TowerImage.AtkTower, }
    AtkDef1 = { 'attr' : DiceAttr.Def,
                'tower' : DiceAttr.Atk,
                'num' : 1,
                'img' : AttrImage.AtkDef1,
                'base' : TowerImage.AtkTowerBase, }
    AtkDef2 = { 'attr' : DiceAttr.Def,
                'tower' : DiceAttr.Atk,
                'num' : 2,
                'img' : AttrImage.AtkDef2,
                'base' : TowerImage.AtkTowerBase, }
    AtkDef3 = { 'attr' : DiceAttr.Def,
                'tower' : DiceAttr.Atk,
                'num' : 3,
                'img' : AttrImage.AtkDef3,
                'base' : TowerImage.AtkTowerBase, }
    AtkMov1 = { 'attr' : DiceAttr.Mov,
                'tower' : DiceAttr.Atk,
                'num' : 1,
                'img' : AttrImage.AtkMov1,
                'base' : TowerImage.AtkTowerBase, }
    AtkMov2 = { 'attr' : DiceAttr.Mov,
                'tower' : DiceAttr.Atk,
                'num' : 2,
                'img' : AttrImage.AtkMov2,
                'base' : TowerImage.AtkTowerBase, }
    AtkMov3 = { 'attr' : DiceAttr.Mov,
                'tower' : DiceAttr.Atk,
                'num' : 3,
                'img' : AttrImage.AtkMov3,
                'base' : TowerImage.AtkTowerBase, }
    AtkSpc1 = { 'attr' : DiceAttr.Spc,
                'tower' : DiceAttr.Atk,
                'num' : 1,
                'img' : AttrImage.AtkSpc1,
                'base' : TowerImage.AtkTowerBase, }
    AtkSpc2 = { 'attr' : DiceAttr.Spc,
                'tower' : DiceAttr.Atk,
                'num' : 2,
                'img' : AttrImage.AtkSpc2,
                'base' : TowerImage.AtkTowerBase, }
    AtkSpc3 = { 'attr' : DiceAttr.Spc,
                'tower' : DiceAttr.Atk,
                'num' : 3,
                'img' : AttrImage.AtkSpc3,
                'base' : TowerImage.AtkTowerBase, }
    AtkHeal1 = { 'attr' : DiceAttr.Heal,
                'tower' : DiceAttr.Atk,
                'num' : 1,
                'img' : AttrImage.AtkHeal1,
                'base' : TowerImage.AtkTowerBase, }
    AtkHeal2 = { 'attr' : DiceAttr.Heal,
                'tower' : DiceAttr.Atk,
                'num' : 2,
                'img' : AttrImage.AtkHeal2,
                'base' : TowerImage.AtkTowerBase, }
    AtkHeal3 = { 'attr' : DiceAttr.Heal,
                'tower' : DiceAttr.Atk,
                'num' : 3,
                'img' : AttrImage.AtkHeal3,
                'base' : TowerImage.AtkTowerBase, }
    DefNor1 = { 'attr' : DiceAttr.Nor,
                'tower' : DiceAttr.Def,
                'num' : 1,
                'img' : AttrImage.DefNor1,
                'base' : TowerImage.DefTowerBase, }
    DefNor2 = { 'attr' : DiceAttr.Nor,
                'tower' : DiceAttr.Def,
                'num' : 2,
                'img' : AttrImage.DefNor2,
                'base' : TowerImage.DefTowerBase, }
    DefNor3 = { 'attr' : DiceAttr.Nor,
                'tower' : DiceAttr.Def,
                'num' : 3,
                'img' : AttrImage.DefNor3,
                'base' : TowerImage.DefTowerBase, }
    DefAtk1 = { 'attr' : DiceAttr.Atk,
                'tower' : DiceAttr.Def,
                'num' : 1,
                'img' : AttrImage.DefAtk1,
                'base' : TowerImage.DefTowerBase, }
    DefAtk2 = { 'attr' : DiceAttr.Atk,
                'tower' : DiceAttr.Def,
                'num' : 2,
                'img' : AttrImage.DefAtk2,
                'base' : TowerImage.DefTowerBase, }
    DefAtk3 = { 'attr' : DiceAttr.Atk,
                'tower' : DiceAttr.Def,
                'num' : 3,
                'img' : AttrImage.DefAtk3,
                'base' : TowerImage.DefTowerBase, }
    DefDef1 = { 'attr' : DiceAttr.Def,
                'tower' : DiceAttr.Def,
                'num' : 1,
                'img' : AttrImage.DefDef1,
                'base' : TowerImage.DefTower, }
    DefDef2 = { 'attr' : DiceAttr.Def,
                'tower' : DiceAttr.Def,
                'num' : 2,
                'img' : AttrImage.DefDef2,
                'base' : TowerImage.DefTower, }
    DefDef3 = { 'attr' : DiceAttr.Def,
                'tower' : DiceAttr.Def,
                'num' : 3,
                'img' : AttrImage.DefDef3,
                'base' : TowerImage.DefTower, }
    DefMov1 = { 'attr' : DiceAttr.Mov,
                'tower' : DiceAttr.Def,
                'num' : 1,
                'img' : AttrImage.DefMov1,
                'base' : TowerImage.DefTowerBase, }
    DefMov2 = { 'attr' : DiceAttr.Mov,
                'tower' : DiceAttr.Def,
                'num' : 2,
                'img' : AttrImage.DefMov2,
                'base' : TowerImage.DefTowerBase, }
    DefMov3 = { 'attr' : DiceAttr.Mov,
                'tower' : DiceAttr.Def,
                'num' : 3,
                'img' : AttrImage.DefMov3,
                'base' : TowerImage.DefTowerBase, }
    DefSpc1 = { 'attr' : DiceAttr.Spc,
                'tower' : DiceAttr.Def,
                'num' : 1,
                'img' : AttrImage.DefSpc1,
                'base' : TowerImage.DefTowerBase, }
    DefSpc2 = { 'attr' : DiceAttr.Spc,
                'tower' : DiceAttr.Def,
                'num' : 2,
                'img' : AttrImage.DefSpc2,
                'base' : TowerImage.DefTowerBase, }
    DefSpc3 = { 'attr' : DiceAttr.Spc,
                'tower' : DiceAttr.Def,
                'num' : 3,
                'img' : AttrImage.DefSpc3,
                'base' : TowerImage.DefTowerBase, }
    DefHeal1 = { 'attr' : DiceAttr.Heal,
                'tower' : DiceAttr.Def,
                'num' : 1,
                'img' : AttrImage.DefHeal1,
                'base' : TowerImage.DefTowerBase, }
    DefHeal2 = { 'attr' : DiceAttr.Heal,
                'tower' : DiceAttr.Def,
                'num' : 2,
                'img' : AttrImage.DefHeal2,
                'base' : TowerImage.DefTowerBase, }
    DefHeal3 = { 'attr' : DiceAttr.Heal,
                'tower' : DiceAttr.Def,
                'num' : 3,
                'img' : AttrImage.DefHeal3,
                'base' : TowerImage.DefTowerBase, }
    MovNor1 = { 'attr' : DiceAttr.Nor,
                'tower' : DiceAttr.Mov,
                'num' : 1,
                'img' : AttrImage.MovNor1,
                'base' : TowerImage.MovTowerBase, }
    MovNor2 = { 'attr' : DiceAttr.Nor,
                'tower' : DiceAttr.Mov,
                'num' : 2,
                'img' : AttrImage.MovNor2,
                'base' : TowerImage.MovTowerBase, }
    MovNor3 = { 'attr' : DiceAttr.Nor,
                'tower' : DiceAttr.Mov,
                'num' : 3,
                'img' : AttrImage.MovNor3,
                'base' : TowerImage.MovTowerBase, }
    MovAtk1 = { 'attr' : DiceAttr.Atk,
                'tower' : DiceAttr.Mov,
                'num' : 1,
                'img' : AttrImage.MovAtk1,
                'base' : TowerImage.MovTowerBase, }
    MovAtk2 = { 'attr' : DiceAttr.Atk,
                'tower' : DiceAttr.Mov,
                'num' : 2,
                'img' : AttrImage.MovAtk2,
                'base' : TowerImage.MovTowerBase, }
    MovAtk3 = { 'attr' : DiceAttr.Atk,
                'tower' : DiceAttr.Mov,
                'num' : 3,
                'img' : AttrImage.MovAtk3,
                'base' : TowerImage.MovTowerBase, }
    MovDef1 = { 'attr' : DiceAttr.Def,
                'tower' : DiceAttr.Mov,
                'num' : 1,
                'img' : AttrImage.MovDef1,
                'base' : TowerImage.MovTowerBase, }
    MovDef2 = { 'attr' : DiceAttr.Def,
                'tower' : DiceAttr.Mov,
                'num' : 2,
                'img' : AttrImage.MovDef2,
                'base' : TowerImage.MovTowerBase, }
    MovDef3 = { 'attr' : DiceAttr.Def,
                'tower' : DiceAttr.Mov,
                'num' : 3,
                'img' : AttrImage.MovDef3,
                'base' : TowerImage.MovTowerBase, }
    MovMov1 = { 'attr' : DiceAttr.Mov,
                'tower' : DiceAttr.Mov,
                'num' : 1,
                'img' : AttrImage.MovMov1,
                'base' : TowerImage.MovTower, }
    MovMov2 = { 'attr' : DiceAttr.Mov,
                'tower' : DiceAttr.Mov,
                'num' : 2,
                'img' : AttrImage.MovMov2,
                'base' : TowerImage.MovTower, }
    MovMov3 = { 'attr' : DiceAttr.Mov,
                'tower' : DiceAttr.Mov,
                'num' : 3,
                'img' : AttrImage.MovMov3,
                'base' : TowerImage.MovTower, }
    MovSpc1 = { 'attr' : DiceAttr.Spc,
                'tower' : DiceAttr.Mov,
                'num' : 1,
                'img' : AttrImage.MovSpc1,
                'base' : TowerImage.MovTowerBase, }
    MovSpc2 = { 'attr' : DiceAttr.Spc,
                'tower' : DiceAttr.Mov,
                'num' : 2,
                'img' : AttrImage.MovSpc2,
                'base' : TowerImage.MovTowerBase, }
    MovSpc3 = { 'attr' : DiceAttr.Spc,
                'tower' : DiceAttr.Mov,
                'num' : 3,
                'img' : AttrImage.MovSpc3,
                'base' : TowerImage.MovTowerBase, }
    MovHeal1 = { 'attr' : DiceAttr.Heal,
                'tower' : DiceAttr.Mov,
                'num' : 1,
                'img' : AttrImage.MovHeal1,
                'base' : TowerImage.MovTowerBase, }
    MovHeal2 = { 'attr' : DiceAttr.Heal,
                'tower' : DiceAttr.Mov,
                'num' : 2,
                'img' : AttrImage.MovHeal2,
                'base' : TowerImage.MovTowerBase, }
    MovHeal3 = { 'attr' : DiceAttr.Heal,
                'tower' : DiceAttr.Mov,
                'num' : 3,
                'img' : AttrImage.MovHeal3,
                'base' : TowerImage.MovTowerBase, }
    SpcNor1 = { 'attr' : DiceAttr.Nor,
                'tower' : DiceAttr.Spc,
                'num' : 1,
                'img' : AttrImage.SpcNor1,
                'base' : TowerImage.SpcTowerBase, }
    SpcNor2 = { 'attr' : DiceAttr.Nor,
                'tower' : DiceAttr.Spc,
                'num' : 2,
                'img' : AttrImage.SpcNor2,
                'base' : TowerImage.SpcTowerBase, }
    SpcNor3 = { 'attr' : DiceAttr.Nor,
                'tower' : DiceAttr.Spc,
                'num' : 3,
                'img' : AttrImage.SpcNor3,
                'base' : TowerImage.SpcTowerBase, }
    SpcAtk1 = { 'attr' : DiceAttr.Atk,
                'tower' : DiceAttr.Spc,
                'num' : 1,
                'img' : AttrImage.SpcAtk1,
                'base' : TowerImage.SpcTowerBase, }
    SpcAtk2 = { 'attr' : DiceAttr.Atk,
                'tower' : DiceAttr.Spc,
                'num' : 2,
                'img' : AttrImage.SpcAtk2,
                'base' : TowerImage.SpcTowerBase, }
    SpcAtk3 = { 'attr' : DiceAttr.Atk,
                'tower' : DiceAttr.Spc,
                'num' : 3,
                'img' : AttrImage.SpcAtk3,
                'base' : TowerImage.SpcTowerBase, }
    SpcDef1 = { 'attr' : DiceAttr.Def,
                'tower' : DiceAttr.Spc,
                'num' : 1,
                'img' : AttrImage.SpcDef1,
                'base' : TowerImage.SpcTowerBase, }
    SpcDef2 = { 'attr' : DiceAttr.Def,
                'tower' : DiceAttr.Spc,
                'num' : 2,
                'img' : AttrImage.SpcDef2,
                'base' : TowerImage.SpcTowerBase, }
    SpcDef3 = { 'attr' : DiceAttr.Def,
                'tower' : DiceAttr.Spc,
                'num' : 3,
                'img' : AttrImage.SpcDef3,
                'base' : TowerImage.SpcTowerBase, }
    SpcMov1 = { 'attr' : DiceAttr.Mov,
                'tower' : DiceAttr.Spc,
                'num' : 1,
                'img' : AttrImage.SpcMov1,
                'base' : TowerImage.SpcTowerBase, }
    SpcMov2 = { 'attr' : DiceAttr.Mov,
                'tower' : DiceAttr.Spc,
                'num' : 2,
                'img' : AttrImage.SpcMov2,
                'base' : TowerImage.SpcTowerBase, }
    SpcMov3 = { 'attr' : DiceAttr.Mov,
                'tower' : DiceAttr.Spc,
                'num' : 3,
                'img' : AttrImage.SpcMov3,
                'base' : TowerImage.SpcTowerBase, }
    SpcSpc1 = { 'attr' : DiceAttr.Spc,
                'tower' : DiceAttr.Spc,
                'num' : 1,
                'img' : AttrImage.SpcSpc1,
                'base' : TowerImage.SpcTower, }
    SpcSpc2 = { 'attr' : DiceAttr.Spc,
                'tower' : DiceAttr.Spc,
                'num' : 2,
                'img' : AttrImage.SpcSpc2,
                'base' : TowerImage.SpcTower, }
    SpcSpc3 = { 'attr' : DiceAttr.Spc,
                'tower' : DiceAttr.Spc,
                'num' : 3,
                'img' : AttrImage.SpcSpc3,
                'base' : TowerImage.SpcTower, }
    SpcHeal1 = { 'attr' : DiceAttr.Heal,
                'tower' : DiceAttr.Spc,
                'num' : 1,
                'img' : AttrImage.SpcHeal1,
                'base' : TowerImage.SpcTowerBase, }
    SpcHeal2 = { 'attr' : DiceAttr.Heal,
                'tower' : DiceAttr.Spc,
                'num' : 2,
                'img' : AttrImage.SpcHeal2,
                'base' : TowerImage.SpcTowerBase, }
    SpcHeal3 = { 'attr' : DiceAttr.Heal,
                'tower' : DiceAttr.Spc,
                'num' : 3,
                'img' : AttrImage.SpcHeal3,
                'base' : TowerImage.SpcTowerBase, }
    HealNor1 = { 'attr' : DiceAttr.Nor,
                'tower' : DiceAttr.Heal,
                'num' : 1,
                'img' : AttrImage.HealNor1,
                'base' : TowerImage.HealTowerBase, }
    HealNor2 = { 'attr' : DiceAttr.Nor,
                'tower' : DiceAttr.Heal,
                'num' : 2,
                'img' : AttrImage.HealNor2,
                'base' : TowerImage.HealTowerBase, }
    HealNor3 = { 'attr' : DiceAttr.Nor,
                'tower' : DiceAttr.Heal,
                'num' : 3,
                'img' : AttrImage.HealNor3,
                'base' : TowerImage.HealTowerBase, }
    HealAtk1 = { 'attr' : DiceAttr.Atk,
                'tower' : DiceAttr.Heal,
                'num' : 1,
                'img' : AttrImage.HealAtk1,
                'base' : TowerImage.HealTowerBase, }
    HealAtk2 = { 'attr' : DiceAttr.Atk,
                'tower' : DiceAttr.Heal,
                'num' : 2,
                'img' : AttrImage.HealAtk2,
                'base' : TowerImage.HealTowerBase, }
    HealAtk3 = { 'attr' : DiceAttr.Atk,
                'tower' : DiceAttr.Heal,
                'num' : 3,
                'img' : AttrImage.HealAtk3,
                'base' : TowerImage.HealTowerBase, }
    HealDef1 = { 'attr' : DiceAttr.Def,
                'tower' : DiceAttr.Heal,
                'num' : 1,
                'img' : AttrImage.HealDef1,
                'base' : TowerImage.HealTowerBase, }
    HealDef2 = { 'attr' : DiceAttr.Def,
                'tower' : DiceAttr.Heal,
                'num' : 2,
                'img' : AttrImage.HealDef2,
                'base' : TowerImage.HealTowerBase, }
    HealDef3 = { 'attr' : DiceAttr.Def,
                'tower' : DiceAttr.Heal,
                'num' : 3,
                'img' : AttrImage.HealDef3,
                'base' : TowerImage.HealTowerBase, }
    HealMov1 = { 'attr' : DiceAttr.Mov,
                'tower' : DiceAttr.Heal,
                'num' : 1,
                'img' : AttrImage.HealMov1,
                'base' : TowerImage.HealTowerBase, }
    HealMov2 = { 'attr' : DiceAttr.Mov,
                'tower' : DiceAttr.Heal,
                'num' : 2,
                'img' : AttrImage.HealMov2,
                'base' : TowerImage.HealTowerBase, }
    HealMov3 = { 'attr' : DiceAttr.Mov,
                'tower' : DiceAttr.Heal,
                'num' : 3,
                'img' : AttrImage.HealMov3,
                'base' : TowerImage.HealTowerBase, }
    HealSpc1 = { 'attr' : DiceAttr.Spc,
                'tower' : DiceAttr.Heal,
                'num' : 1,
                'img' : AttrImage.HealSpc1,
                'base' : TowerImage.HealTowerBase, }
    HealSpc2 = { 'attr' : DiceAttr.Spc,
                'tower' : DiceAttr.Heal,
                'num' : 2,
                'img' : AttrImage.HealSpc2,
                'base' : TowerImage.HealTowerBase, }
    HealSpc3 = { 'attr' : DiceAttr.Spc,
                'tower' : DiceAttr.Heal,
                'num' : 3,
                'img' : AttrImage.HealSpc3,
                'base' : TowerImage.HealTowerBase, }
    HealHeal1 = { 'attr' : DiceAttr.Heal,
                'tower' : DiceAttr.Heal,
                'num' : 1,
                'img' : AttrImage.HealHeal1,
                'base' : TowerImage.HealTower, }
    HealHeal2 = { 'attr' : DiceAttr.Heal,
                'tower' : DiceAttr.Heal,
                'num' : 2,
                'img' : AttrImage.HealHeal2,
                'base' : TowerImage.HealTower, }
    HealHeal3 = { 'attr' : DiceAttr.Heal,
                'tower' : DiceAttr.Heal,
                'num' : 3,
                'img' : AttrImage.HealHeal3,
                'base' : TowerImage.HealTower, }
    
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