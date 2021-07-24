sentence = '从前有座山，'
def mountain():
    print('山里有座庙，')
class Temple:
    sentence = '庙里有个老和尚，'
    @classmethod
    def reading(cls):
        print('在讲故事，')
class Story:
    sentence = '一个长长的故事。'
    def reading(self):
        print('讲的什么故事呢？')
