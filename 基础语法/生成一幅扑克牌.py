def cards():
    global num
    color=['红心','方块','黑桃','梅花']
    num=list(range(2,11))
    num.extend('JQKA')
    print(num)
    return[(x,y)for x in color for y in num]
print(cards())

