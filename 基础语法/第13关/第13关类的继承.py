class 父类():
    def __init__(self,参数):
        self.变量 = 参数
    def 打印属性(self):
        print('变量的值是：')
        print(self.变量)
class 子类(父类):
    pass  # pass语句代表“什么都不做”
子类实例 = 子类(2)
子类实例.打印属性()

    
