import requests
session = requests.session()
url='https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'}
data={
'log': 'spiderman',
'pwd': 'crawler334566',
'wp-submit': '登录',
'redirect_to': 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn',
'testcookie': '1' ,
}
session.post(url,headers=headers,data=data)
url_1='https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-comments-post.php'
data_1={
'comment': input('请输入您的评论：'),
# 'comment': '风变课程对我帮助非常大',
'submit': '发表评论',
'comment_post_ID': '23',
'comment_parent': '0',
}
comment = session.post(url_1,headers=headers,data=data_1)
print(comment)