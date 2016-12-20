#-*- coding: UTF-8 -*-
 
import pygame
from pygame.locals import *
import os, sys

from manager import GameManager
from scene import MenuScene
from window import WindowManager
import util

def run():
    pygame.init()
    game = GameManager()
    window = WindowManager( game, (800,600) )
    window.setTitle( "遊戲試作" )
    window.setIcon(r"panel\DiceAtk.png")
    game.setWindow( window )
    game.setNextScene( MenuScene )
 
    game.loopGame()
 
run()