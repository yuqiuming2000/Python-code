from selenium import webdriver #从selenium库中调用webdriver模块
import time
driver = webdriver.Chrome() # 设置引擎为Chrome，真实地打开一个Chrome浏览器
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/') # 访问页面
time.sleep(2) # 等待2秒
labels = driver.find_elements_by_tag_name('label') # 根据标签名提取所有元素
# print(type(labels)) # 打印labels的数据类型
for i in labels:
    print(i.text)
driver.close() # 关闭浏览器