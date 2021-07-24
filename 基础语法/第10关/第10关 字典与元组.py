import random

player = ['狂血战士']
#角色列表，有一个元素

dict1 = {}
#创建一个字典，存放角色属性信息

def info():
    a = random.randint(1,3)
    b = random.randint(4,6)
    return a,b  # return 多个值时，返回一个元组(a,b)

data = info()
#调用info()函数，将返回的元组(a,b)赋值给变量data
print(data)

dict1[player[0]] = data
#往空字典添加键值对，player[0]即'狂血战士'为键，data（元组）为值。
print(dict1)  
print(dict1[player[0]]) # 打印出字典的值
print(dict1[player[0]][0]) # 打印出字典的值data的第0个元素
print(dict1[player[0]][1]) # 打印出字典的值data的第1个元素