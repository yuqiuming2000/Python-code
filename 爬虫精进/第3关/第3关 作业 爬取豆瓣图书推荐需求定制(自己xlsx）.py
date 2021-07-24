import requests, random, bs4,openpyxl
from bs4 import BeautifulSoup
wb=openpyxl.Workbook()  
sheet=wb.active 
sheet.title='豆瓣图书需求定制' 
sheet['A1'] ='图书名'    
sheet['B1'] ='注释'  
sheet['C1'] ='推荐语'   
sheet['D1'] ='评分'   
sheet['E1'] ='链接'    
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
                sheet.append([name,author,tes,comment,href])  
        except Exception:
            pass
wb.save('豆瓣图书需求定制.xlsx')  