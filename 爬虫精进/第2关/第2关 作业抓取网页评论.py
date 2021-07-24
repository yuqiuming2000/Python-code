# 你需要爬取的是博客【人人都是蜘蛛侠】中，《未来已来（四）——Python学习进阶图谱》的所有文章评论，并且打印。

import requests # 调用requests库
from bs4 import BeautifulSoup # 调用BeautifulSoup库
res =requests.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_04/')
html=res.text
soup=BeautifulSoup(html,'html.parser')
comment=soup.find_all('div',class_='comment-content')
for i in comment:
    print(i.text)