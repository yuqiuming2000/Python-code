# 大家注意了！
# 一个叫“吉多”的人来了。
# 大家注意了！
# 一个叫“范罗苏姆”的男人来了。
# 大家注意了！
# 那个叫“范罗苏姆”的男人留下了他的背影。
class Person:
    def __init__(self, name):
        self.name = name
        print('大家注意了！')
    def show(self):
        print('一个叫“%s”的人来了。' % self.name)
class Man(Person):
    # def __init__(self):
    #     Person.__init__(self, name='范罗苏姆')  # 继承的基础上做一些改变
    #     # 上面的括号里也可以写成(self,'范罗苏姆')，但加上参数后清晰一些，代码看起来更清晰。
    def leave(self):  # 子类定制新方法
        print('那个叫“%s”的男人留下了他的背影。' % self.name)
author1 = Person('吉多')
author1.show()
# author2 = Man('范姆雷特')
# author2.show()
author3 = Man('范姆雷特')
author3.show()
author3.leave()
