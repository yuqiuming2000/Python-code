deposit = [100,300,900,2000,5000,0,2000,4500]
try:
    for i in range(1, len(deposit)) :
        times = deposit[i]/deposit[i-1]
        print('你的存款涨了%f倍'%times)
except ZeroDivisionError:
    print('你上次存款为 0 哦！')
  

    
