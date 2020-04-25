# -*- coding: UTF-8 -*-

def test(mylist):
    j = ''
    for i in mylist:
        j = j + str(i)
    print(j)


if __name__ == '__main__':
    L = [1, 2, 3, 5, 6]
    test(L)
