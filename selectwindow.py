# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from select import *
from createwindow import *
import xlrd
import xlwt
import xlutils
from xlutils.copy import copy

class SelectWindow(QMainWindow,SelectUi):
    data = xlrd.open_workbook('contractMA.xls')
    table = data.sheets()[0]
    nrows = table.nrows
    row = int(nrows)

    listall = dict()
    listcell = dict()
    listbuy = dict()
    listelse = dict()

    i = 1
    while i < row:
        listall[i] = (table.row_values(i))
        i +=1

    for listall_unit in listall.values():
        if listall_unit[2] == "销售合同":
            site = len(listcell)
            listcell[site] = listall_unit
        elif listall_unit[2] == "采购合同":
            site = len(listbuy)
            listbuy[site] = listall_unit
        else:
            site = len(listelse)
            listelse[site] = listall_unit


    def __init__(self, parent=None):
        super(SelectWindow, self).__init__(parent)
        self.setupUi(self)

        self.selectButton.clicked.connect(self.do_select)
        self.addButton.clicked.connect(self.do_add)
        self.delectButton.clicked.connect(self.do_delect)
        self.changeButton.clicked.connect(self.do_change)
        self.content.clicked['QModelIndex'].connect(self.do_choose)
        self.prolist.clicked['QModelIndex'].connect(self.do_choosedetail)

    def do_select(self):
        print(self.listall)

    def do_add(self):
        self.creatN = CreateWindow()
        self.creatN.show()
        print("creatUI")

    def do_delect(self):
        pass

    def do_change(self):
        pass

    def do_choose(self,QModelIndex):
        listindex = QModelIndex.data()

        if listindex == "全部":
            self.prolist.setRowCount(len(self.listall))
            count = 0
            for listall_unit in self.listall.values():
                site = 0
                while site < len(listall_unit):
                    self.prolist.setItem(count,site,QTableWidgetItem(str(listall_unit[site])))
                    site +=1
                count +=1

        elif listindex == "销售合同":
            self.prolist.setRowCount(len(self.listcell))
            count = 0
            for listcell_unit in self.listcell.values():
                site = 0
                while site < len(listcell_unit):
                    self.prolist.setItem(count,site,QTableWidgetItem(str(listcell_unit[site])))
                    site +=1
                count +=1
        elif listindex == "采购合同":
            self.prolist.setRowCount(len(self.listbuy))
            count = 0
            for listbuy_unit in self.listbuy.values():
                site = 0
                while site < len(listbuy_unit):
                    self.prolist.setItem(count,site,QTableWidgetItem(str(listbuy_unit[site])))
                    site +=1
                count +=1
        else:
            self.prolist.setRowCount(len(self.listelse))
            count = 0
            for listelse_unit in self.listelse.values():
                site = 0
                while site < len(listelse_unit):
                    self.prolist.setItem(count,site,QTableWidgetItem(str(listelse_unit[site])))
                    site +=1
                count +=1

    def do_choosedetail(self,QModelIndex):
        pass

