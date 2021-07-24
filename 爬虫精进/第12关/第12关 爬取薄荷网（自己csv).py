from gevent import monkey
monkey.patch_all()
import gevent,requests, bs4, csv,time
from gevent.queue import Queue
from bs4 import BeautifulSoup
start=time.time()
work = Queue()
url_0='http://www.boohee.com/food/'
url_list=[]
task_list=[]
with open('食物热量表.csv','a',newline='')as f:
    writer=csv.writer(f)
    writer.writerow(['食物','热量表','链接'])
for i in range(1,11):
    for number in range(1,11):
        url=url_0+'group'+'/'+str(i)+'?'+'page='+str(number)
        url_list.append(url)

for i in range(1,10):
    url=url_0+'view_menu'+'?'+'page='+str(i)
    url_list.append(url)
print(len(url_list))
for url in url_list:
    work.put_nowait(url)
def crawler():
    while not work.empty():
        url=work.get_nowait()
        res=requests.get(url)
        bs=BeautifulSoup(res.text,'html.parser')
        items=bs.find_all('li',class_='item clearfix')
        for i in items:
            name=i.find('h4')
            hot=i.find('p')
            link_t=i.find('a')
            link='http://www.boohee.com/'+link_t['href']
            row=[name.text,hot.text,link]
            with open('食物热量表.csv','a',newline='')as f:
                writer=csv.writer(f)
                writer.writerow(row)
for i in range(5):
    task=gevent.spawn(crawler)
    task_list.append(task)
gevent.joinall(task_list)
end=time.time()
print(end-start)