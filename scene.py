#-*- coding: UTF-8 -*-
import pygame
from pygame.locals import *

from widget import PygameButton, DicesBoxBar
import util

class Scene:
    def __init__(self, game, window):
        self.game = game
        self.window = window
        self.widgets = dict()
    def update(self):
        for key, widget in self.widgets.items():
            widget.draw()
    def draw(self):
        for key, widget in self.widgets.items():
            widget.update()
    def remove(self):
        pass

class MenuScene(Scene):
    def __init__(self, game, window):
        super().__init__(game, window)

        self.widgets[ "battle" ] = PygameButton( 
            self.game, r"panel\DiceAtk.png", (120,120), (300,100), 
            self.game.startSceneClass, [battleScene] )
        self.widgets[ "equip" ] = PygameButton( 
            self.game, r"panel\DiceDef.png", (120,120), (300,250), 
            self.game.startSceneClass, [EquipScene] )
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
class battleScene(Scene):
    def __init__(self, game, window):
        super().__init__(game, window)
        
        self.game.startBattle()
        self.mode = 0

    def updateMode(self):
        if self.mode == 0:
            self.widgets[ "back" ] = PygameButton( 
                self.game, r"panel\DiceDef.png", (60,60), (600,400), 
                self.game.backScene )
            self.widgets[ "test" ] = PygameButton( 
                self.game, r"panel\DiceSpc.png", (60,60), (600,500), 
                self.game.test )
        elif self.mode == 1:
            self.widgets[ "dicePackage" ] = DicesBoxBar(
                self.game )
            self.widgets[ "test" ] = PygameButton( 
                self.game, r"panel\DiceSpc2.png", (60,60), (600,500), 
                self.game.test2 )

    def remove(self):
        super().remove()
        self.game.endBattle()

    def draw(self):
        screen = pygame.display.get_surface()
        screen.fill(pygame.color.Color("darkgray"))
        super().draw()

    def update(self):
        super().update()
        self.updateMode()

            
class EquipScene(Scene):
    def __init__(self, game, window):
        super().__init__(game, window)

        self.widgets[ "back" ] = PygameButton( 
            self.game, r"panel\DiceDef.png", (60,60), (30,30), 
            self.game.backScene )

    def draw(self):
        screen = pygame.display.get_surface()
        screen.fill(pygame.color.Color("skyblue"))
        super().draw()

    def update(self):
        super().update()