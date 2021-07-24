import requests
import json
#引入requests。
url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
session=requests.session()
#把登录的网址赋值给url。
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
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
print(cookies_dict)
cookies_str=json.dumps(cookies_dict)
print(cookies_str)
with open('cookies.txt','w')as file:
    file.write(cookies_str)