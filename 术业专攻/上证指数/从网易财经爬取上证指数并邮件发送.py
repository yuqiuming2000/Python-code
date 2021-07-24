from selenium import webdriver
from lxml import etree
import time
import requests
import xlrd,xlwt
from re import template
from bs4 import BeautifulSoup
import schedule
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from selenium import  webdriver #从selenium库中调用webdriver模块
from selenium.webdriver.chrome.options import Options # 从options模块中调用Options类
def GetPrice():
    while 1:
        chrome_options = Options() # 实例化Option对象
        chrome_options.add_argument('--headless') # 把Chrome浏览器设置为静默模式
        browser = webdriver.Chrome(options = chrome_options)
        browser.get('http://quotes.money.163.com/0000001.html')
        print('获取网页信息')
        html=browser.page_source
        html_ele = etree.HTML(html)
        price = html_ele.xpath('/html/body/div[2]/div[1]/div[3]/table/tbody/tr/td[2]/div/table/tbody/tr[1]/td[1]/span/strong/text()')[0]
        growth= html_ele.xpath('/html/body/div[2]/div[1]/div[3]/table/tbody/tr/td[2]/div/table/tbody/tr[1]/td[1]/em/text()')[0]
        growth_rate= html_ele.xpath('/html/body/div[2]/div[1]/div[3]/table/tbody/tr/td[2]/div/table/tbody/tr[1]/td[1]/em/text()')[1]
        nowTimes = time.strftime('%H.%M',time.localtime())
        browser.close()
        return nowTimes,price,growth,growth_rate

def Send_mail(nowTimes,price,growth,growth_rate):
    from_addr = '76746694@qq.com'
    password = 'fkbefpkgscnxcbcj'
    smtp_server = 'smtp.qq.com'
    to_addrs = ['76746694@qq.com']
    content='现在时间'+nowTimes+'\n'+'上证指数'+price+'\n'+'增长量'+growth+'\n'+'增长率'+growth_rate
    msg = MIMEText(content,'plain','utf-8')
    msg['From'] = Header(from_addr)
    msg['To'] = Header(str(to_addrs))
    msg['Subject'] = Header('上证指数')
    server = smtplib.SMTP()
    server.connect(smtp_server,587)
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addrs, msg.as_string())
    server.quit()

def job():
    print('开始一次任务')
    nowTimes,price,growth,growth_rate = GetPrice()
    Send_mail(nowTimes,price,growth,growth_rate)
    print('任务完成')
while True:
    nowTimes = time.strftime('%H.%M',time.localtime())
    if 9.30<=float(nowTimes)<=11.30 or 13.00<=float(nowTimes)<=15.00: 
        schedule.every(10).minutes.do(job)
        while 9.30<=float(nowTimes)<=11.30 or 13.00<=float(nowTimes)<=15.00:
            schedule.run_pending()
            time.sleep(20)
            nowTimes = time.strftime('%H.%M',time.localtime())
            continue
    else:
        pass
