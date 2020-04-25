# -*- coding: UTF-8 -*-
# 通过对unittest.TestCase进行子类化创建测试用例。
import unittest
from .getpost import requestmethod


class Testget(unittest.TestCase):

    # setUp():setUp()方法用于测试用例执行前的初始化工作。
    def setUp(self):
        self.requestmethod = requestmethod()
        self.urlfirst = 'https://test-get99-vapi-m.xgo.city'

    # 将测试定义为类中的方法。方法名称必须以"test"开头。
    # @unittest.skip('暂时跳过用例3的测试')
    def test01(self):
        path = '/Advert/Advert/getRecommendList'
        url = self.requestmethod.jointogether(self.urlfirst, path)
        method = 'get'
        data = {
            'cur_page': '1',
            'city_id': '60000000',
            'state_id': '2332453',
            'country_id': '2328926'
        }
        a = self.requestmethod.getpostmethod(method, url, data)

    # tearDown():tearDown()方法用于测试用例执行之后的善后工作
    def tearDown(self):
        print('aaaaa')

