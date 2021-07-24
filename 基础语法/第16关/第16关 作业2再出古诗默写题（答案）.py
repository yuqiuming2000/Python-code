import os
list_test = ['一弦一柱思华年。\n','只是当时已惘然。\n']  # 将要默写的诗句放在列表里。
with open (r'D:\WORK\Python\Python code\第16关\锦瑟.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
print(lines)
with open(r'D:\WORK\Python\Python code\第16关\锦瑟默写.txt','w',encoding='utf-8') as new:
    for line in lines:
        if line in list_test:  # 属于默写列表中的句子，将其替换成横线。
            new.write('____________。\n')
        else:
            new.write(line)
os.replace(r'D:\WORK\Python\Python code\第16关\锦瑟默写.txt',r'D:\WORK\Python\Python code\第16关\锦瑟.txt')