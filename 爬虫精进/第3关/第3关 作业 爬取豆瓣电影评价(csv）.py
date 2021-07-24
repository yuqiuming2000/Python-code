import requests, random, bs4,csv
from bs4 import BeautifulSoup
with open('豆瓣电影爬虫.csv','w',newline='')as f:
    writer=csv.writer(f)
    writer.writerow(['序号','电影名','推荐语','评分','链接'])
for x in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(x*25) + '&filter='
    headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',}
    res = requests.get(url,headers=headers)
    print(res.status_code)
    bs = bs4.BeautifulSoup(res.text, 'html.parser')
    items=bs.find_all('div',class_='item')
    try:
        for i in items:
            num=i.find('em',class_='').text
            title=i.find('span',class_='title').text
            comment=i.find('span',class_='rating_num').text
            tes=i.find('span',class_='inq').text
            url=i.find('a')['href']
            print(num + '.' + title + '——' + comment + '\n' + '推荐语：' + tes +'\n' + url)
            # print(num,title,comment,tes,url)
            # print(num + '.' + title + '——' + comment + '\n' + '推荐语：' + tes +'\n' + url)

            with open('豆瓣电影爬虫.csv','a',newline='')as f:
                writer=csv.writer(f)
                row=[num,title,comment,tes,url]
                writer.writerow(row)
    except AttributeError:
        pass



