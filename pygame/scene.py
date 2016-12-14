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
        pass
    def draw(self):
        pass
    def end(self):
        pass

class MenuScene(Scene):
    def __init__(self, game, window):
        super().__init__(game, window)

        def startEquip():           
            self.game.startScene( EquipScene(self.game, self.window) )
        def endGame():
            self.game.exit()
        self.widgets.append( PygameButton(r"..\panel\DiceMov3.png", (120,120), (100,100), startEquip ) )
        self.widgets.append( PygameButton(r"..\panel\DiceHeal3.png", (120,120), (100,250), endGame ) )

    def draw(self):
        screen = pygame.display.get_surface()
        screen.fill(pygame.color.Color("black"))
        for widget in self.widgets:
            widget.draw()

    def update(self):
        for widget in self.widgets:
            widget.update()
            
class EquipScene(Scene):
    def __init__(self, game, window):
        super().__init__(game, window)

    def draw(self):
        screen = pygame.display.get_surface()
        screen.fill(pygame.color.Color("brown"))
        for widget in self.widgets:
            widget.draw()

    def update(self):
        for widget in self.widgets:
            widget.update()
