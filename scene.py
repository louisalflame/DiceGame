#-*- coding: UTF-8 -*-
import pygame
from pygame.locals import *

from widget import *
import util

class Scene:
    def __init__(self, game, window):
        self.game = game
        self.window = window
        self.widgets = []
    def update(self):
        for widget in self.widgets:
            widget.draw()
    def draw(self):
        for widget in self.widgets:
            widget.update()
    def remove(self):
        pass

class MenuScene(Scene):
    def __init__(self, game, window):
        super().__init__(game, window)

        self.widgets.append( 
            PygameButton( self.game, r"panel\DiceAtk3.png", (120,120), (300,100), 
                          self.game.startSceneClass, [battleScene] ) )
        self.widgets.append( 
            PygameButton( self.game, r"panel\DiceSpc3.png", (120,120), (300,250), 
                          self.game.startSceneClass, [EquipScene] ) )
        self.widgets.append( 
            PygameButton( self.game, r"panel\DiceMov3.png", (120,120), (300,400), 
                          self.game.exit ) )

    def draw(self):
        screen = pygame.display.get_surface()
        screen.fill(pygame.color.Color("black"))
        for widget in self.widgets:
            widget.draw()

    def update(self):
        for widget in self.widgets:
            widget.update()

class battleScene(Scene):
    def __init__(self, game, window):
        super().__init__(game, window)
        
        self.widgets.append( 
            PygameButton( self.game, r"panel\DiceDef.png", (60,60), (30,30), 
                          self.game.backScene ) )

    def draw(self):
        screen = pygame.display.get_surface()
        screen.fill(pygame.color.Color("darkgray"))
        super().draw()

    def update(self):
        super().update()

            
class EquipScene(Scene):
    def __init__(self, game, window):
        super().__init__(game, window)

        self.widgets.append( 
            PygameButton( self.game, r"panel\DiceDef.png", (60,60), (30,30), 
                          self.game.backScene ) )

    def draw(self):
        screen = pygame.display.get_surface()
        screen.fill(pygame.color.Color("skyblue"))
        super().draw()

    def update(self):
        super().update()