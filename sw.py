# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sw.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sw(object):
    def submit(self):
        try:
            side_test = self.lineEdit.text()

            s1 = float(side_test)

            area = 0
            area = 4*s1
            self.label_3.setText(f"Total {area:.2f}")
        except:
            self.label_3.setText(" Enter properly radius")
    def setupUi(self, sw):
        sw.setObjectName("sw")
        sw.resize(259, 307)
        self.centralwidget = QtWidgets.QWidget(sw)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 40, 101, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 35, 10))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 100, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 170, 61, 31))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda: self.submit())
        self.pushButton.setGeometry(QtCore.QRect(90, 230, 56, 17))
        self.pushButton.setObjectName("pushButton")
        sw.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(sw)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 259, 18))
        self.menubar.setObjectName("menubar")
        sw.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(sw)
        self.statusbar.setObjectName("statusbar")
        sw.setStatusBar(self.statusbar)

        self.retranslateUi(sw)
        QtCore.QMetaObject.connectSlotsByName(sw)

    def retranslateUi(self, sw):
        _translate = QtCore.QCoreApplication.translate
        sw.setWindowTitle(_translate("sw", "MainWindow"))
        self.label.setText(_translate("sw", "  SQUARE PERIMETER"))
        self.label_2.setText(_translate("sw", "Side"))
        self.pushButton.setText(_translate("sw", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sw = QtWidgets.QMainWindow()
    ui = Ui_sw()
    ui.setupUi(sw)
    sw.show()
    sys.exit(app.exec_())
