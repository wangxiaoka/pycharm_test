# -*- coding: utf-8 -*-
import wx
import time
from PIL import Image


class AdjustCamera(wx.Frame):

	def __init__(self):
		super(AdjustCamera, self).__init__(title = "摄像头校准")
		# self.win = wx.Frame(None,title = "摄像头校准")
		self.panel = wx.Panel(self)
		self.sizer = wx.GridBagSizer(0,0)
		self.print_debug = 1
		self.x_orig = 0
		self.y_orig = 110

		self.accuracy = wx.StaticText(self.panel, label = "位移精度")
		self.sizer.Add(self.accuracy, pos = (self.x_orig + 1, self.y_orig), flag = wx.ALL | wx.ALIGN_RIGHT, border = 5)
		self.accuracy_tc = wx.TextCtrl(self.panel, -1, value = "1")
		self.sizer.Add(self.accuracy_tc, pos = (self.x_orig + 1, self.y_orig + 1), flag = wx.ALL | wx.EXPAND, border = 5)

		self.x_text = wx.StaticText(self.panel, label = "Current X_location")
		self.sizer.Add(self.x_text, pos = (self.x_orig + 5, self.y_orig), flag = wx.ALL | wx.ALIGN_RIGHT, border = 5)
		self.x_tc = wx.TextCtrl(self.panel, -1, value = "1")
		self.sizer.Add(self.x_tc, pos = (self.x_orig + 5, self.y_orig + 1), flag = wx.ALL | wx.EXPAND, border = 5)

		self.y_text = wx.StaticText(self.panel, label = "Current X_location")
		self.sizer.Add(self.y_text, pos = (self.x_orig + 6, self.y_orig), flag = wx.ALL | wx.ALIGN_RIGHT, border = 5)
		self.y_tc = wx.TextCtrl(self.panel, -1, value = "1")
		self.sizer.Add(self.y_tc, pos = (self.x_orig + 6, self.y_orig + 1), flag = wx.ALL | wx.EXPAND, border = 5)

		self.buttonUP = wx.Button(self.panel, label = "↑")
		self.buttonDOWN = wx.Button(self.panel, label = "↓")
		self.buttonLEFT = wx.Button(self.panel, label = "←")
		self.buttonRIGHT = wx.Button(self.panel, label = "→")
		self.buttonOK = wx.Button(self.panel, label = "OK")

		self.sizer.Add(self.buttonUP, pos =(self.x_orig + 2, self.y_orig + 1), flag = wx.ALL | wx.EXPAND, border = 5)
		self.sizer.Add(self.buttonDOWN, pos =(self.x_orig + 4, self.y_orig + 1), flag = wx.ALL | wx.EXPAND, border = 5)
		self.sizer.Add(self.buttonLEFT, pos =(self.x_orig + 3, self.y_orig + 0), flag = wx.ALL | wx.EXPAND, border = 5)
		self.sizer.Add(self.buttonRIGHT, pos =(self.x_orig + 3, self.y_orig + 2), flag = wx.ALL | wx.EXPAND, border = 5)
		self.sizer.Add(self.buttonOK, pos =(self.x_orig + 3, self.y_orig + 1), flag = wx.ALL | wx.EXPAND, border = 5)

		self.panel.SetSizerAndFit(self.sizer)

		self.Bind(wx.EVT_BUTTON, self.UpClick, self.buttonUP)
		self.Bind(wx.EVT_BUTTON, self.DownClick, self.buttonDOWN)
		self.Bind(wx.EVT_BUTTON, self.LeftClick, self.buttonLEFT)
		self.Bind(wx.EVT_BUTTON, self.RightClick, self.buttonRIGHT)
		self.Bind(wx.EVT_BUTTON, self.OkClick, self.buttonOK)

		try:
			print "start"

		except:
			print 'ERROR'

	def UpClick(self):
		if self.print_debug:
			print time.strftime('%Y-%m-%D %H:%M:%S', time.localtime(time.time())) + '：' + "UpClick is pressed!"

	def DownClick(self):
		if self.print_debug:
			print time.strftime('%Y-%m-%D %H:%M:%S', time.localtime(time.time())) + '：' + "DownClick is pressed!"

	def LeftClick(self):
		if self.print_debug:
			print time.strftime('%Y-%m-%D %H:%M:%S', time.localtime(time.time())) + '：' + "LeftClick is pressed!"

	def RightClick(self):
		if self.print_debug:
			print time.strftime('%Y-%m-%D %H:%M:%S', time.localtime(time.time())) + '：' + "RightClick is pressed!"

	def OkClick(self):
		if self.print_debug:
			print time.strftime('%Y-%m-%D %H:%M:%S', time.localtime(time.time())) + '：' + "OkClick is pressed!"

def NarrowPNG(path):
	print "NarrowPNG"


def NarrowBMP(path):
	print "NarrowBMP"

def Adjust():
	app = wx.App()
	frame = AdjustCamera()
	frame.Show()
	app.MainLoop()
	return True

if __name__ == '__main__':
	Adjust()


