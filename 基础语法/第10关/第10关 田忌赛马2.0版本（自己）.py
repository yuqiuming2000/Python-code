import random
player_list =  ['【狂血战士】','【森林箭手】','【光明骑士】','【独行剑客】','【格斗大师】','【枪弹专家】']
enmy_list =  ['【狂血战士】','【森林箭手】','【光明骑士】','【独行剑客】','【格斗大师】','【枪弹专家】']
players = random.sample(player_list,3)  
enemies = random.sample(enmy_list,3)
player_info = {}
enemies_info={}
# 随机生成两种属性
def born_role():
    life = random.randint(100,180)
    attack = random.randint(30,50)
    return life,attack 
# 给角色赋予随机属性，并展示角色信息。
def show_role():
    print('你的人物：')
    for i in range(3):
        player_info[players[i]]=born_role()
        enemies_info[enemies[i]]=born_role()
        print('{} 血量：{}  攻击值{}'.format(players[i],player_info[players[i]][0],player_info[players[i]][1]))
    print('电脑敌人：')
    for i in range(3):
        player_info[players[i]]=born_role()
        enemies_info[enemies[i]]=born_role()
        print('{} 血量：{}  攻击值{}'.format(enemies[i],enemies_info[enemies[i]][0],enemies_info[enemies[i]][1]))
show_role()
    
