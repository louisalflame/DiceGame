# coding=UTF-8
from gameManager import *
from gui import *

def play():
	game = GameManager()
	app = wx.App(False)
	frame = GameFrame(None, game )
	frame.Show()

	game.initGui()
	app.MainLoop()

if __name__ == "__main__":
	play()