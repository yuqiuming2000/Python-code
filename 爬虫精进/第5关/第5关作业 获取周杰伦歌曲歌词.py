import requests
from bs4 import BeautifulSoup
url='https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
for i in range(5):
    params={
    'ct':'24',
    'remoteplace': 'txt.yqq.top',
    'searchid':'96237302158195195',
    'aggr':'0',
    'catZhida':'1',
    'lossless':'0',
    'sem':'1',
    't':'7',
    'p':str(i+1),
    'n':'5',
    'w':'周杰伦',
    '_':'1624399094275',
    'cv':'4747474',
    'ct':'24',
    'format':'json',
    'inCharset':'utf-8',
    'outCharset':'utf-8',
    'notice':'0',
    'platform':'yqq.json',
    'needNewCode':'0',
    'uin':'0',
    'g_tk_new_20200303':'5381',
    'g_tk':'5381',
    'hostUin':'0',
    'loginUin':'0',
    }
    headers={
    'origin':'https://y.qq.com',
    'referer':'https://y.qq.com/',
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
    }
    res_music=requests.get(url,params=params)
    json_music=res_music.json()
    list_music=json_music['data']['lyric']['list']
    for music in list_music:
        lyric_music=music['content']
        print(lyric_music+'\n')