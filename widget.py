#-*- coding: UTF-8 -*-
import pygame
from pygame.locals import *
from enum import Enum

from image import AttrImage
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

class DicesBox(PygameWidget):
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
    detailSpeed = 10
    prepareTime = 20
    class BoxMode(Enum):
        prepare  = 1
        dropping = 2
        ready    = 3

    def __init__(self, game):
        super().__init__(game)
        self.boxSize = 10
        self.dices = []
        self.diceImages = []
        self.detailImages = []
        self.ready = False
        self.mode = self.BoxMode.prepare
        self.frame = 0

    def update(self):
        self.resetDices()

        if self.mode == self.BoxMode.prepare and self.frame > self.prepareTime:
            self.mode = self.BoxMode.dropping
            self.frame = 0
        #draw dice details if cursor over
        elif self.mode == self.BoxMode.ready:
            self.updateReadyDices()
        #draw dices dropping from top
        elif self.mode == self.BoxMode.dropping:
            self.updateDroppingDices()

        self.frame += 1

    def draw(self):
        screen = pygame.display.get_surface()
        if self.mode == self.BoxMode.ready:
            for image, pos in self.detailImages:
                screen.blit(image, pos)
        for image, pos in self.diceImages:
            screen.blit(image, pos)

    def resetDices(self):
        self.dices = []
        self.diceImages = []
        self.detailImages = []
        for dice in self.game.battle.teamPlayer.dices["box"]:
            self.dices.append( dice.clone() )
        self.boxSize = min( self.maxBoxSize, len(self.dices))

    def updateReadyDices(self):
        for i in range(self.boxSize):
            image = self.getDiceTypeImage(self.dices[i])
            pos = self.countDicePos(i)
            self.diceImages.append( (image, (self.boxLeft, pos)) )
            if self.game.cursor.isOverRect( (self.boxLeft, pos), self.imgSize ):
                self.updateDiceDetailShowing(i, pos)

    def updateDiceDetailShowing(self, i, pos):
        def detailReadyPos(self, j):
            return self.boxLeft+self.imgInterval+self.imgWidth*(j+1)+self.detailBorder*j
        def detailRunningPos(self, j, detailDist):
            return self.boxLeft+self.imgInterval+detailDist+self.detailBorder*j

        #first over, reset the detail progress
        if not self.game.lastCursor.isOverRect( (self.boxLeft, pos), self.imgSize ):
            self.frame = 0

        images = self.getDiceAttrImages(self.dices[i])   
        detailDist = self.frame * self.detailSpeed
        for j in range(6):
            if detailDist > (j+1)*self.imgWidth:
                self.detailImages.insert( 0, ( images[j],  (detailReadyPos(self, j), pos) ) )
            elif detailDist > j*self.imgWidth:
                percent =  0.5*(detailDist - j*self.imgWidth)/self.imgWidth
                self.detailImages.insert( 0, ( imageTransparent(images[j], percent), 
                                               (detailRunningPos(self, j, detailDist), pos) ) )

    def updateDroppingDices(self):
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
            self.diceImages.append( (image, (self.boxLeft, pos) ) )
        if dropDist > 0:
            self.mode = self.BoxMode.ready
            self.ready = True
            self.frame = 0

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


class DicesPlayBox(PygameWidget):
    boxLeft   = 10
    boxTop    = 450
    imgWidth  = 60
    imgHeight = 60
    imgSize   = (60,60)
    imgBorder = 15
    def __init__(self, game):
        super().__init__(game)
        self.dices = []
        self.diceImages = []

    def update(self):
        self.getDices()

    def draw(self):
        screen = pygame.display.get_surface()
        for image, pos in self.diceImages:
            screen.blit(image, pos)

    def getDices(self):
        self.dices = []
        self.diceImages = []
        for i, dice in enumerate(self.game.battle.teamPlayer.dices["play"]):
            if dice.isIdle():
                image = dice.getDiceTypeImage().copy()
            else:
                image = dice.getFace().getFaceAttrImage().copy()
            self.diceImages.append( ( pygame.transform.scale(image, self.imgSize), 
                (self.boxLeft+i*(self.imgBorder+self.imgWidth), self.boxTop) ) )


class TeamInfoBox(PygameWidget):
    boxTop    = 400
    boxLeft   = 500
    imgTop    = 500
    imgWidth  = 48
    imgHeight = 48
    imgSize   = (48,48)
    imgBorder = 2
    def __init__(self, game):
        super().__init__(game)
        self.attrs = [
            { "name": "Nor", "img": AttrImage.Nor, 'num': 0 },
            { "name": "Atk", "img": AttrImage.Atk, 'num': 0 },
            { "name": "Def", "img": AttrImage.Def, 'num': 0 },
            { "name": "Mov", "img": AttrImage.Mov, 'num': 0 },
            { "name": "Spc", "img": AttrImage.Spc, 'num': 0 },
            { "name": "Heal", "img": AttrImage.Heal, 'num': 0 },
        ]

    def update(self):
        self.resetAttr()

    def draw(self):
        def countPos(self, i):
            return self.boxLeft+i*(self.imgBorder+self.imgWidth)
        screen = pygame.display.get_surface()
        for i, attr in enumerate(self.attrs):
            screen.blit( pygame.transform.scale(attr['img'].value, self.imgSize), 
                         (countPos(self, i), self.imgTop) )
            pygame.draw.rect(screen, pygame.color.Color("black"), 
                (countPos(self, i), self.imgTop+self.imgHeight+self.imgBorder, 
                 self.imgWidth, self.imgHeight*0.6), 0)

            font = pygame.font.SysFont("comicsansms", 20)
            text = font.render( str(attr['num']), True, pygame.color.Color("white"))
            text = pygame.transform.scale(text, (text.get_width(),int(48*0.6)))
            screen.blit( text, (countPos(self, i+0.8)-text.get_width(), 
                                self.imgTop+self.imgHeight) )

    def resetAttr(self):
        for attr in self.attrs:
            attr['num'] = self.game.battle.teamPlayer.attr[ attr['name'] ]



