# -*- coding: utf-8 -*-
# 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

for i in range(1, 5):
    # print(i)
    for a in range(1, 5):
        # print(a)
        for d in range(1, 5):
            # print(d)
            if i != a and a != d and i != d:
                print(i, a, d)
            else:
                print("double")
