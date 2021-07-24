import requests
# 引用requests模块
url='https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
for i in range(5):
    params = {
    'ct':'24',
    'qqmusic_ver': '1298',
    'new_json':'1',
    'remoteplace':'sizer.yqq.song_next',
    'searchid':'64405487069162918',
    't':'0',
    'aggr':'1',
    'cr':'1',
    'catZhida':'1',
    'lossless':'0',
    'flag_qc':'0',
    'p':str(i+1),
    'n':'20',
    'w':'周迅',
    'g_tk':'5381',
    'loginUin':'0',
    'hostUin':'0',
    'format':'json',
    'inCharset':'utf8',
    'outCharset':'utf-8',
    'notice':'0',
    'platform':'yqq.json',
    'needNewCode':'0'    
    }
    res_music = requests.get(url,params=params)
    json_music = res_music.json()
    list_music = json_music['data']['song']['list']
    for music in list_music:
        print(music['name'])
        print('所属专辑：'+music['album']['name'])
        print('播放时长：'+str(music['interval'])+'秒')
        print('播放链接：https://y.qq.com/n/yqq/song/'+music['mid']+'.html\n\n')
