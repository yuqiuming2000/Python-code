import requests 
#引入requests库
res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md') 
#发送请求，并把响应结果赋值在变量res上
with open('三国.txt','w') as file:
    file.write(str(res))
