import time
def show_role(player_life,player_attack,enemy_life,enemy_attack):
    print('【玩家】\n血量：%s\n攻击：%s'%(player_life,player_attack))
    print('------------------------')
    time.sleep(1)
    print('【敌人】\n血量：%s\n攻击：%s'%(enemy_life,enemy_attack))
    print('-----------------------')

def pk_role(player_life,player_attack,enemy_life,enemy_attack):
    while player_life > 0 and enemy_life > 0:
            player_life = player_life - enemy_attack 
            enemy_life = enemy_life - player_attack
            print('你发起了攻击，【敌人】剩余血量%s'%(enemy_life))
            print('敌人向你发起了攻击，【玩家】的血量剩余%s'%(player_life))
            print('-----------------------')
            time.sleep(1.2)
    show_result(player_life,enemy_life)
def show_result(player_life,enemy_life):
    if player_life > 0 and enemy_life <= 0:
        print('敌人死翘翘了，这局你赢了')
    elif player_life <= 0 and enemy_life > 0:
        print('悲催，这局敌人把你干掉了！')
    else:
        print('哎呀，这局你和敌人同归于尽了！')
    print('-----------------------')
def main(player_life,player_attack,enemy_life,enemy_attack):
    show_role(player_life,player_attack,enemy_life,enemy_attack)
    pk_role(player_life,player_attack,enemy_life,enemy_attack)
main(100,35,105,33)
main(120,36,100,45)
main(100,35,100,35)
