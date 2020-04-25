# -*- coding: UTF-8 -*-

def kuaipai(mylist, start, end):
    # 设置前 后start，end
    i, j = start, end
    if i > j:
        return
    print(start)
    base = myList[start]
    while i < j:
        while i < j and mylist[j] >= base:
            j -= 1
        while i < j and mylist[i] <= base:
            i += 1
        print('-------')
        if i < j:
            mylist[i], mylist[j] = mylist[j], mylist[i]
        print('a-------a')
        print(mylist)
        print('b-------b')
    print(start)
    print('c-------c')
    mylist[start] = mylist[i]

    print(mylist[i])
    mylist[i] = base
    print(mylist[i])
    print(mylist)

    kuaipai(mylist, start, i - 1)
    kuaipai(mylist, i + 1, end)


if __name__ == '__main__':
    base = 65
    [65,39,48,88,80]
    [48,39,65,88,80]
    myList = [65, 88, 48, 39, 80]
    kuaipai(myList, 0, len(myList) - 1)
    print(myList)
