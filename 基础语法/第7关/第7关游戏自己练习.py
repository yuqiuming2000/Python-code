import time,random
My_score=0
Enemy_score=0
for i in range(1,4):
    print('现在是第%s关'%i)
    My_life=random.randint(100,150)
    Enemy_life=random.randint(100,150)
    My_stack=random.randint(30,50)
    Enemy_stack=random.randint(30,50)
    print('玩家\n血量：%s 攻击值：%s'%(My_life,My_stack))
    time.sleep(5)
    print('敌人\n血量：%s 攻击值：%s'%(Enemy_life,Enemy_stack))
    time.sleep(5)
    while My_life > 0 and Enemy_life > 0:
         My_life= My_life-Enemy_stack
         Enemy_life=Enemy_life-My_life
         print('敌人发起了攻击，玩家血量%s'%My_life)
         print('玩家发起了攻击，敌人血量%s'%Enemy_life)
    if My_life > 0 and Enemy_life <=0:
         My_score=My_score+1
         print('玩家赢了')
    elif My_life <=0 and Enemy_life >0:
         Enemy_score=Enemy_score+1
         print('敌人赢了')
    else:
         print('打和了')
if My_score>Enemy_score:
        print('最终结果：玩家赢了')
elif My_score<Enemy_score:
        print('最终结果：敌人赢了')
else:
        print('最终结果：打和了')


