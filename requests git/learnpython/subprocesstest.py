# -*- coding: UTF-8 -*-

import subprocess


def test(args1):
    ret = subprocess.Popen(args1, shell=True)

    # if ret.returncode == 0:
    #     print("success:", ret)
    # else:
    #     print("error:", ret)
    print(ret)


if __name__ == '__main__':
    args11 = 'ping www.baidu.com'
    args12 = 'ls -l'
    test(args11)
