#-*- coding: UTF-8 -*-
from enum import Enum
import pygame
from pygame.locals import *

class DiceImage(Enum):
    DiceNor = pygame.image.load( r"panel\DiceNor.png" )
    DiceAtk = pygame.image.load( r"panel\DiceAtk.png" )
    DiceDef = pygame.image.load( r"panel\DiceDef.png" )
    DiceMov = pygame.image.load( r"panel\DiceMov.png" )
    DiceSpc = pygame.image.load( r"panel\DiceSpc.png" )
    DiceHeal = pygame.image.load( r"panel\DiceHeal.png" )

class AttrImage(Enum):
    NorNor1 = pygame.image.load( r"panel\NorBaseNor1.png" )
    NorNor2 = pygame.image.load( r"panel\NorBaseNor2.png" )
    NorNor3 = pygame.image.load( r"panel\NorBaseNor3.png" )
    NorAtk1 = pygame.image.load( r"panel\NorBaseAtk1.png" )
    NorAtk2 = pygame.image.load( r"panel\NorBaseAtk2.png" )
    NorAtk3 = pygame.image.load( r"panel\NorBaseAtk3.png" )
    NorDef1 = pygame.image.load( r"panel\NorBaseDef1.png" )
    NorDef2 = pygame.image.load( r"panel\NorBaseDef2.png" )
    NorDef3 = pygame.image.load( r"panel\NorBaseDef3.png" )
    NorMov1 = pygame.image.load( r"panel\NorBaseMov1.png" )
    NorMov2 = pygame.image.load( r"panel\NorBaseMov2.png" )
    NorMov3 = pygame.image.load( r"panel\NorBaseMov3.png" )
    NorSpc1 = pygame.image.load( r"panel\NorBaseSpc1.png" )
    NorSpc2 = pygame.image.load( r"panel\NorBaseSpc2.png" )
    NorSpc3 = pygame.image.load( r"panel\NorBaseSpc3.png" )
    NorHeal1 = pygame.image.load( r"panel\NorBaseHeal1.png" )
    NorHeal2 = pygame.image.load( r"panel\NorBaseHeal2.png" )
    NorHeal3 = pygame.image.load( r"panel\NorBaseHeal3.png" )