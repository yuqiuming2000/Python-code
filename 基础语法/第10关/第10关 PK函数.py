def Print_result(player_life,player_attack,enemy_life,enemy_attack):
    if player_life > 0 and enemy_life <= 0:
        print('敌人死翘翘了，这局你赢了')
    elif player_life <= 0 and enemy_life > 0:
        print('悲催，这局敌人把你干掉了！')
    else:
        print('哎呀，这局你和敌人同归于尽了！')
    print('-----------------------')

    
