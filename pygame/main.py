#-*- coding: UTF-8 -*-
 
import pygame
from pygame.locals import *
import os
from sys import exit

import util
from scene import *
from window import WindowManager

def run():
    window = WindowManager( (800,600) )
    window.setTitle( "遊戲試作" )
    window.setIcon(r"..\panel\DiceAtk.png")
    window.setScene( MenuScene(window) )
 
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
 
        window.draw()
        window.update()
 
if __name__ == "__main__":
    run()