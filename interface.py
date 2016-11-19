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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 600,480 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		self.MainSizer = wx.BoxSizer( wx.VERTICAL )
				
		self.initLabel()
		self.initCenterSizer()
		self.initAttrTower()
		self.initSubmit()		
		
		self.SetSizer( self.MainSizer )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.submit.Bind( wx.EVT_BUTTON, self.textSubmit )

	def initLabel(self):
		self.MainLabel = wx.StaticText( self, wx.ID_ANY, u"                Dice Game --prototype--", wx.Point( 200,0 ), wx.DefaultSize, 0 )
		
		self.MainLabel.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 76, 90, 90, False, wx.EmptyString ) )		
		self.MainSizer.Add( self.MainLabel, 0, wx.ALL, 5 )

	def initCenterSizer(self):
		self.CenterSizer = wx.BoxSizer( wx.HORIZONTAL )

		self.outputField = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,280 ), wx.TE_MULTILINE|wx.TE_READONLY )
		self.CenterSizer.Add( self.outputField, 0, wx.ALL, 5 )

		self.DiceViewSizer = wx.BoxSizer( wx.VERTICAL )

		self.DiceInfoLabel = wx.StaticText( self, wx.ID_ANY, u" -- Dice Info -- ", wx.DefaultPosition ,wx.DefaultSize, 0  )
		self.DiceViewSizer.Add( self.DiceInfoLabel, 0, 0, 5 )

		self.DiceInfoPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 250,40 ), wx.TAB_TRAVERSAL )
		self.DiceInfoPanelSizer = wx.BoxSizer( wx.HORIZONTAL )
		self.DiceInfoPanel.SetSizer( self.DiceInfoPanelSizer )
		self.DiceInfoPanel.Layout()		
		self.DiceViewSizer.Add( self.DiceInfoPanel, 0, wx.ALL, 5 )

		self.DicesLabel = wx.StaticText( self, wx.ID_ANY, u" -- Dices View -- ", wx.DefaultPosition ,wx.DefaultSize, 0  )
		self.DiceViewSizer.Add( self.DicesLabel, 0, 0, 5 )

		self.DicesPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 250,120 ), wx.TAB_TRAVERSAL )
		self.DicesPanelSizer = wx.BoxSizer( wx.VERTICAL )
		self.DicesPanel.SetSizer( self.DicesPanelSizer )
		self.DicesPanel.Layout()		
		self.DiceViewSizer.Add( self.DicesPanel, 0, wx.ALL, 5 )

		self.DicePlayLabel = wx.StaticText( self, wx.ID_ANY, u" -- Dice Result -- ", wx.DefaultPosition ,wx.DefaultSize, 0  )
		self.DiceViewSizer.Add( self.DicePlayLabel, 0, 0, 5 )

		self.DicePlayPanel = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 250,60 ), wx.TAB_TRAVERSAL )
		self.DicePlaySizer = wx.BoxSizer( wx.HORIZONTAL )
		self.DicePlayPanel.SetSizer( self.DicePlaySizer )
		self.DicePlayPanel.Layout()
		self.DiceViewSizer.Add( self.DicePlayPanel, 0, wx.ALL, 5 )	

		self.CenterSizer.Add( self.DiceViewSizer, 1, wx.ALL, 5 )

		self.MainSizer.Add( self.CenterSizer, 0, 0, 0 )

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
	
