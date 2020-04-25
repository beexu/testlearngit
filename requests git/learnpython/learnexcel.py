import xlrd
import xlwt
from xlutils.copy import copy
import json

# file = '/Users/beexu/Downloads/孕管后台.xlsx'
# data = xlrd.open_workbook(file)
# print(data.sheet_names())
# table = data.sheets()[0]
# print(table.nrows)
# print(table.ncols)
# print(table.row_values(1))
# print(table.col_values(0))
#
# # sheet相关
# # 获取所有Sheet的name
# print(data.sheet_names())
# # 获取excel里面sheet的总数
# print(data.nsheets)
# # 获取所有Sheet的对象
# print(data.sheets())
# # 获取对应sheetname的对象
# print(data.sheet_by_name("Sheet1"))
# # 通过索引获取
# print(data.sheet_by_index(0))
#
# # sheet里面数据的统计
# x1 = data.sheets()[0]
# # 获取sheet名字
# print(x1.name)
# # 获取sheet行数
# print(x1.nrows)
# # 获取sheet列数
# print(x1.ncols)
#
# # sheet单元批量获取
# # 获取整行的值
# print(x1.row_values(0))
# # 获取整列的值
# print(x1.col_values(0))
#
# # 表操作
# print('aa')
# # 获取行的值
# print(x1.row_values(0, 1, 3))
# # 获取列的值
# print(x1.col_values(0, 1, 10))
#

class ExcelMethod:

    def GetExcel(self):
        data1 = xlrd.open_workbook('/Users/beexu/Downloads/孕管后台.xlsx')
        xsheet = data1.sheets()[0]
        countrow = xsheet.nrows
        # for写法
        # print(countrow)
        # data2 = []
        # for i in range(countrow):
        #     # data2 = xsheet.row_values(i) 这样写会越界
        #     data2.append(xsheet.row_values(i))

        # print(data2)
        # while测试

        x = 1
        data2 = []
        while x < countrow:
            data2.append(xsheet.row_values(x))
            x = x + 1
        return data2

    def GettestExcel(self, x, y):
        testflie = '/Users/beexu/Documents/wengao/requests/工作簿1.xlsx'
        data3 = xlrd.open_workbook(testflie)
        testsheet = data3.sheets()[0]
        xy = testsheet.cell_value(x, y)
        return xy

    def GettestRow(self):
        data = xlrd.open_workbook('/Users/beexu/Documents/wengao/requests/工作簿1.xlsx')
        datasheet =data.sheets()[0]
        countrow = datasheet.nrows
        return countrow

    def WriteEXcel(self, i, res):
        testfile = '/Users/beexu/Documents/wengao/requests/工作簿1.xlsx'
        data = xlrd.open_workbook(testfile)
        data1 = copy(data)
        data2 = data1.get_sheet(0)
        res = json.dumps(res, ensure_ascii=False)
        data2.write(i, 4, res)
        data1.save(testfile)

    def WriteCode(self, i, state):
        testfile = '/Users/beexu/Documents/wengao/requests/工作簿1.xlsx'
        data = xlrd.open_workbook(testfile)
        data1 = copy(data)
        data2 = data1.get_sheet(0)
        data2.write(i, 5, state)
        data1.save(testfile)

    def Getreturn(self, i):
        testfile = '/Users/beexu/Documents/wengao/requests/工作簿1.xlsx'
        data = xlrd.open_workbook(testfile)
        data2 = data.sheets()[0]
        getreturndata = data2.cell_value(i, 6)
        return getreturndata







#
# test = ExcelMethod()
# result = test.GetExcel()
# print(result)
# print(result[0])
# print(result[1])
# result1 = test.GettestExcel(0, 0)
# print(result1)

