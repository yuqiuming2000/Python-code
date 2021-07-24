file=open(r'C:\Users\喻秋明\Desktop\test\abc.txt','a',encoding='utf-8')
file.write('赵敏\n')     
file.write('下龙女\n') 
file.close
file = open(r'C:\Users\喻秋明\Desktop\test\abc.txt', 'r',encoding='utf-8')
filecontent=file.read()
print(filecontent)
