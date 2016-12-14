#-*- coding: UTF-8 -*-
import sys

class GameManager:
    def __init__(self):
        self.sceneStack = []

    def setWindow(self, window):
        self.window = window

    def startScene(self, scene):
        self.sceneStack.append( scene )
        self.window.setScene( scene )

    def exit(self):
        sys.exit()
