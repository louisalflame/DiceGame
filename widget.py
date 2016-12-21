#-*- coding: UTF-8 -*-
import pygame
from pygame.locals import *
from enum import Enum
from util import *

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
        #draw 1.1 bigger when over, 1.2 bigger when pressed
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
    maxBoxSize  = 10
    boxTop      = -100
    boxBottom   = 400
    boxLeft     = 10
    imgWidth    = 40
    imgHeight   = 40
    imgSize     = (40,40)
    imgInterval = 10
    detailBorder = 2
    dropSpeed   = 100
    detailSpeed = 20
    prepareTime = 20
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
            self.dices.append( dice.clone() )

    def update(self):
        self.getDices()
        self.boxSize = min( self.maxBoxSize, len(self.dices))
        if self.mode == self.BoxMode.prepare and self.frame > self.prepareTime:
            self.frame = 0
            self.mode = self.BoxMode.dropping
        self.frame += 1

    def draw(self):
        if self.mode == self.BoxMode.prepare:
            pass
        #draw dice details if cursor over
        elif self.mode == self.BoxMode.ready:
            self.drawReadyDices()
        #draw dices dropping from top
        elif self.mode == self.BoxMode.dropping:
            self.drawDroppingDices()

    def drawReadyDices(self):
        screen = pygame.display.get_surface()
        for i in range(self.boxSize):
            image = self.getDiceTypeImage(self.dices[i])
            pos = self.countDicePos(i)
            screen.blit(image, (self.boxLeft, pos) )
            self.drawDiceDetailShowing(i, pos)

    def drawDiceDetailShowing(self, i, pos):
        if not self.game.cursor.isOverRect( (self.boxLeft, pos), self.imgSize ):
            return
        def detailReadyPos(self, j):
            return self.boxLeft+self.imgInterval+self.imgWidth*(j+1)+self.detailBorder*j
        def detailRunningPos(self, j, detailDist):
            return self.boxLeft+self.imgInterval+detailDist+self.detailBorder*j

        screen = pygame.display.get_surface()
        #first over, reset the detail progress
        if not self.game.lastCursor.isOverRect( (self.boxLeft, pos), self.imgSize ) or \
            self.frame < 0:
            self.frame = 0
        else:
            images = self.getDiceAttrImages(self.dices[i])   
            detailDist = self.frame * self.detailSpeed
            for j in range(6):
                j = 5-j
                if detailDist > (j+1)*self.imgWidth:             
                    screen.blit( images[j],  (detailReadyPos(self, j), pos) )
                elif detailDist > j*self.imgWidth:
                    percent =  0.5*(detailDist - j*self.imgWidth)/self.imgWidth
                    screen.blit( imageTransparent(images[j], percent), 
                        (detailRunningPos(self, j, detailDist), pos) )

    def drawDroppingDices(self):
        screen = pygame.display.get_surface()
        dropDist = self.dropSpeed * self.frame
        for i in range(self.boxSize):
            image = self.getDiceTypeImage(self.dices[i])
            pos = self.countDicePos(i)
            if dropDist >= pos-self.boxTop:
                dropDist -= pos-self.boxTop
            else:
                pos = dropDist+self.boxTop
                dropDist = 0
                image = imageTransparent(image, 0.5)
            screen.blit(image, (self.boxLeft, pos))
        if dropDist > 0:
            self.mode = self.BoxMode.ready
            self.ready = True
            self.frame = -10

    def countDicePos(self, i):
        return self.boxBottom-i*(self.imgHeight+self.imgInterval)

    def getDiceTypeImage(self, dice):
        image = dice.getDiceTypeImage().copy()
        return pygame.transform.scale( image, self.imgSize )

    def getDiceAttrImages(self, dice):
        images = []
        for face in dice.faces:
            image = face.getFaceAttrImage().copy()
            images.append( pygame.transform.scale( image, self.imgSize ) )
        return images

class DicesPlayBar(PygameWidget):
    def __init__(self, game):
        super().__init__(game)
        self.getDices()

    def getDices(self):
        self.dices = []
        for dice in self.game.battle.teamPlayer.dices["play"]:
            image = pygame.transform.scale( dice.getDiceTypeImage(), (60,60) )
            self.dices.append( image )

    def update(self):
        pass

    def draw(self):
        screen = pygame.display.get_surface()
        for i, diceImage in enumerate( self.dices ):
            screen.blit(diceImage, (10+i*70, 520) )