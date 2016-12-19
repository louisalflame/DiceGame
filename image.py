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