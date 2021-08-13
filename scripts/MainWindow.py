# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2290, 1644)
        MainWindow.setStyleSheet("background-color: #FFF")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plotWidget = MplWidget(self.centralwidget)
        self.plotWidget.setGeometry(QtCore.QRect(40, 30, 2211, 1251))
        self.plotWidget.setObjectName("plotWidget")
        self.btnShow = QtWidgets.QPushButton(self.centralwidget)
        self.btnShow.setGeometry(QtCore.QRect(990, 1380, 221, 71))
        self.btnShow.setStyleSheet("color: #fff;\n"
"background-color: #337ab7;\n"
"border-color: #2e6da4;\n"
"cursor: pointer;\n"
"background-image: none;\n"
"border: 1px solid transparent;\n"
"border-radius: 4px;")
        self.btnShow.setObjectName("btnShow")
        self.spinNum = QtWidgets.QSpinBox(self.centralwidget)
        self.spinNum.setGeometry(QtCore.QRect(990, 1480, 221, 25))
        self.spinNum.setMinimum(1)
        self.spinNum.setMaximum(999999999)
        self.spinNum.setObjectName("spinNum")
        self.btnClear = QtWidgets.QPushButton(self.centralwidget)
        self.btnClear.setGeometry(QtCore.QRect(1320, 1380, 221, 71))
        self.btnClear.setStyleSheet("color: #fff;\n"
"background-color: #337ab7;\n"
"border-color: #2e6da4;\n"
"cursor: pointer;\n"
"background-image: none;\n"
"border: 1px solid transparent;\n"
"border-radius: 4px;")
        self.btnClear.setObjectName("btnClear")
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        self.btnExit.setGeometry(QtCore.QRect(2180, 1490, 71, 71))
        self.btnExit.setStyleSheet("color: #fff;\n"
"background-color: #d9534f;\n"
"border-color: #d43f3a;\n"
"cursor: pointer;\n"
"background-image: none;\n"
"border: 1px solid transparent;\n"
"border-radius: 4px;")
        self.btnExit.setObjectName("btnExit")
        self.btnRange = QtWidgets.QPushButton(self.centralwidget)
        self.btnRange.setGeometry(QtCore.QRect(450, 1380, 221, 71))
        self.btnRange.setStyleSheet("color: #fff;\n"
"background-color: #337ab7;\n"
"border-color: #2e6da4;\n"
"cursor: pointer;\n"
"background-image: none;\n"
"border: 1px solid transparent;\n"
"border-radius: 4px;")
        self.btnRange.setObjectName("btnRange")
        self.spinLower = QtWidgets.QSpinBox(self.centralwidget)
        self.spinLower.setGeometry(QtCore.QRect(270, 1400, 171, 25))
        self.spinLower.setMinimum(1)
        self.spinLower.setMaximum(999999999)
        self.spinLower.setObjectName("spinLower")
        self.spinUpper = QtWidgets.QSpinBox(self.centralwidget)
        self.spinUpper.setGeometry(QtCore.QRect(680, 1400, 181, 25))
        self.spinUpper.setMinimum(1)
        self.spinUpper.setMaximum(999999999)
        self.spinUpper.setObjectName("spinUpper")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 1360, 141, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(690, 1350, 141, 31))
        self.label_2.setObjectName("label_2")
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        self.btnSave.setGeometry(QtCore.QRect(1630, 1380, 221, 71))
        self.btnSave.setStyleSheet("color: #fff;\n"
"background-color: #337ab7;\n"
"border-color: #2e6da4;\n"
"cursor: pointer;\n"
"background-image: none;\n"
"border: 1px solid transparent;\n"
"border-radius: 4px;")
        self.btnSave.setObjectName("btnSave")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 2290, 31))
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
        self.btnShow.setText(_translate("MainWindow", "Show"))
        self.btnClear.setText(_translate("MainWindow", "clear Plot"))
        self.btnExit.setText(_translate("MainWindow", "Exit"))
        self.btnRange.setText(_translate("MainWindow", "plot range"))
        self.label.setText(_translate("MainWindow", "Lower Limit"))
        self.label_2.setText(_translate("MainWindow", "Upper Limit"))
        self.btnSave.setText(_translate("MainWindow", "save as pdf"))

from mplwidget import MplWidget
