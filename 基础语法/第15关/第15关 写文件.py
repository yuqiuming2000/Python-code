# 【练习时间来咯】1.请你在一个叫1.txt文件里写入字符串'难念的经' 2.然后请你读取这个1.txt文件的内容，并打印出来。
file=open(r'C:\Users\喻秋明\Desktop\test\ceshi.txt','w',encoding='utf-8')
file.write('难念的经\n')
file.close()
file=open(r'C:\Users\喻秋明\Desktop\test\ceshi.txt','r',encoding='utf-8')
filecontent=file.read()
print(filecontent)