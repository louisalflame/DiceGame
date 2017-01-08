#-*- coding: UTF-8 -*-
import pygame
from pygame.locals import *
from enum import Enum

from image import DiceImage, AttrImage, TowerImage
from data import DiceAttr
from util import *

class PygameWidget:
    def __init__(self, game):
        self.game = game
        self.ready = True
        self.visible = True
        self.exist = True
    def show(self):
        self.visible = True
    def hide(self):
        self.visible = False
    def toggle(self):
        self.visible = not self.visible
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
        #not draw if not visible, half alpha if not ready
        if not self.exist or not self.visible:
            return
        elif not self.game.currentScene.isReady():
            image = pygame.transform.scale( imageTransparent(self.image, 0.5), self.size )
            pos = self.pos            

        #draw 1.1 bigger when over, 1.2 bigger when pressed
        elif self.game.cursor.isPressDown( self.pos, self.size ):
            image, pos = imageScaleFromCenter( self.image, self.pos, self.size, 1.2 )
        elif self.game.cursor.isOverRect( self.pos, self.size ):
            image, pos = imageScaleFromCenter( self.image, self.pos, self.size, 1.1 )
        else:
            image = pygame.transform.scale( self.image, self.size )
            pos = self.pos

        screen = pygame.display.get_surface()
        screen.blit(image, pos)

    def update(self):
        if not self.exist:
            return
        if self.game.cursor.isClick( self.pos, self.size ) and \
            self.game.currentScene.isReady() :
            self.func( *self.argv )

class DicesBox(PygameWidget):
    maxBoxSize  = 10
    boxTop      = -100
    boxBottom   = 400
    boxLeft     = 10
    infoTop     = 5
    infoLeft    = 60
    infoHeight  = 50
    infoWidth   = 50
    infoInterval = 30
    infoSize    = (50,50)
    imgWidth    = 40
    imgHeight   = 40
    imgSize     = (40,40)
    imgInterval = 10
    detailBorder = 2
    dropSpeed   = 150
    detailSpeed = 10
    prepareTime = 5
    class BoxMode(Enum):
        prepare  = 1
        dropping = 2
        ready    = 3

    def __init__(self, game):
        super().__init__(game)
        self.boxSize = 10
        self.boxNum = 0
        self.usedNum = 0
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
        #draw dices dropping from top
        elif self.mode == self.BoxMode.dropping:
            self.updateDroppingDices()
        #draw dice details if cursor over
        elif self.mode == self.BoxMode.ready:
            self.updateReadyDices()

        self.frame += 1

    def draw(self):
        screen = pygame.display.get_surface()
        self.drawBoxInfo()
        if self.mode == self.BoxMode.ready:
            for image, pos in self.detailImages:
                screen.blit(image, pos)
        for image, pos in self.diceImages:
            screen.blit(image, pos)

    def resetDices(self):
        self.dices = self.game.battle.teamPlayer.dices.getBoxList()
        self.boxNum = len(self.dices)
        self.usedNum = len(self.game.battle.teamPlayer.dices.getUsedList())
        self.boxSize = min(self.maxBoxSize, self.boxNum)
        self.diceImages = []
        self.detailImages = []

    def updateReadyDices(self):
        for i in range(self.boxSize):
            image = self.dices[i].getDiceTypeImageWithSize(self.imgSize)
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
        if self.game.cursor.isNewMoveIn( (self.boxLeft, pos), self.imgSize ):
            self.frame = 0

        images = [ face.getFaceAttrImageWithSize(self.imgSize) for face in self.dices[i].faces ]
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
            image = self.dices[i].getDiceTypeImageWithSize(self.imgSize)
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

    def drawBoxInfo(self):
        screen = pygame.display.get_surface()
        image = pygame.transform.scale( DiceImage.DiceBox.value, self.infoSize )
        screen.blit(image, (self.infoLeft, self.infoTop))
        pygame.draw.rect( screen, pygame.color.Color("black"), 
            (self.infoLeft, self.infoTop+self.infoHeight+2, 
            self.infoWidth, self.infoInterval-4), 0)
        text = imageNumInBlock(self, self.boxNum, self.infoWidth, self.infoHeight)
        screen.blit( text, 
            (self.infoLeft + int(self.infoWidth*0.9) - text.get_width(), 
            self.infoTop+self.infoHeight) )
        image = pygame.transform.scale( DiceImage.DiceUsed.value, self.infoSize )
        screen.blit(image, (self.infoLeft, self.infoTop+self.infoHeight+self.infoInterval))
        pygame.draw.rect( screen, pygame.color.Color("black"), 
            (self.infoLeft, self.infoTop+self.infoHeight*2+self.infoInterval+2, 
            self.infoWidth, self.infoInterval-4), 0)
        text = imageNumInBlock(self, self.usedNum, self.infoWidth, self.infoHeight)
        screen.blit( text, 
            (self.infoLeft + int(self.infoWidth*0.9) - text.get_width(), 
            self.infoTop+self.infoHeight*2+self.infoInterval) )


