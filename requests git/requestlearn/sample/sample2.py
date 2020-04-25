# -*- coding: UTF-8 -*-
import unittest
from .getpost import requestmethod


class healthFragrance(unittest.TestCase):

    def setUp(self):
        self.firsturl = 'https://test-get99-vapi-m.xgo.city'
        self.requestmethod = requestmethod()

    def test02(self):
        method = 'get'
        path = '/category/Attribute/getEnumByNames'
        url = self.requestmethod.jointogether(self.firsturl, path)
        data = {
            'category_id': '197'
        }
        self.requestmethod.getpostmethod(method, url, params=data)
