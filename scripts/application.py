# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 11:14:09 2021

@author: Jonas
"""

import os
import sys


import random
from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QFileDialog

from MainWindow import Ui_MainWindow

import numpy as np

from PyQt5 import QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as Canvas
import matplotlib

# Ensure using PyQt5 backend
matplotlib.use('QT5Agg')






class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

        


    def connectSignalsSlots(self):
        self.btnShow.clicked.connect(self.plotNum)
        self.btnClear.clicked.connect(self.plotClear)
        self.btnExit.clicked.connect(self.exitOut)
        self.btnRange.clicked.connect(self.plotRange)
        self.btnSave.clicked.connect(self.save)

    def exitOut(self):
        os._exit(0)
        self.close()
  
    def calcAll(self, num, values):
        if num == 1:
            values.append(1)
            return values
        if num % 2 != 0:
            nextVal = num*3 + 1
            values.append(num)
            return self.calcAll(nextVal, values)
        else:
            nextVal = num/2
            values.append(num)
            return self.calcAll(nextVal, values)

  
    def plotClear(self):
        self.plotWidget.canvas.ax.cla()
        self.plotWidget.canvas.draw()
        
        
    def plotNum(self):
        
        self.plotWidget.canvas.ax.tick_params(axis="x",direction="in")
        self.plotWidget.canvas.ax.tick_params(axis="y",direction="in")
        self.plotWidget.canvas.ax.set_ylabel('intensity',fontsize=16)
    
        self.plotWidget.canvas.ax.tick_params(labelleft=True)
        self.plotWidget.canvas.ax.set_xlabel('Steps', fontsize=16)
        self.plotWidget.canvas.ax.set_ylabel('Value', fontsize=16)
        
        number = self.spinNum.value()
        values = []
        allVals = self.calcAll(number, values)
        print(allVals)
        self.plotWidget.canvas.ax.plot(range(len(allVals)), allVals)
        self.plotWidget.canvas.draw()

    def plotRange(self):
        lower = self.spinLower.value()
        upper = self.spinUpper.value()
        for i in range(lower, upper+1):
            values = []
            allVals = self.calcAll(i, values)
            self.plotWidget.canvas.ax.plot(range(len(allVals)), allVals)
            self.plotWidget.canvas.draw()
        

    def save(self):
        self.plotWidget.canvas.fig.savefig("Figure.pdf");


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    win = Window()
    win.show()
    sys.exit(app.exec())