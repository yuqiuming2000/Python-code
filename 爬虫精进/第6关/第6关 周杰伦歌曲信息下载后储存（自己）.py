import openpyxl 
import requests
wb=openpyxl.Workbook() 
sheet=wb.active
sheet.title='周杰伦'
sheet['A1']='歌手'
sheet['B1']='专辑'
sheet['C1']='播放时长'
sheet['D1']='链接'
url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp'
for x in range(5):

    params = {
        'ct': '24',
        'qqmusic_ver': '1298',
        'new_json': '1',
        'remoteplace': 'sizer.yqq.song_next',
        'searchid': '64405487069162918',
        't': '0',
        'aggr': '1',
        'cr': '1',
        'catZhida': '1',
        'lossless': '0',
        'flag_qc': '0',
        'p': str(x + 1),
        'n': '20',
        'w': '周杰伦',
        'g_tk': '5381',
        'loginUin': '0',
        'hostUin': '0',
        'format': 'json',
        'inCharset': 'utf8',
        'outCharset': 'utf-8',
        'notice': '0',
        'platform': 'yqq.json',
        'needNewCode': '0'
    }
    # 将参数封装为字典
    res_music = requests.get(url, params=params)
    # 调用get方法，下载这个列表
    json_music = res_music.json()
    # 使用json()方法，将response对象，转为列表/字典
    list_music = json_music['data']['song']['list']
    # 一层一层地取字典，获取歌单列表
    
    for music in list_music:
        name=music['name']
        album=music['album']['name']
        time=music['interval']
        herf='https://y.qq.com/n/yqq/song/' + music['file']['media_mid'] + '.html'
        row= [name,album,time,herf]
        sheet.append(row)
        wb.save('周杰伦.xlsx')