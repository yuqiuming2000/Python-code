import requests
import json

from requests.sessions import session
session=requests.session()
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
def login():
    url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
    session=requests.session()
    #把登录的网址赋值给url。

    #加请求头，前面有说过加请求头是为了模拟浏览器正常的访问，避免被反爬虫。
    data = {
    'log': 'spiderman',  #写入账户
    'pwd': 'crawler334566',  #写入密码
    'wp-submit': '登录',
    'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
    'testcookie': '1'
    }
    session.post(url,headers=headers,data=data)
    cookies_dict=requests.utils.dict_from_cookiejar(session.cookies)
    cookies_str=json.dumps(cookies_dict)
    with open('cookies.txt','w')as file:
        file.write(cookies_str)
   

def readcookies():
    cookies_text=open('cookies.txt','r')
    cookies_dict=json.loads(cookies_text.read())
    cookies=requests.utils.cookiejar_from_dict(cookies_dict)
    session.cookies=cookies
    return(cookies)
def comment():
    url_1='https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
    data_1={
    'comment': input('请输入您的评论：'),
    # 'comment': '风变课程对我帮助非常大',
    'submit': '发表评论',
    'comment_post_ID': '23',
    'comment_parent': '0',
    }
    comment = session.post(url_1,headers=headers,data=data_1)
    return(comment.status_code)
try: 
    session.cookies = readcookies()
except FileNotFoundError:
    login()
    session.cookies = readcookies()
number=comment()
print(number)
for i in range(10):
    if number==200:
        print('恭喜你，成功了')
        break
    else:
        login()
        session.cookies = readcookies()
        comment()

