from gevent import monkey
#从gevent库里导入monkey模块。
monkey.patch_all()
#monkey.patch_all()能把程序变成协作式运行，就是可以帮助程序实现异步。
import gevent,time,requests
#导入gevent、time、requests。
start = time.time()
#记录程序开始时间。
url_list = [
'https://localprod.pandateacher.com/python-manuscript/hello-spiderman/',
'https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w=%E5%91%A8%E6%9D%B0%E4%BC%A6',
'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/',
]

for url in url_list:
    res = requests.get(url)
    print(res.status_code)
end = time.time()
print(end-start)
#打印程序最终所需时间。