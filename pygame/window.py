#-*- coding: UTF-8 -*-
import pygame
from pygame.locals import *

class WindowManager:
    def __init__(self, size):
        self.size = size
        pygame.init()
        pygame.display.set_mode(self.size, 0, 32)

    def setScene(self, scene):
        self.scene = scene

    def setTitle(self, title):
        pygame.display.set_caption(title)

    def setIcon(self, iconFile):
        icon = pygame.image.load(iconFile)
        icon = pygame.transform.scale( icon, (32,32) )
        pygame.display.set_icon(icon)

    def draw(self):
        self.scene.draw()

    def update(self):
        self.scene.update()
        pygame.display.flip()
