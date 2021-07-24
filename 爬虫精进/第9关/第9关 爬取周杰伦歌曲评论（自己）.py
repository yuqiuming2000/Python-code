from selenium import webdriver
import time
driver=webdriver.Chrome()
url='https://y.qq.com/n/yqq/song/000xdZuV2LcQ19.html'
driver.get(url)
time.sleep(5)
comments=driver.find_elements_by_class_name('js_hot_text')
for i in comments:
    print(i.text)
driver.close()