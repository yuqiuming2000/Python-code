for i in range(5):
    b=5-i
    a = int(input('请输入0来结束循环，你还有%d次机会:'%b))
    if a == 0:
        print('你触发了break语句，循环结束，导致else语句不会生效。')    
        break
else:
    print('5次循环你都错过了，else语句生效了。')

