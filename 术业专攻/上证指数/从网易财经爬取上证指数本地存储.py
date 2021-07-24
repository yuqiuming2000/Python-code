from selenium import webdriver
from lxml import etree
import time
import requests
import xlrd,xlwt


def GetPrice(out_time,row):
    while 1:
        #获取当前页面源码
        html=browser.page_source
        #解析数据
        html_ele = etree.HTML(html)
        price = html_ele.xpath('/html/body/div[2]/div[1]/div[3]/table/tbody/tr/td[2]/div/table/tbody/tr[1]/td[1]/span/strong/text()')[0]
        nowTimes = time.strftime('%H.%M',time.localtime())
        print(nowTimes,price)
        #将数据写入xls表格
        sheet.write(row[0],0,nowTimes)
        sheet.write(row[0],1,float(price))
        row[0] = row[0]+1
        if float(nowTimes)>=out_time:
            print('时间到，下班喽')
            break
        time.sleep(60)

def Relax(start_time):
    while 1:
        nowTimes = time.strftime('%H.%M',time.localtime())
        print('当前时间：'+nowTimes,end=' ')
        if float(nowTimes)>=start_time:
            print('醒醒，该起床干活了，爬数据去...')
            break
        print('还早着呢，多睡会儿吧...')
        time.sleep(60)


if __name__=='__main__':
    #打开模拟浏览器
    browser = webdriver.Chrome()
    browser.get('http://quotes.money.163.com/0000001.html')
    print('获取网页信息')

    #创建储存数据的表格
    row = [1]
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet("sheet")
    sheet.write(0,0,'时间')
    sheet.write(0,1,'上证指数')

    #爬取数据
    Relax(9.30)
    GetPrice(11.30,row)
    Relax(13.00)
    GetPrice(18.12,row)

    print('保存数据')
    today = time.strftime('%Y-%m-%d',time.localtime())
    print(today)
    workbook.save("{}.xls".format(today))
    browser.close()
