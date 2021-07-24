import requests, random, bs4,openpyxl
from bs4 import BeautifulSoup
wb=openpyxl.Workbook()  
sheet=wb.active 
sheet.title='豆瓣电影' 
sheet['A1'] ='序号'    
sheet['B1'] ='电影名'  
sheet['C1'] ='推荐语'   
sheet['D1'] ='评分'   
sheet['E1'] ='链接'
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
            if float(comment)>=9.0:
                sheet.append([num,title,comment,tes,url])  
    except AttributeError:
        pass
wb.save('豆瓣电影.xlsx') 


