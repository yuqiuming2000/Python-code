import numpy as np
A=[91, 95, 97, 99]
B=[92, 93, 96, 98] 
C=A
C.extend(B)
C.sort()
print(C)
D=[]
averge=np.mean(C)
print('平均值是{}'.format(averge))
for i in C:
    if i <averge:
        D.append(i)
print(D)




