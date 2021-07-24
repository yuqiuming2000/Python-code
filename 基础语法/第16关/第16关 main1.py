# import test  # 导入test模块

# print(test.a)  # 使用“模块.变量”调用模块中的变量

# test.hi()  # 使用“模块.函数()”调用模块中的函数

# print(test.Go1.a)   # 使用“模块.类.变量”调用模块中的类属性
# test.Go1.do1()  # 使用“模块.类.函数()”调用模块中的类方法

# A = test.Go2()  # 使用“变量 = 模块.类()”实例化模块中的类
# print(A.a)  # 实例化后，不再需要“模块.”
# A.do2()  # 实例化后，不再需要“模块.”

from test import *
print(a)  # 打印变量“a”
hi()  # 调用函数“hi”
print(Go1.a)  # 打印类属性“a”
Go1.do1()  # 调用类方法“Go1”
A = Go2()  # 实例化“Go2”类
print(A.a)  # 打印实例属性“a”
A.do2()  # 调用实例方法“do2”