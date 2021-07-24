import requests
from bs4 import BeautifulSoup
from re import template
import time
import schedule
import smtplib
from email.mime.text import MIMEText
from email.header import Header
def menu():
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
    bs_foods = BeautifulSoup(res_foods.text,'html.parser')
    list_foods = bs_foods.find_all('div',class_='info pure-u')
    list_all = ''
    num=0
    for food in list_foods:
        num+=1
        tag_a = food.find('a')
        name = tag_a.text.strip()
        URL = 'http://www.xiachufang.com'+tag_a['href']
        tag_p = food.find('p',class_='ing ellipsis')
        ingredients = tag_p.text.strip()
        food_info='''
        序号：{}
        菜名：{}
        链接：{}
        原料：{}
        '''.format(num,name,url,ingredients)
        list_all+=food_info
    return(list_all)
def Send_mail(list_all):
    from_addr = '76746694@qq.com'
    password = 'fkbefpkgscnxcbcj'
    smtp_server = 'smtp.qq.com'
    to_addrs = ['76746694@qq.com']
    content=list_all
    msg = MIMEText(content,'plain','utf-8')
    msg['From'] = Header(from_addr)
    msg['To'] = Header(str(to_addrs))
    msg['Subject'] = Header('本周最受欢迎菜谱')
    server = smtplib.SMTP()
    server.connect(smtp_server,25)
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addrs, msg.as_string())
    server.quit()
def job():
    print('开始一次任务')
    list_all = menu()
    Send_mail(list_all)
    print('任务完成')
schedule.every(5).seconds.do(job) 
# schedule.every().day.at('7:30').do(job)
while True:
    schedule.run_pending()
    time.sleep(2)