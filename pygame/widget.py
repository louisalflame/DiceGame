#-*- coding: UTF-8 -*-
import pygame
from pygame.locals import *

class PygameButton:
    def __init__(self, image, size, position):
        self.size = size        
        self.image = pygame.transform.scale( pygame.image.load(image), self.size )
        self.pos = position

    def draw(self):
        screen = pygame.display.get_surface()
        screen.blit(self.image, self.pos)

    def update(self):
        pass

        '''
        font = util.font_MsjhBd(80)
        text = font.render(str("按鈕一"), True, pygame.color.Color("white"))
        '''
