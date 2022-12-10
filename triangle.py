# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'triangle.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_triangle_1(object):
    def submit(self):
        try:
            side_test = self.lineEdit.text()
            side2_test = self.lineEdit_2.text()

            s1 = float(side_test)
            s2 = float(side2_test)

            area = 0
            area = (s1 * s2)/2
            self.label_4.setText(f"Total {area:.2f}")
        except:
            self.label_4.setText(" Enter properly radius")
    def setupUi(self, triangle_1):
        triangle_1.setObjectName("triangle_1")
        triangle_1.resize(245, 268)
        self.centralwidget = QtWidgets.QWidget(triangle_1)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 20, 81, 41))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 70, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 110, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 35, 10))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 35, 10))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget,clicked=lambda: self.submit())
        self.pushButton.setGeometry(QtCore.QRect(80, 210, 56, 17))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(74, 150, 91, 41))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        triangle_1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(triangle_1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 245, 18))
        self.menubar.setObjectName("menubar")
        triangle_1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(triangle_1)
        self.statusbar.setObjectName("statusbar")
        triangle_1.setStatusBar(self.statusbar)

        self.retranslateUi(triangle_1)
        QtCore.QMetaObject.connectSlotsByName(triangle_1)

    def retranslateUi(self, triangle_1):
        _translate = QtCore.QCoreApplication.translate
        triangle_1.setWindowTitle(_translate("triangle_1", "MainWindow"))
        self.label.setText(_translate("triangle_1", "TRIANGLE AREA "))
        self.label_2.setText(_translate("triangle_1", "Length"))
        self.label_3.setText(_translate("triangle_1", "Width"))
        self.pushButton.setText(_translate("triangle_1", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    triangle_1 = QtWidgets.QMainWindow()
    ui = Ui_triangle_1()
    ui.setupUi(triangle_1)
    triangle_1.show()
    sys.exit(app.exec_())
