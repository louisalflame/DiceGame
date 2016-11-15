# coding=UTF-8
import wx
from noname import *
from game import *

class GameFrame(MainFrame):
	#constructor
	def __init__(self, parent, gameManager):
		#initialize parent class
		MainFrame.__init__(self, parent)

		self.gm = gameManager
		self.gm.setInterface( self )

	def textSubmit(self, event):
		string = self.inputField.GetValue()
		self.inputField.SetValue( str("") )
		self.gm.updateStatus( string )

	def showText(self, text):
		self.outputField.AppendText( text+'\n' )

	def clearText(self):
		self.inputField.SetValue( str("") )
		self.outputField.SetValue( str("") )

	def clearDiceRadio(self):
		self.diceRadio_1.SetValue(False)
		self.diceRadio_2.SetValue(False)
		self.diceRadio_3.SetValue(False)
		self.diceRadio_4.SetValue(False)
		self.diceRadio_5.SetValue(False)

	def showAttrs(self, attrs):
		self.AttrBox_1.SetValue( str(attrs[0]) )
		self.AttrBox_2.SetValue( str(attrs[1]) )
		self.AttrBox_3.SetValue( str(attrs[2]) )
		self.AttrBox_4.SetValue( str(attrs[3]) )
		self.AttrBox_5.SetValue( str(attrs[4]) )
		self.AttrBox_6.SetValue( str(attrs[5]) )

	def getRadioIndex(self):
		if self.diceRadio_1.GetValue():
			return 1
		elif self.diceRadio_2.GetValue():
			return 2
		elif self.diceRadio_3.GetValue():
			return 3
		elif self.diceRadio_4.GetValue():
			return 4
		elif self.diceRadio_5.GetValue():
			return 5
		return None

	def changeImage(self):
		image = wx.Image(u"tmpPanel/def.bmp", wx.BITMAP_TYPE_BMP)
		image.Rescale(20,20) 
		self.diceImage1.SetBitmap( wx.BitmapFromImage(image) )





def play():
	game = GameManager()
	app = wx.App(False)
	frame = GameFrame(None, game )
	frame.Show()

	game.init()

	app.MainLoop()

