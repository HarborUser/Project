# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mastermind.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CentralUnit(object):
    def setupUi(self, CentralUnit):
        CentralUnit.setObjectName("CentralUnit")
        CentralUnit.resize(256, 256)
        self.centralwidget = QtWidgets.QWidget(CentralUnit)
        self.centralwidget.setObjectName("centralwidget")
        self.A_button = QtWidgets.QPushButton(self.centralwidget)
        self.A_button.setGeometry(QtCore.QRect(90, 50, 71, 41))
        self.A_button.setObjectName("A_button")
        self.Bbutton = QtWidgets.QPushButton(self.centralwidget)
        self.Bbutton.setGeometry(QtCore.QRect(90, 120, 71, 51))
        self.Bbutton.setObjectName("Bbutton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(54, 10, 161, 20))
        self.label.setObjectName("label")
        CentralUnit.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CentralUnit)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 256, 18))
        self.menubar.setObjectName("menubar")
        CentralUnit.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CentralUnit)
        self.statusbar.setObjectName("statusbar")
        CentralUnit.setStatusBar(self.statusbar)

        self.retranslateUi(CentralUnit)
        QtCore.QMetaObject.connectSlotsByName(CentralUnit)

    def retranslateUi(self, CentralUnit):
        _translate = QtCore.QCoreApplication.translate
        CentralUnit.setWindowTitle(_translate("CentralUnit", "MainWindow"))
        self.A_button.setText(_translate("CentralUnit", "AREA"))
        self.Bbutton.setText(_translate("CentralUnit", "PERIMETER"))
        self.label.setText(_translate("CentralUnit", "    AREA-PERIMETER MACHINE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CentralUnit = QtWidgets.QMainWindow()
    ui = Ui_CentralUnit()
    ui.setupUi(CentralUnit)
    CentralUnit.show()
    sys.exit(app.exec_())
