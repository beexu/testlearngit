# -*- coding: UTF-8 -*-
import re


def find1(hero):
    sanguo = open('sanguo.txt', encoding='gb18030')
    sanguotxt = sanguo.read()
    sanguotxt1 = sanguotxt.replace('\n', '')
    num = re.findall(hero, sanguotxt1)
    num1 = len(num)
    print(num1)
    return num1


def heronum():
    herodic = {}
    h = open('name.txt')
    hname = h.read()
    data = hname.split('|')
    # print(data)
    for i in data:
        # print(i)
        num = find1(i)
        herodic[i] = num
    print(herodic)


if __name__ == '__main__':
    heronum()
    # hero = '馬超'
    # find1(hero)
