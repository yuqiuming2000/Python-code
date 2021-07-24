#主人，我的三围是：
# 胸围：33
# 腰围：44
# 臀围：55
# 哈哈哈哈哈，下面粗上面细，我长得像个圆锥。
class A():
    胸围=33
    腰围=44
    臀围=55

    @classmethod
    def B(cls):
        print('主人，我的三围是：')
        print('胸围:{}'.format(cls.胸围))
        print('腰围:{}'.format(cls.腰围))
        print('臀围:{}'.format(cls.臀围))
        print(' 哈哈哈哈哈，下面粗上面细，我长得像个圆锥。')
A.B()


    
