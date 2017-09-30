# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from basic import BasicUi
from createwindow import CreateWindow
from selectwindow import SelectWindow

class BasicWindow(QMainWindow,BasicUi):


    def __init__(self, parent = None):
        super(BasicWindow, self).__init__(parent)
        self.setupUi(self)

        self.creatButton.clicked.connect(self.creatnew)
        self.selectButton.clicked.connect(self.select)

    def creatnew(self):
        self.creatN = CreateWindow()
        self.creatN.show()
        print("creatUI")

    def select(self):
        self.selectN = SelectWindow()
        self.selectN.show()
        print("selectUI")

if __name__ == "__main__":   
    app = QtWidgets.QApplication(sys.argv)
    myWindow = BasicWindow()
    myWindow.show()
    sys.exit(app.exec_())