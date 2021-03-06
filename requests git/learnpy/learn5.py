# -*- coding: utf-8 -*-
import time

# 生成timestamp
print(time.time())
# 1553938054.279089
print(type(time.time()))
# <class 'float'>

# 从timestamp转换成struct_time
print(time.localtime(time.time()))
# time.struct_time(tm_year=2019, tm_mon=3, tm_mday=30, tm_hour=17, tm_min=32, tm_sec=15, tm_wday=5, tm_yday=89, tm_isdst=0)
print(type(time.localtime(time.time())))
# <class 'time.struct_time'>

#从sturct_time转换成format time
print(time.strftime("%Y-%m-%d %X", time.localtime(time.time())))
# 2019-03-30 17:34:58
print(type(time.strftime("%Y-%m-%d %X", time.localtime(time.time()))))
# <class 'str'>