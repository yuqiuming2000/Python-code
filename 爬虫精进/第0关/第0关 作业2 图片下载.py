# 题目要求：获取文章《HTTP状态响应码》全部内容，并且打印出全文内容。
import requests
res = requests.get('https://res.pandateacher.com/2019-01-12-15-29-33.png')
picter=res.content
with open('第0关作业2.jpg','wb')as file:
    file.write(picter)