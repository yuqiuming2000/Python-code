from requests.sessions import session
from selenium import webdriver
import time
import requests
while True:
    comment_content = input('请输入你想要的评论的内容，按回车提交：')
    if comment_content == '':
        print('&' * 5, '评论内容不允许为空', '&' * 5)
    else:
        break
driver = webdriver.Chrome() # 实例化浏览器对象
driver.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php')
time.sleep(5)
# 定位到用户名输入框，输入用户名
login_name = driver.find_element_by_id('user_login')
login_name.send_keys('spiderman')
time.sleep(1)
password = driver.find_element_by_id('user_pass')
password.send_keys('crawler334566')
submit_btn = driver.find_element_by_id('wp-submit')
submit_btn.click()
time.sleep(2)
article_link = driver.find_element_by_partial_link_text('同九义何汝秀')
article_link.click()
comment_area = driver.find_element_by_id('comment')
comment_area.send_keys(comment_content)
time.sleep(2)
comment_submit = driver.find_element_by_id('submit')
comment_submit.click()
time.sleep(10)
driver.close()
print('#' * 6, '评论成功，浏览器已关闭', '#' * 6)