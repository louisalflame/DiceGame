#-*- coding: UTF-8 -*-
import pygame
from pygame.locals import *

from widget import *
import util

class Scene:
    def __init__(self, window):
        self.window = window
    def update(self):
        pass
    def draw(self):
        pass
    def end(self):
        pass

class MenuScene(Scene):
    def __init__(self, window):
        super().__init__(window)

        self.widgets = []
        self.widgets.append( PygameButton(r"..\panel\DiceMov3.png", (120,120), (100,100)) )
        self.widgets.append( PygameButton(r"..\panel\DiceHeal3.png", (120,120), (100,250)) )
        self.widgets.append( PygameButton(r"..\panel\DiceDef3.png", (120,120), (100,400)) )

    def draw(self):
        screen = pygame.display.get_surface()
        screen.fill(pygame.color.Color("black"))
        for widget in self.widgets:
            widget.draw()

    def update(self):
        for widget in self.widgets:
            widget.update()