# -*- coding: UTF-8 -*-
from mytest.testinter import interface1
import unittest


class learntest002(unittest.TestCase):
    def setUp(self):
        self.testurl = interface1()
        self.url = 'http://lovebee.crazylaw.cn/single/sign.php'

    def test02(self):
        data1 = {
            'url': 'https://papi.mama.cn/api/new_record/add?',
            'source': 1,
            'device_id': '3ec04a29313a4ba6124f4772678c0c566b7b5e1b',
            'uid': 73700839,
            'version': '6.2.0',
            'bid': 23844204,
            'username': 'mumt10',
            'category': 1,
            'type': 1,
            'view_status': 1,
            'content': 'content',
            'title': 'title',
            'tag': [{"tag_is_first": "1", "tag_name": "", "tag_id": ""},
                    {"tag_is_first": "0", "tag_name": "", "tag_id": ""}],
            'record_date': '2018-07-16',
            'location': ' ',
            'appkey': 'pt_android'
        }
        res = self.testurl.send_post(self.url, data1)
        # assertEqual(self, first, second, msg=SBB)
        print(res)
