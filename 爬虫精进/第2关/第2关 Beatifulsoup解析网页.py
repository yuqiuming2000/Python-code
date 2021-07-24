import requests # 调用requests库
from bs4 import BeautifulSoup # 调用BeautifulSoup库
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
# 返回一个response对象，赋值给res
html = res.text
# 把res的内容以字符串的形式返回
soup = BeautifulSoup( html,'html.parser') 
# 把网页解析为BeautifulSoup对象
items = soup.find_all(class_='books') # 通过定位标签和属性提取我们想要的数据
for item in items:
    kind = item.find('h2') # 在列表中的每个元素里，匹配标签<h2>提取出数据
    title = item.find(class_='title') #在列表中的每个元素里，匹配属性class_='title'提取出数据
    brief = item.find(class_='info') #在列表中的每个元素里，匹配属性class_='info'提取出数据
    print(kind.text,'\n',title.text,'\n',title['href'],'\n',brief.text)
