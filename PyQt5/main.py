import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic

from random import choice


class MyWindow(QMainWindow):
	"""docstring for MyWindow"""
	def __init__(self):
		super(MyWindow, self).__init__()
		uic.loadUi('gui_Project.ui', self)

		self.colorButton.clicked.connect(self.change_color_func)

		self.show()
		

	def change_color_func(self):
		# print('#####################')
		hex = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]

		hex_list = [str(choice(hex)) for x in range(6)]

		hex_string = '#' + ''.join(hex_list)
		print(hex_string)

		# ------------------------
		# Change the text of '#XXXXXX' to current hex text
		self.hex_text.setText(hex_string)

		# ------------------------
		# Change background color to current hex color
		self.setStyleSheet("background-color: {};".format(hex_string))


if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MyWindow()
	sys.exit(app.exec_())






