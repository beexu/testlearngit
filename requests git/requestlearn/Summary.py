# -*- coding: UTF-8 -*-
# 最后，从unittest模块调用main（）方法

from sample.getpost import requestmethod
from sample.sample1 import Testget
from sample.sample2 import healthFragrance

import unittest

# 如果直接运行该文件(__name__值为__main__),则执行以下语句，常用于测试脚本是否能够正常运行
if __name__ == '__main__':
    unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(healthFragrance('test02'))
    # # suite.addTest(learntest('test02'))
    # # print(suite)
    # runner = unittest.TextTestRunner(verbosity=2).run(suite)
    # print(runner)

    # 8.2执行测试用例方案二如下：
    # 8.2.1先构造测试集
    # 8.2.1.1实例化测试套件
    # suite = unittest.TestSuite()
    # 8.2.1.2将测试用例加载到测试套件中。
    # 执行顺序是安装加载顺序：先执行test_case2，再执行test_case1
    # suite.addTest(Test('test_case2'))
    # suite.addTest(Test('test_case1'))
    # 8.2.2执行测试用例
    # 8.2.2.1实例化TextTestRunner类
    # runner = unittest.TextTestRunner()
    # 8.2.2.2使用run()方法运行测试套件（即运行测试套件中的所有用例）
    # runner.run(suite)
