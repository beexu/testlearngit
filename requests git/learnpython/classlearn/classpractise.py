# -*- coding: UTF-8 -*-
# 练习:
# 自己定义一个类Human（人类),有两个属性：姓名/年龄，有3个方法：设置姓名(setName)作用是添加或修改,设置年龄(setage)添加或修改
# 显示信息(infos)显示人的信息
# 用此类来创建 两个对象:张3，20岁。李四，21岁。
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def printimfomation(self):
        print(self.name)
        print(self.age)

zhang1 = Human('张三', '20岁')
lisi = Human('李四', '21岁')

zhang1.printimfomation()
lisi.printimfomation()



