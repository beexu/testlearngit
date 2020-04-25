#-*- coding: UTF-8 -*-
from mytest.testinter import interface1
import unittest

class learntest001(unittest.TestCase):
    def setUp(self):
        self.testurl = interface1()
        self.url = 'http://lovebee.crazylaw.cn/single/sign.php'

    def test01(self):
        data = {
            'url': 'https://papi.mama.cn/v5_2_0/api/group/my_group_list.php?',
            'version': '6.2.0',
            'device_id': '3ec04a29313a4ba6124f4772678c0c566b7b5e1b',
            'uid': 73700839,
            'appkey': 'pt_android',
            'source': 1,
            'page': 1,
            'perpage': 10
        }
        res = self.testurl.send_get(self.url, data)
        print(res)
        # self.assertEqual(res['status'], 200)
