#-*- coding: UTF-8 -*-
 
import pygame
from pygame.locals import *
import os
from sys import exit

import util
import scene
 
size = (800, 600)
black = (0, 0, 0)
white = (255, 255, 255)
title = "Hello, Pygame!"
chinese_message = "來寫遊戲吧！"
message = str(chinese_message)
 



class WindowManager:
    def __init__(self, size):
        pygame.init()

        screen = pygame.display.set_mode(size, 0, 32)

    def setTitle(self, title):
        pygame.display.set_caption(title)

    def setIcon(self, iconFile):
        icon = pygame.image.load(iconFile)
        icon = pygame.transform.scale( icon, (32,32) )
        pygame.display.set_icon(icon)

    def draw(self):
        font = util.font_MsjhBd(80)
        text = font.render(message, True, white)
     
        x = (size[0]-text.get_width()) / 2
        y = (size[1]-text.get_height()) / 2

        screen = pygame.display.get_surface()
        screen.fill(black)
        screen.blit(text, (x, y))

    def update(self):
        pygame.display.update()


def run():
    window = WindowManager( (800,600) )
    window.setTitle( "來寫遊戲吧！" )
    window.setIcon(r"..\panel\DiceNor2.png") 
 
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
 
        window.draw()
        window.update()
 
if __name__ == "__main__":
    run()