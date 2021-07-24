# 题目要求：获取文章《HTTP状态响应码》全部内容，并且打印出全文内容。
import requests
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/exercise/HTTP%E5%93%8D%E5%BA%94%E7%8A%B6%E6%80%81%E7%A0%81.md')
novel=res.text
print(novel)