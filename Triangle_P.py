# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Triangle_P.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TC(object):
    def button(self):
        try:
            side_test = self.lineEdit.text()
            side2_test = self.lineEdit_2.text()
            side3_test = self.lineEdit_3.text()
            s1 = float(side_test)
            s2 = float(side2_test)
            s3 = float(side3_test)
            area = 0
            area = s1 + s2 + s3
            self.label_5.setText(f"Total {area:.2f}")
        except:
            self.label_5.setText(" Enter numeric value")
    def setupUi(self, TC):
        TC.setObjectName("TC")
        TC.resize(260, 306)
        self.centralwidget = QtWidgets.QWidget(TC)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 60, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 140, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 100, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 70, 35, 10))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 35, 10))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 140, 35, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 20, 71, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(80, 190, 51, 31))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget,clicked= lambda: self.button())
        self.pushButton.setGeometry(QtCore.QRect(80, 250, 56, 17))
        self.pushButton.setObjectName("pushButton")
        TC.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TC)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 260, 18))
        self.menubar.setObjectName("menubar")
        TC.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TC)
        self.statusbar.setObjectName("statusbar")
        TC.setStatusBar(self.statusbar)

        self.retranslateUi(TC)
        QtCore.QMetaObject.connectSlotsByName(TC)

    def retranslateUi(self, TC):
        _translate = QtCore.QCoreApplication.translate
        TC.setWindowTitle(_translate("TC", "MainWindow"))
        self.label.setText(_translate("TC", "Side 1"))
        self.label_2.setText(_translate("TC", "Side 2"))
        self.label_3.setText(_translate("TC", "Side 3"))
        self.label_4.setText(_translate("TC", "Triangle Perimeter   "))
        self.pushButton.setText(_translate("TC", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TC = QtWidgets.QMainWindow()
    ui = Ui_TC()
    ui.setupUi(TC)
    TC.show()
    sys.exit(app.exec_())
