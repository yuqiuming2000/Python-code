import os
# os.getcwd()  # 返回当前工作目录
# os.listdir(path)   # 返回path指定的文件夹包含的文件或文件夹的名字的列表
# os.mkdir(path)  # 创建文件夹
# os.path.abspath(path)   # 返回绝对路径
# os.path.basename(path)   # 返回文件名
# os.path.isfile(path)   # 判断路径是否为文件
# os.path.isdir(path)   # 判断路径是否为目录
import random
with open (r'D:\WORK\Python\Python code\第16关\锦瑟.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
print(lines)
list_test = random.sample(lines,2)
print(list_test)
with open(r'D:\WORK\Python\Python code\第16关\锦瑟默写.txt','w',encoding='utf-8') as new:
    for line in lines:
        if line in list_test:  
            new.write('____________。\n')
        else:
            new.write(line)
# os.replace('锦瑟默写.txt','锦瑟.txt')