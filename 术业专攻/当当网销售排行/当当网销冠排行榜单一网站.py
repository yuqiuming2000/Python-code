import sys
import requests
from bs4 import BeautifulSoup

hearers={'USER_AGENT':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
url = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-month-2021-6-1-1'
res=requests.get(url,headers=hearers)
print(res.status_code)
bs = BeautifulSoup(res.text,'html.parser')
bs_1=bs.find('ul',class_='bang_list clearfix bang_list_mode')
# datas = bs.find_all('li',class_="")
datas = bs_1.find_all('li')
print(len(datas))
for data in  datas:
    num= data.find('div',class_='list_num').text
    name = data.find('div',class_='name').text
    href= data.find('div',class_='name').find('a')['href']
    price_n = data.find('span',class_='price_n').text
    price_r = data.find('span',class_='price_r').text
    price_s = data.find('span',class_='price_s').text
    title=data.find_all('a')[3]['title']
    print(num,name,href,price_n,price_r,price_s+'\n')
