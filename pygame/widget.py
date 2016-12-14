#-*- coding: UTF-8 -*-
import pygame
from pygame.locals import *
from util import *

class PygameButton:
    def __init__(self, image, size, position, func, argv=() ):
        self.size = size        
        self.image = pygame.image.load(image)
        self.pos = position
        self.func = func
        self.argv = argv

    def draw(self):
        cursor = Cursor( pygame.mouse.get_pos(), pygame.mouse.get_pressed() )
        if cursor.isOverRect( self.pos, self.size ) and cursor.isLeftClick():
            image = pygame.transform.scale( self.image, (int(self.size[0]*1.2), int(self.size[1]*1.2)) )
            pos = ( self.pos[0]-int(self.size[0]*0.1), self.pos[1]-int(self.size[1]*0.1) )
            self.func( *self.argv )
        elif cursor.isOverRect( self.pos, self.size ):
            image = pygame.transform.scale( self.image, (int(self.size[0]*1.1), int(self.size[1]*1.1)) )
            pos = ( self.pos[0]-int(self.size[0]*0.05), self.pos[1]-int(self.size[1]*0.05) )
        else:
            image = pygame.transform.scale( self.image, self.size )
            pos = self.pos

        screen = pygame.display.get_surface()
        screen.blit(image, pos)

    def update(self):
        pass

        '''
        font = util.font_MsjhBd(80)
        text = font.render(str("按鈕一"), True, pygame.color.Color("white"))
        '''
