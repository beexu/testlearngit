# -*- coding: UTF-8 -*-

import requests
import sys
import unittest

# sys.path.insert(0, '..')  # 这个可以
sys.path.append('..')
# 这个不行


# print(sys.path)
from learnexcel import *
from learnfixexcel import *
from learnjson import *
from mytest.testinter import *


class testurl(unittest.TestCase):
    def __init__(self):
        self.learnexcel1 = ExcelMethod()
        self.learnfixexcel1 = fixtest()
        self.learnjson1 = Getpython()
        self.testinter1 = interface1()

    def run(self, methon, path):
        self.url = "http://lovebee.crazylaw.cn/single/sign.php"
        if methon == "get":
            res, code = self.testinter1.send_get(self.url, path)
            return res, code
        elif methon == "post":
            res, code = self.testinter1.send_post(self.url, path)
            return res, code

    def test(self):
        row = self.learnexcel1.GettestRow()
        truepath = ''
        a = []
        for i in range(1, row):
            print(i)
            url = self.learnfixexcel1.getexcelurl(i)
            methon = self.learnfixexcel1.getexcelmethon(i)
            path = self.learnfixexcel1.getexcelpath(i)
            try:
                truepath = {'url': ''}
                truepath['url'] = url
                # print(truepath)
                littletruepath = self.learnjson1.getjsonid(path)
                for key, value in littletruepath.items():
                    truepath[key] = littletruepath[key]
                # print('aaa')
                # print(truepath)
            except Exception as e:
                # traceback = __import__('traceback')
                # print(traceback.print_exc())print_exc
                print(e)
            result, code = self.run(methon, truepath)
            # 存入excel
            self.learnexcel1.WriteEXcel(i, result)
            self.learnexcel1.WriteCode(i, code)
            returndata = self.learnexcel1.Getreturn(i)
            self.assertIn(returndata, result)
            print("test")
            print(code)
            print(returndata)
            # result = self.testinter1.send_get('http://lovebee.crazylaw.cn/single/sign.php', truepath)
            # result = self.testinter1.send_post('http://lovebee.crazylaw.cn/single/sign.php', truepath)
            # print(result)
            one1 = type(result)

            a.append(result)


        return a


if __name__ == '__main__':
    testa = testurl().test()
    print(testa)
