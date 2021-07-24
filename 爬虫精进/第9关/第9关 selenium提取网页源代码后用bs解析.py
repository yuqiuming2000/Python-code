from selenium import webdriver #从selenium库中调用webdriver模块
import time
from bs4 import BeautifulSoup
driver = webdriver.Chrome() # 设置引擎为Chrome，真实地打开一个Chrome浏览器
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/') # 访问页面
time.sleep(2) # 等待2秒
page_source=driver.page_source
print(page_source)
bs=BeautifulSoup(page_source,'html.parser')
labels=bs.find_all('label')
# print(type(labels)) # 打印labels的数据类型
for i in labels:
    print(i.text)
driver.close() # 关闭浏览器