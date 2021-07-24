class Survey():
    # 收集调查问卷的答案
    def __init__(self, question):
        self.question = question
        self.response = []
    # 显示调查问卷的题目
    def show_question(self):
        print(self.question)
    # 存储问卷搜集的答案2
    def store_response(self, new_response):
        self.response.append(new_response)
# 请定义实名调查问卷的新类 RealNameSurvey，继承自 Survey 类
class RealNameSurvey(Survey):
    def __init__(self, question):
        Survey.__init__(self, question)
        self.response = {}  # 由于籍贯地和名字挂钩，所以用构成为“键值对”的字典来存放。
    # 存储问卷搜集的答案（覆盖父类的类方法）
    def store_response(self, name, new_response):  # 除了 self，还需要两个参数。
        self.response[name] = new_response  # 键值对的新增
survey = RealNameSurvey('你的籍贯地是哪？')
survey.show_question()
while True:
    response = input('请回答问卷问题，按 q 键退出：')
    if response == 'q':
        break