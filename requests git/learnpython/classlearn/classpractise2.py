# -*- coding: UTF-8 -*-

# 题目三：定义一个学生类
#
# 有下面的类属性：
#
# 1 姓名
#
# 2 年龄
#
# 3 成绩（语文，数学，英语)[每课成绩的类型为整数]
#
# 类方法：
#
# 1 获取学生的姓名：get_name() 返回类型:str
#
# 2 获取学生的年龄：get_age() 返回类型:int
#
# 3 返回3门科目中最高的分数。get_course() 返回类型:int
#
# 写好类以后，可以定义2个同学测试下:

class Student:
    def __init__(self, name, age, chinesescore, mathscore, englishscore):
        self.name = name
        self.age = age
        self.chinesescore = chinesescore
        self.mathscore = mathscore
        self.englishscore = englishscore

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_course(self):
        scorelist = [self.chinesescore, self.mathscore, self.englishscore]
        print(type(scorelist))
        maxscroe = max(scorelist)
        print(maxscroe)
        return maxscroe


studet1 = Student('student1', 22, 88, 99, 100)
student1maxscore = studet1.get_course()
print(student1maxscore)
