# -*- coding: UTF-8 -*-
# 冒泡排序法

def maopao(mylist):
    for j in range(len(mylist) - 1):
        for i in range(len(mylist) - 1 - j):
            if mylist[i] > mylist[i + 1]:
                mylist[i], mylist[i + 1] = mylist[i + 1], mylist[i]
    return mylist


if __name__ == '__main__':
    list1 = [48, 33, 25, 66]
    L = maopao(list1)
    print(L)
