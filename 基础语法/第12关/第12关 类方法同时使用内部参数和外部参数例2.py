class 加100类():
    变量 = 100

    @classmethod
    def 加100函数(cls,参数1,参数2,参数3):
        总和 = cls.变量 + 参数1 + 参数2 + 参数3
        print('加100函数计算结果如下：')
        print(总和)
参数1 = int(input('请输入一个整数：'))
参数2 = int(input('请输入一个整数：'))
参数3 = int(input('请输入一个整数：'))
加100类.加100函数(参数1,参数2,参数3)
