# -*- coding: UTF-8 -*-
import requests
import json
import urllib


class interface1:
    def __init__(self):
        pass

    def send_get(self, url, data=None):
        res = None
        data = data
        res = requests.get(url, data)
        # one = type(res)
        res = res.json()
        returnres = json.dumps(res, indent=2)
        returnresdict = json.loads(returnres)
        # #
        # # # 做数据拼接工作
        if 't' in returnresdict.keys() and 'sign' in returnresdict.keys():
            data['sign'] = returnresdict['sign']
            data['t'] = returnresdict['t']
            if 'app_auth_token' in returnresdict.keys():
                data['app_auth_token'] = returnresdict['app_auth_token']
            else:
                pass
        else:
            print('没有t 和sign')

        urlget = data['url']
        del data['url']
        result = requests.get(urlget, data)
        code = result.status_code
        result = result.json()
        # result = json.dumps(result, indent=2, ensure_ascii=False)
        return result, code

    def send_post(self, url, data=None):
        res = None
        res = requests.get(url, data)
        res = res.json()
        returnres = json.dumps(res, indent=2)
        returnresdict = json.loads(returnres)
        # 做接口测试的拼接操作
        if 't' in returnresdict.keys() and 'sign' in returnresdict.keys():
            data['sign'] = returnresdict['sign']
            data['t'] = returnresdict['t']
            if 'app_auth_token' in returnresdict.keys():
                data['app_auth_token'] = returnresdict['app_auth_token']
            else:
                pass
        else:
            print('没有t 和sign')
        urlget = data['url']
        del data['url']
        result = requests.post(urlget, data)
        code = result.status_code
        result = result.json()
        # result = json.dumps(result, indent=2, ensure_ascii=False)
        return result, code


# if __name__ == '__main__':
#     ceshi = interface1()
#     data = {
#         "url": 'https://papi.mama.cn/v5_2_0/api/group/my_group_list.php?',
#         "version": "6.2.0",
#         "device_id": "3ec04a29313a4ba6124f4772678c0c566b7b5e1b",
#         "uid": 73700839,
#         "appkey": "pt_android",
#         "source": 1,
#         "page": 1,
#         "perpage": 10
#     }
#     res = ceshi.send_get('http://lovebee.crazylaw.cn/single/sign.php', data)
#     print(res)
