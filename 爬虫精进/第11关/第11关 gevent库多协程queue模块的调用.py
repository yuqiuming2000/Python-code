from gevent import monkey
monkey.patch_all()
import gevent,time,requests
from gevent.queue import Queue
start = time.time()
url_list = [
'https://localprod.pandateacher.com/python-manuscript/hello-spiderman/',
'https://y.qq.com/portal/search.html#page=1&searchid=1&remoteplace=txt.yqq.top&t=song&w=%E5%91%A8%E6%9D%B0%E4%BC%A6',
'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/',
'http://www.weather.com.cn/weather/101240101.shtml',
'http://www.weather.com.cn/weather/101280601.shtml',
]
work = Queue()
for url in url_list:
    work.put_nowait(url)
def crawler():
    while not work.empty():
        url = work.get_nowait()
        r = requests.get(url)
        print(url,work.qsize(),r.status_code)
tasks_list  = [ ]
for x in range(2):
    task = gevent.spawn(crawler)
    tasks_list.append(task)
gevent.joinall(tasks_list)
end = time.time()
print(end-start)
    