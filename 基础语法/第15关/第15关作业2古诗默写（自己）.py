import random
with open (r'D:\WORK\Python\Python code\第15关\锦瑟.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
print(lines)
list_test = random.sample(lines,2)
print(list_test)
with open(r'D:\WORK\Python\Python code\第15关\锦瑟默写.txt','w',encoding='utf-8') as new:
    for line in lines:
        if line in list_test:  
            new.write('____________。\n')
        else:
            new.write(line)
