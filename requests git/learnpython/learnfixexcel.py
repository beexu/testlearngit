# -*- coding: UTF-8 -*-
# from learnpython.learnexcel import *
# from learnpython.configdata import *
from configdata import *
from learnexcel import *


class fixtest:
    def __init__(self):
        self.exceltest = ExcelMethod()
        self.configtest = globalconfig()

    def getexcelid(self, casenum):
        id = getid()
        excelid = self.exceltest.GettestExcel(casenum, id)
        return excelid

    def getexcelurl(self, casenum):
        url = geturl()
        excelurl = self.exceltest.GettestExcel(casenum, url)
        return excelurl

    def getexcelmethon(self, casenum):
        methon = getmethon()
        excelmethon = self.exceltest.GettestExcel(casenum, methon)
        return excelmethon

    def getexcelpath(self, casenum):
        path = getpath()
        excelpath = self.exceltest.GettestExcel(casenum, path)
        return excelpath




casenum = 2
a = fixtest()
b = a.getexcelid(casenum)
c = a.getexcelurl(casenum)
d = a.getexcelmethon(casenum)
# print(d)
