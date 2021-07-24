from os import name
from bs4.element import Comment
import requests 
from bs4 import BeautifulSoup
url='https://book.douban.com/top250?start='
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'}
res=requests.get(url,headers=headers)
print(res.status_code)
bs=BeautifulSoup(res.text,'html.parser')
items=bs.find_all('tr',class_='item')
for i in items:
    name_0=i.find('div',class_='pl2')
    name=name_0.find('a')['title']
    href=i.find('a')['href']
    author=i.find('p',class_='pl').text
    tes=i.find('span',class_='inq').text
    comment=i.find('span',class_='rating_nums').text
    print(name,author,tes,comment,href+'\n')