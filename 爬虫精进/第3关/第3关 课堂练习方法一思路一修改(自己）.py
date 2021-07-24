import requests
# 引用requests库
from bs4 import BeautifulSoup
# 引用BeautifulSoup库
url='http://www.xiachufang.com/explore/'
headers={
'Accept':' text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding':' gzip, deflate, br',
'Accept-Language':' zh-CN,zh;q=0.9',
'Connection':' keep-alive',
'Cookie':' bid=ZSQek0sw; __utmz=177678124.1623903366.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217a182eed1bc8-03220294c5e1de-4373266-1440000-17a182eed1c30%22%2C%22%24device_id%22%3A%2217a182eed1bc8-03220294c5e1de-4373266-1440000-17a182eed1c30%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; __gads=ID=d7093b5342b36e7f-224f157b82c900b7:T=1623903367:RT=1623903367:S=ALNI_MaMMsF8DJY5qICvS1J3_oVICjK7UA; Hm_lvt_ecd4feb5c351cc02583045a5813b5142=1623903366,1623911415; __utma=177678124.1333524118.1623903366.1623903366.1623911416.2',
'Host':' www.xiachufang.com',
'sec-ch-ua':' " Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
'sec-ch-ua-mobile':' ?0',
'Sec-Fetch-Dest':' document',
'Sec-Fetch-Mode':' navigate',
'Sec-Fetch-Site':' none',
'Sec-Fetch-User':' ?1',
'Upgrade-Insecure-Requests':' 1',
'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
}
res_foods = requests.get(url,headers=headers)
print(res_foods.status_code)
bs=BeautifulSoup(res_foods.text,'html.parser')
items=bs.find_all('div',class_='info pure-u')
for i in items:
    name=i.find('a')
    feedstock=i.find(class_='ing ellipsis')
    URL = 'http://www.xiachufang.com'+name['href']
    print('菜名是：'+name.text+'\n'+'链接是：'+URL+'\n'+'食材是：'+feedstock.text+'\n')