# -*- coding: UTF-8 -*-
# 快速排序

def kuaipai(list, start, left):
    i, j = start, left
    if i > j:
        return
    base = list[start]
    while i < j:
        while i < j and list[j] >= base:
            j -= 1
        while i < j and list[i] <= base:
            i += 1
        list[i], list[j] = list[j], list[i]
    list[start] = list[i]
    list[i] = base

    kuaipai(list, start, i - 1)
    kuaipai(list, i + 1, left)


if __name__ == '__main__':
    list = [65, 88, 48, 39, 80]
    kuaipai(list, 0, len(list) - 1)
    print(list)
