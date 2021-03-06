#-*- coding: UTF-8 -*-
import pygame
from pygame.locals import *
 
from widget import PygameButton, DicesBox, DicesPlayBox, TeamInfoBox
import util
 
class Scene:
    def __init__(self, game, window):
        self.game = game
        self.window = window
        self.ready = True
        self.widgets = dict()
    def isReady(self):
        return self.ready
    def draw(self):
        for key, widget in self.widgets.items():
            widget.draw()
    def update(self):
        for key, widget in self.widgets.items():
            widget.update()
    def construct(self):
        pass
    def remove(self):
        pass
 
class MenuScene(Scene):
    def __init__(self, game, window):
        super().__init__(game, window)
 
    def construct(self):
        self.widgets[ "battle" ] = PygameButton( 
            self.game, r"panel\DiceAtk.png", (120,120), (300,100), 
            self.game.setNextScene, [BattleScene] )
        self.widgets[ "equip" ] = PygameButton( 
            self.game, r"panel\DiceDef.png", (120,120), (300,250), 
            self.game.setNextScene, [EquipScene] )
        self.widgets[ "exit" ] = PygameButton( 
            self.game, r"panel\DiceHeal.png", (120,120), (300,400), 
            self.game.exit )
 
    def draw(self):
        screen = pygame.display.get_surface()
        screen.fill(pygame.color.Color("black"))
        super().draw()
 
    def update(self):
        super().update()
 
#========================
# Battle Scene
#========================
class BattleScene(Scene):
    def __init__(self, game, window):
        super().__init__(game, window)
        self.mode = 0
        self.nextMode = 0
         
    def construct(self):
        self.game.startBattle(self)
        self.drawGUI()
        self.game.battle.updateStage()
 
    def remove(self):
        super().remove()
        self.game.endBattle()
 
    def draw(self):
        screen = pygame.display.get_surface()
        screen.fill(pygame.color.Color("darkgray"))
        super().draw()
 
    def update(self):
        super().update()
        self.updateReady()


    def drawGUI(self):
        self.widgets[ "back" ] = PygameButton( 
            self.game, r"panel\DiceDef.png", (40,40), (750,10), 
            self.game.setNextScene, [MenuScene] )
        self.widgets[ "updateStage" ] = PygameButton( 
            self.game, r"panel\DiceSpc.png", (40,40), (700,10), 
            self.game.battle.updateStage )
        self.widgets[ "diceBox" ] = DicesBox( self.game )
        self.widgets[ "teamInfo" ] = TeamInfoBox( self.game )
        self.widgets[ "dicePlay" ] = DicesPlayBox( self.game )

    def updateReady(self):
        for key, widget in self.widgets.items():
            if not widget.ready:
                self.ready = False
                break
        else:
            self.ready = True
 
             
class EquipScene(Scene):
    def __init__(self, game, window):
        super().__init__(game, window)
 
    def construct(self):
        self.widgets[ "back" ] = PygameButton( 
            self.game, r"panel\DiceDef.png", (60,60), (30,30), 
            self.game.setNextScene, [MenuScene] )
 
    def draw(self):
        screen = pygame.display.get_surface()
        screen.fill(pygame.color.Color("skyblue"))
        super().draw()
 
    def update(self):
        super().update()