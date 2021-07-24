import sys
import scrapy
import bs4
sys.path.append('music')
from items import MusicItem

class MusicSpider(scrapy.Spider):
    name = 'music'
    allowed_domains = ['//y.qq.com/']
    
    url='https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=61709175336869544&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=10&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk_new_20200303=5381&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0'
    start_urls = [url]
    def parse(self, response):
        json_music = response.json()
        list_music = json_music['data']['song']['list']
        for music in list_music:
            item=MusicItem()
            item['name']=music['name']
            item['album']=music['album']['name']
            item['interval']=music['interval']
            item['href']='https://y.qq.com/n/yqq/song/'+music['mid']+'.html\n\n'     
            print(item['name'])
            yield item
      