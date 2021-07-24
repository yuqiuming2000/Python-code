deposit = [100,300,900,2000,5000,0,2000,4500]
for i in range(1, len(deposit)):
    if deposit[i-1] == 0:  # 判断被除数等于0时，特殊处理。
        print('你上次存款为 0 哦！')
    else:
        times = deposit[i]/deposit[i-1]
        print('你的存款涨了%f倍'%times)

    
