# 你的幸运数是多少？请输入一个整数。（用户输入：66）
# 好的，我把它存了起来，然后翻了888倍还给你：58608



class 类():
    @classmethod
    def Double(cls):
        print('好的，我把它存了起来，然后翻了888倍还给你：{}'.format(cls.lucky_number*888))
类.lucky_number = int(input('请你的幸运数是多少？请输入一个整数。'))
类.Double()
    

