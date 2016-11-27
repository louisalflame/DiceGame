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
		self.gm.updateStatus()

	def showText(self, text):
		self.OutputField.AppendText( text+'\n' )

	def clearText(self):
		self.OutputField.SetValue( str("") )

	def cleanDicePlay(self):
		self.DicePlaySizer.Clear(True)
		self.DiceInfoSizer.Clear(True)

	def showAttrs(self, attrs):
		self.AttrNorNum.SetValue( str(attrs[0]) )
		self.AttrAtkNum.SetValue( str(attrs[1]) )
		self.AttrDefNum.SetValue( str(attrs[2]) )
		self.AttrMovNum.SetValue( str(attrs[3]) )
		self.AttrSpcNum.SetValue( str(attrs[4]) )
		self.AttrHealNum.SetValue( str(attrs[5]) )

	def showDices(self, battleDices):
		dicesField = battleDices[0]
		dicesPrepare = battleDices[1]
		dicesUsed = battleDices[2]
		self.showDicesPrepare( dicesPrepare )
		self.showDicesField( dicesField )

	def showDicesPrepare(self, dicesPrepare):
		self.DicesPanelSizer.Clear(True)
		
		for i in range( int( len(dicesPrepare)/5 ) ):
			sizer = wx.BoxSizer( wx.HORIZONTAL )
			for j in range(5):
				if (i*5+j) >= len(dicesPrepare):
					break
				dice = dicesPrepare[i*5+j]
				diceImage = wx.BitmapButton( self.DicesPanel, wx.ID_ANY, 
					wx.Bitmap( wx.Image(u"panel/"+dice.getDiceTypeImageSrc(), wx.BITMAP_TYPE_PNG).Rescale(30,30) ),
					wx.DefaultPosition, wx.DefaultSize, 0 )
				diceImage.Bind( wx.EVT_BUTTON, self.checkDiceInfo(dice) )
				sizer.Add( diceImage, 0, wx.BOTTOM, 2 )
			self.DicesPanelSizer.Add( sizer, 0, 0, 5 )

		self.DicesPanel.SetSizer( self.DicesPanelSizer )
		self.MainSizer.Layout()

	def showDicesField(self, dicesField):
		self.DicePlaySizer.Clear(True)

		diceSizer = wx.BoxSizer( wx.HORIZONTAL )
		PanelSizer = wx.BoxSizer( wx.HORIZONTAL )
		for dice in dicesField:
			panel = dice.getPanel()
			diceImage = wx.BitmapButton( self.DicePlayPanel, wx.ID_ANY, 
				wx.Bitmap( wx.Image(u"panel/"+panel.getAttrImageSrc(), wx.BITMAP_TYPE_PNG).Rescale(40,40) ),
				wx.DefaultPosition, wx.DefaultSize, 0 )
			diceImage.Bind( wx.EVT_BUTTON, self.checkDiceInfo( dice ) )
			diceSizer.Add( diceImage, 0, wx.BOTTOM, 2 )

			panelImage = wx.BitmapButton( self.DicePlayPanel, wx.ID_ANY, 
				wx.Bitmap( wx.Image(u"panel/"+panel.getBaseImageSrc(), wx.BITMAP_TYPE_PNG).Rescale(40,40) ),
				wx.DefaultPosition, wx.DefaultSize, 0 )
			panelImage.Bind( wx.EVT_BUTTON, self.pickPanel( dice ) )
			PanelSizer.Add( panelImage, 0, wx.BOTTOM, 2 )

		self.DicePlaySizer.Add( diceSizer, 0, 0, 5 )
		self.DicePlaySizer.Add( PanelSizer, 0, 0, 5 )
		self.DicePlaySizer.Layout()

	def getBitmapByPath(self, path, height=20, width=20):
		image = wx.Image(path, wx.BITMAP_TYPE_PNG)
		image.Rescale(height, width)
		return wx.Bitmap(image)

	def checkDiceInfo(self, dice):
		def OnClick(event):
			self.DiceInfoSizer.Clear(True)
			sizer = wx.BoxSizer( wx.HORIZONTAL )
			for panel in dice.getAllPanels():
				if not dice.isIdle() and panel.getPanelID() == dice.getNum():
					image = wx.Image( u"panel/"+panel.getAttrImageSrc(), wx.BITMAP_TYPE_PNG).Rescale(50,50)
				else:
					image = wx.Image( u"panel/"+panel.getAttrImageSrc(), wx.BITMAP_TYPE_PNG).Rescale(30,30)

				panelImage = wx.StaticBitmap( self.DiceInfoPanel, wx.ID_ANY, 
					wx.Bitmap(image), wx.DefaultPosition, wx.DefaultSize, 0 )
				sizer.Add( panelImage, 0, wx.ALL, 2 )

			self.DiceInfoSizer.Add( sizer, 0, 0, 5 )
			self.DiceInfoSizer.Layout()
		return OnClick

	def pickPanel(self, dice):
		def OnClick(event):
			self.gm.pickPanel( dice.getPanel() )
		return OnClick




	def changeToPlayScene(self):
		self.initDicePlayFrame()
