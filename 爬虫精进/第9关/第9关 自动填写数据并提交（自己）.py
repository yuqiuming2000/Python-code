from selenium import webdriver
import time
driver=webdriver.Chrome()
url='https://localprod.pandateacher.com/python-manuscript/hello-spiderman/'
driver.get(url)
time.sleep(5)
teacher=driver.find_element_by_id('teacher')
teacher.send_keys('吴枫')
assistant=driver.find_element_by_id('assistant')
assistant.send_keys('酱酱')
sub=driver.find_element_by_class_name('sub')
sub.click()
time.sleep(20)
driver.close()