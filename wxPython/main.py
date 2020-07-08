import wx
from gui import MyWindow_1

from random import choice


class MyWindow_2(MyWindow_1):
	def __init__(self, parent):
		MyWindow_1.__init__ (self, parent)
		
	def change_color_func(self, event):
		# print('#####################')
		hex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]

		hex_list = [str(choice(hex)) for x in range(6)]

		hex_string = '#' + ''.join(hex_list)
		print(hex_string)

		# ---------------
		# Change the text of '#XXXXXX' to current hex text
		self.hex_text.SetLabel(hex_string)
		self.Layout()

		# ------------------------
		# Change background color to current hex color
		self.SetBackgroundColour(hex_string)
		self.Refresh()


app = wx.App(0)
MyWindow_2(None).Show()
app.MainLoop()



# app = wx.App(False)
# frame = MyWindow_2(None)
# frame.Show()
# app.MainLoop()



