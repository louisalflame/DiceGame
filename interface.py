# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.lib.scrolledpanel

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, 
			title = wx.EmptyString, pos = wx.DefaultPosition, 
			size = wx.Size( 600,550 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )		
		self.MainSizer = wx.BoxSizer( wx.VERTICAL )		

		self.initDiceSettingFrame()

#==========================================================================
# Widget for Setting
#==========================================================================
	def initDiceSettingFrame(self):
		self.MainSizer.Clear(True)
		self.initLabel()


		self.MainPlayerLabel = wx.StaticText( self, wx.ID_ANY, u" -- Player -- ",
			wx.DefaultPosition, wx.DefaultSize, 0 )
		self.MainSizer.Add( self.MainPlayerLabel, 0, wx.ALL, 5 )

		self.MainPlayerSizer = wx.BoxSizer( wx.HORIZONTAL )
		self.MainPlayerText = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString,
			wx.DefaultPosition, wx.Size(200,50), wx.TE_READONLY )
		self.MainPlayerSizer.Add( self.MainPlayerText, 0, wx.ALL, 5 )
		self.MainPlayerPanel = wx.lib.scrolledpanel.ScrolledPanel( self, wx.ID_ANY, 
			wx.DefaultPosition, wx.Size(250,50), wx.TAB_TRAVERSAL )
		self.MainPlayerPanel.SetupScrolling()
		self.MainPlayerSizer.Add( self.MainPlayerPanel, 0, wx.ALL, 5 )
		self.MainSizer.Add( self.MainPlayerSizer, 0, 0, 0 )

		self.EnemyPlayerLabel = wx.StaticText( self, wx.ID_ANY, u" -- Enemy -- ",
			wx.DefaultPosition, wx.DefaultSize, 0 )
		self.MainSizer.Add( self.EnemyPlayerLabel, 0, wx.ALL, 5 )

		self.EnemyPlayerSizer = wx.BoxSizer( wx.HORIZONTAL )
		self.EnemyPlayerText = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString,
			wx.DefaultPosition, wx.Size(200,50), wx.TE_READONLY )
		self.EnemyPlayerSizer.Add( self.EnemyPlayerText, 0, wx.ALL, 5 )
		self.EnemyPlayerPanel = wx.lib.scrolledpanel.ScrolledPanel( self, wx.ID_ANY, 
			wx.DefaultPosition, wx.Size(250,50), wx.TAB_TRAVERSAL )
		self.EnemyPlayerPanel.SetupScrolling()
		self.EnemyPlayerSizer.Add( self.EnemyPlayerPanel, 0, wx.ALL, 5 )
		self.MainSizer.Add( self.EnemyPlayerSizer, 0, 0, 0 )

		self.DiceMenuLabel = wx.StaticText( self, wx.ID_ANY, u" -- Dice Package -- ",
			wx.DefaultPosition, wx.DefaultSize, 0 )
		self.MainSizer.Add( self.DiceMenuLabel, 0, wx.ALL, 5 )

		self.DiceMenuSizer = wx.BoxSizer( wx.HORIZONTAL )
		self.DicePackagePanel = wx.lib.scrolledpanel.ScrolledPanel( self, wx.ID_ANY, 
			wx.DefaultPosition, wx.Size(250,200), wx.TAB_TRAVERSAL )
		self.DicePackagePanel.SetupScrolling()
		self.DiceMenuSizer.Add( self.DicePackagePanel, 0, wx.ALL, 5 )

		self.DiceDataPanel = wx.lib.scrolledpanel.ScrolledPanel( self, wx.ID_ANY, 
			wx.DefaultPosition, wx.Size(250,200), wx.TAB_TRAVERSAL )
		self.DiceDataPanel.SetupScrolling()
		self.DiceMenuSizer.Add( self.DiceDataPanel, 0, wx.ALL, 5 )

		self.MainSizer.Add( self.DiceMenuSizer, 0, 0, 0 )

		self.initSubmit()

		self.SetSizer( self.MainSizer )
		self.Layout()		

