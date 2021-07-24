import requests
#引用requests库
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
#下载《三国演义》第一回，我们得到一个对象，它被命名为res
novel=res.text
#把Response对象的内容以字符串的形式返回
# print(novel[:800])
# #现在，可以打印小说了，但考虑到整章太长，只输出800字看看就好。在关于列表的知识那里，你学过[:800]的用法。
with open('三国.txt','w') as file:
    file.write(str(novel))