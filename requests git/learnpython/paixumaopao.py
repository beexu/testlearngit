# -*- coding: UTF-8 -*-
# 排序冒泡法https://www.jianshu.com/p/e8ae3a0bc2e4

def main():
    li = [10, 8, 4, 7, 5]

    for i in range(len(li) - 1):
        for j in range(len(li) - 1 - i):
            if li[j] > li[j + 1]:
                # 多元赋值
                li[j], li[j + 1] = li[j + 1], li[j]
                print(j)
                print(li)

    li1 = [10, 8, 4, 7, 5]
    li1.sort()
    print(li1)


if __name__ == '__main__':
    main()
