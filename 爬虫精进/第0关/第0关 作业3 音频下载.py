# 题目要求：获取文章《HTTP状态响应码》全部内容，并且打印出全文内容。
import requests
res = requests.get('https://static.pandateacher.com/Over%20The%20Rainbow.mp3')
song=res.content
with open('第0关作业3.mp3','wb')as file:
    file.write(song)