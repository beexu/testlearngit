# -*- coding: UTF-8 -*-
import json


class Getpython:
    jsonpathfile = '/Users/beexu/Documents/wengao/requests/pathfile.json'

    def __init__(self):
        pass

    def getjson(self):
        testa = "/Users/beexu/Documents/wengao/requests/pathfile.json"
        res = None
        with open(self.jsonpathfile) as fp:
            res = json.load(fp)
            return res

    def getjsonid(self, id):
        testa = "/Users/beexu/Documents/wengao/requests/pathfile.json"
        res = None
        with open(self.jsonpathfile) as fp:
            res = json.load(fp)
            return res[id]


# test = Getpython()
# a = test.getjson()
# print(a)
# b = test.getjsonid('fisrt')
# print(b)
# # fp = open('/Users/beexu/Documents/wengao/requests/pathfile.json')
# # b = json.load(fp)
# # print(b)
