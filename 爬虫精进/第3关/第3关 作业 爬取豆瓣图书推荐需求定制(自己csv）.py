import requests, random, bs4,csv
from bs4 import BeautifulSoup
with open('豆瓣图书需求定制.csv','w',newline='')as f:
    writer=csv.writer(f)
    writer.writerow(['图书名','注释','推荐语','评分','链接'])
for x in range(10):
    url = 'https://book.douban.com/top250?start=' + str(x*25) + '&filter='
    headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',}
    res = requests.get(url,headers=headers)
    # res.encoding='utf-8-sig'
    print(res.status_code)
    bs=BeautifulSoup(res.text,'html.parser')
    items=bs.find_all('tr',class_='item')
    for i in items:
        try:
            name_0=i.find('div',class_='pl2')
            name=name_0.find('a')['title']
            href=i.find('a')['href']
            author=i.find('p',class_='pl').text
            tes=i.find('span',class_='inq').text
            comment=i.find('span',class_='rating_nums').text
            print(name,author,tes,comment,href+'\n')
                
            if float(comment)>=9.0:
                with open('豆瓣图书需求定制.csv','a',newline='',encoding='utf-8')as f:
                    writer=csv.writer(f)
                    row=[name,author,tes,comment,href]
                    writer.writerow(row)
        except Exception:
            pass
