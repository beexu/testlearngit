#-*- coding: UTF-8 -*-

from mytest.learntest01 import learntest001
from mytest.learntest02 import learntest002
from util.HTMLTestRunner_PY3 import HTMLTestRunner
# import util.HTMLTestRunner_PY3
from mytest.testinter import *


import unittest


# class learntest(unittest.TestCase):
#     def setUp(self):
#         self.testurl = interface()
#         self.url = 'http://lovebee.crazylaw.cn/single/sign.php'
#
#     def test01(self):
#         data = {
#             'url': 'https://papi.mama.cn/v5_2_0/api/group/my_group_list.php?',
#             'version': '6.2.0',
#             'device_id': '3ec04a29313a4ba6124f4772678c0c566b7b5e1b',
#             'uid': 73700839,
#             'appkey': 'pt_android',
#             'source': 1,
#             'page': 1,
#             'perpage': 10
#         }
#         res = self.testurl.send_get(self.url, data)
#         print(res)
#
#     def test02(self):
#         data1 = {
#             'url': 'https://papi.mama.cn/api/new_record/add?',
#             'source': 1,
#             'device_id': '3ec04a29313a4ba6124f4772678c0c566b7b5e1b',
#             'uid': 73700839,
#             'version': '6.2.0',
#             'bid': 23844204,
#             'username': 'mumt10',
#             'category': 1,
#             'type': 1,
#             'view_status': 1,
#             'content': 'content',
#             'title': 'title',
#             'tag': [{"tag_is_first": "1", "tag_name": "", "tag_id": ""},
#                     {"tag_is_first": "0", "tag_name": "", "tag_id": ""}],
#             'record_date': '2018-07-16',
#             'location': ' ',
#             'appkey': 'pt_android'
#         }
#         res = self.testurl.send_post(self.url, data1)
#         # assertEqual(self, first, second, msg=SBB)
#         print(res)

    # def suite():
    #     suite = unittest.TestSuite()
    #     suite.addTest(learntest('test01'))
    #     suite.addTest(learntest('test02'))
    #     return suite
    #
    # def suite2():
    #     test = ['test01', 'test02']
    #     return unittest.TestSuite(map(learntest, test))


if __name__ == '__main__':
    # unittest.main()
    # 方法一
    # suite = unittest.TestSuite()
    # suite.addTest(learntest('test01'))
    # suite.addTest(learntest('test02'))
    # print(suite)
    # runner = unittest.TextTestRunner(verbosity=2).run(suite)
    # print(runner)

    # 方法二
    # 在方法里添加一个方法，并在方法里添加好测试用例，并返回一个测试集
    # def suite():
    #     suite = unittest.TestSuite()
    #     suite.addTest(learntest('test01'))
    #     suite.addTest(learntest('test02'))
    #     return suite
    # runner = unittest.TextTestRunner().run(learntest.suite())

    # 方法三
    # 在方法里添加一个方法，并在方法里添加测试用例，用到unittest.TestSuite(map(learntest, test))
    #     def suite2():
    #         test = ['test01', 'test02']
    #         return unittest.TestSuite(map(learntest, test))
    # runner = unittest.TextTestRunner().run(learntest.suite2())

    # 方法四
    #
    # a = unittest.TestLoader().loadTestsFromTestCase(learntest)
    # print(a)
    # runner = unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(learntest))

    # 方法五（不同文件的loadTestsFromTestCase）
    suite1 = unittest.TestLoader().loadTestsFromTestCase(learntest001)
    # print(suite1)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(learntest002)
    alltests = unittest.TestSuite([suite1, suite2])
    # print(alltests)

    # runner = unittest.TextTestRunner().run(alltests)

    file = '/Users/beexu/Documents/wengao/requests/Htmlreport/html1.html'
    with open(file, 'wb') as f:
        # runner = util.HTMLTestRunner_PY3.HTMLTestRunner(f, verbosity=2, title='示例测试报告', description='执行人：灰蓝')
        runner = HTMLTestRunner(f, verbosity=2, title='示例测试报告', description='执行人：灰蓝')
        runner.run(alltests)
        # runner.run(suite1)

















# data1 = {
#     'url':'https://papi.mama.cn/api/new_record/add?',
#     'source':1,
#     'device_id':'3ec04a29313a4ba6124f4772678c0c566b7b5e1b',
#     'uid': 73700839,
#     'version':'6.2.0',
#     'bid': 23844204,
#     'username':'mumt10',
#     'category':1,
#     'type':1,
#     'view_status':1,
#     'content':'content',
#     'title':'title',
#     'tag':[{"tag_is_first":"1","tag_name":"","tag_id":""},{"tag_is_first":"0","tag_name":"","tag_id":""}],
#     'record_date':'2018-07-16',
#     'location':' ',
#     'appkey': 'pt_android'
# }
# url = 'http://lovebee.crazylaw.cn/single/sign.php'
# test = interface()
# run = test.send_post(url, data1)
# print(isinstance(run, dict))
# print(run)
# # print(run.text)


# data = {
#     'url': 'https://papi.mama.cn/v5_2_0/api/group/my_group_list.php?',
#     'version': '6.2.0',
#     'device_id': '3ec04a29313a4ba6124f4772678c0c566b7b5e1b',
#     'uid': 73700839,
#     'appkey': 'pt_android',
#     'source': 1,
#     'page': 1,
#     'perpage': 10
# }
#
# url = 'http://lovebee.crazylaw.cn/single/sign.php'
# run = send_get(url, data)
# print(run)
# print(type(run))
# result = json.loads(run)
# print(result)

# 之前学习的
# print(isinstance(result, dict))
# data['t'] = result['t']
# data['sign'] = result['sign']
# data['app_auth_token'] = result['app_auth_token']
# print(data)

# r = requests.get('https://api.github.com/events')
# print(r.text)
# print(r.url)
# print(r.encoding)
# print(r.json())
# print(r.status_code)
# print(r.headers)
# print(r.history)
