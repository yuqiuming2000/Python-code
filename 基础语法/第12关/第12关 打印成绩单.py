class 成绩单():
    @classmethod
    def 录入成绩单(cls):
        cls.学生姓名 = input('请输入学生姓名：')
        cls.语文_成绩 = int(input('请输入语文成绩：'))
        cls.数学_成绩 = int(input('请输入数学成绩：'))
        
    @classmethod
    def 打印成绩单(cls):
        print(cls.学生姓名 + '的成绩单如下：')
        print('语文成绩：'+ str(cls.语文_成绩))
        print('数学成绩：'+ str(cls.数学_成绩))
    @classmethod
    def 打印平均分(cls):
        cls.总分=cls.语文_成绩+cls.数学_成绩
        cls.平均分=cls.总分/2
        print(cls.学生姓名 + '的平均分是：'+str(cls.平均分))
    @classmethod
    def 评级(cls):
        if cls.平均分>=90:
            print(cls.学生姓名 + '的评级是：优')
        elif 80<=cls.平均分<90:
            print(cls.学生姓名 + '的评级是：良')
        elif 60<=cls.平均分<80:
            print(cls.学生姓名 + '的评级是：中')
        else:
            print(cls.学生姓名 + '的评级是：差')
成绩单.录入成绩单()
成绩单.打印成绩单()
成绩单.打印平均分()
成绩单.评级()
# print(成绩单.学生姓名 + '的成绩单如下：')
# print('语文成绩：'+ str(成绩单.语文_成绩))
#请写出一个类方法成绩单.打印成绩单()，代替那两句print语句，起到同样的运行效果。
