# 运行代码即可。
import time,random

player_list =  ['【狂血战士】','【森林箭手】','【光明骑士】','【独行剑客】','【格斗大师】','【枪弹专家】']
enemy_list = ['【暗黑战士】','【黑暗弩手】','【暗夜骑士】','【嗜血刀客】','【首席刺客】','【陷阱之王】']
players = random.sample(player_list,3)  
enemies = random.sample(enemy_list,3)
player_info = {}
enemy_info = {}

# 随机生成两种属性
def born_role():
    life = random.randint(100,180)
    attack = random.randint(30,50)
    return life,attack  # return 多个元素时，返回一个元组（昨天课堂有讲）
    
# 给角色生成随机属性，并展示角色信息。
def show_role():
    for i in range(3):
        player_info[players[i]] = born_role()
        enemy_info[enemies[i]] = born_role()
    
    # 展示我方的3个角色
    print('----------------- 角色信息 -----------------')
    print('你的人物：')
    for i in range(3):
        print('%s  血量：%d  攻击：%d' 
        %(players[i],player_info[players[i]][0],player_info[players[i]][1]))
    print('--------------------------------------------')
    print('电脑敌人：')
    
    # 展示敌方的3个角色
    for i in range(3):
        print('%s  血量：%d  攻击：%d' 
        %(enemies[i],enemy_info[enemies[i]][0],enemy_info[enemies[i]][1]))
    print('--------------------------------------------')

show_role()