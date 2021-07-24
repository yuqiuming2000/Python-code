class 乘法表():
    def __init__(self,n):
        self.n = n
    def 打印(self):
        for i in range(1,self.n + 1):
            for x in range(1,i+1):
                print( '%d X %d = %d' % (i ,x ,i*x) ,end = '  ' )
            print('  ')

三三乘法表 = 乘法表(3)
三三乘法表.打印()


五五乘法表 = 乘法表(5)
五五乘法表.打印()