# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		self.MainSizer = wx.BoxSizer( wx.VERTICAL )
				
		self.initLabel()
		self.initCenterSizer()
		self.initDicePlay()
		self.initAttrTower()
		self.initSubmit()		
		
		self.SetSizer( self.MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.submit.Bind( wx.EVT_BUTTON, self.textSubmit )

	def initLabel(self):
		self.label = wx.StaticText( self, wx.ID_ANY, u"                                 Dice Game --prototype--", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		self.label.Wrap( -1 )
		self.label.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 76, 90, 90, False, wx.EmptyString ) )		
		self.MainSizer.Add( self.label, 0, wx.TOP|wx.BOTTOM, 5 )

	def initCenterSizer(self):
		self.CenterSizer = wx.BoxSizer( wx.HORIZONTAL )

		self.outputField = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,180 ), wx.TE_MULTILINE|wx.TE_READONLY )
		self.CenterSizer.Add( self.outputField, 0, wx.ALL, 5 )
		
		self.DicesSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.DiceSizer_1 = wx.BoxSizer( wx.HORIZONTAL )		
		self.diceRadio_1 = wx.RadioButton( self, wx.ID_ANY, u"Dice 1", wx.DefaultPosition, wx.Size( -1,20 ), wx.RB_GROUP )
		self.DiceSizer_1.Add( self.diceRadio_1, 0, wx.ALL, 5 )		
		self.diceImage1 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.Point( -1,-1 ), wx.Size( 20,20 ), 0 )
		self.DiceSizer_1.Add( self.diceImage1, 0, wx.ALL, 5 )		
		self.DicesSizer.Add( self.DiceSizer_1, 0, 0, 5 )
		
		self.DiceSizer_2 = wx.BoxSizer( wx.HORIZONTAL )		
		self.diceRadio_2 = wx.RadioButton( self, wx.ID_ANY, u"Dice 2", wx.DefaultPosition, wx.Size( -1,20 ), 0 )
		self.DiceSizer_2.Add( self.diceRadio_2, 0, wx.ALL, 5 )		
		self.diceImage2 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 20,20 ), 0 )
		self.DiceSizer_2.Add( self.diceImage2, 0, wx.ALL, 5 )				
		self.DicesSizer.Add( self.DiceSizer_2, 0, 0, 5 )

		self.DiceSizer_3 = wx.BoxSizer( wx.HORIZONTAL )		
		self.diceRadio_3 = wx.RadioButton( self, wx.ID_ANY, u"Dice 3", wx.DefaultPosition, wx.Size( -1,20 ), 0 )
		self.DiceSizer_3.Add( self.diceRadio_3, 0, wx.ALL, 5 )		
		self.diceImage3 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 20,20 ), 0 )
		self.DiceSizer_3.Add( self.diceImage3, 0, wx.ALL, 5 )		
		self.DicesSizer.Add( self.DiceSizer_3, 0, 0, 5 )	

		self.DiceSizer_4 = wx.BoxSizer( wx.HORIZONTAL )		
		self.diceRadio_4 = wx.RadioButton( self, wx.ID_ANY, u"Dice 4", wx.DefaultPosition, wx.Size( -1,20 ), 0 )
		self.DiceSizer_4.Add( self.diceRadio_4, 0, wx.ALL, 5 )		
		self.diceImage4 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.DiceSizer_4.Add( self.diceImage4, 0, wx.ALL, 5 )		
		self.DicesSizer.Add( self.DiceSizer_4, 0, 0, 5 )
		
		self.DiceSizer_5 = wx.BoxSizer( wx.HORIZONTAL )		
		self.diceRadio_5 = wx.RadioButton( self, wx.ID_ANY, u"Dice 5", wx.DefaultPosition, wx.Size( -1,20 ), 0 )
		self.DiceSizer_5.Add( self.diceRadio_5, 0, wx.ALL, 5 )		
		self.diceImage5 = wx.StaticBitmap( self, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.DiceSizer_5.Add( self.diceImage5, 0, wx.ALL, 5 )		
		self.DicesSizer.Add( self.DiceSizer_5, 0, 0, 5 )
		
		self.NullDiceSizer = wx.BoxSizer( wx.HORIZONTAL )		
		self.diceRadio_0 = wx.RadioButton( self, wx.ID_ANY, u"Null", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.NullDiceSizer.Add( self.diceRadio_0, 0, wx.ALL, 5 )		
		self.DicesSizer.Add( self.NullDiceSizer, 1, wx.EXPAND, 5 )		
		
		self.CenterSizer.Add( self.DicesSizer, 1, wx.EXPAND, 5 )
		self.MainSizer.Add( self.CenterSizer, 0, 0, 0 )

	def initDicePlay(self):				
		self.DicePlaySizer = wx.BoxSizer( wx.HORIZONTAL )

		self.MainSizer.Add( self.DicePlaySizer , 0, wx.ALL, 5 )
		
	def initAttrTower(self):		
		self.AttrTowerSizer = wx.BoxSizer( wx.VERTICAL )		
		self.AttrSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.Attr_1 = wx.BoxSizer( wx.VERTICAL )		
		self.AttrLabel_1 = wx.StaticText( self, wx.ID_ANY, u"   Normal", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.AttrLabel_1.Wrap( -1 )
		self.Attr_1.Add( self.AttrLabel_1, 0, wx.TOP|wx.RIGHT|wx.LEFT, 5 )		
		self.AttrBox_1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), wx.TE_READONLY )
		self.Attr_1.Add( self.AttrBox_1, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )	
		self.AttrSizer.Add( self.Attr_1, 0, 0, 5 )
		
		self.Attr_2 = wx.BoxSizer( wx.VERTICAL )		
		self.AttrLabel_2 = wx.StaticText( self, wx.ID_ANY, u"   Attack", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.AttrLabel_2.Wrap( -1 )
		self.Attr_2.Add( self.AttrLabel_2, 0, wx.TOP|wx.RIGHT|wx.LEFT, 5 )		
		self.AttrBox_2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), wx.TE_READONLY )
		self.Attr_2.Add( self.AttrBox_2, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )		
		self.AttrSizer.Add( self.Attr_2, 0, 0, 5 )
		
		self.Attr_3 = wx.BoxSizer( wx.VERTICAL )		
		self.AttrLabel_3 = wx.StaticText( self, wx.ID_ANY, u"   Defense", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.AttrLabel_3.Wrap( -1 )
		self.Attr_3.Add( self.AttrLabel_3, 0, wx.TOP|wx.RIGHT|wx.LEFT, 5 )		
		self.AttrBox_3 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), wx.TE_READONLY )
		self.Attr_3.Add( self.AttrBox_3, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		self.AttrSizer.Add( self.Attr_3, 0, 0, 5 )
		
		self.Attr_4 = wx.BoxSizer( wx.VERTICAL )		
		self.AttrLabel_4 = wx.StaticText( self, wx.ID_ANY, u"   Move", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.AttrLabel_4.Wrap( -1 )
		self.Attr_4.Add( self.AttrLabel_4, 0, wx.TOP|wx.RIGHT|wx.LEFT, 5 )		
		self.AttrBox_4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), wx.TE_READONLY )
		self.Attr_4.Add( self.AttrBox_4, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )
		self.AttrSizer.Add( self.Attr_4, 0, 0, 5 )
		
		self.Attr_5 = wx.BoxSizer( wx.VERTICAL )		
		self.AttrLabel_5 = wx.StaticText( self, wx.ID_ANY, u"   Special", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.AttrLabel_5.Wrap( -1 )
		self.Attr_5.Add( self.AttrLabel_5, 0, wx.TOP|wx.RIGHT|wx.LEFT, 5 )		
		self.AttrBox_5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), wx.TE_READONLY )
		self.Attr_5.Add( self.AttrBox_5, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )		
		self.AttrSizer.Add( self.Attr_5, 0, 0, 5 )
		
		self.Attr_6 = wx.BoxSizer( wx.VERTICAL )		
		self.AttrLabel_6 = wx.StaticText( self, wx.ID_ANY, u"   Health", wx.DefaultPosition, wx.Size( 80,-1 ), 0 )
		self.AttrLabel_6.Wrap( -1 )
		self.Attr_6.Add( self.AttrLabel_6, 0, wx.TOP|wx.RIGHT|wx.LEFT, 5 )		
		self.AttrBox_6 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 80,-1 ), wx.TE_READONLY )
		self.Attr_6.Add( self.AttrBox_6, 0, wx.BOTTOM|wx.RIGHT|wx.LEFT, 5 )		
		
		self.AttrSizer.Add( self.Attr_6, 0, 0, 5 )
		self.AttrTowerSizer.Add( self.AttrSizer, 1, wx.EXPAND, 5 )
		
		self.MainSizer.Add( self.AttrTowerSizer, 0, 0, 5 )

	def initSubmit(self):		
		self.InputSizer = wx.BoxSizer( wx.HORIZONTAL )

		self.inputField = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 450,30 ), 0 )
		self.InputSizer.Add( self.inputField, 0, wx.ALL, 5 )
		
		self.submit = wx.Button( self, wx.ID_ANY, u"Enter", wx.DefaultPosition, wx.Size( 100,30 ), 0 )
		self.InputSizer.Add( self.submit, 0, wx.ALL, 5 )		
		
		self.MainSizer.Add( self.InputSizer, 0, 0, 5 )
	
	def __del__( self ):
		pass
	
