#-*- coding: UTF-8 -*-
 
import pygame
from pygame.locals import *
import os, sys

from manager import GameManager
from scene import *
from window import WindowManager
import util

def run():
    game = GameManager()
    window = WindowManager( game, (800,600) )
    window.setTitle( "遊戲試作" )
    window.setIcon(r"..\panel\DiceAtk.png")
    game.setWindow( window )
    game.startScene( MenuScene(game, window) )
 
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

        window.draw()
        window.update()
 
run()