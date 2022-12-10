from PyQt5.QtWidgets import *
from project import *
from circle import *
from math import pi
from mastermind import *
from project2 import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

class master(QMainWindow,Ui_CentralUnit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setupUi(self)
        self.A_button.clicked.connect(lambda: self.news())
        self.Bbutton.clicked.connect(lambda : self.news2())
    def news(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Bot()
        self.ui.setupUi(self.window)
        self.window.show()

    def news2(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Sot()
        self.ui.setupUi(self.window)
        self.window.show()