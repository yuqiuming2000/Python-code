class 成绩单():
    @classmethod
    def 录入成绩单(cls):
        cls.学生姓名 = input('请输入学生姓名：')
        cls.语文_成绩 = int(input('请输入语文成绩：'))
        cls.数学_成绩 = int(input('请输入数学成绩：'))

    @classmethod
    def 计算平均分(cls):
        平均分 = (cls.语文_成绩 + cls.数学_成绩)/2
        return 平均分

    @classmethod
    def 评级(cls):
        平均分 = cls.计算平均分()
        if 平均分>=90:
            print(cls.学生姓名 + '的评级是：优')
        elif 平均分>= 80 and 平均分<90 :
            print(cls.学生姓名 + '的评级是：良')
        elif 平均分>= 60 and 平均分<80 :
            print(cls.学生姓名 + '的评级是：中')
        else:
            print(cls.学生姓名 + '的评级是：差')

成绩单.录入成绩单()
成绩单.评级()
