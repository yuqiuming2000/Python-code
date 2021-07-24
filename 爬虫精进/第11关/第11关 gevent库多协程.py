from gevent import monkey
monkey.patch_all()
import gevent,time,requests
start = time.time()
url_list = [
'https://localprod.pandateacher.com/python-manuscript/hello-spiderman/',
'https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w=%E5%91%A8%E6%9D%B0%E4%BC%A6',
'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/',
]
def crawler(url):
    r = requests.get(url)
    print(url,time.time()-start,r.status_code)
tasks_list = [ ]
for url in url_list:
    task = gevent.spawn(crawler,url)
    tasks_list.append(task)
gevent.joinall(tasks_list)
end = time.time()
print(end-start)