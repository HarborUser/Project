# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Circle_perimeter.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_C1(object):

    def submit(self):
        try:
            radius_test = self.lineEdit.text()
            radius = float(radius_test)
            area =0
            area = 2 *pi * (radius)
            self.label_3.setText(f"Total {area:.2f}")
        except:
            self.label_3.setText(" Enter properly radius")


    def setupUi(self, C1):
        C1.setObjectName("C1")
        C1.resize(285, 311)
        self.centralwidget = QtWidgets.QWidget(C1)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 20, 71, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 35, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 90, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 160, 61, 31))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 230, 56, 17))
        self.pushButton.setObjectName("pushButton")
        C1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(C1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 285, 18))
        self.menubar.setObjectName("menubar")
        C1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(C1)
        self.statusbar.setObjectName("statusbar")
        C1.setStatusBar(self.statusbar)

        self.retranslateUi(C1)
        QtCore.QMetaObject.connectSlotsByName(C1)

    def retranslateUi(self, C1):
        _translate = QtCore.QCoreApplication.translate
        C1.setWindowTitle(_translate("C1", "MainWindow"))
        self.label.setText(_translate("C1", "  Circle Perimeter"))
        self.label_2.setText(_translate("C1", "Radius"))
        self.pushButton.setText(_translate("C1", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    C1 = QtWidgets.QMainWindow()
    ui = Ui_C1()
    ui.setupUi(C1)
    C1.show()
    sys.exit(app.exec_())