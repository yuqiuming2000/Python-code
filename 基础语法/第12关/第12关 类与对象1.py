class 智能机器人():
    胸围 = 33
    腰围 = 44
    臀围 = 55
    智商 = 200
    # 以上为类属性
    def 打招呼():
        print('主人你好！')
    def 卖萌():
        print('主人，求抱抱！')
    def 生气():
        print('主人，我要报警了！')
    def 奔跑():
        print('我快乐地奔跑、奔跑……哎呦喂！撞墙了。')

print('把类的属性打印出来：')
print(智能机器人.胸围)
print(智能机器人.腰围)
print(智能机器人.腰围)
print(智能机器人.智商)
智能机器人.打招呼()
智能机器人.卖萌()
智能机器人.奔跑()

#智能机器人.奔跑()，当运行这个方法的时候，屏幕上会打印出一串字符:我快乐地奔跑、奔跑……哎呦喂！撞墙了。
#智商 = 200，当运行print(智能机器人.智商)这个的时候，屏幕上会打印出200。请补全代码。