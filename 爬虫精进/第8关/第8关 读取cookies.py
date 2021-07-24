import requests
import json
session=requests.session
cookies_text=open('cookies.txt','r')
cookies_dict=json.loads(cookies_text.read())
cookies=requests.utils.cookiejar_from_dict(cookies_dict)
session.cookies=cookies
print(session.cookies)