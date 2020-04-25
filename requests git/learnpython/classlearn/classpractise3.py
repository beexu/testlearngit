# -*- coding: UTF-8 -*-
# 题目四：定义一个字典类：dictclass。完成下面的功能：
#
# dict = dictclass({你需要操作的字典对象})
#
#     1 删除某个key
#
#         del_dict(key)
#
#     2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
#
#         get_dict(key)
#
#     3 返回键组成的列表：返回类型;(list)
#
#         get_key()
#
#     4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
#
#         update_dict({要合并的字典})

class dictclass:
    def __init__(self, dict1):
        self.dict = dict1

    def del_dict(self, key):
        del self.dict[key]

    def get_dict(self, key):
        if key in self.dict:
            return self.dict[key]
        else:
            return 'notfount'

    def get_key(self):
        return type(self.dict)

dictbbb = {1:'aaa','b':'bbb','c':'ccc','d':'ddd'}

dicttest = dictclass(dictbbb)
a = dicttest.get_key()
print(a)

b = dicttest.get_dict('b')
print(b)
c = dicttest.get_dict('g')
print(c)
d = dicttest.del_dict('d')





