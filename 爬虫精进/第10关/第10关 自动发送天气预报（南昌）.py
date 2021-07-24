from re import template
import requests
from bs4 import BeautifulSoup
import time
import schedule
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import csv
def Send_mail(A,B,C):
    from_addr = '76746694@qq.com'
    password = 'fkbefpkgscnxcbcj'
    smtp_server = 'smtp.qq.com'
    to_addrs = ['76746694@qq.com']
    content=A+'\n'+B+'\n'+C+'\n'
    msg = MIMEText(content,'plain','utf-8')
    msg['From'] = Header(from_addr)
    msg['To'] = Header(str(to_addrs))
    msg['Subject'] = Header('南昌天气预报')
    server = smtplib.SMTP()
    server.connect(smtp_server,25)
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addrs, msg.as_string())
    server.quit()

def weather_spider():
    headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    #封装headers
    url='http://www.weather.com.cn/weather/101240101.shtml'
    #把URL链接赋值到变量url上。
    res=requests.get(url,headers=headers)
    res.encoding='utf-8'
    #发送requests请求，并把响应的内容赋值到变量res中。
    print(res.status_code)
    #检查响应状态是否正常
    #打印出res对象的网页源代码   
    bs=BeautifulSoup(res.text,'html.parser')
    connent=bs.find('li',class_='sky skyid lv1 on')
    time=connent.find('h1')
    weather=connent.find('p')
    tem=connent.find('p',class_='tem')
    high_tem=tem.find('span')
    low_tem=tem.find('i')
    A='时间：'+time.text
    B='天气：'+weather.text
    C='温度:'+high_tem.text+'/'+low_tem.text
    return A,B,C
def job():
    print('开始一次任务')
    A,B,C = weather_spider()
    Send_mail(A,B,C)
    print('任务完成')
# schedule.every(5).seconds.do(job) 
schedule.every().day.at('07:30').do(job)
while True:
    schedule.run_pending()
    time.sleep(2)

