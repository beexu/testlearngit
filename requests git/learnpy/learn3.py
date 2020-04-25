# 输入某年某月某日，判断这一天是这一年的第几天？
#
# 程序分析：以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：
#
# 程序源代码：

# -*- coding: utf-8 -*-
y = 2015
m = 6
d = 7
days = 0
for i in range(1, m):
    if i % 2 == 0:
        # print(1111)
        # print(i)
        # print(i%2)
        if i == 2:
            if y % 4 == 0:
                days+=29
            else:
                days+=28
        else:
            days+=30

    else:
        days+=31

print(days+d)
