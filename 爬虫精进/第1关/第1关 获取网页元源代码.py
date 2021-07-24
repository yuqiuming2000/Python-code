import requests
res=requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/spider-men5.0.html')
code=res.text
with open ('网页源代码.txt','w',encoding='utf-8') as file:
    file.write(code)
