class 成绩单():
    @classmethod
    def 录入成绩单(cls):
        cls.学生姓名 = input('请输入学生姓名：')
        cls.成绩 = int(input('请输入考试成绩：'))

    @classmethod
    def 计算是否及格(cls):
        if cls.成绩 >= 60:
            return '及格'
        else:
            return '不及格'

    @classmethod
    def 考试结果(cls):
        if cls.计算是否及格()=='及格':
            print('王明明同学考试通过啦！')
        else:
            print('王明明同学需要补考！')

成绩单.录入成绩单()
成绩单.考试结果()

