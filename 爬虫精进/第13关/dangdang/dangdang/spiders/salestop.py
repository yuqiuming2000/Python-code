import sys
import scrapy
import bs4
import requests
from bs4 import BeautifulSoup
sys.path.append('dangdang')
from items import dangdangItem

class DoubanSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['http://bang.dangdang.com']
    start_urls = []
    for i in range(3):
        url = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-month-2021-6-1-'+str(i)
        start_urls.append(url)

    def parse(self, response):
        bs = BeautifulSoup(response.text,'html.parser')
        bs_1=bs.find('ul',class_='bang_list clearfix bang_list_mode')
        datas = bs_1.find_all('li')
        for data in  datas:
            item = dangdangItem()
            item['num']= data.find('div',class_='list_num').text
            item['name'] = data.find('div',class_='name').text
            item['href']= data.find('div',class_='name').find('a')['href']
            item['price_n'] = data.find('span',class_='price_n').text
            item['price_r'] = data.find('span',class_='price_r').text
            item['price_s'] = data.find('span',class_='price_s').text
            item['title']=data.find_all('a')[3]['title']
            yield item
     