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
    res.encoding='utf-8-sig'
    print(res.status_code)
    bs = bs4.BeautifulSoup(res.text, 'html.parser')
    datas = bs.find_all('tr',class_="item")
        #用find_all提取<tr class="item">元素，这个元素里含有书籍信息。
    try:
        for data in  datas:
            #遍历data。
            title = data.find_all('a')[1]['title']
            #提取出书名。
            publish = data.find('p',class_='pl').text
            #提取出出版信息。
            score = data.find('span',class_='rating_nums').text
            #提取出评分。
            tes=data.find('span',class_="inq").text
            href=data.find('a')['href']
            print([title,publish,score,tes,href])
                #打印上述信息。
            if float(score)>=9.0:
                with open('豆瓣图书需求定制.csv','a',newline='',encoding='utf-8-sig')as f:
                    writer=csv.writer(f)
                    row=[title,publish,tes,score,href]
                    writer.writerow(row)
    except AttributeError:
        pass


