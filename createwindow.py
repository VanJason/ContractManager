# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from createnew import CreatUi
import xlrd
import xlwt
import xlutils
from xlutils.copy import copy

class CreateWindow(QMainWindow,CreatUi):
    prolist = [None,None,None,None,None,None]
    accountlist = [None,None,None,None,None,None]

    data = xlrd.open_workbook('contractMA.xls')
    table = data.sheets()[0]
    nrows = table.nrows

    def __init__(self, parent=None):
        super(CreateWindow, self).__init__(parent)
        self.setupUi(self)

        self.pronumber.textEdited['QString'].connect(self.get_Pnumber)
        self.proname.textEdited['QString'].connect(self.get_Pname)
        self.dutyname.textEdited['QString'].connect(self.get_Pduty)
        self.prodate.userDateChanged['QDate'].connect(self.get_Pdate)
        self.proaccount.textEdited['QString'].connect(self.get_Paccount)
        self.receiveaccount.textEdited['QString'].connect(self.get_reciveaccount)
        self.receivedate.userDateChanged['QDate'].connect(self.get_receivedate)
        self.payaccount.textEdited['QString'].connect(self.get_payaccount)
        self.paydate.userDateChanged['QDate'].connect(self.get_paydate)
        self.sucessButton.clicked.connect(self.do_sucess)
        self.clearButton.clicked.connect(self.do_clear)
        self.closeButton.clicked.connect(self.close)
        self.apartment.activated['QString'].connect(self.get_apartment)
        self.accounttype.activated['QString'].connect(self.get_accounttype)
        self.protype.activated['QString'].connect(self.get_Ptype)

    def get_Pnumber(self,QString):
        self.prolist[0] = QString

    def get_Pname(self,QString):
        self.prolist[1] = QString

    def get_Ptype(self,QString):
        self.prolist[2] = QString

    def get_Pduty(self,QString):
        self.prolist[3] = QString

    def get_apartment(self,QString):
        self.prolist[4] = QString

    def get_Pdate(self,QDate):
        datetuple = QDate.getDate()
        datelist = []
        for datetuple_unit in datetuple:
        	datelist.append(datetuple_unit)
        self.prolist[5] = datelist

    def get_Paccount(self,QString):
        self.accountlist[0] = QString

    def get_accounttype(self,QString):
        self.accountlist[1] = QString

    def get_reciveaccount(self,QString):
        self.accountlist[2] = QString

    def get_receivedate(self,QDate):
        datetuple = QDate.getDate()
        self.accountlist[3] = datetuple

    def get_payaccount(self,QString):
        self.accountlist[4] = QString

    def get_paydate(self,QDate):
        datetuple = QDate.getDate()
        self.accountlist[5] = datetuple

    def do_sucess(self):

        datachange = copy(self.data)
        tablechange = datachange.get_sheet(0)
        row = self.nrows

        tablechange.write(row,0,self.prolist[0])
        tablechange.write(row,1,self.prolist[1])
        tablechange.write(row,2,self.prolist[2])
        tablechange.write(row,3,self.prolist[3])
        tablechange.write(row,4,self.prolist[4])
        tablechange.write(row,5,self.prolist[5])

        tablechange.write(row,6,self.accountlist[0])
        tablechange.write(row,7,self.accountlist[1])
        tablechange.write(row,8,self.accountlist[2])
        tablechange.write(row,9,self.accountlist[3])
        tablechange.write(row,10,self.accountlist[4])
        tablechange.write(row,11,self.accountlist[5])

        datachange.save('contractMA.xls')
        QtWidgets.QMessageBox.information(self.sucessButton,"标题","成功")

    def do_clear(self):
        self.prolist = [None,None,None,None,None,None]
        self.accountlist = [None,None,None,None,None,None]
        self.proname.clear()
        self.pronumber.clear()
        self.protype.clear()
        self.apartment.clear()
        self.dutyname.clear()
        self.proaccount.clear()
        self.moneytpye.clear()
        self.receiveaccount.clear()
        self.payaccount.clear()
        self.prodate.clear()
        self.receivedate.clear()
        self.paydate.clear()
