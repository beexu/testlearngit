# -*- coding: UTF-8 -*-
import unittest


def testip(ipnum):
    iplist = ipnum.strip().split('.')
    if len(iplist) != 4:
        print("wrong")
        return False
    if lplist[0] == 0:
        return False
    try:
        for ip in iplist:
            if 1 <= ip <= 255:
                pass
            else:
                return False
    except Exception as e:
        print(e)
        return False
    return True


class testiptest(unittest.TestCase):
    def test_01(self):
        ip = '0.0.0.0'
        self.assertTrue(testip(ip))


if __name__ == '__main__':
    umittest.main()
