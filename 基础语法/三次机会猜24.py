for i in range(3):
    b=3-i
    a = int(input('请猜猜这个数，你还有%d次机会:'%b))
    if a == 24:
        print('你猜对了。')    
        break
    elif a<24:
        print('你猜小了。')  
    else:
        print('你猜大了。')
else:
    print('你失败了。')

