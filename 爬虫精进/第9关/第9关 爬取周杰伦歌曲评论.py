from selenium import webdriver 
import time 
driver = webdriver.Chrome() 
driver.get('https://y.qq.com/n/yqq/song/000xdZuV2LcQ19.html') # 访问页面
time.sleep(2)
comments = driver.find_element_by_class_name('js_hot_list').find_elements_by_class_name('js_cmt_li') 
print(len(comments)) 
for comment in comments: 
    sweet = comment.find_element_by_tag_name('p') 
    print ('评论：%s\n ---\n'%sweet.text) 
driver.close() 
