# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/ecc.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = '../platforms'

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 330, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.txt_sign = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_sign.setGeometry(QtCore.QRect(170, 290, 481, 87))
        self.txt_sign.setObjectName("txt_sign")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 170, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 40, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.btn_gen_keys = QtWidgets.QToolButton(self.centralwidget)
        self.btn_gen_keys.setGeometry(QtCore.QRect(90, 510, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_gen_keys.setFont(font)
        self.btn_gen_keys.setObjectName("btn_gen_keys")
        self.txt_info = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_info.setGeometry(QtCore.QRect(170, 150, 481, 87))
        self.txt_info.setObjectName("txt_info")
        self.btn_verify = QtWidgets.QToolButton(self.centralwidget)
        self.btn_verify.setGeometry(QtCore.QRect(650, 500, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_verify.setFont(font)
        self.btn_verify.setObjectName("btn_verify")
        self.btn_sign = QtWidgets.QToolButton(self.centralwidget)
        self.btn_sign.setGeometry(QtCore.QRect(400, 500, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_sign.setFont(font)
        self.btn_sign.setObjectName("btn_sign")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Signature"))
        self.label_2.setText(_translate("MainWindow", "Information"))
        self.label.setText(_translate("MainWindow", "ECC CIPHER"))
        self.btn_gen_keys.setText(_translate("MainWindow", "Generate Keys"))
        self.btn_verify.setText(_translate("MainWindow", "Verify"))
        self.btn_sign.setText(_translate("MainWindow", "Sign"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
