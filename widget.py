#-*- coding: UTF-8 -*-
import pygame
from pygame.locals import *
from enum import Enum

class PygameWidget:
    def __init__(self, game):
        self.game = game
        self.ready = True
    def isReady(self):
        return self.ready
    def draw(self):
        pass
    def update(self):
        pass

class PygameButton(PygameWidget):
    def __init__(self, game, image, size, position, func, argv=() ):
        super().__init__(game)
        self.size = size        
        self.image = pygame.image.load(image)
        self.pos = position
        self.func = func
        self.argv = argv

    def draw(self):
        if self.game.cursor.isOverRect( self.pos, self.size ) and self.game.cursor.isLeftClick():
            image = pygame.transform.scale( self.image, (int(self.size[0]*1.2), int(self.size[1]*1.2)) )
            pos = ( self.pos[0]-int(self.size[0]*0.1), self.pos[1]-int(self.size[1]*0.1) )
        elif self.game.cursor.isOverRect( self.pos, self.size ):
            image = pygame.transform.scale( self.image, (int(self.size[0]*1.1), int(self.size[1]*1.1)) )
            pos = ( self.pos[0]-int(self.size[0]*0.05), self.pos[1]-int(self.size[1]*0.05) )
        else:
            image = pygame.transform.scale( self.image, self.size )
            pos = self.pos

        screen = pygame.display.get_surface()
        screen.blit(image, pos)

    def update(self):
        if self.game.cursor.isOverRect( self.pos, self.size ) and \
            not self.game.cursor.isLeftClick() and self.game.lastCursor.isLeftClick():
            self.func( *self.argv )

class DicesBoxBar(PygameWidget):
    class BoxMode(Enum):
        prepare  = 1
        dropping = 2
        ready    = 3
    def __init__(self, game):
        super().__init__(game)
        self.boxSize = 10
        self.dices = []
        self.ready = False
        self.mode = self.BoxMode.prepare
        self.frame = 0

    def getDices(self):
        self.dices = []
        for dice in self.game.battle.teamPlayer.dices["box"]:
            image = pygame.transform.scale( dice.getDiceTypeImage().value, (40,40) )
            self.dices.append( image )

    def update(self):
        self.getDices()
        self.boxSize = min(10, len(self.dices))
        if self.mode == self.BoxMode.prepare and self.frame > 100:
            self.frame = 0
            self.mode = self.BoxMode.dropping
        self.frame += 1

    def draw(self):
        screen = pygame.display.get_surface()
        if self.mode == self.BoxMode.prepare:
            pass
        elif self.mode == self.BoxMode.ready:
            for i in range(self.boxSize):
                pos = (400-i*50)
                screen.blit(self.dices[i], (10, pos) ) 
                if self.game.cursor.isOverRect( (10, pos), (40,40) ):                    
                    screen.blit(self.dices[i], (10+45, pos) ) 
        elif self.mode == self.BoxMode.dropping:
            dropDist = 8 * self.frame
            for i in range(self.boxSize):
                image = self.dices[i]
                pos = (400-i*50)
                dist = pos-(-100)
                if dropDist >= dist:
                    dropDist -= dist
                else:
                    pos = dropDist-100
                    dropDist = 0
                    image.convert()
                    image.set_alpha(128)
                screen.blit(image, (10, pos))
            if dropDist > 0:
                self.mode = self.BoxMode.ready
                self.ready = True

class DicesPlayBar(PygameWidget):
    def __init__(self, game):
        super().__init__(game)
        self.getDices()

    def getDices(self):
        self.dices = []
        for dice in self.game.battle.teamPlayer.dices["play"]:
            image = pygame.transform.scale( dice.getDiceTypeImage().value, (60,60) )
            self.dices.append( image )

    def update(self):
        pass

    def draw(self):
        screen = pygame.display.get_surface()
        for i, diceImage in enumerate( self.dices ):
            screen.blit(diceImage, (10+i*70, 520) )