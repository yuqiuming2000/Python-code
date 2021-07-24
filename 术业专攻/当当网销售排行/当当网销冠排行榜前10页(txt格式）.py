import sys
import requests
from bs4 import BeautifulSoup
import csv
with open('当当网2021年6月份销售排行榜.txt','w',newline='')as f:
    writer=csv.writer(f)
    writer.writerow(['名词','书名','作者','链接','售价','原价','折扣'])
hearers={'USER_AGENT':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
for i in range(1,4):
    url = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-month-2021-6-1-'+str(i)
    res=requests.get(url,headers=hearers)
    res.encoding='gb2312'
    bs = BeautifulSoup(res.text,'html.parser')
    bs_1=bs.find('ul',class_='bang_list clearfix bang_list_mode')
    datas = bs_1.find_all('li')
    for data in  datas:
        try:
            num= data.find('div',class_='list_num').text
            name = data.find('div',class_='name').text
            href= data.find('div',class_='name').find('a')['href']
            price_n = data.find('span',class_='price_n').text
            price_r = data.find('span',class_='price_r').text
            price_s = data.find('span',class_='price_s').text
            title=data.find_all('a')[3]['title']
            # print(num,name,href,price_n,price_r,price_s,title+'\n')
            content=num+name+href+price_n+price_r+price_s+title+'\n'
            print(content)
            with open('当当网2021年6月份销售排行榜.txt','a')as f:
                f.write(content)
        except Exception:
            pass