#==========================================================================
# Widget for Playing
#==========================================================================
	def initDicePlayFrame(self):
		self.MainSizer.Clear(True)

		self.initLabel()

		self.CenterSizer = wx.BoxSizer( wx.HORIZONTAL )
		self.initDiceSizer()
		self.initAttrTower()
		self.MainSizer.Add( self.CenterSizer, 0, 0, 0 )

		self.initSubmit()

		self.SetSizer( self.MainSizer )
		self.Layout()		

	def initLabel(self):
		self.MainLabel = wx.StaticText( self, wx.ID_ANY, u"                Dice Game --prototype--",
			wx.Point( 200,0 ), wx.DefaultSize, 0 )
		self.MainSizer.Add( self.MainLabel, 0, wx.ALL, 5 )

	def initDiceSizer(self):
		self.DiceViewSizer = wx.BoxSizer( wx.VERTICAL )

		self.DiceInfoLabel = wx.StaticText( self, wx.ID_ANY, u" -- Dice Info -- ",
			wx.DefaultPosition ,wx.DefaultSize, 0  )
		self.DiceViewSizer.Add( self.DiceInfoLabel, 0, 0, 0 )

		self.DiceInfoPanel = wx.Panel( self, wx.ID_ANY, 
			wx.DefaultPosition, wx.Size( 250,50 ), wx.TAB_TRAVERSAL )
		self.DiceInfoSizer = wx.BoxSizer( wx.HORIZONTAL )
		self.DiceInfoPanel.SetSizer( self.DiceInfoSizer )
		self.DiceInfoPanel.Layout()		
		self.DiceViewSizer.Add( self.DiceInfoPanel, 0, wx.ALL, 5 )

		self.DicesLabel = wx.StaticText( self, wx.ID_ANY, u" -- Dices View -- ",
			wx.DefaultPosition ,wx.DefaultSize, 0  )
		self.DiceViewSizer.Add( self.DicesLabel, 0, 0, 0 )

		self.DicesPanel = wx.lib.scrolledpanel.ScrolledPanel( self, wx.ID_ANY, 
			wx.DefaultPosition, wx.Size(250,120), wx.TAB_TRAVERSAL )
		self.DicesPanel.SetupScrolling()
		self.DicesPanelSizer = wx.BoxSizer( wx.VERTICAL )
		self.DicesPanel.SetSizer( self.DicesPanelSizer )
		self.DicesPanel.Layout()		
		self.DiceViewSizer.Add( self.DicesPanel, 0, wx.ALL, 5 )

		self.DicePlayLabel = wx.StaticText( self, wx.ID_ANY, u" -- Dice Result -- ",
			wx.DefaultPosition ,wx.DefaultSize, 0  )
		self.DiceViewSizer.Add( self.DicePlayLabel, 0, 0, 0 )

		self.DicePlayPanel = wx.Panel( self, wx.ID_ANY, 
			wx.DefaultPosition, wx.Size(250,100), wx.TAB_TRAVERSAL )
		self.DicePlaySizer = wx.BoxSizer( wx.VERTICAL )
		self.DicePlayPanel.SetSizer( self.DicePlaySizer )
		self.DicePlayPanel.Layout()
		self.DiceViewSizer.Add( self.DicePlayPanel, 0, wx.ALL, 5 )	

		self.CenterSizer.Add( self.DiceViewSizer, 1, wx.ALL, 5 )

	def initAttrTower(self):		
		self.AttrTowerSizer = wx.BoxSizer( wx.VERTICAL )

		self.TowerViewLabel = wx.StaticText( self, wx.ID_ANY, u" -- Tower Place -- ",
			wx.DefaultPosition, wx.DefaultSize, 0 )
		self.AttrTowerSizer.Add( self.TowerViewLabel, 0, 0, 0 )
		self.TowerViewPanel = wx.Panel( self, wx.ID_ANY, 
			wx.DefaultPosition, wx.Size(250, 100), wx.TAB_TRAVERSAL )
		self.AttrTowerSizer.Add( self.TowerViewPanel, 0, wx.ALL, 5 )

		self.AttrViewLabel = wx.StaticText( self, wx.ID_ANY, u" -- Attribute Point -- ",
			wx.DefaultPosition, wx.DefaultSize, 0 )
		self.AttrTowerSizer.Add( self.AttrViewLabel, 0, 0, 0 )

		self.AttrSizer = wx.BoxSizer( wx.HORIZONTAL )

		self.AttrNor = wx.BoxSizer( wx.VERTICAL )
		self.AttrNorBitmap = wx.StaticBitmap( self, wx.ID_ANY, 
			wx.Bitmap( wx.Image(u"panel/AttrNor.png", wx.BITMAP_TYPE_PNG).Rescale(40,40) ), 
			wx.DefaultPosition, wx.DefaultSize, 0 )
		self.AttrNor.Add( self.AttrNorBitmap, 0, 0, 0 )
		self.AttrNorNum = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString,
			wx.DefaultPosition, wx.Size(40,30), wx.TE_READONLY )
		self.AttrNor.Add( self.AttrNorNum, 0, wx.TOP, 2 )
		self.AttrSizer.Add( self.AttrNor, 0, wx.ALL, 2 )

		self.AttrAtk = wx.BoxSizer( wx.VERTICAL )
		self.AttrAtkBitmap = wx.StaticBitmap( self, wx.ID_ANY, 
			wx.Bitmap( wx.Image(u"panel/AttrAtk.png", wx.BITMAP_TYPE_PNG).Rescale(40,40) ),
			wx.DefaultPosition, wx.DefaultSize, 0 )
		self.AttrAtk.Add( self.AttrAtkBitmap, 0, 0, 0 )
		self.AttrAtkNum = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString,
			wx.DefaultPosition, wx.Size(40,30), wx.TE_READONLY )
		self.AttrAtk.Add( self.AttrAtkNum, 0, wx.TOP, 2 )
		self.AttrSizer.Add( self.AttrAtk, 0, wx.ALL, 2 )

		self.AttrDef = wx.BoxSizer( wx.VERTICAL )
		self.AttrDefBitmap = wx.StaticBitmap( self, wx.ID_ANY, 
			wx.Bitmap( wx.Image(u"panel/AttrDef.png", wx.BITMAP_TYPE_PNG).Rescale(40,40) ),
			wx.DefaultPosition, wx.DefaultSize, 0 )
		self.AttrDef.Add( self.AttrDefBitmap, 0, 0, 0 )
		self.AttrDefNum = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString,
			wx.DefaultPosition, wx.Size(40,30), wx.TE_READONLY )
		self.AttrDef.Add( self.AttrDefNum, 0, wx.TOP, 2 )
		self.AttrSizer.Add( self.AttrDef, 0, wx.ALL, 2 )

		self.AttrMov = wx.BoxSizer( wx.VERTICAL )
		self.AttrMovBitmap = wx.StaticBitmap( self, wx.ID_ANY, 
			wx.Bitmap( wx.Image(u"panel/AttrMov.png", wx.BITMAP_TYPE_PNG).Rescale(40,40) ),
			wx.DefaultPosition, wx.DefaultSize, 0 )
		self.AttrMov.Add( self.AttrMovBitmap, 0, 0, 0 )
		self.AttrMovNum = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString,
			wx.DefaultPosition, wx.Size(40,30), wx.TE_READONLY )
		self.AttrMov.Add( self.AttrMovNum, 0, wx.TOP, 2 )
		self.AttrSizer.Add( self.AttrMov, 0, wx.ALL, 2 )

		self.AttrSpc = wx.BoxSizer( wx.VERTICAL )
		self.AttrSpcBitmap = wx.StaticBitmap( self, wx.ID_ANY,
			wx.Bitmap( wx.Image(u"panel/AttrSpc.png", wx.BITMAP_TYPE_PNG).Rescale(40,40) ),
			wx.DefaultPosition, wx.DefaultSize, 0 )
		self.AttrSpc.Add( self.AttrSpcBitmap, 0, 0, 0 )
		self.AttrSpcNum = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString,
			wx.DefaultPosition, wx.Size(40,30), wx.TE_READONLY )
		self.AttrSpc.Add( self.AttrSpcNum, 0, wx.TOP, 2 )
		self.AttrSizer.Add( self.AttrSpc, 0, wx.ALL, 2 )

		self.AttrHeal = wx.BoxSizer( wx.VERTICAL )
		self.AttrHealBitmap = wx.StaticBitmap( self, wx.ID_ANY, 
			wx.Bitmap( wx.Image(u"panel/AttrHeal.png", wx.BITMAP_TYPE_PNG).Rescale(40,40) ),
			wx.DefaultPosition, wx.DefaultSize, 0 )
		self.AttrHeal.Add( self.AttrHealBitmap, 0, 0, 0 )
		self.AttrHealNum = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString,
			wx.DefaultPosition, wx.Size(40,30), wx.TE_READONLY )
		self.AttrHeal.Add( self.AttrHealNum, 0, wx.TOP, 2 )
		self.AttrSizer.Add( self.AttrHeal, 0, wx.ALL, 2 )	
		
		self.AttrTowerSizer.Add( self.AttrSizer, 1, wx.EXPAND, 5 )
		
		self.CenterSizer.Add( self.AttrTowerSizer, 1, wx.ALL, 5 )

	def initSubmit(self):		
		self.OutputSizer = wx.BoxSizer( wx.HORIZONTAL )
		
		self.OutputField = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, 
			wx.DefaultPosition, wx.Size( 400,50 ), wx.TE_MULTILINE|wx.TE_READONLY )
		self.OutputSizer.Add( self.OutputField, 0, wx.ALL, 5 )
		
		self.submit = wx.Button( self, wx.ID_ANY, u"Enter", 
			wx.DefaultPosition, wx.Size( 100,50 ), 0 )
		self.submit.Bind( wx.EVT_BUTTON, self.textSubmit )
		self.OutputSizer.Add( self.submit, 0, wx.ALL, 5 )		
		
		self.MainSizer.Add( self.OutputSizer, 0, 0, 0 )
	
	def __del__( self ):
		pass
	
