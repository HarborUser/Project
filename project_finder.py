from PyQt5.QtWidgets import *
from project import *
from circle import *
from math import pi

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class project_finder(QMainWindow,Ui_Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.Circle_button = None
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.circle())




    def circle(self):

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Circle()
        self.ui.setupUi(self.window)
        self.window.show()