class DicesPlayBox(PygameWidget):
    boxLeft      = 10
    boxTop       = 450
    playBoxTop   = 520
    imgWidth     = 60
    imgHeight    = 60
    imgSize      = (60,60)
    imgBorder    = 15
    detailHeight = 40
    detailWidth  = 40
    detailSize   = (40,40)
    detailTop    = 470
    detailBorder = 2
    detailSpeed  = 8
    def __init__(self, game):
        super().__init__(game)
        self.diceImages = []
        self.detailImages = []
        self.frame = 0

    def update(self):
        self.diceImages = []
        self.detailImages = []
        self.getDicesBase()
        self.getDicesPlay()
        if self.game.battle.stage == self.game.battle.BattleMode.MovThrow:
            self.getDicesDetails()
            self.frame += 1


    def draw(self):
        screen = pygame.display.get_surface()
        for image, pos in self.detailImages:
            screen.blit(image, pos)
        for image, pos in self.diceImages:
            if self.game.cursor.isPressDown(pos, self.imgSize):
                image ,pos = imageScaleFromCenter(image, pos, self.imgSize, 1.2)
            elif self.game.cursor.isOverRect(pos, self.imgSize):
                image ,pos = imageScaleFromCenter(image, pos, self.imgSize, 1.1)
            else:
                image ,pos = imageScaleFromCenter(image, pos, self.imgSize, 1)
            screen.blit(image, pos)

    def getDicesBase(self):
        for i, dice in enumerate(self.game.battle.teamPlayer.dices.getBaseList()):
            pos = (self.boxLeft+i*(self.imgBorder+self.imgWidth), self.boxTop)
            if self.game.cursor.isClick( pos, self.imgSize ) and \
                self.game.currentScene.isReady() and not dice.isIdle():
                self.game.battle.teamPlayer.diceBaseTurnPlay(i)
            else:
                image = dice.getFace().getTowerAttrImage()
                self.diceImages.append( (image, pos) )

    def getDicesPlay(self):
        for i, dice in enumerate(self.game.battle.teamPlayer.dices.getPlayList()):
            pos = (self.boxLeft+i*(self.imgBorder+self.imgWidth), self.playBoxTop)
            if self.game.cursor.isClick( pos, self.imgSize ) and \
                self.game.currentScene.isReady() and not dice.isIdle():
                self.game.battle.teamPlayer.dicePlayTurnBase(i)
            else:
                image = dice.getDiceTypeImage() if dice.isIdle() else \
                        dice.getFace().getFaceAttrImage()
                self.diceImages.append( (image, pos) )

    def getDicesDetails(self):
        def countPosX(self, i):
            return self.boxLeft+i*(self.imgBorder+self.imgWidth)
        def detailReadyPos(self, i, j):
            return countPosX(self, i)+(self.detailWidth+self.detailBorder)*j
        def detailRunningPos(self, i, j, detailDist):
            return countPosX(self, i)+detailDist-self.detailWidth+self.detailBorder*j
        def detailStartPos(self, detailDist):
            return self.detailTop+self.detailWidth-detailDist

        for i, dice in enumerate(self.game.battle.teamPlayer.dices.getPlayList()):
            pos = (countPosX(self, i), self.playBoxTop)

            if self.game.cursor.isOverRect( pos, self.imgSize ):
                #first over, reset the detail progress
                if self.game.cursor.isNewMoveIn( pos, self.imgSize ):
                    self.frame = 0

                images = [ face.getFaceAttrImageWithSize(self.detailSize) for face in dice.faces ]
                detailDist = self.frame * self.detailSpeed
                for j in range(6):
                    if detailDist > (j+1)*self.detailWidth:
                        self.detailImages.insert( 0, ( images[j],  (detailReadyPos(self, i, j), self.detailTop) ) )
                    elif j == 0 and detailDist < self.detailWidth:
                        percent =  0.5*detailDist/self.detailWidth
                        self.detailImages.insert( 0, ( imageTransparent(images[j], percent), 
                                                       (countPosX(self, i), detailStartPos(self, detailDist)) ) )
                    elif detailDist > j*self.detailWidth:
                        percent =  0.5*(detailDist - j*self.detailWidth)/self.detailWidth
                        self.detailImages.insert( 0, ( imageTransparent(images[j], percent), 
                                                       (detailRunningPos(self, i, j, detailDist), self.detailTop) ) )




class TeamInfoBox(PygameWidget):
    boxTop    = 460
    boxLeft   = 500
    imgTop    = 510
    imgWidth  = 48
    imgHeight = 48
    imgSize   = (48,48)
    imgBorder = 2
    attrOrder = [
        DiceAttr.Nor,
        DiceAttr.Atk,
        DiceAttr.Def,
        DiceAttr.Mov,
        DiceAttr.Spc,
        DiceAttr.Heal,
    ]
    def __init__(self, game):
        super().__init__(game)
        self.numFont = pygame.font.SysFont("impact", 24)
        self.attrs = DiceAttr.getNewAttrsDict()
        self.towers = []

    def update(self):
        self.resetAttr()

    def draw(self):
        screen = pygame.display.get_surface()
        for i, tower in enumerate(self.towers):
            screen.blit( pygame.transform.scale(tower, self.imgSize),
                         (self.countPos(i), self.boxTop) )
        for i, attr in enumerate(self.attrOrder):
            screen.blit( pygame.transform.scale(attr.value.value.copy(), self.imgSize), 
                         (self.countPos(i), self.imgTop) )
            pygame.draw.rect( screen, pygame.color.Color("black"), 
                (self.countPos(i), self.imgTop+self.imgHeight+self.imgBorder, 
                 self.imgWidth, self.imgHeight*0.6), 0)

            text = imageNumInBlock(self, self.attrs[attr], self.imgWidth, self.imgHeight) 
            textPos = self.countPos(i) + int(self.imgWidth*0.9) - text.get_width()
            screen.blit( text, (textPos, self.imgTop+self.imgHeight) )

    def resetAttr(self):
        self.attrs = self.game.battle.teamPlayer.attr.getAttrs()
        self.towers = self.game.battle.teamPlayer.tower.getTowersImage()

    def countPos(self, i):
        return self.boxLeft+i*(self.imgBorder+self.imgWidth)





