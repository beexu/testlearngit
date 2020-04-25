# -*- coding: UTF-8 -*-
# 步骤1 - 在程序中导入unittest模块。
# 步骤2 - 定义要测试的功能。自定义一个requestmethod
import requests
import json


class requestmethod:
    def __init__(self):
        pass

    def getpostmethod(self, method, url, params):
        if method == 'get':
            res = requests.get(url,
                               params=params)  # verify是否验证服务器的SSL证书 res = requests.get(url, params=params, verify=False)
            code = res.status_code
            # resjson=res.json()
            # resdump = json.dumps(resjson, indent=2)
            # resreturn = json.loads(resdump)
            restext = res.text
            # print(restext)
            print(code)
            print('----------------------')
            print(res.text)
            return code, res
        elif method == 'post':
            print(nonono)
            pass

    def jointogether(self, firsturl, endurl):
        print(firsturl)
        print(endurl)
        Actualurl = firsturl + endurl
        return Actualurl
