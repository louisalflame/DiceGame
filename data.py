#-*- coding: UTF-8 -*-
from enum import Enum
from attr import *
from image import DiceImage, AttrImage


class FaceData(Enum):
    NorNor1 = {
        'attr' : DiceAttr.Nor,
        'base' : TowerAttr.Nor,
        'num' : 1,
        'img' : AttrImage.NorNor1,
    }
    NorNor2 = {
        'attr' : DiceAttr.Nor,
        'base' : TowerAttr.Nor,
        'num' : 2,
        'img' : AttrImage.NorNor2,
    }
    NorNor3 = {
        'attr' : DiceAttr.Nor,
        'base' : TowerAttr.Nor,
        'num' : 3,
        'img' : AttrImage.NorNor3,
    }
    NorAtk1 = {
        'attr' : DiceAttr.Atk,
        'base' : TowerAttr.Nor,
        'num' : 1,
        'img' : AttrImage.NorAtk1,
    }
    NorAtk2 = {
        'attr' : DiceAttr.Atk,
        'base' : TowerAttr.Nor,
        'num' : 2,
        'img' : AttrImage.NorAtk2,
    }
    NorAtk3 = {
        'attr' : DiceAttr.Atk,
        'base' : TowerAttr.Nor,
        'num' : 3,
        'img' : AttrImage.NorAtk3,
    }
    NorDef1 = {
        'attr' : DiceAttr.Def,
        'base' : TowerAttr.Nor,
        'num' : 1,
        'img' : AttrImage.NorDef1,
    }
    NorDef2 = {
        'attr' : DiceAttr.Def,
        'base' : TowerAttr.Nor,
        'num' : 2,
        'img' : AttrImage.NorDef2,
    }
    NorDef3 = {
        'attr' : DiceAttr.Def,
        'base' : TowerAttr.Nor,
        'num' : 3,
        'img' : AttrImage.NorDef3,
    }
    NorMov1 = {
        'attr' : DiceAttr.Mov,
        'base' : TowerAttr.Nor,
        'num' : 1,
        'img' : AttrImage.NorMov1,
    }
    NorMov2 = {
        'attr' : DiceAttr.Mov,
        'base' : TowerAttr.Nor,
        'num' : 2,
        'img' : AttrImage.NorMov2,
    }
    NorMov3 = {
        'attr' : DiceAttr.Mov,
        'base' : TowerAttr.Nor,
        'num' : 3,
        'img' : AttrImage.NorMov3,
    }
    NorSpc1 = {
        'attr' : DiceAttr.Spc,
        'base' : TowerAttr.Nor,
        'num' : 1,
        'img' : AttrImage.NorSpc1,
    }
    NorSpc2 = {
        'attr' : DiceAttr.Spc,
        'base' : TowerAttr.Nor,
        'num' : 2,
        'img' : AttrImage.NorSpc2,
    }
    NorSpc3 = {
        'attr' : DiceAttr.Spc,
        'base' : TowerAttr.Nor,
        'num' : 3,
        'img' : AttrImage.NorSpc3,
    }
    NorHeal1 = {
        'attr' : DiceAttr.Heal,
        'base' : TowerAttr.Nor,
        'num' : 1,
        'img' : AttrImage.NorHeal1,
    }
    NorHeal2 = {
        'attr' : DiceAttr.Heal,
        'base' : TowerAttr.Nor,
        'num' : 2,
        'img' : AttrImage.NorHeal2,
    }
    NorHeal3 = {
        'attr' : DiceAttr.Heal,
        'base' : TowerAttr.Nor,
        'num' : 3,
        'img' : AttrImage.NorHeal3,
    }
    
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
                FaceData.NorAtk3,
                FaceData.NorAtk3,
                FaceData.NorAtk3,
                FaceData.NorNor2,
                FaceData.NorDef2,
                FaceData.NorMov2, ],
            'img' : DiceImage.DiceAtk }

    Def = { 'info' : [
                FaceData.NorDef3,
                FaceData.NorDef3,
                FaceData.NorDef3,
                FaceData.NorNor2,
                FaceData.NorAtk2,
                FaceData.NorHeal2, ],
            'img' : DiceImage.DiceDef }

    Mov = { 'info' : [
                FaceData.NorMov3,
                FaceData.NorMov2,
                FaceData.NorMov2,
                FaceData.NorNor3,
                FaceData.NorAtk2,
                FaceData.NorSpc2, ],
            'img' : DiceImage.DiceMov }

    Spc = { 'info' : [ 
                FaceData.NorSpc3,
                FaceData.NorSpc2,
                FaceData.NorSpc2,
                FaceData.NorNor3,
                FaceData.NorMov2,
                FaceData.NorHeal2, ],
            'img' : DiceImage.DiceSpc }

    Heal = { 'info' : [ 
                FaceData.NorHeal2,
                FaceData.NorHeal2,
                FaceData.NorHeal2,
                FaceData.NorNor3,
                FaceData.NorDef3,
                FaceData.NorAtk3 ],
            'img' : DiceImage.DiceHeal }

    
