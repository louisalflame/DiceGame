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
 
def run():
    pygame.init()
 
    screen = pygame.display.set_mode(size, 0, 32)
    pygame.display.set_caption(title)
    icon = pygame.image.load(r"C:\Users\user\Desktop\DiceGame\panel\AttrAtk.png")
    icon = pygame.transform.scale( icon, (32,32) )
    pygame.display.set_icon(icon)
 
    font = util.fontMsjhBd(80)
    text = font.render(message, True, white)
 
    x = (size[0]-text.get_width()) / 2
    y = (size[1]-text.get_height()) / 2
 
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
 
        screen.fill(black)
        screen.blit(text, (x, y))
 
        pygame.display.update()
 
if __name__ == "__main__":
    run()