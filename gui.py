# coding=UTF-8
import wx
from interface import *

class GameFrame(MainFrame):
	#constructor
	def __init__(self, parent, gameManager):
		#initialize parent class
		MainFrame.__init__(self, parent)

		self.gm = gameManager
		self.gm.setGUI( self )

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
		pass

	def showAttrs(self, attrs):
		self.AttrBox_1.SetValue( str(attrs[0]) )
		self.AttrBox_2.SetValue( str(attrs[1]) )
		self.AttrBox_3.SetValue( str(attrs[2]) )
		self.AttrBox_4.SetValue( str(attrs[3]) )
		self.AttrBox_5.SetValue( str(attrs[4]) )
		self.AttrBox_6.SetValue( str(attrs[5]) )

	def getRadioIndex(self):
		return None

	def showDices(self, battleDices):
		dicesField = battleDices[0]
		dicesPrepare = battleDices[1]
		dicesUsed = battleDices[2]
		self.showDicesPrepare( dicesPrepare )

	def showDicesPrepare(self, dicesPrepare):
		for i in range( int( len(dicesPrepare)/5 ) ):
			sizer = wx.BoxSizer( wx.HORIZONTAL )
			for j in range(5):
				if (i*5+j) >= len(dicesPrepare):
					break
				bitmap = self.getBitmapByPath( u"tmpPanel/base.bmp" )
				diceImage = wx.BitmapButton( self.dicesPanel, wx.ID_ANY, bitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
				diceImage.Bind( wx.EVT_BUTTON, self.checkDicePrepare( str(dicesPrepare[i*5+j]) ) )
				sizer.Add( diceImage, 0, wx.ALL, 5 )
			self.dicesPanelSizer.Add( sizer, 1, wx.EXPAND, 5 )
		self.dicesPanel.SetSizer( self.dicesPanelSizer )
		self.MainSizer.Layout()
		self.Centre( wx.BOTH )

	def getBitmapByPath(self, path):
		image = wx.Image(path, wx.BITMAP_TYPE_BMP)
		image.Rescale(20,20)
		return wx.Bitmap(image)

	def changeImage(self):
		image = wx.Image(u"tmpPanel/def.bmp", wx.BITMAP_TYPE_BMP)
		image.Rescale(20,20) 

		#self.m_bitmap6.SetBitmap( wx.Bitmap(image) )
		diceImageX = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap(image), wx.DefaultPosition, wx.DefaultSize, 0 )
		self.DicePlaySizer.Add( diceImageX , 0, wx.ALL, 5 )
		self.MainSizer.Layout()
		self.Layout()
		#self.DicePlayPanel.Add( self.diceImageX, 0, wx.ALL, 5 )

	def checkDicePrepare(self, dicePrepare):
		def OnClick(event):
			self.showText( str(dicePrepare) )
		return OnClick
